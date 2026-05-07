# Homework

Homework assignments, counters, self-evaluation tags, and group-related settings for the DZ (homework) tab.

## Endpoints

### GET /count/homework

Count of homework items per status type.

**Purpose:** Tab badges on the homework page — shows how many items are in each status category.

**Response:** Array of objects with `counter_type`, `counter`.

**counter_type values:**

| Value | Meaning |
|-------|---------|
| 0 | Overdue — deadline passed, auto-fail grade assigned |
| 1 | Reviewed by teacher — has a grade |
| 2 | Submitted — awaiting teacher review |
| 3 | Current — not yet submitted by student |
| 4 | Total across all types |
| 5 | Deleted by teacher — was submitted but rejected |

### GET /homework/settings/group-history

Student's groups with their subjects (specs).

**Purpose:** Group switcher in the DZ tab. Shows all groups the student belongs to, with subjects for each.

**Response:** Array of objects with `id`, `name`, `specs` (array of `GroupSpecItem`).

Note: `group_id` for homework requests comes from `current_group_id` in `/settings/user-info`, not from this endpoint.

### GET /settings/group-specs

Subjects (specs) linked to the student's current group.

**Purpose:** Subject filter/selector for homework — shows which subjects the current group studies.

**Response:** Array of objects with `id`, `name`, `short_name`.

### GET /homework/evaluation/operations/get-tags

Tags for the homework self-evaluation form.

**Purpose:** Self-assessment tags shown to the student after submitting homework.

**Response:** Array of objects with `id`, `translate_key`, `type`.

### GET /homework/operations/list

Paginated list of homework assignments.

**Purpose:** Main homework list in the DZ tab. Returns assignments filtered by status, type, and group.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `page` | int | Page number for pagination |
| `status` | int | Filter: 0=overdue, 1=reviewed, 2=submitted, 3=current, 5=deleted |
| `type` | int | 0=regular homework, 1=lab work (identical response structure) |
| `group_id` | int | From `current_group_id` in `/settings/user-info` |

**Response:** Array of `HomeworkItem` objects with `id`, `id_spec`, `id_teach`, `id_group`, `fio_teach`, `theme`, `completion_time`, `creation_time`, `overdue_time`, `filename`, `file_path`, `comment`, `name_spec`, `status`, `common_status`, `cover_image`, `homework_stud` (nested submission), `homework_comment` (nested teacher comment).
