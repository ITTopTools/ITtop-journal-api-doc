# Progress

Academic progress: visit records with grades and exam results.

## Endpoints

### GET /progress/operations/student-visits

Visit records with grades per lesson.

**Purpose:** Visit journal page — shows attendance and grades for each lesson. Each entry includes the visit status and separate grade fields for different work types.

**Response:** Array of objects with `date_visit`, `lesson_number`, `status_was`, `spec_id`, `teacher_name`, `spec_name`, `lesson_theme`, `control_work_mark`, `home_work_mark`, `lab_work_mark`, `class_work_mark`, `practical_work_mark`, `final_work_mark`.

### GET /progress/operations/student-exams

Exam results with grades and file attachments.

**Purpose:** Exam grades page — shows exam scores, teacher comments, and attached files.

**Response:** Array of objects with `teacher`, `mark`, `mark_type`, `date`, `ex_file_name`, `id_file`, `exam_id`, `file_path`, `comment_teach`, `need_access`, `spec`.

<!-- ?UNSURE: mark_type values not documented — observed 0 and 1 in data -->
