# src/

Pipeline modules — each handles one stage of the collection-to-publication flow.

| Package | Purpose | Key files |
|---------|---------|-----------|
| `collector/` | Auth + API data collection | `client.py`, `endpoints.py`, `array_trimmer.py` |
| `validator/` | Pydantic models + validation | `models.py`, `validator.py` |
| `anonymizer/` | Faker PII replacement | `anonymizer.py`, `rules.py` |
| `publisher/` | OpenAPI + Swagger UI generation | `builder.py`, `templates/swagger/` |

Tests mirror this structure in `tests/`.
