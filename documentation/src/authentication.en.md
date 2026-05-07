# Authentication

## Login

All endpoints except `/auth/login` require a Bearer token.

### POST /auth/login

```json
{
  "application_key": "<key>",
  "id_city": null,
  "username": "<login>",
  "password": "<password>"
}
```

Returns `access_token`, used as `Bearer <token>`.

You can call this endpoint directly from Swagger UI — the worker proxies the request to the real API. Click "Try it out", fill in the fields, and execute.

## Headers for Direct Requests

When making direct API requests (bypassing the worker), every authenticated request must include:

| Header | Value |
|--------|-------|
| `Authorization` | `Bearer <access_token>` |
| `Origin` | `https://journal.top-academy.ru` |
| `Referer` | `https://journal.top-academy.ru/` |

Without `Origin` and `Referer`, the API returns **403 Forbidden**.

## Working in Swagger UI

In Swagger UI, you don't need to set `Origin` and `Referer` headers — the worker adds them automatically when proxying.

### Authorize Button

1. Click **Authorize** (lock icon at the top of the page)
2. Paste your `access_token` into the value field (without `Bearer` — Swagger adds it automatically)
3. Click **Authorize**, then **Close**
4. All subsequent requests will include the `Authorization` header

### Without a Token

Swagger UI works without a token too — the mock server returns anonymized example data for every endpoint.
