# GET /dashboard/progress/leader-group-points

Retrieve the current student's position in the group leaderboard.

## Purpose

Used by the dashboard to display the student's rank, total participants, and week/month position changes within their group.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `totalCount` | integer | Total number of students in the group |
| `studentPosition` | integer | Current student's position in the group |
| `weekDiff` | integer | Position change compared to last week |
| `monthDiff` | integer | Position change compared to last month |

**Response type:** Single object (not a list)

## See Also

- [Leader Group](leader-group.md) — full group leaderboard list
- [Leader Stream Points](leader-stream-points.md) — student position in stream (same structure)
