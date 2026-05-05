"""Pipeline entrypoint for collection, validation, anonymization, and publishing."""

import argparse
import asyncio
import json
import os
import sys
import traceback
from pathlib import Path
from typing import Any

from src.anonymizer.anonymizer import Anonymizer
from src.collector.client import JournalClient
from src.collector.endpoints import ENDPOINTS, Endpoint
from src.publisher.builder import OpenAPIBuilder
from src.validator.validator import Validator

VALIDATION_FAILED_MARKER = "VALIDATION_FAILED"
PIPELINE_OK_MARKER = "PIPELINE_OK"

RAW_PATH = Path("data/raw/latest.json")
EXAMPLES_PATH = Path("data/examples/latest.json")
VALIDATION_ISSUE_PATH = Path("data/validation_issue.md")
OPENAPI_PATH = Path("documentation/src/openapi.json")


def _write_json(path: Path, payload: Any) -> None:
    """Write JSON payload to disk with UTF-8 formatting."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _read_json(path: Path) -> Any:
    """Read JSON from disk."""

    return json.loads(path.read_text(encoding="utf-8"))


def _write_error_report(action: str, error_message: str, tb: str) -> None:
    """Write a structured error report for manual troubleshooting."""

    report_path = Path("data/error_report.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report = (
        "# Pipeline Error Report\n\n"
        f"## Action\n{action}\n\n"
        f"## Error\n```text\n{error_message}\n```\n\n"
        "## Traceback\n"
        f"```text\n{tb}\n```\n"
    )
    report_path.write_text(report, encoding="utf-8")


# --- Individual pipeline steps ---


async def _async_step_collect() -> int:
    """Async implementation of the collect step."""

    login = os.environ["JOURNAL_LOGIN"]
    password = os.environ["JOURNAL_PASSWORD"]

    endpoint_map: dict[str, Endpoint] = {e.path: e for e in ENDPOINTS}

    client = JournalClient(login, password)
    try:
        raw, raw_counts = await client.collect_all(ENDPOINTS)
    finally:
        await client.close()

    _write_json(RAW_PATH, raw)

    # Count validation on untrimmed data
    count_warnings: dict[str, str] = {}
    for path, count in raw_counts.items():
        ep = endpoint_map[path]
        if ep.validate_count and ep.expected_max_items is not None:
            if count > ep.expected_max_items:
                count_warnings[path] = (
                    f"Expected <= {ep.expected_max_items} items, got {count}"
                )

    return 0


def step_collect() -> int:
    """Collect raw API data and write data/raw/latest.json."""

    return asyncio.run(_async_step_collect())


def step_validate() -> int:
    """Validate raw data and optionally write issue file. Always exits 0."""

    raw = _read_json(RAW_PATH)

    # Reconstruct count_warnings from raw counts (not available in step mode)
    validator = Validator()
    results = validator.validate_all(raw)

    has_failures = validator.has_failures(results) or any(r.count_warning for r in results)

    if has_failures:
        issue_body = validator.format_issue_body(results)
        VALIDATION_ISSUE_PATH.parent.mkdir(parents=True, exist_ok=True)
        VALIDATION_ISSUE_PATH.write_text(issue_body, encoding="utf-8")
        print(VALIDATION_FAILED_MARKER)

        gh_output = os.environ.get("GITHUB_OUTPUT")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write("validation_failed=true\n")

    return 0


def step_anonymize() -> int:
    """Anonymize raw data and write data/examples/latest.json."""

    if not RAW_PATH.exists():
        print("WARNING: data/raw/latest.json not found, skipping anonymization")
        return 0

    raw = _read_json(RAW_PATH)
    endpoint_map: dict[str, Endpoint] = {e.path: e for e in ENDPOINTS}

    anonymizer = Anonymizer()
    clean: dict[str, Any] = {}
    for path, data in raw.items():
        ep = endpoint_map.get(path)
        if ep is not None and not ep.anonymize:
            clean[path] = data
        else:
            clean[path] = anonymizer.anonymize(data)

    _write_json(EXAMPLES_PATH, clean)
    return 0


def step_publish() -> int:
    """Build OpenAPI spec from examples and write documentation/openapi.json."""

    if not EXAMPLES_PATH.exists():
        print("ERROR: data/examples/latest.json not found, cannot publish", file=sys.stderr)
        return 1

    clean = _read_json(EXAMPLES_PATH)

    is_api_down = bool(clean) and all(
        isinstance(item, dict) and "error" in item for item in clean.values()
    )

    builder = OpenAPIBuilder()
    spec = builder.build(examples=clean, is_api_down=is_api_down)
    builder.save(spec)
    return 0


# --- Full pipeline (backward compat) ---


async def run_pipeline() -> None:
    """Execute the full collection-to-publication pipeline."""

    login = os.environ["JOURNAL_LOGIN"]
    password = os.environ["JOURNAL_PASSWORD"]

    endpoint_map: dict[str, Endpoint] = {e.path: e for e in ENDPOINTS}

    client = JournalClient(login, password)
    try:
        raw, raw_counts = await client.collect_all(ENDPOINTS)
    finally:
        await client.close()

    _write_json(RAW_PATH, raw)

    # Count validation on untrimmed data
    count_warnings: dict[str, str] = {}
    for path, count in raw_counts.items():
        ep = endpoint_map[path]
        if ep.validate_count and ep.expected_max_items is not None:
            if count > ep.expected_max_items:
                count_warnings[path] = (
                    f"Expected <= {ep.expected_max_items} items, got {count}"
                )

    validator = Validator()
    results = validator.validate_all(raw)

    # Merge count warnings into validation results
    for r in results:
        if r.endpoint in count_warnings:
            r.count_warning = count_warnings[r.endpoint]

    if validator.has_failures(results) or count_warnings:
        issue_body = validator.format_issue_body(results)
        VALIDATION_ISSUE_PATH.parent.mkdir(parents=True, exist_ok=True)
        VALIDATION_ISSUE_PATH.write_text(issue_body, encoding="utf-8")
        print(VALIDATION_FAILED_MARKER)

    # Per-endpoint anonymization
    anonymizer = Anonymizer()
    clean: dict[str, Any] = {}
    for path, data in raw.items():
        ep = endpoint_map.get(path)
        if ep is not None and not ep.anonymize:
            clean[path] = data
        else:
            clean[path] = anonymizer.anonymize(data)
    _write_json(EXAMPLES_PATH, clean)

    is_api_down = bool(raw) and all(isinstance(item, dict) and "error" in item for item in raw.values())

    builder = OpenAPIBuilder()
    spec = builder.build(examples=clean, is_api_down=is_api_down)
    builder.save(spec)

    print(PIPELINE_OK_MARKER)


def main() -> int:
    """Run pipeline — full or single step via --step."""

    parser = argparse.ArgumentParser(description="IT Top Journal API pipeline")
    parser.add_argument(
        "--step",
        choices=["collect", "validate", "anonymize", "publish"],
        help="Run a single pipeline step instead of the full pipeline",
    )
    args = parser.parse_args()

    if args.step:
        step_funcs = {
            "collect": step_collect,
            "validate": step_validate,
            "anonymize": step_anonymize,
            "publish": step_publish,
        }
        try:
            return step_funcs[args.step]()
        except Exception as error:  # noqa: BLE001
            tb = traceback.format_exc()
            print(tb, file=sys.stdout)
            _write_error_report(f"step {args.step}", str(error), tb)
            return 1

    # Full pipeline (backward compat)
    try:
        asyncio.run(run_pipeline())
    except Exception as error:  # noqa: BLE001
        tb = traceback.format_exc()
        print(tb, file=sys.stdout)
        _write_error_report("running pipeline", str(error), tb)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
