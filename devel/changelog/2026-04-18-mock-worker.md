# Add Cloudflare Worker for mock API and proxy

## What changed
- Added `scripts/build_worker.py` — builds a Cloudflare Worker that serves anonymized mock data without auth and proxies authenticated requests to the real API
- Added `mock/worker.js` — the Worker source: no-Bearer → mock response, Bearer present → proxy to `msapi.top-academy.ru`
- Added `wrangler.toml` — Cloudflare Worker deployment config
- Integrated worker deployment into `.github/workflows/collect.yml`
- Added mock server URL to OpenAPI spec as the only server entry
- Added `scripts/build_worker.py` artifact to `.gitignore`
- CORS proxy: if Bearer token is present, the Worker proxies to the real API backend; without a token, it returns pre-built anonymized mock responses

## Why
- Direct browser access to `msapi.top-academy.ru` is blocked by CORS — Swagger UI can't make live requests
- Worker solves this transparently: no token → mock data (always works), with token → live data (real API)
- Having a single server URL in the spec simplifies the Swagger UI experience

## Affected files
- `scripts/build_worker.py` (new)
- `mock/worker.js`
- `wrangler.toml` (new)
- `.github/workflows/collect.yml`
- `src/publisher/builder.py`
- `.gitignore`
