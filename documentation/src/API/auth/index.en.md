# Auth

Authentication section — login to obtain JWT tokens required by all other endpoints.

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| POST | `/auth/login` | Submit login credentials | [Details](login.md) |

## Auth Flow

1. Call `POST /auth/login` with credentials
2. Extract `access_token` from the response
3. Use it as `Authorization: Bearer <access_token>` for all subsequent requests

This endpoint can be called directly from Swagger UI — the worker proxies the request to the real API. If the real API is unavailable, the worker falls back to mock data.

## Dependencies

All other API sections depend on a valid JWT token obtained from this section. See [Authentication](../../authentication.md) for detailed instructions on using the Authorize button in Swagger UI.
