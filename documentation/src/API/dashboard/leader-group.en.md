# GET /dashboard/progress/leader-group

Retrieve the group leaderboard rankings.

## Purpose

Used by the dashboard to display a ranked list of students within the student's current group based on their point totals.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Student identifier |
| `full_name` | string | Full name of the student |
| `photo_path` | string | Path to the student photo |
| `position` | integer | Rank position in the group |
| `amount` | number | Total points |

**Response type:** Array of objects

## See Also

- [Leader Stream](leader-stream.md) — same structure for stream-wide leaderboard
- [Leader Group Points](leader-group-points.md) — current student's position in group
