# Mock Server

A Cloudflare Worker sits between the browser and the real API.

## How It Works

- **No token** → returns anonymized mock data (try it without logging in)
- **With token** → proxies to the real API, adding required headers

## Why This Exists

Swagger UI hosted on `github.io` cannot call the real API directly because:

1. **CORS** — the API doesn't allow cross-origin requests from arbitrary domains
2. **Origin/Referer** — the API requires these headers set to `journal.top-academy.ru`, which a browser on github.io cannot do

The Worker solves both problems: it adds the correct CORS headers to every response and injects `Origin`/`Referer` when proxying.

## Source Code

The Worker is built from `mock/build_worker.py` which embeds anonymized example payloads into a self-contained `worker.js`.
