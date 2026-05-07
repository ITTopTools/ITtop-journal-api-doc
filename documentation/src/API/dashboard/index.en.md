# Dashboard

Dashboard overview section — charts, leaderboards, activity feed, and upcoming exams.

## Endpoints

| Method | Path | Summary | Link |
|--------|------|---------|------|
| GET | `/dashboard/chart/average-progress` | Monthly average progress chart | [Details](average-progress.md) |
| GET | `/dashboard/chart/attendance` | Monthly attendance chart | [Details](attendance.md) |
| GET | `/dashboard/chart/progress` | Progress grouped by chart type | [Details](chart-progress.md) |
| GET | `/dashboard/progress/activity` | Activity feed | [Details](activity.md) |
| GET | `/dashboard/progress/leader-group` | Group leaderboard | [Details](leader-group.md) |
| GET | `/dashboard/progress/leader-stream` | Stream leaderboard | [Details](leader-stream.md) |
| GET | `/dashboard/progress/leader-group-points` | Student position in group | [Details](leader-group-points.md) |
| GET | `/dashboard/progress/leader-stream-points` | Student position in stream | [Details](leader-stream-points.md) |
| GET | `/dashboard/info/future-exams` | Upcoming exams list | [Details](future-exams.md) |

## Chart Endpoints

The chart-type endpoints (`average-progress`, `attendance`, `chart-progress`) share a similar response structure based on date, points, and previous_points values for rendering trend lines.

## Dependencies

- [Auth](../auth/index.md) — all endpoints require a valid JWT token
