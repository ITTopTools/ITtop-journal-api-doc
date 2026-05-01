# Migrate to latest template and fix validator test

## What changed
- Migrated project to latest `main-template-repo` version:
  - Added `CLAUDE.md`, `GEMINI.md`, `LICENSE` — AI agent instructions and license
  - Updated `AGENTS.md` — shared rules for all agents
  - Added `skills/` directory — systematic-debugging, TDD, writing-plans, verification
  - Reorganized `README.md` structure
- Fixed `test_validate_all_for_known_path` — `MODELS` entries must be `(model, is_list)` tuples, not `(model,)`
- Updated `README.md` with deployment instructions, endpoint table, mock server info
- Bumped `pyproject.toml` dependencies

## Why
- Template migration brings standardized AI agent files and project structure
- Validator test was broken after the model registration refactor added `is_list` flag — test expected old tuple format

## Affected files
- `CLAUDE.md` (new)
- `GEMINI.md` (new)
- `LICENSE` (new)
- `AGENTS.md`
- `skills/systematic-debugging.md`
- `skills/test-driven-development.md`
- `skills/writing-plans.md`
- `README.md`
- `pyproject.toml`
- `tests/test_validator.py`
- `uv.lock`
