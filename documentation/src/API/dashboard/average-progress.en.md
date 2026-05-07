# GET /dashboard/chart/average-progress

Retrieve monthly average progress chart data.

## Purpose

Used by the dashboard to render the average progress trend chart, comparing current and previous period scores.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Date for the data point (YYYY-MM-DD format) |
| `points` | number | Current period score |
| `previous_points` | number | Previous period score |
| `has_rasp` | boolean | Whether the data relates to a schedule entry |

**Response type:** Array of objects

## See Also

- [Attendance](attendance.md) — similar chart structure for attendance percentage
- [Chart Progress](chart-progress.md) — progress grouped by chart type
