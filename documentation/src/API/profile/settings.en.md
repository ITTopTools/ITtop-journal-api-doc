# GET /profile/operations/settings

Retrieve editable student profile settings.

## Purpose

Used by the profile editor form to display and allow modification of student personal information such as address, email, and photo.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Profile record identifier |
| `ful_name` | string | Full name (API typo — note the missing `l`) |
| `address` | string | Student address |
| `date_birth` | string | Date of birth |
| `study` | string | Study information |
| `email` | string | Student email |
| `last_approving_status` | string | Last approval status |
| `form_type` | string | Form type |
| `photo_path` | string | Path to student photo |
| `has_not_approved_data` | boolean | Whether there is unapproved data |
| `has_not_approved_photo` | boolean | Whether there is an unapproved photo |
| `is_email_verified` | boolean | Whether the email is verified |
| `is_phone_verified` | boolean | Whether the phone is verified |
| `fill_percentage` | number | Profile completion percentage |

**Response type:** Single object

<!-- ?UNSURE: exact values for `last_approving_status` and `form_type` are not documented -->

## See Also

- [User Info](user-info.md) — read-only student identity data
