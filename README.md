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

Claude Code loads skills from `~/.claude/skills/`. To install one skill, make a link to it:

1. Change to the skill directory of Claude Code.
   ```sh
   cd ~/.claude/skills
   ```
2. Link the skill you want.
   ```sh
   ln -s ~/Development/claude/agent-skills/state-machines .
   ```
3. Start a new Claude Code session. Claude reads skills at startup.

To install every skill, repeat step 2 for each directory. To use a skill in one project only, link it into `.claude/skills/` inside that project.

## Add a skill

1. Make a directory with the name of the skill.
2. Write `SKILL.md` in that directory.
3. Give the file YAML frontmatter with a `name` field and a `description` field.
4. Write the `description` so it states what the skill does and when to use it. Claude matches on this text.
5. Put long reference material in a `references/` directory. Keep `SKILL.md` short.

## License

No license file yet. Ask before you reuse this material.
