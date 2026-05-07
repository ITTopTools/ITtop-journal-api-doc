# Mock Server

The Cloudflare Worker sits between the browser and the real API.

**Worker URL:** `https://ittop-mock.blazer19092008.workers.dev/api/v2`

**Real API:** `https://msapi.top-academy.ru/api/v2`

## Routing Logic

The worker processes each request as follows:

1. **OPTIONS** (CORS preflight) → immediate `204 No Content` response with CORS headers
2. **POST /auth/login** → proxy to the real API; on 4xx error or network failure → return mock data
3. **Has `Authorization: Bearer ...` header** → proxy to the real API with `Origin`/`Referer` added
4. **No token** → return anonymized mock data

## Why This Is Needed

Swagger UI on `github.io` cannot call the real API directly:

1. **CORS** — the API does not allow cross-origin requests from arbitrary domains
2. **Origin/Referer** — the API requires these headers to equal `journal.top-academy.ru`, which the browser on github.io cannot set

The worker solves both problems: it adds CORS headers to every response and injects `Origin`/`Referer` when proxying.

## Build and Deploy

- `mock/build_worker.py` — generates `worker.js` from a template + anonymized example data
- `mock/wrangler.toml` — Cloudflare Wrangler configuration
- Deploy: `wrangler deploy` (automatically via CI, step `worker`)
