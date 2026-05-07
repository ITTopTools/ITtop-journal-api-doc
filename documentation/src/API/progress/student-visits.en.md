# GET /progress/operations/student-visits

Get visit records with per-lesson grades for the authenticated student.

## Purpose

Visit journal page — shows attendance and grades for each lesson. Each entry includes the visit status and separate grade fields for different work types (control work, homework, lab work, class work, practical work, final work).

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `date_visit` | string | Date of the visit (`YYYY-MM-DD`) |
| `lesson_number` | integer | Lesson number within the day |
| `status_was` | string | Visit/attendance status |
| `spec_id` | integer | Subject (specialization) ID |
| `teacher_name` | string | Full name of the teacher |
| `spec_name` | string | Subject name |
| `lesson_theme` | string | Topic/theme of the lesson |
| `control_work_mark` | string \| null | Grade for the control work |
| `home_work_mark` | string \| null | Grade for the homework |
| `lab_work_mark` | string \| null | Grade for the lab work |
| `class_work_mark` | string \| null | Grade for the class work |
| `practical_work_mark` | string \| null | Grade for the practical work |
| `final_work_mark` | string \| null | Grade for the final work |

**Response type:** Array of objects

## See Also

- [Student exams](student-exams.md)
