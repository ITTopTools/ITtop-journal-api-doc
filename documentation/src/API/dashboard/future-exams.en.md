# GET /dashboard/info/future-exams

Retrieve a list of upcoming exams.

## Purpose

Used by the dashboard to display scheduled future exams for the student, including subject and date.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `spec` | string | Exam subject or specialty |
| `date` | string | Exam date |

**Response type:** Array of objects

## See Also

- [User Info](../profile/user-info.md) — student group and stream information relevant to exam scheduling
