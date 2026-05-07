# GET /schedule/operations/get-by-date

Get the class schedule for a specific date.

## Purpose

Daily schedule view — shows lessons with times, teacher, subject, and room info for a single day.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `date_filter` | query | string | yes | Date in `YYYY-MM-DD` format |

## Response

Returns the common [ScheduleItem](index.md#scheduleitem-structure) structure.

**Response type:** Array of ScheduleItem objects

## See Also

- [Get by date range](get-by-date-range.md)
- [Get by month](get-by-month.md)
