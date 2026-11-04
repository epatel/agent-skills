#!/usr/bin/env python3
"""PostToolUse hook: check a skill after an edit.

- <skill>/SKILL.md: frontmatter `name` matches the directory, `description`
  is present and at most 1024 characters, README.md lists the skill.
- Any file under <skill>/: an installed copy in .claude/skills/<skill> or
  ../ai-setup/.claude/skills/<skill>, if present, must still match the source.

Exits 2 with the problems on stderr so Claude sees them; exits 0 otherwise.
"""
import filecmp
import json
import os
import sys


def frontmatter(text):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    fields, key = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if line[:1] in (" ", "\t") and key:
            fields[key] = (fields[key] + " " + line.strip()).strip()
        elif ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            fields[key] = "" if value in (">", "|", ">-", "|-") else value
    return None


def differs(a, b):
    c = filecmp.dircmp(a, b, ignore=["__pycache__", ".DS_Store"])
    if c.left_only or c.right_only or c.diff_files or c.funny_files:
        return True
    return any(differs(os.path.join(a, d), os.path.join(b, d)) for d in c.common_dirs)


def main():
    try:
        path = json.load(sys.stdin).get("tool_input", {}).get("file_path") or ""
    except (ValueError, AttributeError):
        return 0
    root = os.path.realpath(os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd())
    rel = os.path.relpath(os.path.realpath(path), root) if path else ".."
    parts = rel.split(os.sep)
    if len(parts) < 2 or parts[0].startswith(".") or parts[0] == "..":
        return 0
    skill = parts[0]
    src = os.path.join(root, skill)
    if not os.path.isfile(os.path.join(src, "SKILL.md")):
        return 0

    problems = []
    if parts[1:] == ["SKILL.md"]:
        with open(os.path.join(src, "SKILL.md"), encoding="utf-8") as f:
            fm = frontmatter(f.read())
        if fm is None:
            problems.append("SKILL.md has no closed YAML frontmatter")
        else:
            if fm.get("name") != skill:
                problems.append(f"frontmatter name is {fm.get('name')!r}, directory is {skill!r}")
            desc = fm.get("description", "")
            if not desc:
                problems.append("frontmatter description is missing")
            elif len(desc) > 1024:
                problems.append(f"description is {len(desc)} characters, limit is 1024")
        try:
            with open(os.path.join(root, "README.md"), encoding="utf-8") as f:
                if f"`{skill}`" not in f.read():
                    problems.append(f"README.md does not list `{skill}`")
        except OSError:
            pass

    for label in (".claude/skills", "../ai-setup/.claude/skills"):
        copy = os.path.normpath(os.path.join(root, label, skill))
        if os.path.isdir(copy) and differs(src, copy):
            problems.append(f"{label}/{skill} no longer matches {skill}/ - re-copy it")

    if problems:
        print(f"{skill}: " + "; ".join(problems), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
