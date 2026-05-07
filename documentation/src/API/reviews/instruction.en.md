# GET /reviews/index/instruction

Get review submission guidelines.

## Purpose

Displays review guidelines to the student before they submit feedback, explaining how reviews should be written.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| — | string \| null | Review instruction text, or `null` when no instruction is available |

**Response type:** Single object (string or null)

## See Also

- [Lesson reviews](list.md)
- [Evaluate lesson](evaluate-lesson.md)
