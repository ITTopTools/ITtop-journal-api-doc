# GET /signal/operations/problems-list

Get the reference list of problem types used in signals.

## Purpose

Problem type catalog — maps problem IDs to human-readable titles. Used to display problem type labels alongside signal data.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Problem type identifier |
| `title` | string | Human-readable problem type title |

**Response type:** Array of objects

## See Also

- [Signals list](signals-list.md)
