# Agent Guidelines

> Read this before doing anything. No exceptions.

## Project Context

- **Project:** journal-api-docs
- **Language / Stack:** Python 3.12 / uv / httpx / Pydantic v2 / Faker
- **Infrastructure:** Cloudflare Worker (mock API + proxy to real API)
- **Documentation:** MkDocs Material with swagger-ui-tag plugin
- **Test runner:** pytest (37 tests)
- **Linter / formatter:** ruff

The Cloudflare Worker routes requests: no token returns mock data, with token proxies to the real API, `/auth/login` always proxies first and falls back to mock on 4xx.

---

## Non-Negotiables

- Zero compiler/linter warnings on every commit
- Tests before implementation (RED -> GREEN -> REFACTOR)
- No magic numbers — constants go in a dedicated config/constants file
- English comments only, conversational ("why not what")
- One problem per commit, descriptive commit messages

---

## Workflow

### Before Writing Any Code

1. **Clarify the task.** Ask one focused question if the spec is ambiguous. Don't guess.
2. **Check existing code.** Don't reinvent what's already there.
3. **Write the plan.** For anything >1 file or >30 min of work, write a plan to `devel/plans/YYYY-MM-DD-name.md` first.

### Implementation Loop

```
Write failing test -> confirm it fails -> implement minimal code -> confirm it passes -> commit
```

Never skip the "confirm it fails" step. It proves the test actually catches the bug.

### Before Marking a Task Done

- [ ] All tests pass
- [ ] No new warnings introduced
- [ ] Linter/formatter clean
- [ ] Committed with a clear message

---

## Debugging Protocol

**Find root cause before touching anything.**

1. Read the full error — stack trace, line numbers, error codes
2. Reproduce it reliably
3. Check recent changes (`git diff`, recent commits)
4. Form one hypothesis: *"X is broken because Y"*
5. Make the smallest possible change to test it
6. If 3+ fixes failed -> stop, the architecture is wrong, discuss

Red flags — stop and re-investigate if you're thinking:
- "Just try this and see what happens"
- "Quick fix for now"
- "It's probably X" (without evidence)

---

## File Structure

```
src/          Source code
  collector/  Auth + data collection
  validator/  Pydantic models + validation
  anonymizer/ Faker PII replacement
  publisher/  OpenAPI generation
data/
  raw/        Raw API responses (gitignore)
  examples/   Anonymized examples (committed)
documentation/
  src/        Markdown + openapi.json
  site/       Built site (gitignore, gh-pages)
mock/
  worker.js        Generated Cloudflare Worker
  build_worker.py  Template that generates worker.js
  wrangler.toml    Worker deployment config
devel/
  design/     Design documents
  plans/      Implementation plans
  changelog/  Changelog
  skills/     Agent skill references
tests/        Pytest tests (37 total)
```

---

## CI Pipeline

7 steps in order: tests -> collect -> validate -> anonymize -> publish -> worker -> mkdocs

---

## Skills

When tackling a specific type of task, read the relevant skill file first:

| Situation | Skill file |
|-----------|-----------|
| Something is broken | `devel/skills/systematic-debugging.md` |
| Planning a feature | `devel/skills/writing-plans.md` |
| Code review | `devel/skills/code-review.md` |
| About to claim done | `devel/skills/verification-before-completion.md` |
| Implementing anything | `devel/skills/test-driven-development.md` |

---

## What Not To Do

- Don't add dependencies without asking
- Don't refactor unrelated code "while you're there"
- Don't open PRs without human review of the full diff
- Don't leave TODOs without a linked issue or explanation
- Don't assume — ask
