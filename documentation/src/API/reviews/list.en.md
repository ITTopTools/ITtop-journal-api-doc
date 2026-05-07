# GET /reviews/index/list

List reviews written about the student's lessons.

## Purpose

Displays teacher reviews on the student's profile page. Each entry includes the review date, message text, subject, and teacher name.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Review date |
| `message` | string | Review text |
| `spec` | string | Short subject name |
| `full_spec` | string | Full subject name |
| `teacher` | string | Teacher name |

**Response type:** Array of objects

## See Also

- [Review instruction](instruction.md)
- [Evaluate lesson](evaluate-lesson.md)
