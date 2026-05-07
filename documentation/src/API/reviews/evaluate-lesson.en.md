# GET /feedback/students/evaluate-lesson-list

List lessons available for student evaluation.

## Purpose

Used by the feedback form to show past lessons where the student can rate the teacher. Each entry has lesson date, teacher name, and subject.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `key` | string | Unique lesson identifier |
| `date_visit` | string | Date the lesson took place |
| `fio_teach` | string | Teacher full name |
| `spec_name` | string | Subject name |
| `teach_photo` | string | Teacher photo URL |

**Response type:** Array of objects

## See Also

- [Lesson reviews](list.md)
- [Social reviews](social-review.md)
