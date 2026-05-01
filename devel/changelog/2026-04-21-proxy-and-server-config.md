# Add official API server, CORS proxy, and Worker updates

## What changed
- Added `msapi.top-academy.ru` as the official API server in OpenAPI spec
- Updated `mock/worker.js` with new anonymized data and integrated proxy to the real backend (CORS bypass when Bearer token is present)
- Updated `scripts/build_worker.py` to reflect new data and proxy config
- Updated `src/publisher/builder.py` — added official server entry, refined spec generation
- Updated `tests/test_builder.py` — new test for single worker server
- Regenerated `uv.lock` and updated `.gitignore`

## Why
- Swagger UI users need to see where the real API lives, separate from the mock worker
- Worker needed CORS proxy functionality so that authenticated Swagger UI requests can reach the real API through the worker

## Affected files
- `mock/worker.js`
- `scripts/build_worker.py`
- `src/publisher/builder.py`
- `tests/test_builder.py`
- `uv.lock`
- `.gitignore`
