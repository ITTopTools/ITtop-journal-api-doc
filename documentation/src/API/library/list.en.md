# GET /library/operations/list

List learning materials from the library.

## Purpose

Used by the library section of the app to display available learning materials filtered by type and category.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `material_type` | query | int | no | Material type filter (default: 2) |
| `filter_type` | query | int | no | Filter type (default: 0) |
| `recommended_type` | query | int | no | Recommended type (default: 0) |

## Response

| Field | Type | Description |
|-------|------|-------------|
| — | — | Response schema unknown — collected data was empty |

**Response type:** Array of objects

## See Also

- [Library overview](index.md)

<!-- ?UNSURE: parameter meanings inferred from UI; response schema unknown -->
