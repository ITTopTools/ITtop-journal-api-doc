# GET /dashboard/chart/progress

Retrieve progress data grouped by chart type.

## Purpose

Used by the dashboard to render multiple progress charts, each identified by a chart type value and containing its own set of data models.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `chart_type` | integer | Chart type identifier |
| `chart_models` | array | Array of chart data models for this type |

Each item in `chart_models` has the same structure as the chart endpoints (see [Average Progress](average-progress.md)).

**Response type:** Array of objects

<!-- ?UNSURE: meaning of `chart_type` integer values is not documented -->

## See Also

- [Average Progress](average-progress.md) — monthly average progress chart
- [Attendance](attendance.md) — monthly attendance chart
