# GET /public/translations

Get localization key-value pairs for the given language.

## Purpose

UI translation strings — returns a flat dictionary of translation keys mapped to localized strings. Used by the frontend to render all user-facing text in the selected language.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| `language` | query | string | yes | Locale code (e.g. "ru") |

## Response

| Field | Type | Description |
|-------|------|-------------|
| *(dynamic keys)* | string | Translation key mapped to its localized string value |

**Response type:** Single object (flat dictionary — thousands of keys)

## See Also

- [Languages](languages.md)
- [Tags](tags.md)
