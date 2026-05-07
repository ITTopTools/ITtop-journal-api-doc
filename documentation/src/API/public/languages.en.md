# GET /public/languages

List available UI languages supported by the application.

## Purpose

Language selector reference — lists locales supported by the app. Used to populate the language picker in the UI.

## Parameters

| Param | In | Type | Required | Description |
|-------|----|------|----------|-------------|
| — | — | — | — | No parameters |

## Response

| Field | Type | Description |
|-------|------|-------------|
| `name_mystat` | string | Display name of the language |
| `short_name` | string | Locale code (e.g. "ru") |

**Response type:** Array of objects

## See Also

- [Translations](translations.md)
