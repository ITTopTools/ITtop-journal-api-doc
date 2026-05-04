# Plan: Documentation Content

## What

Fill in the 8 API section pages under `documentation/src/API/` with real endpoint details.

## Focus

What Swagger cannot show — **semantics**:
- What `counter_type: 2` means
- What `status_was: 3` means
- What `gender`, `group_status` values represent
- Field-by-field explanations of response structures

## Pages

Each API page follows the template:
1. Section overview (what this group does, when you need it)
2. Endpoints table (method | path | description)
3. Per-endpoint: parameters, response fields, enum value meanings

## Source data

- Endpoint registry: `src/collector/endpoints.py`
- Pydantic models: `src/validator/models.py`
- Example responses: `data/examples/latest.json`

## Verification

- `mkdocs build` succeeds
- All API pages render with tables and descriptions
- No broken internal links
