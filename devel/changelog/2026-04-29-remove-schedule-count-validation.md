# Remove fixed count validation on schedule endpoints

## What changed
- Removed `validate_count=True` and `expected_max_items` from all three schedule endpoints (`get-by-date`, `get-by-date-range`, `get-month`) in `src/collector/endpoints.py`
- Updated test in `tests/test_endpoints.py` to assert schedule endpoints have `validate_count=False` and no `expected_max_items`
- Added per-endpoint `anonymize` flag and `max_items`/`validate_count`/`expected_max_items` fields to `Endpoint` dataclass
- Client now returns `raw_counts` alongside collected data for count validation
- Pipeline performs count validation on untrimmed data and surfaces `count_warning` in validation results
- Per-endpoint anonymization: public endpoints (`/public/*`) skip anonymization
- Added `count_warning` field to `ValidationResult` and included it in issue body formatting
- Added new tests for client (`test_client.py`) and endpoint config (`test_endpoints.py`)

## Why
- Schedule API returns items per class/lesson, not per day — the count depends on how many pairs occur on a given day, so a fixed `expected_max_items` (1/7/31) was incorrect. For example, `get-month` returned 80 items instead of the expected 31.
- Count validation framework is still available for other endpoints that have predictable item counts.

## Affected files
- `src/collector/endpoints.py`
- `src/collector/client.py`
- `src/validator/validator.py`
- `main.py`
- `tests/test_endpoints.py`
- `tests/test_client.py`
- `tests/test_validator.py`
- `tests/test_anonymizer.py`
