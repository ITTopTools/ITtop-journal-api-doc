# Profile

Student profile section — identity information, editable settings, and achievement badges.

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| GET | `/settings/user-info` | Get student identity and group info | [Details](user-info.md) |
| GET | `/profile/operations/settings` | Get editable profile settings | [Details](settings.md) |
| GET | `/profile/statistic/student-achievements` | Get student achievement badges | [Details](achievements.md) |

## Dependencies

- [Auth](../auth/index.md) — all endpoints require a valid JWT token
