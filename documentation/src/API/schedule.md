# Schedule

Class schedule by date and date range.

## Endpoints

### GET /schedule/operations/get-by-date

Class schedule for a specific date.

**Purpose:** Daily schedule view — shows lessons with times, teacher, subject, and room info.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `date_filter` | string | Date in `YYYY-MM-DD` format |

**Response:** Array of objects with `date`, `lesson` (lesson number), `started_at`, `finished_at`, `teacher_name`, `subject_name`, `room_name`.

### GET /schedule/operations/get-by-date-range

Class schedule for a date range.

**Purpose:** Weekly/monthly schedule view — returns lessons between start and end dates inclusive. Returns an empty array if no classes fall within the range.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `date_start` | string | Start date in `YYYY-MM-DD` format |
| `date_end` | string | End date in `YYYY-MM-DD` format |

**Response:** Array of lesson objects (same structure as get-by-date). Empty array is normal for date ranges with no classes.

### GET /schedule/operations/get-month

Class schedule for the month containing the given date.

**Purpose:** Monthly schedule overview — same item structure as get-by-date.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `date_filter` | string | Any date in `YYYY-MM-DD` format within the target month |

**Response:** Array of lesson objects (same structure as get-by-date).
