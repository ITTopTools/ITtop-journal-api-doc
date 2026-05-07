# Auth

Authentication endpoint — login to obtain a JWT access token required by all other endpoints.

## Endpoints

### POST /auth/login

Login with credentials to obtain JWT tokens for API access.

**Request body:**

| Field | Type | Description |
|-------|------|-------------|
| `application_key` | string | Application key (fixed value) |
| `id_city` | number \| null | City ID (optional) |
| `username` | string | Student login |
| `password` | string | Student password |

**Response:** Object with `access_token`, `refresh_token`, `expires_in_access`, `expires_in_refresh`, `user_type`, `city_data`, `user_role`.

**Auth flow:**

1. Call `POST /auth/login` with credentials
2. Extract `access_token` from the response
3. Use it as `Authorization: Bearer <access_token>` for all subsequent requests

This endpoint can be called directly from Swagger UI — the worker proxies the request to the real API. If the real API is unavailable, the worker falls back to mock data.

See [Authentication](../authentication.md) for detailed instructions on using the Authorize button in Swagger UI.
