#!/usr/bin/env python3
"""
Install this repository's git hooks (scripts/git-hooks/<hook>) into the clone's hooks folder,
which every worktree of the clone shares: task git-hooks.

    pre-push   refuses to push a mods/<name> branch anywhere but the mod repository <name>.

A hook already there that this script did not install is left alone, with a message.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARKER = "Installed by task git-hooks"


def main() -> int:
    common = subprocess.run(["git", "rev-parse", "--git-common-dir"], cwd=HERE, capture_output=True,
                            text=True, check=True).stdout.strip()
    hooks = (Path(common) if Path(common).is_absolute() else (HERE / common).resolve()) / "hooks"
    hooks.mkdir(exist_ok=True)
    status = 0
    for src in sorted(p for p in HERE.iterdir() if p.is_file() and not p.suffix):
        dst = hooks / src.name
        if dst.exists() and MARKER not in dst.read_text(encoding="utf-8", errors="replace"):
            print(f"skipped {src.name}: {dst} is another hook; merge the two by hand")
            status = 1
            continue
        # Git runs hooks with sh, which needs LF line endings whatever the checkout uses.
        dst.write_bytes(src.read_text(encoding="utf-8").replace("\r\n", "\n").encode("utf-8"))
        dst.chmod(0o755)
        print(f"installed {src.name} in {hooks}")
    return status


if __name__ == "__main__":
    sys.exit(main())
