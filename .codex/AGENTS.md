# Codex Setup

## First-Time Setup

If you haven't installed superpowers skills globally:

```bash
git clone https://github.com/obra/superpowers.git ~/.codex/superpowers
mkdir -p ~/.agents/skills
ln -s ~/.codex/superpowers/skills ~/.agents/skills/superpowers
```

## Per-Project Instructions

Read `../AGENTS.md` before starting any task in this project.

## Style

- Prefer explicit over implicit
- No `auto` where type clarity matters (C++)
- Descriptive variable names, no single-letter variables outside loops
- If you're unsure about a decision — ask, don't assume

## Commit Style

```
type: short description

- optional bullet if more context needed
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`
