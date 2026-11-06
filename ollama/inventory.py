#!/usr/bin/env -S uv run --script
"""Update installed Ollama models and atomically capture a digest-backed inventory."""

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpie",
#   "pydantic>=2,<3",
#   "opentelemetry-sdk",
#   "opentelemetry-exporter-otlp-proto-http",
# ]
# ///

import argparse
import json
import logging
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated, Any, Literal

from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from pydantic import AwareDatetime, BaseModel, BeforeValidator, ConfigDict, Field, JsonValue, StrictInt, StrictStr

__all__ = ["InventoryV1", "collect_inventory", "inventory_schema", "main", "parse_sections", "write_inventory"]

logger = logging.getLogger("ollama.inventory")
ANSI_ESCAPE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")

NonEmptyString = Annotated[StrictStr, Field(min_length=1)]


def timestamp_string(value: object) -> str:
    """Require JSON date-time strings rather than Pydantic's numeric epoch coercion."""
    if not isinstance(value, str) or not re.fullmatch(
        r"\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:[Zz]|[+-]\d{2}:\d{2})", value
    ):
        raise ValueError("Expected an ISO 8601 date-time string with timezone")
    return value


Timestamp = Annotated[AwareDatetime, BeforeValidator(timestamp_string)]


class InventoryObject(BaseModel):
    """Reject unknown fields in the inventory-owned contract."""

    model_config = ConfigDict(extra="forbid")


class PullResult(InventoryObject):
    """Record a pull decision or attempt, independent of manifest modification."""

    status: Literal["not_requested", "skipped", "succeeded", "failed"]
    attempted_at: Timestamp | None = None
    finished_at: Timestamp | None = None
    reason: StrictStr | None = None
    error: StrictStr | None = None


class InspectionError(InventoryObject):
    """Describe a failed inspection without discarding the model record."""

    source: Literal["cli", "api", "snapshot"]
    error: NonEmptyString


class ModelRecord(InventoryObject):
    """Fields shared by installed and concurrently removed models."""

    name: NonEmptyString
    details: dict[str, list[StrictStr]]
    inspection_errors: list[InspectionError]
    pull: PullResult
    last_pull: PullResult | None = None


class InstalledModelRecord(ModelRecord):
    """Locally observed manifest identity and flexible upstream metadata."""

    digest: Annotated[StrictStr, Field(pattern=r"^[0-9a-f]{64}$")]
    size_bytes: Annotated[StrictInt, Field(ge=0)]
    updated: Timestamp
    observed_at: Timestamp
    metadata: dict[str, JsonValue]


class MissingModelRecord(ModelRecord):
    """A model removed before its manifest could be inspected."""

    inspection_errors: Annotated[list[InspectionError], Field(min_length=1)]


class InventoryV1(InventoryObject):
    """Version 1 of the inventory, including incomplete checkpoints."""

    schema_version: Literal[1]
    digest_algorithm: Literal["sha256"]
    started_at: Timestamp
    generated_at: Timestamp | None
    status: Literal["in_progress", "completed", "completed_with_errors"]
    ollama_version: NonEmptyString
    research_metadata: dict[str, JsonValue]
    expected_models: list[NonEmptyString]
    models: list[InstalledModelRecord | MissingModelRecord]


def inventory_schema() -> dict[str, Any]:
    """Generate the portable schema from the runtime validation models."""
    return {"$schema": "https://json-schema.org/draft/2020-12/schema", **InventoryV1.model_json_schema()}


def now() -> str:
    """Return the current UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


class JsonFormatter(logging.Formatter):
    """Format console events as structured JSON."""

    def format(self, record: logging.LogRecord) -> str:
        """Serialize a log event and its context."""
        return json.dumps(
            {
                "timestamp": now(),
                "level": record.levelname,
                "event": record.getMessage(),
                **getattr(record, "context", {}),
            }
        )


def configure_telemetry() -> tuple[TracerProvider, MeterProvider, LoggerProvider]:
    """Send best-effort telemetry only to the local collector."""
    resource = Resource.create({"service.name": "ollama-inventory"})
    traces = TracerProvider(resource=resource)
    traces.add_span_processor(
        BatchSpanProcessor(OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces", timeout=2))
    )
    metrics = MeterProvider(
        resource=resource,
        metric_readers=[
            PeriodicExportingMetricReader(
                OTLPMetricExporter(endpoint="http://localhost:4318/v1/metrics", timeout=2),
                export_interval_millis=60000,
            )
        ],
    )
    logs = LoggerProvider(resource=resource)
    logs.add_log_record_processor(
        BatchLogRecordProcessor(OTLPLogExporter(endpoint="http://localhost:4318/v1/logs", timeout=2))
    )
    console = logging.StreamHandler()
    console.setFormatter(JsonFormatter())
    logger.setLevel(logging.INFO)
    logger.addHandler(console)
    logger.addHandler(LoggingHandler(logger_provider=logs))
    return traces, metrics, logs


def command(*args: str, timeout: int = 120) -> str:
    """Run a bounded command, preserving useful failure output."""
    with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
        result = subprocess.run(args, stdout=stdout, stderr=stderr, timeout=timeout, check=False)
        if result.returncode:
            stdout.seek(max(0, stdout.tell() - 16384))
            stderr.seek(max(0, stderr.tell() - 16384))
            error = (stderr.read() + stdout.read()).decode("utf-8", errors="replace")
            raise RuntimeError(ANSI_ESCAPE.sub("", error).strip())
        stdout.seek(0)
        return ANSI_ESCAPE.sub("", stdout.read().decode("utf-8"))


def api(path: str, model: str | None = None) -> dict[str, Any]:
    """Read structured metadata from the same server as the Ollama CLI."""
    host = os.environ.get("OLLAMA_HOST", "http://localhost:11434").rstrip("/")
    if "://" not in host:
        host = f"http://{host}"
    args = ["http", "--ignore-stdin", "--check-status", "--body", "--timeout=60"]
    args.extend(["POST" if model else "GET", f"{host}/api/{path}"])
    if model:
        args.append(f"model={model}")
    response = json.loads(command(*args))
    if not isinstance(response, dict):
        raise ValueError(f"Unexpected response from /api/{path}")
    return response


def parse_sections(output: str) -> dict[str, list[str]]:
    """Preserve show output by section, including repeated and nested values."""
    sections: dict[str, list[str]] = {}
    section: list[str] | None = None
    for line in output.splitlines():
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip())
        if indent <= 2:
            section = sections.setdefault(line.strip(), [])
        elif section is not None:
            section.append(line[4:].rstrip())
        else:
            raise ValueError(f"Unrecognized Ollama show output: {line}")
    if not sections:
        raise ValueError("Ollama show returned no sections")
    return sections


def write_inventory(path: Path, inventory: dict[str, Any]) -> None:
    """Validate before replacing an inventory, preserving timestamp precision."""
    InventoryV1.model_validate(inventory)
    write_json(path, inventory)


def write_json(path: Path, content: dict[str, Any]) -> None:
    """Replace JSON atomically without truncating an earlier snapshot."""
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
            temporary = Path(handle.name)
            json.dump(content, handle, indent=2, ensure_ascii=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def inspect_model(name: str, tag: dict[str, Any], research: dict[str, Any]) -> dict[str, Any]:
    """Capture CLI sections plus structured metadata without loading a model."""
    record: dict[str, Any] = {
        "name": name,
        "digest": tag["digest"],
        "size_bytes": tag["size"],
        "updated": tag["modified_at"],
        "observed_at": now(),
        "details": {},
        "metadata": {"registry_details": tag.get("details", {}), "supports": tag.get("capabilities", [])},
        "inspection_errors": [],
    }
    if name.rsplit(":", 1)[0] in research:
        record["metadata"]["research"] = research[name.rsplit(":", 1)[0]]
    for source in ("cli", "api"):
        try:
            if source == "cli":
                record["details"] = parse_sections(command("ollama", "show", name))
            else:
                show = api("show", name)
                record["metadata"].update(
                    {
                        "supports": show.get("capabilities", record["metadata"]["supports"]),
                        "registry_details": show.get("details", record["metadata"]["registry_details"]),
                        "model_info": {
                            key: value
                            for key, value in show.get("model_info", {}).items()
                            if not key.startswith("tokenizer.")
                        },
                        "thinking": show.get("thinking"),
                        "remote_model": show.get("remote_model"),
                        "remote_host": show.get("remote_host"),
                    }
                )
        except (RuntimeError, subprocess.TimeoutExpired, ValueError) as error:
            record["inspection_errors"].append({"source": source, "error": str(error)})
            logger.error("inspection_failed", extra={"context": {"model": name, "source": source, "error": str(error)}})
    current = {item["name"]: item for item in api("tags")["models"]}.get(name)
    if current is None or current["digest"] != tag["digest"]:
        record["inspection_errors"].append(
            {"source": "snapshot", "error": "Model removed or digest changed during inspection; rerun inventory"}
        )
        logger.error("snapshot_changed", extra={"context": {"model": name}})
    return record


def collect_inventory(
    output: Path, update: bool, skip: set[str], research: dict[str, Any], pull_timeout: int
) -> dict[str, Any]:
    """Process every installed tag, checkpointing failures and successful pulls."""
    previous = InventoryV1.model_validate_json(output.read_text()) if output.exists() else None
    previous_models = (
        {item.name: item.model_dump(mode="json", exclude_unset=True) for item in previous.models} if previous else {}
    )
    listed = command("ollama", "list")
    names = [line.split()[0] for line in listed.splitlines()[1:] if line.strip()]
    inventory: dict[str, Any] = {
        "schema_version": 1,
        "digest_algorithm": "sha256",
        "started_at": now(),
        "generated_at": None,
        "status": "in_progress",
        "ollama_version": command("ollama", "--version").strip(),
        "research_metadata": research.get("_metadata", {}),
        "expected_models": names,
        "models": [],
    }
    write_inventory(output, inventory)
    for name in sorted(names):
        pull: dict[str, Any] = {"status": "not_requested"}
        if update and name in skip:
            pull = {"status": "skipped", "reason": "Explicit skip"}
        elif update:
            logger.info("pull_started", extra={"context": {"model": name}})
            pull = {"status": "succeeded", "attempted_at": now()}
            try:
                command("ollama", "pull", name, timeout=pull_timeout)
            except (RuntimeError, subprocess.TimeoutExpired) as error:
                pull.update(status="failed", error=str(error))
                logger.error("pull_failed", extra={"context": {"model": name, "error": str(error)}})
            pull["finished_at"] = now()
        tags = {tag["name"]: tag for tag in api("tags")["models"]}
        if name not in tags:
            record = {
                "name": name,
                "details": {},
                "inspection_errors": [{"source": "snapshot", "error": "Model no longer installed"}],
            }
            logger.error("model_missing", extra={"context": {"model": name}})
        else:
            record = inspect_model(name, tags[name], research)
        record["pull"] = pull
        prior = previous_models.get(name, {})
        if pull["status"] in {"succeeded", "failed"}:
            record["last_pull"] = pull
        elif "last_pull" in prior:
            record["last_pull"] = prior["last_pull"]
        elif prior.get("pull", {}).get("status") in {"succeeded", "failed"}:
            record["last_pull"] = prior["pull"]
        inventory["models"].append(record)
        write_inventory(output, inventory)
        logger.info("model_recorded", extra={"context": {"model": name, "pull_status": pull["status"]}})
    inventory["status"] = (
        "completed_with_errors"
        if any(item["inspection_errors"] or item["pull"]["status"] == "failed" for item in inventory["models"])
        else "completed"
    )
    inventory["generated_at"] = now()
    write_inventory(output, inventory)
    return inventory


def main(argv: list[str] | None = None) -> int:
    """Run the utility; return nonzero when any update or inspection fails."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("model-inventory.json"))
    parser.add_argument("--update", action="store_true", help="Pull installed tags before inspection")
    parser.add_argument("--skip", action="append", default=[], help="Exact tag to exclude from pulls (repeatable)")
    parser.add_argument("--research", type=Path, help="Curated JSON metadata keyed by model family")
    parser.add_argument("--pull-timeout", type=int, default=7200, help="Per-model pull timeout in seconds")
    parser.add_argument("--export-schema", type=Path, help="Write the JSON Schema and exit without contacting Ollama")
    args = parser.parse_args(argv)
    if args.export_schema:
        try:
            write_json(args.export_schema, inventory_schema())
        except (OSError, ValueError) as error:
            parser.exit(1, f"Schema export failed: {error}\n")
        return 0
    if args.pull_timeout <= 0:
        parser.error("--pull-timeout must be positive")
    traces, metrics, logs = configure_telemetry()
    try:
        research = json.loads(args.research.read_text()) if args.research else {}
        if not isinstance(research, dict) or any(not isinstance(value, dict) for value in research.values()):
            raise ValueError("Research must be a JSON object keyed by family with object values")
        with traces.get_tracer(__name__).start_as_current_span("inventory"):
            inventory = collect_inventory(args.output, args.update, set(args.skip), research, args.pull_timeout)
            metrics.get_meter(__name__).create_counter("ollama.inventory.models").add(len(inventory["models"]))
        logger.info(
            "inventory_finished", extra={"context": {"status": inventory["status"], "output": str(args.output)}}
        )
        return 0 if inventory["status"] == "completed" else 1
    except (OSError, RuntimeError, subprocess.TimeoutExpired, ValueError, KeyError) as error:
        logger.error("inventory_failed", extra={"context": {"error": str(error)}})
        return 1
    except KeyboardInterrupt:
        logger.warning("inventory_interrupted")
        return 130
    finally:
        traces.shutdown()
        metrics.shutdown()
        logs.shutdown()


if __name__ == "__main__":
    sys.exit(main())
