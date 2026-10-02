#!/usr/bin/env python3
"""
Claude Code PreToolUse hook: refuse any shell command that launches the game or attaches the
goalc debugger to it.

Agents may compile (task compile-check, goalc --cmd "(mi)") but never run the game: a crashing
game plus automated retries pops windows on the user's machine. The user launches it and reports
what they see. Exit code 2 blocks the tool call and sends stderr back to the agent.
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
            # goalc: attach to (lt) or debug (dbg) a running game.
            r"\((?:lt|dbg)[\s)]",
        ]
    ),
    re.MULTILINE,
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0
    if payload.get("tool_name") not in ("Bash", "PowerShell"):
        return 0
    command = (payload.get("tool_input") or {}).get("command", "")
    if GAME_LAUNCH.search(command):
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
