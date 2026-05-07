# GET /settings/user-info

Retrieve the main student identity and group information.

## Purpose

Used by the student profile page to display the student's name, group, stream, level, and other identity details.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `student_id` | integer | Student identifier |
| `full_name` | string | Full name of the student |
| `group_name` | string | Name of the current group |
| `stream_name` | string | Name of the stream |
| `level` | string | Current study level |
| `age` | integer | Student age |
| `gender` | string | Student gender |
| `birthday` | string | Date of birth |
| `last_date_visit` | string | Date of last visit |
| `registration_date` | string | Date of registration |
| `current_group_id` | integer | ID of the current group — used as `group_id` in homework endpoints |
| `current_group_status` | string | Status of the current group |
| `stream_id` | integer | Stream identifier |
| `achieves_count` | integer | Number of achievements |
| `photo` | string | URL or path to student photo |
| `study_form_short_name` | string | Short name of the study form |
| `groups` | array | List of groups the student belongs to |

**Response type:** Single object

## See Also

- [Settings](settings.md) — editable profile fields
- [Achievements](achievements.md) — student badge details
