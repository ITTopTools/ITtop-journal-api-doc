# Library

Learning materials and library resources.

## Endpoints

### GET /library/operations/list

Learning materials from the library.

**Purpose:** Material list in the library section of the app.

**Parameters:**

| Param | Type | Description |
|-------|------|-------------|
| `material_type` | int | Filter value (default: 2) |
| `filter_type` | int | Filter value (default: 0) |
| `recommended_type` | int | Filter value (default: 0) |

**Response:** Array of material items.

<!-- ?UNSURE: material_type/filter_type/recommended_type values are inferred from UI defaults, not documented; response schema unknown — collected data was empty -->
