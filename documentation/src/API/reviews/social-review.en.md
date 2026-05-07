# GET /feedback/social-review/get-review-list

List social review submissions by the student.

## Purpose

Social review tracking — shows which reviews the student has submitted on external platforms, their approval status, and teacher comments.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Review submission status |
| `social_id` | integer | Social review platform identifier |
| `link_id` | integer | Link identifier |
| `link` | string | URL of the submitted review |
| `screen_shot` | string | Screenshot URL of the review |
| `review_id` | integer | Unique review identifier |
| `comment` | string | Teacher comment on the review |
| `teach_name` | string | Teacher name |
| `updated_at` | string | Last update timestamp |
| `is_visibility` | boolean | Whether the review is visible |

**Response type:** Array of objects

## See Also

- [Evaluate lesson](evaluate-lesson.md)
- [Lesson reviews](list.md)
