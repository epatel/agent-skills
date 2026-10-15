# agent-skills

Claude Code skills (one directory per skill, `SKILL.md` + optional `references/`, `scripts/`, `assets/`). Projects install them by copying into `.claude/skills/`, following https://ai.memention.net/setup (source: `../ai-setup`). `README.md` is the skill list that setup reads, so keep it in sync when adding, renaming, or removing a skill.

## Commands

- Check agent docs: `python3 -I ../ai-setup/site/cards/check-agent-docs.py .`
- Smoke-test `project-discovery` (creates a venv in the user cache on first run): follow the "How to run" block in `project-discovery/SKILL.md` with `<ROOT>` = `.`

## Rules

- `name` in the frontmatter matches the directory name. `description` is at most 1024 characters and says when to use the skill.
- Diagrams in skills are mermaid, never ASCII.
- A change to a skill that a project with a copied version should act on needs an `Affects: skill:<name>` item in `../ai-setup/site/cards/setup-changelog.md` (with a version bump in `site/setup`). Otherwise refresh mode never tells those projects to re-copy it. If `../ai-setup/.claude/skills/` holds a copy of the changed skill, update that copy too.
- Claims about how Claude Code loads skills or settings must match `../ai-setup/cards/claude-code-loading.md`.
