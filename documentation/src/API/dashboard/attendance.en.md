# GET /dashboard/chart/attendance

Retrieve monthly attendance percentage chart data.

## Purpose

Used by the dashboard to render the attendance trend chart, comparing current and previous period attendance rates.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Date for the data point (YYYY-MM-DD format) |
| `points` | number | Current period attendance percentage |
| `previous_points` | number | Previous period attendance percentage |
| `has_rasp` | boolean | Whether the data relates to a schedule entry |

**Response type:** Array of objects

## See Also

- [Average Progress](average-progress.md) — similar chart structure for average progress
- [Chart Progress](chart-progress.md) — progress grouped by chart type
