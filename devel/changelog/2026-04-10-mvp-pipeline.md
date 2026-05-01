# MVP pipeline: collector, validator, anonymizer, publisher, main entrypoint

## What changed
- Added `src/collector/client.py` — httpx-based HTTP client with auth, pagination, retry
- Added `src/collector/endpoints.py` — endpoint registry with `Endpoint` dataclass and `ENDPOINTS` list
- Added `src/validator/models.py` — initial Pydantic models (placeholder schemas with `extra="allow"`)
- Added `src/validator/validator.py` — validates collected responses against models, produces `ValidationResult`
- Added `src/anonymizer/anonymizer.py` — recursive Faker-based PII replacement
- Added `src/anonymizer/rules.py` — field-level anonymization rules
- Added `src/publisher/builder.py` — builds `openapi.json` from collected examples
- Added `publisher/templates/swagger/` — Swagger UI assets
- Added `main.py` — pipeline entrypoint orchestrating collect → validate → anonymize → build
- Added tests for validator, anonymizer, and builder in `tests/`
- Added `.github/workflows/collect.yml` — daily scheduled pipeline + manual trigger
- Added data directory placeholders (`data/raw/`, `data/examples/`)

## Why
- Core pipeline needed to go from zero to working: auth against API, collect responses, validate structure, anonymize PII, and publish OpenAPI docs
- CI workflow ensures the pipeline runs automatically and publishes to GitHub Pages

## Affected files
- `src/collector/client.py`
- `src/collector/endpoints.py`
- `src/validator/models.py`
- `src/validator/validator.py`
- `src/anonymizer/anonymizer.py`
- `src/anonymizer/rules.py`
- `src/publisher/builder.py`
- `main.py`
- `tests/test_validator.py`
- `tests/test_anonymizer.py`
- `tests/test_builder.py`
- `.github/workflows/collect.yml`
- `documentation/index.html`
- `documentation/openapi.json`
- `data/examples/.gitkeep`
- `data/raw/.gitkeep`
