# GET /count/homework

Get status counters for homework items.

## Purpose

Tab badges on the homework page — shows how many items are in each status category, enabling the frontend to display badge numbers on status tabs.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `counter_type` | integer | Status category identifier (see table below) |
| `counter` | integer | Number of items in this category |

**counter_type values:**

| Value | Meaning |
|-------|---------|
| 0 | Overdue — deadline passed, auto-fail grade assigned |
| 1 | Reviewed by teacher — has a grade |
| 2 | Submitted — awaiting teacher review |
| 3 | Current — not yet submitted by student |
| 4 | Total across all types |
| 5 | Deleted by teacher — was submitted but rejected |

**Response type:** Array of objects

## See Also

- [Homework list](list.md) — filtered by status values matching `counter_type`
- [Group specs](group-specs.md) — subject filter for to refine the list
