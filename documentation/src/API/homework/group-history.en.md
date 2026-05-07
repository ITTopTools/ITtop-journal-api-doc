# GET /homework/settings/group-history

Get the student's groups with their subjects for the group switcher.

## Purpose

Group switcher in the homework tab — shows all groups the student belongs to, with subjects (specs) for each group. Used to let the student switch between groups in the UI.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Group ID |
| `name` | string | Group name |
| `specs` | array | Nested array of GroupSpecItem objects (see below) |

**GroupSpecItem (nested in `specs`):**

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Subject (specialization) ID |
| `name` | string | Full subject name |
| `short_name` | string | Abbreviated subject name |

**Response type:** Array of objects

**Note:** This endpoint is NOT used for `group_id` resolution. The `group_id` parameter for homework requests comes from `current_group_id` in `/settings/user-info`.

## See Also

- [Group specs](group-specs.md) — subjects of the current group only
- [Homework list](list.md) — uses `group_id` from user-info
