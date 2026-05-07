# Profile

Student profile and personal settings.

## Endpoints

### GET /settings/user-info

Returns the authenticated student's profile: name, group, stream, current group ID, and other personal details.

**Purpose:** Main student identity endpoint. `current_group_id` from this response is used as the `group_id` parameter in homework endpoints.

**Response:** Object with `student_id`, `full_name`, `group_name`, `stream_name`, `level`, `age`, `gender`, `birthday`, `last_date_visit`, `registration_date`, `current_group_id`, `current_group_status`, `stream_id`, `achieves_count`, `photo`, `study_form_short_name`, `groups` (array), and other fields.

### GET /profile/operations/settings

Editable student profile fields.

**Purpose:** Profile editing page — name, address, email, phone verification, photo upload, profile completion percentage.

**Response:** Object with `id`, `ful_name` (API typo for `full_name`), `address`, `date_birth`, `study`, `email`, `last_approving_status`, `form_type`, `photo_path`, `has_not_approved_data`, `has_not_approved_photo`, `is_email_verified`, `is_phone_verified`, `fill_percentage`.

<!-- ?UNSURE: fields like last_approving_status and form_type exact values are not documented -->

### GET /profile/statistic/student-achievements

Achievements earned by the student (badges, milestones).

**Purpose:** Achievement display on the profile page. Each achievement has a `translate_key` for the UI label and `achieve_points` list.

**Response:** Array of objects with `id`, `translate_key`, `is_active`, `achieve_points`.
