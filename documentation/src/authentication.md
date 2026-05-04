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

Returns an `access_token` used as `Bearer <token>`.

## Required Headers

Every authenticated request must include:

| Header | Value |
|--------|-------|
| `Authorization` | `Bearer <access_token>` |
| `Origin` | `https://journal.top-academy.ru` |
| `Referer` | `https://journal.top-academy.ru/` |

Without `Origin` and `Referer`, the API returns **403 Forbidden**.
