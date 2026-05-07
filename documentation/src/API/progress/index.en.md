# Progress

Academic progress tracking: visit records with per-lesson grades and exam results with file attachments.

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| GET | `/progress/operations/student-visits` | Visit records with grades per lesson | [Details](student-visits.md) |
| GET | `/progress/operations/student-exams` | Exam results with grades and files | [Details](student-exams.md) |

## Dependencies

Both endpoints require a valid JWT token from the [Auth](../auth/index.md) section.
