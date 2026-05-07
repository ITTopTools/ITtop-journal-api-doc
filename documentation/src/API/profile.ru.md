# Профиль

Профиль ученика и личные настройки.

## Конечные точки

### GET /settings/user-info

Возвращает профиль аутентифицированного ученика: имя, группу, поток, ID текущей группы и другие персональные данные.

**Назначение:** Основная конечная точка идентификации ученика. Значение `current_group_id` из этого ответа используется как параметр `group_id` в конечных точках домашнего задания.

**Ответ:** Объект с полями `student_id`, `full_name`, `group_name`, `stream_name`, `level`, `age`, `gender`, `birthday`, `last_date_visit`, `registration_date`, `current_group_id`, `current_group_status`, `stream_id`, `achieves_count`, `photo`, `study_form_short_name`, `groups` (массив) и другими полями.

### GET /profile/operations/settings

Редактируемые поля профиля ученика.

**Назначение:** Страница редактирования профиля — имя, адрес, электронная почта, подтверждение телефона, загрузка фото, процент заполнения профиля.

**Ответ:** Объект с полями `id`, `ful_name` (опечатка API вместо `full_name`), `address`, `date_birth`, `study`, `email`, `last_approving_status`, `form_type`, `photo_path`, `has_not_approved_data`, `has_not_approved_photo`, `is_email_verified`, `is_phone_verified`, `fill_percentage`.

<!-- ?UNSURE: fields like last_approving_status and form_type exact values are not documented -->

### GET /profile/statistic/student-achievements

Достижения, полученные учеником (значки, этапы).

**Назначение:** Отображение достижений на странице профиля. Каждое достижение имеет `translate_key` для метки в интерфейсе и список `achieve_points`.

**Ответ:** Массив объектов с полями `id`, `translate_key`, `is_active`, `achieve_points`.
