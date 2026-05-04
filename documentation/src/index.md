# IT Top Journal API Documentation

IT Top Academy Journal does not have public API documentation. This project fills the gap.

## Quick Start

1. **Get a token** — see [Authentication](authentication.md)
2. **Try it live** — open [Swagger UI](swagger.md) and explore
3. **Read the docs** — pick an [API section](API/dashboard.md) for details

## What This Project Does

- **Collects** real API responses via authorized requests
- **Validates** structure with Pydantic — pipeline fails and opens an Issue if the API changes
- **Anonymizes** data with Faker — no real names, IDs, or dates in the public repo
- **Generates** `openapi.json` and publishes Swagger UI + text documentation

## Navigation

| Page | What you'll find |
|------|-----------------|
| [Authentication](authentication.md) | How to get a token, required headers |
| [Swagger UI](swagger.md) | Interactive API explorer |
| [Mock Server](mock-server.md) | How the Cloudflare Worker works |
