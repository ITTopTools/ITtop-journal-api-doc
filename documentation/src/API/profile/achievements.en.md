# GET /profile/statistic/student-achievements

Retrieve student achievement badges and their point breakdowns.

## Purpose

Used by the student profile page to display earned badges and associated point values.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Achievement identifier |
| `translate_key` | string | Localization key for the achievement name |
| `is_active` | boolean | Whether the achievement is currently active |
| `achieve_points` | array | List of point entries for this achievement |

Each item in `achieve_points`:

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Point entry identifier |
| `points_count` | integer | Number of points awarded |

**Response type:** Array of objects

## See Also

- [User Info](user-info.md) — student identity including `achieves_count` summary
