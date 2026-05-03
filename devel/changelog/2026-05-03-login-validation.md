# Add /auth/login validation and anonymize JWT tokens

## What changed
- Added `LoginResponse` Pydantic model to `src/validator/models.py` (fields: access_token, refresh_token, expires_in_refresh, expires_in_access, user_type, city_data, user_role)
- Registered `/auth/login` in `MODELS` dict in `src/validator/validator.py` (is_list=False)
- Changed `JournalClient.authenticate()` return type from `str` to `dict` — full login response is now saved to `collected[/auth/login]`
- Added JWT detection in `Anonymizer._anonymize_node` — strings matching `xxx.yyy.zzz` base64 pattern are replaced with `fake.sha256()` instead of random string
- Marked all plan checklists as completed (6 plans had stale unchecked items despite code being implemented)

## Why
- Login response was the only endpoint not validated — schema changes would go unnoticed
- JWT tokens in anonymized output were replaced with random strings; now they get consistent sha256 hashes that visually resemble tokens

## Affected files
- `src/validator/models.py`
- `src/validator/validator.py`
- `src/collector/client.py`
- `src/anonymizer/anonymizer.py`
- `devel/plans/*.md` (6 files — checklist updates only)
