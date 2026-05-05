# src/

Pipeline modules — each handles one stage of the collection-to-publication flow.

## collector/

Auth and API data collection.

- `client.py` — `JournalClient`: authenticates and fetches data from the journal API.
- `endpoints.py` — `ENDPOINTS` list + `Endpoint` dataclass: defines all API endpoints to collect.
- `array_trimmer.py` — Trims large arrays in responses to keep example sizes manageable.

## validator/

Pydantic models and validation.

- `models.py` — Pydantic v2 models that define the expected shape of each API response.
- `validator.py` — `Validator`: validates raw responses against the models.

## anonymizer/

Faker-based PII replacement.

- `anonymizer.py` — `Anonymizer`: replaces personally identifiable information in validated data.
- `rules.py` — Replacement rules mapping fields to Faker providers.

## publisher/

OpenAPI specification generation.

- `builder.py` — `OpenAPIBuilder`: generates `openapi.json` from anonymized examples.

Tests mirror this structure in `tests/` (test_client.py, test_endpoints.py, test_validator.py, test_anonymizer.py, test_builder.py, test_worker.py).
