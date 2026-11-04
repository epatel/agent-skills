# agent-skills

Claude Code skills (one directory per skill, `SKILL.md` + optional `references/`, `scripts/`, `assets/`). Projects install them by copying into `.claude/skills/`, following https://ai.memention.net/setup (source: `../ai-setup`). `README.md` is the skill list that setup reads, so keep it in sync when adding, renaming, or removing a skill.

## Commands

- Check agent docs: `python3 -I ../ai-setup/site/cards/check-agent-docs.py .`
- Smoke-test `project-discovery` (creates a venv in the user cache on first run): follow the "How to run" block in `project-discovery/SKILL.md` with `<ROOT>` = `.`

## Rules

- `description` says when to use the skill. A hook (`.claude/hooks/check-skill.py`) checks after each edit that `name` matches the directory, `description` is at most 1024 characters, README lists the skill, and `.claude/skills/<name>` still matches its source — fix what it reports.
- `.claude/skills/review-agentic-setup` is this project's installed copy: re-copy it after changing `review-agentic-setup/`.
- Diagrams in skills are mermaid, never ASCII.
- A change to a skill that a project with a copied version should act on needs an `Affects: skill:<name>` item in `../ai-setup/site/cards/setup-changelog.md` (with a version bump in `site/setup`). Otherwise refresh mode never tells those projects to re-copy it. If `../ai-setup/.claude/skills/` holds a copy of the changed skill, update that copy too.
- Claims about how Claude Code loads skills or settings must match `../ai-setup/cards/claude-code-loading.md`.

## Cards

- [standing-defaults](cards/standing-defaults.md) — adding a Python script or dependency to a skill, or a skill that stores data
