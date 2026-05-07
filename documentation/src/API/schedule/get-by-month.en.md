# GET /schedule/operations/get-month

Get the class schedule for the month containing a given date.

## Purpose

Monthly schedule overview — shows all lessons for the entire month that contains the specified date.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `date_filter` | query | string | yes | Any date in `YYYY-MM-DD` format within the target month |

## Response

Returns the common [ScheduleItem](index.md#scheduleitem-structure) structure.

**Response type:** Array of ScheduleItem objects

## See Also

- [Get by date](get-by-date.md)
- [Get by date range](get-by-date-range.md)
