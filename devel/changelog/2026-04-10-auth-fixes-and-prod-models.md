# Fix auth payload and replace placeholder models with real schemas

## What changed
- Fixed auth payload in `src/collector/client.py`:
  - Changed `application_key` from empty string to actual key
  - Renamed `login` field to `username` (matching the real API)
- Replaced all placeholder Pydantic models with real schemas derived from first API collection:
  - Introduced `_Base` class with `ConfigDict(extra="allow")` — all models inherit from it
  - All fields now `| None = None` — API may omit any field at any time
  - Models now reflect actual API response structure (e.g. `UserInfoResponse` has `student_id`, `full_name`, `group_name`, etc.)
- Added `data/validation_issue.md` and `data/error_report.md` (later removed and gitignored)
- Added timeless logging for response body in collector

## Why
- Auth was failing because payload field names didn't match the real API (`login` vs `username`, missing `application_key`)
- Placeholder models with generic fields (e.g. `average: float`) never matched real responses, causing validation to always fail
- `extra="allow"` and `| None = None` pattern adopted after discovering that API omits fields unpredictably and adds new ones without notice

## Affected files
- `src/collector/client.py`
- `src/validator/models.py`
- `src/validator/validator.py`
- `src/validator/__init__.py`
- `tests/test_validator.py`
- `tests/test_anonymizer.py`
