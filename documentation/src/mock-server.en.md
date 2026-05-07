# Mock Server

The Cloudflare Worker ([worker](glossary.md#worker)) sits between the browser and the real API, providing a transparent proxy with CORS support and anonymous mock data.

**Worker URL:** `https://ittop-mock.blazer19092008.workers.dev/api/v2`

**Real API:** `https://msapi.top-academy.ru/api/v2`

## Why This Is Needed

Swagger UI on `github.io` cannot call the real API directly:

1. **CORS** — the API does not return `Access-Control-Allow-Origin`, so the browser blocks cross-origin responses
2. **Origin/Referer** — the API requires these headers to equal `journal.top-academy.ru`, which the browser on github.io cannot set

The worker solves both problems: it adds CORS headers to every response and injects `Origin`/`Referer` when proxying to the real API.

## Routing Logic

The worker processes each request as follows:

```
Request arrives
    │
    ├─ OPTIONS (CORS preflight)?
    │   └─ → 204 No Content + CORS headers
    │
    ├─ POST /auth/login?
    │   ├─ Proxy to real API
    │   │   ├─ 2xx → return real response + CORS headers
    │   │   └─ 4xx / network error → return mock data
    │   └─ No mock available → 404 Not Found
    │
    ├─ Has Authorization: Bearer ...?
    │   └─ Proxy to real API + CORS headers
    │      (Origin/Referer/User-Agent injected automatically)
    │
    └─ No token?
        ├─ Mock data exists for this path → return mock + CORS headers
        └─ No mock data → 404 Not Found
```

## Mock Data

When there is no Bearer token, the worker returns anonymized mock data from an embedded `MOCK` object. This data comes from the project's data pipeline:

1. **Collect** — real API responses are fetched with student credentials
2. **Anonymize** — sensitive data (names, IDs, dates) is replaced with generated values via [Faker](glossary.md#faker)
3. **Embed** — `mock/build_worker.py` injects the anonymized data into `worker.js` as the `MOCK` constant
4. **Deploy** — `wrangler deploy` pushes the worker to Cloudflare

The mock data covers all **34 endpoints** — every path that the project collects. The structure of mock responses is identical to real API responses (same field names and types), only the values are anonymized.

### What mock data looks like

Example mock response for `POST /auth/login`:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "expires_in_access": 7200,
  "expires_in_refresh": 86400,
  "user_type": 0,
  "city_data": { "id": 1, "name": "Generated City" },
  "user_role": "student"
}
```

The `access_token` in the mock is a real JWT structure but with invalid signatures — it cannot be used to authenticate against the real API.

### When mock data may be outdated

If the API was unavailable during the nightly collection, the pipeline adds a warning to `openapi.json` and the mock data reflects the last successful collection. The CI step `validate` checks for schema mismatches — if the API structure changed, the pipeline fails and opens a GitHub Issue.

## Updating Mock Data

Mock data is regenerated automatically by the CI pipeline:

```
tests → collect → validate → anonymize → publish
                        ↘ build_worker → deploy
```

To update manually:

```bash
# Full pipeline (requires JOURNAL_LOGIN and JOURNAL_PASSWORD)
JOURNAL_LOGIN=your_login JOURNAL_PASSWORD=your_password uv run main.py

# Just rebuild the worker from existing anonymized data
uv run main.py --step publish
python mock/build_worker.py
wrangler deploy
```

## Limitations

| Limitation | Details |
|------------|---------|
| HTTP methods | Only `GET` and `POST` are supported — `PATCH`, `PUT`, `DELETE` are not proxied or mocked |
| Write operations | No mock support for homework submission, profile updates, etc. — only read endpoints are collected |
| Data freshness | Mock data reflects the last successful collection run; can be up to 24 hours stale |
| Cloudflare limits | Worker has a 50 ms CPU time limit (free plan) and 128 MB memory limit |
| Login mock | The `/auth/login` mock token cannot be used against the real API — it's for structure exploration only |

## Build and Deploy

- `mock/build_worker.py` — generates `worker.js` from a template + anonymized example data from `data/examples/latest.json`
- `mock/wrangler.toml` — Cloudflare Wrangler configuration (`ittop-mock`, `compatibility_date: 2025-01-01`)
- Deploy: `wrangler deploy` (automatically via CI, step `worker`)
