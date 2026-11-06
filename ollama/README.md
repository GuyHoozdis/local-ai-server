# Ollama utilities

- [pull.sh](pull.sh): pull explicitly named models.
- [inventory.py](inventory.py): inspect installed tags; optionally update them first.
- [model-inventory.json](model-inventory.json): generated local snapshot and pull outcomes.
- [model-research.json](model-research.json): sourced family-level use cases, separate from local capabilities.

```bash
./ollama/inventory.py --update --skip qwen3.5:latest --research ollama/model-research.json
./ollama/inventory.py --research ollama/model-research.json
```

Requires `uv` and the native `ollama` CLI. Script dependencies are managed by `uv`.
`OLLAMA_HOST` selects the server for both CLI and metadata requests. Pulls are sequential;
`--skip` is repeatable and excludes only pulls, not inspection. Without `--update`, no models
are downloaded. No models are loaded for inference or removed.

The inventory records full manifest digests, byte sizes, local modification timestamps
(`updated`, **not** upstream release dates), observation times, and individual pull outcomes.
`details` preserves `ollama show` sections as arrays of display lines, including nesting and
repeated parameters. Structured API metadata includes capabilities, quantization, architecture,
and non-tokenizer model information. Family research is curated, not fetched on each run;
it is not evidence of a particular local variant's benchmark performance.

Digests identify the observed manifests and expose duplicate tags. They are **not** a
restorable lock: mutable tags can change and registries may not support pulling old digests.
For cloud-backed tags, a digest identifies the local routing manifest, not remote weights.
No separate checksum is needed for the Git-tracked inventory.

Snapshots are replaced atomically after each model. Interrupted runs retain `in_progress`
and the expected tag list; failures are recorded and cause a nonzero exit after remaining
models are processed. A digest changing during inspection is reported as an inconsistent
snapshot. Refresh after any concurrent update completes. Successful pulls may leave the
digest unchanged; their attempt timestamps are separate from `updated`.
`pull` describes the current run; `last_pull` preserves the last attempted pull across
inspection-only refreshes so updating research does not erase update provenance.

Structured logs, traces, and model counts are sent best-effort to the local OTLP collector
on port 4318. Collector failures do not prevent inventory generation.
