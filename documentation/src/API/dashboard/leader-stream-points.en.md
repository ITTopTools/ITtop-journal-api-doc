# GET /dashboard/progress/leader-stream-points

Retrieve the current student's position in the stream leaderboard.

## Purpose

Used by the dashboard to display the student's rank, total participants, and week/month position changes across the entire stream.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `totalCount` | integer \| null | Total number of students in the stream (can be null) |
| `studentPosition` | integer | Current student's position in the stream |
| `weekDiff` | integer | Position change compared to last week |
| `monthDiff` | integer | Position change compared to last month |

**Response type:** Single object (not a list)

## See Also

- [Leader Stream](leader-stream.md) — full stream leaderboard list
- [Leader Group Points](leader-group-points.md) — student position in group (same structure)
