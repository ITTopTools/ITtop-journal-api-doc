# GET /news/operations/latest-news

Get the latest news items from the academy.

## Purpose

News feed on the dashboard — shows announcements, events, and updates from the academy. Includes read/unread tracking per student.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id_bbs` | integer | News item identifier |
| `theme` | string | News item title/topic |
| `time` | string | Publication timestamp |
| `viewed` | boolean | Whether the student has read this item |

**Response type:** Array of objects

## See Also

- [News overview](index.md)
