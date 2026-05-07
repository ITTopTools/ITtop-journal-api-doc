# GET /settings/group-specs

Get the subjects (specs) linked to the student's current group.

## Purpose

Subject filter/selector in the homework UI — shows which subjects the current group studies, allowing the student to filter homework by subject.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Subject (specialization) ID |
| `name` | string | Full subject name |
| `short_name` | string | Abbreviated subject name |

**Response type:** Array of objects

## See Also

- [Group history](group-history.md) — all groups with their specs
- [Homework list](list.md) — can be filtered by subject via `id_spec`
