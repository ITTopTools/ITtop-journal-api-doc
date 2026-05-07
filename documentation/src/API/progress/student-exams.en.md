# GET /progress/operations/student-exams

Get exam results with grades and file attachments for the authenticated student.

## Purpose

Exam grades page — shows exam scores, teacher comments, and attached files for each exam the student has taken.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `teacher` | string | Teacher who administered the exam |
| `mark` | string \| null | Exam grade/score |
| `mark_type` | integer | Type of mark (see note below) |
| `date` | string | Exam date |
| `ex_file_name` | string \| null | Name of the exam file |
| `id_file` | integer \| null | File ID |
| `exam_id` | integer | Unique exam identifier |
| `file_path` | string \| null | Path to the attached file |
| `comment_teach` | string \| null | Teacher's comment on the exam |
| `need_access` | boolean | Whether access request is needed for the file |
| `spec` | string | Subject/specialization name |

**Response type:** Array of objects

<!-- ?UNSURE: mark_type values not documented — observed 0 and 1 in data -->

## See Also

- [Student visits](student-visits.md)
