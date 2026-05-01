# Add homework endpoints to main pipeline

## What changed
- Added 4 homework endpoints to `ENDPOINTS` list in `src/collector/endpoints.py`:
  - `/homework/settings/group-history` — student's groups with subjects
  - `/settings/group-specs` — subjects linked to current group
  - `/homework/evaluation/operations/get-tags` — self-evaluation tags
  - `/homework/operations/list` — homework list (with params: page, status, type, group_id)
- Added 6 Pydantic models to `src/validator/models.py`:
  - `GroupSpecItem` — for `/settings/group-specs`
  - `HomeworkGroupHistoryItem` — for `/homework/settings/group-history` (uses `list[GroupSpecItem]`)
  - `HomeworkEvalTagItem` — for `/homework/evaluation/operations/get-tags`
  - `HomeworkStudItem` — nested object in homework responses
  - `HomeworkCommentItem` — nested object in homework responses
  - `HomeworkItem` — main homework list item (uses `HomeworkStudItem`, `HomeworkCommentItem`)
- Registered 4 new models in `MODELS` dict in `src/validator/validator.py` (all `is_list=True`)
- Added `pytest-asyncio` to dev dependencies (was missing — 4 async tests in `test_client.py` were failing)
- Added detailed comments to `/count/homework` (counter_type meanings) and homework endpoints in `endpoints.py`
- Updated generated `data/examples/latest.json` and `documentation/openapi.json`

## Why
- Temporary file `endpoints_homework_new.py` was used to collect the homework dataset separately; now the endpoints are merged into the main pipeline so they get collected, validated, and documented automatically
- Without `pytest-asyncio`, async test functions could not run at all — they were silently skipped

## Affected files
- `src/collector/endpoints.py`
- `src/validator/models.py`
- `src/validator/validator.py`
- `pyproject.toml`
- `uv.lock`
- `data/examples/latest.json`
- `documentation/openapi.json`
