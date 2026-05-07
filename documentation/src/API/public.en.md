# Public

Public reference data — no authentication required.

## Endpoints

### GET /public/languages

Available UI languages.

**Purpose:** Language selector reference — lists locales supported by the app.

**Response:** Array of objects with `name_mystat` (display name), `short_name` (locale code, e.g. "ru").

### GET /public/translations

Localization key-value pairs for the given language.

**Purpose:** UI translation strings. Returns a flat dictionary of translation keys to translated strings.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `language` | string | Locale code (e.g. "ru"). Only Russian was collected; other locales share the same schema. |

**Response:** Flat dictionary of string keys to string values (translation map).

### GET /public/tags

Reference list of public tags.

**Purpose:** Tag reference data used across the app.

**Response:** Array of tag items.

<!-- ?UNSURE: response schema unknown — collected data returned an empty array -->
