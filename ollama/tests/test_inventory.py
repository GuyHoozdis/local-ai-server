import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

from ollama import inventory


class CommandTestCase(unittest.TestCase):
    def test_it_includes_stderr_and_response_body_on_failure(self) -> None:
        code = "import sys; print('response error'); print('status error', file=sys.stderr); sys.exit(1)"

        with self.assertRaises(RuntimeError) as error:
            inventory.command(sys.executable, "-c", code)

        self.assertIn("response error", str(error.exception))
        self.assertIn("status error", str(error.exception))


class ParseSectionsTestCase(unittest.TestCase):
    def test_it_preserves_nested_capabilities_and_repeated_parameters(self) -> None:
        output = (
            "  Model\n    architecture    qwen3\n\n"
            "  Capabilities\n    thinking\n        levels    false, true\n"
            "  Parameters\n    stop    a\n    stop    b\n"
        )

        result = inventory.parse_sections(output)

        self.assertEqual(result["Model"], ["architecture    qwen3"])
        self.assertEqual(result["Capabilities"], ["thinking", "    levels    false, true"])
        self.assertEqual(result["Parameters"], ["stop    a", "stop    b"])

    def test_it_rejects_empty_output(self) -> None:
        with self.assertRaises(ValueError):
            inventory.parse_sections("")


class CollectInventoryTestCase(unittest.TestCase):
    def test_it_skips_pulls_but_inspects_and_continues_after_failure(self) -> None:
        tag = {"digest": "a" * 64, "size": 42, "modified_at": "2026-11-06T00:00:00Z", "details": {}}

        def fake_command(*args: str, timeout: int = 120) -> str:
            if args[:2] == ("ollama", "list"):
                return "NAME ID SIZE MODIFIED\nbad:latest a 42 B\nqwen3.5:latest b 42 B\n"
            if args[:2] == ("ollama", "--version"):
                return "ollama version test"
            if args[:2] == ("ollama", "pull"):
                raise RuntimeError("registry unavailable")
            return "  Model\n    parameters    1B\n"

        def fake_api(path: str, model: str | None = None) -> dict[str, Any]:
            if path == "tags":
                return {"models": [{"name": name, **tag} for name in ("bad:latest", "qwen3.5:latest")]}
            return {"capabilities": ["vision"], "model_info": {"general.architecture": "test"}}

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "inventory.json"
            with (
                patch.object(inventory, "command", spec=inventory.command, side_effect=fake_command) as run,
                patch.object(inventory, "api", spec=inventory.api, side_effect=fake_api),
                self.assertLogs(inventory.logger, level="ERROR"),
            ):
                result = inventory.collect_inventory(output, True, {"qwen3.5:latest"}, {}, 30)

            self.assertEqual(result["status"], "completed_with_errors")
            self.assertEqual([item["pull"]["status"] for item in result["models"]], ["failed", "skipped"])
            self.assertEqual(result["models"][1]["metadata"]["supports"], ["vision"])
            self.assertEqual(json.loads(output.read_text()), result)
            pulls = [call.args for call in run.call_args_list if call.args[:2] == ("ollama", "pull")]
            self.assertEqual(pulls, [("ollama", "pull", "bad:latest")])

    def test_it_records_show_failure_and_concurrent_digest_change(self) -> None:
        tag = {"digest": "before", "size": 1, "modified_at": "date"}
        with (
            patch.object(
                inventory, "command", spec=inventory.command, side_effect=subprocess.TimeoutExpired("ollama", 120)
            ),
            patch.object(
                inventory,
                "api",
                spec=inventory.api,
                side_effect=[
                    {"capabilities": ["completion"]},
                    {"models": [{"name": "model:latest", "digest": "after"}]},
                ],
            ),
            self.assertLogs(inventory.logger, level="ERROR"),
        ):
            result = inventory.inspect_model("model:latest", tag, {})

        self.assertEqual(result["details"], {})
        self.assertEqual([error["source"] for error in result["inspection_errors"]], ["cli", "snapshot"])
        self.assertEqual(result["digest"], "before")


if __name__ == "__main__":
    unittest.main()
