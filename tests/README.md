# tests/

Tests mirror `src/` structure.

| src/ | tests/ |
|------|--------|
| `src/collector/` | `tests/test_client.py`, `tests/test_endpoints.py` |
| `src/validator/` | `tests/test_validator.py` |
| `src/anonymizer/` | `tests/test_anonymizer.py` |
| `src/publisher/` | `tests/test_builder.py` |
| `mock/` (worker template) | `tests/test_worker.py` |

Write the test before the implementation. Always.
