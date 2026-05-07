# Dashboard

Overview data rendered on the student's main dashboard page: progress charts, attendance, leaderboards, and upcoming exams.

## Endpoints

### GET /dashboard/chart/average-progress

Monthly average progress values for the student.

**Purpose:** Renders the progress line chart on the main dashboard. `points` is the current month's value, `previous_points` is the prior month.

**Response:** Array of objects with `date`, `points`, `previous_points`, `has_rasp`.

### GET /dashboard/chart/attendance

Monthly attendance percentages for the student's group.

**Purpose:** Renders the attendance chart on the main dashboard. `points` is the attendance percentage for the given month.

**Response:** Array of objects with `date`, `points`, `previous_points`, `has_rasp`.

### GET /dashboard/chart/progress

Progress chart data grouped by chart type.

**Purpose:** Multi-chart dashboard view — each group represents a different metric type. `chart_models` has the same structure as average-progress items.

**Response:** Array of objects with `chart_type` (int), `chart_models` (array of date/points items).

<!-- ?UNSURE: meaning of each chart_type value is not documented by the API -->

### GET /dashboard/progress/activity

Activity feed with points, achievements, and badges.

**Purpose:** Shows recent actions on the dashboard activity section — earned points, unlocked achievements.

**Response:** Array of objects with `date`, `action`, `current_point`, `point_types_id`, `point_types_name`, `achievements_id`, `achievements_name`, `achievements_type`, `badge`, `old_competition`.

### GET /dashboard/progress/leader-group

Top students in the student's group ranked by points.

**Purpose:** Group leaderboard on the dashboard. Each entry has position, name, photo, and total points.

**Response:** Array of objects with `id`, `full_name`, `photo_path`, `position`, `amount`.

### GET /dashboard/progress/leader-stream

Top students across the entire stream ranked by points.

**Purpose:** Stream-wide leaderboard. Same structure as group leaderboard but covering all groups in the stream.

**Response:** Array of objects with `id`, `full_name`, `photo_path`, `position`, `amount`.

### GET /dashboard/progress/leader-group-points

Current student's position and point stats within the group.

**Purpose:** Student's rank card on the dashboard — shows group position, total members, and weekly/monthly point changes.

**Response:** Object with `totalCount` (group size), `studentPosition`, `weekDiff`, `monthDiff`.

### GET /dashboard/progress/leader-stream-points

Current student's position and point stats within the stream.

**Purpose:** Same as leader-group-points but for the whole stream. `totalCount` can be null.

**Response:** Object with `totalCount`, `studentPosition`, `weekDiff`, `monthDiff`.

### GET /dashboard/info/future-exams

List of upcoming exams.

**Purpose:** Upcoming exams alert on the dashboard.

**Response:** Array of objects with `spec` (subject name), `date`.
