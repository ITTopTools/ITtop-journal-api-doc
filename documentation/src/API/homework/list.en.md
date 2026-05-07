# GET /homework/operations/list

Get a paginated list of homework assignments filtered by status, type, and group.

## Purpose

Main homework list in the homework tab — returns assignments filtered by status, type, and group. This is the primary endpoint driving the homework page UI.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `page` | query | integer | yes | Page number for pagination |
| `status` | query | integer | no | Filter by status: 0=overdue, 1=reviewed, 2=submitted, 3=current, 5=deleted |
| `type` | query | integer | no | 0=regular homework, 1=lab work (identical response structure) |
| `group_id` | query | integer | yes | From `current_group_id` in `/settings/user-info` |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Homework assignment ID |
| `id_spec` | integer | Subject (specialization) ID |
| `id_teach` | integer | Teacher ID |
| `id_group` | integer | Group ID |
| `fio_teach` | string | Teacher's full name |
| `theme` | string | Assignment topic/theme |
| `completion_time` | string \| null | Deadline for completion |
| `creation_time` | string | When the assignment was created |
| `overdue_time` | string \| null | When the assignment became overdue |
| `filename` | string \| null | Original attachment filename |
| `file_path` | string \| null | Path to the attachment |
| `comment` | string \| null | Assignment description/comment |
| `name_spec` | string | Subject name |
| `status` | integer | Assignment status (matches counter_type values) |
| `common_status` | integer | Aggregated status for display |
| `cover_image` | string \| null | Cover image URL or path |
| `homework_stud` | object \| null | Nested student submission (see below) |
| `homework_comment` | object \| null | Nested teacher comment (see below) |

**homework_stud (nested student submission):**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Submission ID |
| `filename` | string \| null | Submitted file name |
| `file_path` | string \| null | Path to the submitted file |
| `tmp_file` | string \| null | Temporary file reference |
| `mark` | string \| null | Grade given by teacher |
| `creation_time` | string | When the student submitted |
| `stud_answer` | string \| null | Student's text answer |
| `auto_mark` | string \| null | Auto-generated mark (e.g. for overdue) |

**homework_comment (nested teacher comment):**

| Field | Type | Description |
|-------|------|-------------|
| `text_comment` | string \| null | Teacher's comment text |
| `attachment` | string \| null | Comment attachment filename |
| `attachment_path` | string \| null | Path to the comment attachment |
| `date_updated` | string \| null | When the comment was last updated |

**Response type:** Array of HomeworkItem objects

## See Also

- [Counters](counters.md) — status counts matching `status` values
- [Group specs](group-specs.md) — subject filter options
- [Evaluation tags](evaluation-tags.md) — homework evaluation tags shown after submission
