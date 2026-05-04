# Project Restructure and MkDocs Setup

## What changed

- Moved `skills/` → `devel/skills/` — skill references belong under devel with plans, design, changelog
- Moved `scripts/build_worker.py` → `mock/build_worker.py` — single script doesn't need its own directory
- Moved `devel/branch-strategy.md` → `devel/design/08-branch-strategy.md` — architectural decision belongs with design docs
- Removed `src/.gitkeep` — directory has real content now
- Replaced generic template READMEs in `src/` and `tests/` with project-specific descriptions
- Cleaned `.claude/settings.local.json` — removed stale pip/python permissions, one-off pytest command
- Added `.pytest_cache/` and `.ruff_cache/` to `.gitignore`
- Set up MkDocs documentation structure under `documentation/`:
  - `documentation/src/` — markdown source + openapi.json (MkDocs docs_dir)
  - `documentation/site/` — built site (MkDocs site_dir, gitignored, deployed to Pages)
- Removed tracked `documentation/index.html` and `documentation/openapi.json` (now MkDocs-generated)
- Updated `src/publisher/builder.py` — openapi.json now written to `documentation/src/`
- Added `mkdocs build` step to CI and changed `publish_dir` to `./documentation/site`
- Created stub documentation pages: index, authentication, mock-server, swagger + 8 API sections
- Added MkDocs with Material theme (deep-purple palette, dark/light toggle, nav tabs, search)

## Why

- `skills/` at root level was orphaned — logically part of `devel/` infrastructure
- `scripts/` with one file is noise — `mock/` already owns the worker domain
- Branch strategy is an architectural decision, not a standalone document
- Template READMEs confused newcomers with references to non-existent files (parser.py, C++, Rust)
- MkDocs enables text documentation alongside Swagger — semantics that OpenAPI can't express
- Keeping all documentation under `documentation/` makes the directory self-contained

## Affected files

- `skills/*.md` → `devel/skills/*.md`
- `scripts/build_worker.py` → `mock/build_worker.py`
- `devel/branch-strategy.md` → `devel/design/08-branch-strategy.md`
- `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `devel/init.md`, `devel/plans/init.md` — updated paths
- `.claude/settings.local.json` — cleaned permissions
- `.gitignore` — added cache dirs and documentation/site/
- `src/README.md`, `tests/README.md` — project-specific content
- `src/.gitkeep` — removed
- `documentation/index.html`, `documentation/openapi.json` — untracked (MkDocs-generated)
- `documentation/src/` — new markdown source tree
- `mkdocs.yml` — new
- `src/publisher/builder.py` — save path updated
- `.github/workflows/collect.yml` — mkdocs build + publish_dir change
- `pyproject.toml` — docs dependency group
