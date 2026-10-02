#!/usr/bin/env python3
"""
Bring the knowledge-base submodule (.agents/skills) up to date.

.agents/skills is a git submodule of whozghiar/opengoal-modding-kb. A submodule is checked out
at the commit the host repository recorded, without a branch. This script initialises it when
needed, puts it on `main` when that loses nothing, and fast-forwards `main` to origin/main.
It never discards work: commits or edits that block a fast-forward are left alone and reported.
Offline, it keeps the current copy.

Run it with `task kb-update`. The SessionStart hook in .claude/settings.json runs it with
--quiet before linking the skills for Claude Code.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
KB = ".agents/skills"


def git(*args: str, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("--quiet", action="store_true", help="print nothing unless something needs attention")
    args = parser.parse_args()
    log = (lambda message: None) if args.quiet else print
    kb = REPO_ROOT / KB

    if not (kb / ".git").exists():
        init = git("submodule", "update", "--init", KB)
        if init.returncode:
            print(f"kb-update: could not initialise {KB}: {init.stderr.strip()}", file=sys.stderr)
            return 1
        log(f"initialised {KB}")

    if git("fetch", "--quiet", "origin", "main", cwd=kb).returncode:
        log("kb-update: remote unavailable, keeping the current knowledge base")
        return 0

    if git("branch", "--show-current", cwd=kb).stdout.strip() != "main":
        # Detached HEAD is the normal submodule state. Commits made on it would be lost by
        # switching away, so only switch when HEAD is already part of origin/main.
        if git("merge-base", "--is-ancestor", "HEAD", "origin/main", cwd=kb).returncode:
            print(f"kb-update: {KB} has commits outside origin/main on a detached HEAD; "
                  "create a branch for them and push it before updating", file=sys.stderr)
            return 1
        has_main = git("rev-parse", "--verify", "--quiet", "refs/heads/main", cwd=kb).returncode == 0
        switch = git("switch", "--quiet", "main", cwd=kb) if has_main else \
            git("switch", "--quiet", "--create", "main", "--track", "origin/main", cwd=kb)
        if switch.returncode:
            print(f"kb-update: could not switch {KB} to main: {switch.stderr.strip()}", file=sys.stderr)
            return 1

    merge = git("merge", "--ff-only", "--quiet", "origin/main", cwd=kb)
    if merge.returncode:
        print(f"kb-update: {KB} main cannot fast-forward to origin/main "
              "(local commits or edits); push or commit them first", file=sys.stderr)
        return 1

    log(f"{KB} is at {git('log', '-1', '--format=%h %s', cwd=kb).stdout.strip()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
