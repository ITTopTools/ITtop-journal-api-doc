# Прогресс

Учебный прогресс: записи посещений с оценками и результаты экзаменов.

## Эндпоинты

### GET /progress/operations/student-visits

Записи посещений с оценками за занятие.

**Назначение:** Страница журнала посещений — отображает посещаемость и оценки за каждое занятие. Каждая запись включает статус посещения и отдельные поля оценок для разных видов работ.

**Ответ:** Массив объектов с полями `date_visit`, `lesson_number`, `status_was`, `spec_id`, `teacher_name`, `spec_name`, `lesson_theme`, `control_work_mark`, `home_work_mark`, `lab_work_mark`, `class_work_mark`, `practical_work_mark`, `final_work_mark`.

### GET /progress/operations/student-exams

Результаты экзаменов с оценками и прикреплёнными файлами.

**Назначение:** Страница оценок за экзамены — отображает баллы за экзамены, комментарии преподавателя и прикреплённые файлы.

**Ответ:** Массив объектов с полями `teacher`, `mark`, `mark_type`, `date`, `ex_file_name`, `id_file`, `exam_id`, `file_path`, `comment_teach`, `need_access`, `spec`.

<!-- ?UNSURE: mark_type values not documented — observed 0 and 1 in data -->
