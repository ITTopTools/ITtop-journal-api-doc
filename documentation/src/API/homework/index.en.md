# Homework

Homework assignments, status counters, homework evaluation tags, and group-related settings for the homework tab.

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| GET | `/count/homework` | Status counters for homework | [Details](counters.md) |
| GET | `/homework/settings/group-history` | Student's groups with subjects | [Details](group-history.md) |
| GET | `/settings/group-specs` | Subjects of the current group | [Details](group-specs.md) |
| GET | `/homework/evaluation/operations/get-tags` | Homework evaluation tags | [Details](evaluation-tags.md) |
| GET | `/homework/operations/list` | Paginated homework list | [Details](list.md) |

## Dependencies

The homework data flow relies on endpoints from other sections. The relationship is:

```
/settings/user-info
  |
  |-- current_group_id ──► group_id param for /homework/operations/list
  |
/settings/group-specs
  |
  |-- subject list ──► filter/selector in the homework UI
  |
/count/homework
  |
  |-- status counters ──► badge numbers on homework tabs
```

1. **`/settings/user-info`** (profile section) provides `current_group_id`, which must be passed as the `group_id` parameter when calling `/homework/operations/list`.
2. **`/settings/group-specs`** (this section) returns the subjects available in the student's current group, used for the subject filter in the homework UI.
3. **`/count/homework`** (this section) returns status counters that drive the badge numbers displayed on homework tab headers.
