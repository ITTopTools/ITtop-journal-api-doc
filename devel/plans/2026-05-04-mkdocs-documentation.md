# Plan: MkDocs Documentation Site

> **Status:** Structure done (2026-05-04). Content filling continues in [2026-05-05-documentation-content.md](2026-05-05-documentation-content.md).

## Context

The project currently publishes only `openapi.json` + Swagger UI to GitHub Pages. Swagger shows *structure* (paths, params, schemas) but not *semantics* — what `counter_type: 2` means, why `Origin`/`Referer` headers are required, or how the mock server works. A text documentation site fills that gap.

---

## Stack

| Component | What it does |
|-----------|-------------|
| MkDocs + Material theme | Engine + styling |
| mkdocs-awesome-pages | Auto-navigation from file tree — no manual nav config |
| mkdocs-swagger-ui-tag | Embeds Swagger UI inside an MkDocs page |
| `site_dir: documentation/` | MkDocs writes directly to the folder already deployed by Pages — CI unchanged |

---

## Directory Structure

```
docs/
  index.md              ← Main: what this is, why, quick start
  authentication.md     ← How to get a token, required headers
  mock-server.md        ← Worker explanation: mock vs real mode
  swagger.md            ← Page with embedded Swagger UI
  API/
    dashboard.md
    schedule.md
    homework.md
    progress.md
    library.md
    signals.md
    news.md
    public.md
```

Each `API/` file covers one logical section, not one endpoint. All related endpoints are described together.

---

## API Page Template

Every `API/` file follows the same structure. Example for `homework.md`:

```markdown
# Homework

Brief description of what this section does and when you need it.

## Endpoints overview
Table: method | path | what it does

## GET /count/homework
Description, parameters, example response with field explanations,
specific value meanings (enums, statuses).

## GET /homework/operations/list
...
```

**Focus on semantics** — what `counter_type: 2` means, what `status_was: 3` means. This is what Swagger cannot show and why text docs exist.

---

## Key Pages

### index.md — Entry Point

For someone who knows nothing about the project:

- What is IT Top Journal API
- Why there's no official docs and how this project fills the gap
- 3-step quick start: get token → try Swagger → read docs
- Links to key sections

### authentication.md

- How to obtain a Bearer token via `/auth/login`
- Required headers: `Authorization`, `Origin`, `Referer`
- Token lifecycle (expiry, renewal)

### swagger.md

- Swagger UI embedded via `mkdocs-swagger-ui-tag`
- How to authorize directly in the UI
- Without token → mock data; with token → real API
- Link to `authentication.md` for details

### mock-server.md

Explains the non-obvious Cloudflare Worker setup:

- Worker sits between browser and real API
- No token → returns anonymized mock data (try without logging in)
- With token → proxies to real API with required headers
- Why this exists (CORS, Origin/Referer problem on github.io)

---

## Navigation Order

Newcomer path: **index → authentication → swagger (try it) → specific API section**.
Experienced path: **straight to swagger or the needed API section**.

---

## Implementation Steps

1. Install MkDocs dependencies: `mkdocs`, `mkdocs-material`, `mkdocs-awesome-pages-plugin`, `mkdocs-swagger-ui-tag`
2. Create `mkdocs.yml` at project root with Material theme, awesome-pages plugin, swagger-ui-tag plugin, `site_dir: documentation/`
3. Create `docs/` directory with all `.md` files listed above
4. Write `index.md`, `authentication.md`, `mock-server.md`, `swagger.md`
5. Write each `API/*.md` file based on endpoint data from `src/collector/endpoints.py` and `src/validator/models.py`
6. Verify locally: `mkdocs serve` → check all pages render, Swagger UI loads
7. Verify build: `mkdocs build` → check `documentation/` output is correct
8. Add dependencies to `pyproject.toml` under a `[docs]` extra or similar
9. Commit

---

## Verification

- `mkdocs build` succeeds and writes to `documentation/`
- `mkdocs serve` renders all pages locally
- Swagger UI page loads and displays the spec
- Navigation follows the intended order
- CI (`collect.yml`) still deploys correctly — `site_dir` is the same `documentation/`
