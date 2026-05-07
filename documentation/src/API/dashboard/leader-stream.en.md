# GET /dashboard/progress/leader-stream

Retrieve the stream leaderboard rankings.

## Purpose

Used by the dashboard to display a ranked list of students across the entire stream based on their point totals.

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
| `position` | integer | Rank position in the stream |
| `amount` | number | Total points |

**Response type:** Array of objects

## See Also

- [Leader Group](leader-group.md) — same structure for group-level leaderboard
- [Leader Stream Points](leader-stream-points.md) — current student's position in stream
