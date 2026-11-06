import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import patch

from pydantic import ValidationError

from ollama import inventory


def snapshot() -> dict[str, Any]:
    return {
        "schema_version": 1,
        "digest_algorithm": "sha256",
        "started_at": "2026-11-06T00:00:00Z",
        "generated_at": None,
        "status": "in_progress",
        "ollama_version": "test",
        "research_metadata": {},
        "expected_models": [],
        "models": [],
    }


class InventoryV1TestCase(unittest.TestCase):
    def test_it_validates_the_committed_inventory_and_generated_schema(self) -> None:
        directory = Path(inventory.__file__).parent
        data = (directory / "model-inventory.json").read_text()

        model = inventory.InventoryV1.model_validate_json(data)

        self.assertEqual(len(model.models), len(model.expected_models))
        self.assertEqual(
            json.loads((directory / "model-inventory.schema.json").read_text()), inventory.inventory_schema()
        )
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "inventory.json"

            inventory.write_inventory(path, json.loads(data))

            self.assertEqual(json.loads(path.read_text()), json.loads(data))

    def test_it_rejects_invalid_writes_without_changing_the_existing_file(self) -> None:
        for field, value in (
            ("schema_version", 2),
            ("status", "done"),
            ("started_at", "yesterday"),
            ("started_at", 1793980800),
        ):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / "inventory.json"
                path.write_text("original")
                data = snapshot()
                data[field] = value

                with self.assertRaises(ValidationError):
                    inventory.write_inventory(path, data)

                self.assertEqual(path.read_text(), "original")

    def test_it_rejects_malformed_installed_model_fields(self) -> None:
        record = {
            "name": "model:latest",
            "digest": "a" * 64,
            "size_bytes": 1,
            "updated": "2026-11-06T00:00:00Z",
            "observed_at": "2026-11-06T00:00:00Z",
            "details": {},
            "metadata": {"upstream_extension": {"values": [True, None, 42]}},
            "inspection_errors": [],
            "pull": {"status": "not_requested"},
        }
        data = snapshot()
        data["models"] = [record]
        inventory.InventoryV1.model_validate(data)

        for field, value in (
            ("digest", "short"),
            ("size_bytes", -1),
            ("size_bytes", "42"),
            ("updated", "2026-11-06T00:00:00"),
            ("pull", {"status": "unknown"}),
            ("unexpected_field", True),
        ):
            with self.subTest(field=field, value=value):
                data["models"] = [{**record, field: value}]

                with self.assertRaises(ValidationError):
                    inventory.InventoryV1.model_validate(data)

    def test_it_rejects_invalid_existing_inventory_before_running_commands(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "inventory.json"
            data = snapshot()
            data["schema_version"] = 2
            path.write_text(json.dumps(data))
            with patch.object(inventory, "command", spec=inventory.command) as command:
                with self.assertRaises(ValidationError):
                    inventory.collect_inventory(path, True, set(), {}, 30)

            command.assert_not_called()
            self.assertEqual(json.loads(path.read_text()), data)

    def test_it_exports_schema_without_ollama_or_telemetry(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "schema.json"
            with (
                patch.object(inventory, "command", spec=inventory.command) as command,
                patch.object(inventory, "configure_telemetry", spec=inventory.configure_telemetry) as telemetry,
            ):
                result = inventory.main(["--export-schema", str(path)])

            self.assertEqual(result, 0)
            self.assertEqual(json.loads(path.read_text()), inventory.inventory_schema())
            command.assert_not_called()
            telemetry.assert_not_called()


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
    def test_it_writes_a_failed_record_when_model_is_removed_before_inspection(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "inventory.json"
            with (
                patch.object(
                    inventory,
                    "command",
                    spec=inventory.command,
                    side_effect=["NAME ID SIZE MODIFIED\nmodel:latest a 1 B\n", "version"],
                ),
                patch.object(inventory, "api", spec=inventory.api, return_value={"models": []}),
                self.assertLogs(inventory.logger, level="ERROR"),
            ):
                result = inventory.collect_inventory(output, False, set(), {}, 30)

            model = inventory.InventoryV1.model_validate_json(output.read_text())

        self.assertEqual(result["status"], "completed_with_errors")
        self.assertIsInstance(model.models[0], inventory.MissingModelRecord)

    def test_it_preserves_last_pull_during_inspection_only_refresh(self) -> None:
        prior_pull = {"status": "succeeded", "attempted_at": "2026-11-06T00:00:00Z"}
        tag = {"name": "model:latest", "digest": "a" * 64, "size": 1, "modified_at": "2026-11-06T00:00:00Z"}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "inventory.json"
            prior = snapshot()
            prior["models"] = [
                {
                    "name": "model:latest",
                    "details": {},
                    "inspection_errors": [{"source": "snapshot", "error": "Model no longer installed"}],
                    "pull": prior_pull,
                }
            ]
            output.write_text(json.dumps(prior))
            with (
                patch.object(
                    inventory,
                    "command",
                    spec=inventory.command,
                    side_effect=["NAME ID SIZE MODIFIED\nmodel:latest a 1 B\n", "version", "  Model\n    size    1B\n"],
                ),
                patch.object(
                    inventory,
                    "api",
                    spec=inventory.api,
                    side_effect=[{"models": [tag]}, {"capabilities": ["completion"]}, {"models": [tag]}],
                ),
            ):
                result = inventory.collect_inventory(output, False, set(), {"_metadata": {"scope": "family"}}, 30)

        self.assertEqual(result["models"][0]["pull"], {"status": "not_requested"})
        self.assertEqual(result["models"][0]["last_pull"], prior_pull)
        self.assertEqual(result["research_metadata"], {"scope": "family"})

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
