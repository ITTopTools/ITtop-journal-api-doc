# Enrich OpenAPI spec: auth scheme, required headers, correct response schemas

## What changed
- Added `BearerAuth` security scheme to OpenAPI spec in `src/publisher/builder.py`
- Authenticated operations now declare `security: [{"BearerAuth": []}]`
- Added required request headers (`Origin`, `Referer`, `User-Agent`) as parameters on authenticated endpoints
- Fixed response schemas: list endpoints now use `type: array` instead of `type: object`, based on `MODELS` dict `is_list` flag
- Fixed login request example: uses `username` field (matching real API) instead of `login`
- Added 7 new tests in `tests/test_builder.py` covering all enrichment features

## Why
- Without `BearerAuth` scheme, Swagger UI couldn't demonstrate authenticated requests
- `Origin` and `Referer` headers are required by the real API (CORS enforcement) — without them, requests fail with 403
- Response schemas were all generated as `type: object` regardless of whether the endpoint returns a list or dict — the `is_list` flag in `MODELS` already had this information

## Affected files
- `src/publisher/builder.py`
- `tests/test_builder.py`
