# Add array trimmer and refactor collector/anonymizer

## What changed
- Added `src/collector/array_trimmer.py` — trims long API response arrays to a configurable max size for compact examples
- Refactored `src/collector/client.py` — integrated trimmer, improved pagination and retry logic
- Refactored `src/anonymizer/anonymizer.py` — improved recursive replacement, better handling of nested structures
- Updated `src/validator/validator.py` — restructured validation logic for cleaner error handling
- Updated tests in `test_anonymizer.py` and `test_validator.py`

## Why
- Some endpoints return hundreds of items (e.g. `/homework/operations/list` with 457 entries) — trimming keeps the generated OpenAPI examples compact while preserving representative data
- Collector and anonymizer needed refactoring to handle the trimmer output and real API quirks discovered during first collection runs

## Affected files
- `src/collector/array_trimmer.py` (new)
- `src/collector/client.py`
- `src/anonymizer/anonymizer.py`
- `src/validator/validator.py`
- `src/validator/__init__.py`
- `tests/test_anonymizer.py`
- `tests/test_validator.py`
