# GET /dashboard/progress/activity

Retrieve the student activity feed.

## Purpose

Used by the dashboard to display a chronological list of student actions, point changes, and achievement unlocks.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Date of the activity |
| `action` | string | Description of the action performed |
| `current_point` | number | Point balance after the action |
| `point_types_id` | integer | Identifier for the point type |
| `point_types_name` | string | Name of the point type |
| `achievements_id` | integer | Identifier for the associated achievement |
| `achievements_name` | string | Name of the associated achievement |
| `achievements_type` | string | Type of the associated achievement |
| `badge` | string | Badge identifier or path |
| `old_competition` | boolean | Whether this relates to an old competition |

**Response type:** Array of objects

## See Also

- [Leader Group](leader-group.md) — group leaderboard rankings
- [Achievements](../profile/achievements.md) — full achievement badge details
