# GET /homework/evaluation/operations/get-tags

Get homework evaluation tags.

## Purpose

Homework evaluation tags shown to the student after submitting homework — the student selects tags that describe their confidence and effort level.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| *(none)* | | | | This endpoint takes no parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Tag ID |
| `translate_key` | string | Translation key for i18n rendering |
| `type` | integer | Tag type/category |

**Response type:** Array of objects

## See Also

- [Homework list](list.md) — where tags are used after submission
