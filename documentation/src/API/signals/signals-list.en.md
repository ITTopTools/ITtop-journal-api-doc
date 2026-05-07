# GET /signal/operations/signals-list

List academic signals and alerts assigned to the student.

## Purpose

Signal feed — shows active alerts, requests, and problems the academy has flagged for the student. Used to display the early warning dashboard.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Signal identifier |
| `date_desired` | string | Desired resolution date |
| `date_start` | string | Date the signal was created |
| `priority` | string | Signal priority level |
| `status` | string | Current signal status |
| `message` | string | Signal message text |
| `initiator_name` | string | Name of the person who initiated the signal |
| `problem_id` | integer | Associated problem type ID |
| `problem_name` | string | Associated problem type name |
| `problem_type` | string | Problem category |
| `days_diff` | integer | Days since the signal was created |
| `theme` | string | Signal theme or topic |

**Response type:** Array of objects

## See Also

- [Problem types](problems-list.md)
