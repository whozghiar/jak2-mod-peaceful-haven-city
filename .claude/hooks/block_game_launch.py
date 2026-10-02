#!/usr/bin/env python3
"""
Claude Code PreToolUse hook: refuse any shell command that launches the game or attaches the
goalc debugger to it.

Agents may compile (task compile-check, goalc --cmd "(mi)") but never run the game: a crashing
game plus automated retries pops windows on the user's machine. The user launches it and reports
what they see. Exit code 2 blocks the tool call and sends stderr back to the agent.

It reads the whole command text, heredocs included, since a heredoc can run code. A commit
message that names a launcher therefore trips it: pass such a message with git commit -F <file>.
"""
from __future__ import annotations

import json
import re
import sys

# Start of a command: beginning of the line, or after a separator (; && || | & {).
COMMAND_START = r"(?:^|[;&|{]\s*)"

GAME_LAUNCH = re.compile(
    "|".join(
        [
            # Taskfile launchers.
            COMMAND_START + r"task\s+(?:boot-game(?:-retail)?|run-game)\b",
            # The runtime on PATH, optionally through Start-Process.
            COMMAND_START + r"(?:Start-Process\s+(?:-FilePath\s+)?)?['\"]?gk(?:\.exe)?\b(?!-)",
            # The runtime by path, e.g. ./out/build/Release/bin/gk.exe.
            r"[/\\]gk(?:\.exe)?['\"]?(?=\s|$|[;&|)])",
            # The launcher scripts: scripts/batch/gk*.bat, scripts/shell/gk.sh, boot_game.sh.
            r"\bgk\d?(?:-[\w-]+)?\.(?:bat|sh)\b",
            r"\bboot_(?:game|kernel)\.sh\b",
        ]
    ),
    re.MULTILINE,
)

# goalc attaching to (lt) or debugging (dbg) a running game. Only in a command that runs goalc,
# so a commit message or a search that merely mentions "(lt)" goes through.
DEBUGGER = re.compile(r"\((?:lt|dbg)[\s)]")
GOALC = re.compile(r"goalc|\btask\s+repl\b|\bgc\d?\.(?:bat|sh)\b", re.IGNORECASE)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if payload.get("tool_name") not in ("Bash", "PowerShell"):
        return 0
    command = (payload.get("tool_input") or {}).get("command", "")
    if GAME_LAUNCH.search(command) or (DEBUGGER.search(command) and GOALC.search(command)):
        print(
            "Blocked by .claude/hooks/block_game_launch.py: agents may compile "
            "(task compile-check) but never launch the game or attach the debugger. "
            "Give the user the exact command to run and ask them to report what they see.",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
