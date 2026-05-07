# Schedule

Class schedule by date, date range, or month. All three endpoints return the same ScheduleItem structure described below.

<a id="scheduleitem-structure"></a>
## ScheduleItem Structure

Every endpoint in this section returns an array of objects with the following fields:

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Lesson date (`YYYY-MM-DD`) |
| `lesson` | integer | Lesson number within the day |
| `started_at` | string | Lesson start time |
| `finished_at` | string | Lesson end time |
| `teacher_name` | string | Full name of the teacher |
| `subject_name` | string | Name of the subject |
| `room_name` | string | Room/auditorium name |

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| GET | `/schedule/operations/get-by-date` | Get schedule for a date | [Details](get-by-date.md) |
| GET | `/schedule/operations/get-by-date-range` | Get schedule for a date range | [Details](get-by-date-range.md) |
| GET | `/schedule/operations/get-month` | Get schedule for a month | [Details](get-by-month.md) |
