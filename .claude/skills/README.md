# Claude Code skills

Do not add skills here. Skills live in [`.agents/skills/`](../../.agents/skills/), which
Gemini CLI, Codex, GitHub Copilot and Cursor read natively. Claude Code only reads this
folder, so `task ai-link` fills it with links to each shared skill (`task kb-update` and the
SessionStart hook in `.claude/settings.json` do it for you). The links are ignored by git.
