# IT Top Academy Journal API Documentation

IT Top Academy has no public API documentation. This project fills the gap — covering **34 endpoints**.

## Quick Start

1. **Open Swagger UI** — [Swagger UI](swagger.md) works immediately, no token needed: the mock server returns anonymized data
2. **Try logging in** — click "Try it out" on `/auth/login`, the worker proxies the request to the real API
3. **Get a token** — if you need access to real data, see [Authentication](authentication.md)
4. **Read the docs** — pick an [API section](API/dashboard.md) for details

## What the Project Does

- **Collects** real API responses via authenticated requests
- **Validates** structure with Pydantic — when the API changes, the pipeline fails and opens a GitHub Issue
- **Anonymizes** data with Faker — no real names, IDs, or dates in the public repository
- **Generates** `openapi.json` and publishes Swagger UI + text documentation

## CI Pipeline

Steps executed on each run (nightly cron or manual trigger):

```
tests → collect → validate → anonymize → publish → worker
                                          ↘ mkdocs
```

1. **tests** — project unit tests
2. **collect** — requests to the real API, response collection
3. **validate** — Pydantic schema validation; on failure — GitHub Issue
4. **anonymize** — sensitive data replacement via Faker
5. **publish** — generate `openapi.json` and deploy Swagger UI to GitHub Pages
6. **worker** — build and deploy Cloudflare Worker (mock server)
7. **mkdocs** — build and deploy text documentation to GitHub Pages

## Navigation

| Page | Content |
|------|---------|
| [Authentication](authentication.md) | Getting a token, headers, Authorize button |
| [Swagger UI](swagger.md) | Interactive API explorer |
| [Mock Server](mock-server.md) | How the Cloudflare Worker works |
