# agent-skills

Claude Code skills for code structure, planning, and writing. Each skill is one directory with a `SKILL.md` file. Some skills add a `references/` directory for longer material.

Claude reads the `description` field in each `SKILL.md` to decide when a skill applies. You can also name a skill directly.

## Skills

### Code structure

| Skill | What it does |
| --- | --- |
| `state-machines` | Replaces boolean-flag soup with a named state enum and a transition table. |
| `adt-types` | Turns anemic records into abstract data types that hide their representation. |
| `clean-modules` | Restores module boundaries: one public surface, one direction of dependency. |
| `focused-refactor` | Applies the three skills above to one bounded concept, in order. |

### Project work

| Skill | What it does |
| --- | --- |
| `project-discovery` | Builds an architecture digest of an unfamiliar repository with tree-sitter. |
| `makefile-actions` | Writes a Makefile that lists and runs the real commands of a project. |
| `design-system` | Sets up design tokens for color, spacing, and type, with light and dark themes. |
| `review-agentic-setup` | Reviews and updates the agent configuration of a project. |

### Thinking and writing

| Skill | What it does |
| --- | --- |
| `backward-planning` | Plans from a clear success outcome back to the goals that cause it. |
| `ste-writing` | Rewrites prose into ASD-STE100 Simplified Technical English. |

## Install

Install skills per project. A project skill lives in `.claude/skills/` inside the repository and is committed with it. Then every collaborator, worktree, and fresh clone gets the same version, and the skill triggers only in projects where it applies.

1. Go to the root of the project.
2. Copy the skills that the project needs.
   ```sh
   SRC=$(mktemp -d)
   git clone --depth 1 https://github.com/epatel/agent-skills.git "$SRC"
   mkdir -p .claude/skills
   cp -R "$SRC/focused-refactor" .claude/skills/
   ```
3. Commit `.claude/skills/`.
4. Use the skill. Skills live-reload, so the running session sees it. If `.claude/skills/` did not exist when the session started, run `/reload-skills` first.

Copy, do not link. A link points into your home directory and breaks for collaborators and fresh clones. Install only the skills that match the work of the project. Each installed skill puts its description into every session of that project.

The setup at https://ai.memention.net/setup does these steps for you and records each skill as `skill:<name>` so that a later refresh can update it.

A personal install in `~/.claude/skills/` loads the skill in every project on the machine and is not shared. Use it only for a skill that you want everywhere and that no collaborator needs.

## Add a skill

1. Make a directory with the name of the skill.
2. Write `SKILL.md` in that directory.
3. Give the file YAML frontmatter with a `name` field and a `description` field.
4. Write the `description` so it states what the skill does and when to use it. Claude matches on this text.
5. Put long reference material in a `references/` directory. Keep `SKILL.md` short.

## License

No license file yet. Ask before you reuse this material.
