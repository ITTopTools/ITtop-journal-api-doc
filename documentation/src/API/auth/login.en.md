# POST /auth/login

Submit credentials to obtain JWT tokens for API access.

## Purpose

Used by the login form on the frontend to authenticate the student and retrieve tokens needed for all subsequent API calls.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `application_key` | body | string | yes | Application key (fixed value) |
| `id_city` | body | number \| null | no | City ID |
| `username` | body | string | yes | Student login |
| `password` | body | string | yes | Student password |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `access_token` | string | JWT access token for API authorization |
| `refresh_token` | string | JWT refresh token |
| `expires_in_access` | integer | Access token expiration time in seconds |
| `expires_in_refresh` | integer | Refresh token expiration time in seconds |
| `user_type` | string | Type of the authenticated user |
| `city_data` | object | City information for the user |
| `user_role` | string | Role assigned to the user |

**Response type:** Single object

## See Also

- [Authentication](../../authentication.md) — instructions for using the Authorize button in Swagger UI
