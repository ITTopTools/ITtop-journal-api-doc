# Signals

Academic alert signals and problem indicators — early warning system for academic issues.

## Endpoints

### GET /signal/operations/signals-list

Academic signals/alerts assigned to the student.

**Purpose:** Signal feed — shows active alerts, requests, and problems the academy has flagged for the student.

**Response:** Array of objects with `id`, `date_desired`, `date_start`, `priority`, `status`, `message`, `initiator_name`, `problem_id`, `problem_name`, `problem_type`, `days_diff`, `theme`.

### GET /signal/operations/problems-list

Reference list of problem types used in signals.

**Purpose:** Problem type catalog — maps problem IDs to human-readable titles.

**Response:** Array of objects with `id`, `title`.
