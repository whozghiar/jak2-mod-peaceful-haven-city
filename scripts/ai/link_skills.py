#!/usr/bin/env python3
"""
Expose the shared skills in .agents/skills/ to Claude Code.

.agents/skills/ is the one place skills live in this repository. Gemini CLI, Codex, GitHub
Copilot and Cursor read it natively; Claude Code only reads .claude/skills/. This script fills
.claude/skills/ with one directory link per shared skill and removes links whose skill is gone:
a junction on Windows (no admin rights or Developer Mode needed), a relative symlink elsewhere.
The links are never committed: git cannot store junctions, and with core.symlinks=false (the
Git for Windows default) a committed symlink checks out as a plain text file.

Run it with `task ai-link`. The SessionStart hook in .claude/settings.json also runs it with
--quiet, so a fresh clone gets its links during the first Claude Code session.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
SHARED_SKILLS = REPO_ROOT / ".agents" / "skills"
# Skills folders of the tools that do not read .agents/skills/ natively.
TOOL_SKILL_DIRS = [REPO_ROOT / ".claude" / "skills"]

FILE_ATTRIBUTE_REPARSE_POINT = 0x400


def is_link(path: Path) -> bool:
    """True for a symlink or a Windows junction, which Path.is_symlink() misses before 3.12."""
    if path.is_symlink():
        return True
    try:
        attributes = getattr(os.lstat(path), "st_file_attributes", 0)
    except FileNotFoundError:
        return False
    return bool(attributes & FILE_ATTRIBUTE_REPARSE_POINT)


def make_link(link: Path, target: Path) -> None:
    if os.name == "nt":
        subprocess.run(
            ["cmd", "/c", "mklink", "/J", str(link), str(target)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
    else:
        link.symlink_to(os.path.relpath(target, link.parent), target_is_directory=True)


def remove_link(link: Path) -> None:
    # rmdir drops a junction (or a Windows directory symlink) without touching its target;
    # never use shutil.rmtree here, which could follow the link.
    if os.name == "nt":
        os.rmdir(link)
    else:
        link.unlink()


def sync(tool_dir: Path, skills: list[Path], log) -> None:
    tool_dir.mkdir(parents=True, exist_ok=True)
    wanted = {skill.name for skill in skills}

    for entry in tool_dir.iterdir():
        if is_link(entry) and entry.name not in wanted:
            remove_link(entry)
            log(f"removed stale link {entry.relative_to(REPO_ROOT)}")

    for skill in skills:
        link = tool_dir / skill.name
        if is_link(link):
            if link.resolve() == skill.resolve():
                continue
            remove_link(link)
        elif link.exists():
            print(f"warning: {link.relative_to(REPO_ROOT)} is a real folder, left untouched", file=sys.stderr)
            continue
        make_link(link, skill)
        log(f"linked {link.relative_to(REPO_ROOT)} -> {skill.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--quiet", action="store_true", help="print nothing unless something fails")
    args = parser.parse_args()
    log = (lambda message: None) if args.quiet else print

    if not SHARED_SKILLS.is_dir():
        print(f"error: {SHARED_SKILLS.relative_to(REPO_ROOT)} not found", file=sys.stderr)
        return 1
    skills = sorted(path for path in SHARED_SKILLS.iterdir() if (path / "SKILL.md").is_file())

    try:
        for tool_dir in TOOL_SKILL_DIRS:
            sync(tool_dir, skills, log)
    except (OSError, subprocess.CalledProcessError) as err:
        print(f"error: could not link skills: {err}", file=sys.stderr)
        return 1

    log(f"{len(skills)} shared skills exposed in: " + ", ".join(str(d.relative_to(REPO_ROOT)) for d in TOOL_SKILL_DIRS))
    return 0


if __name__ == "__main__":
    sys.exit(main())
