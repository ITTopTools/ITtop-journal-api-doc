# GET /schedule/operations/get-by-date-range

Get the class schedule for a date range.

## Purpose

Weekly or monthly schedule view — returns lessons between start and end dates inclusive. An empty array is a normal response when no classes fall within the range.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `date_start` | query | string | yes | Start date in `YYYY-MM-DD` format |
| `date_end` | query | string | yes | End date in `YYYY-MM-DD` format |

## Response

Returns the common [ScheduleItem](index.md#scheduleitem-structure) structure.

**Response type:** Array of ScheduleItem objects (empty array is normal)

## See Also

- [Get by date](get-by-date.md)
- [Get by month](get-by-month.md)
