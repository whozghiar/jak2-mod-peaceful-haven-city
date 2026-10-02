# Agent Guide — OpenGOAL Modding Fork

Instructions for any AI coding agent working in this repository. Claude Code loads this file
through `CLAUDE.md`; Codex, Copilot and Cursor read it natively; Gemini CLI reads it through
`.gemini/settings.json`. Source of truth: `master-dev` of `whozghiar/jak-project`.

## 1. Project

OpenGOAL ports the PS2 Jak & Daxter trilogy to native x86-64. `goalc` is the GOAL compiler and
REPL, `game/` builds the `gk` runtime, `decompiler/` extracts assets and code from the ISO,
`goal_src/jak[1-3]/` holds the GOAL source, and `custom_assets/` holds texture replacements and
custom models. This fork adds modding tooling on `master-dev`; every mod is derived from it.
Architecture details: [`docs/project-overview.md`](docs/project-overview.md).

## 2. Skills and knowledge base

Skills live in [`.agents/skills/`](.agents/skills/), a git submodule of
[`whozghiar/opengoal-modding-kb`](https://github.com/whozghiar/opengoal-modding-kb) shared by
this repository and every mod repository: one folder per skill with a `SKILL.md`, and the Lisp
wiki in `.agents/skills/goal-lisp/wiki/`. Gemini CLI, Codex, Copilot and Cursor read
`.agents/skills/` natively. Claude Code reads `.claude/skills/`, which `task ai-link` fills with
links; a SessionStart hook refreshes the submodule (`task kb-update`) and the links. Load a skill
only when its description matches the task.

## 3. Verify before you claim

- **Compile, never launch.** Agents may run `task compile-check` (headless `(mi)` through
  `goalc --cmd`, no game window), `task build-release-game` and `task build-release-decomp`.
  Agents never launch the game (`gk`, `task boot-game*`, `task run-game`) and never attach the
  debugger (`(lt)`, `(dbg)`): give the user the exact command and ask what they see. In Claude
  Code, a PreToolUse hook (`.claude/hooks/block_game_launch.py`) enforces this.
- **A cold boot is the final check.** Code hot-reloaded with `(mi)` into a running game can look
  fine while broken on a clean launch (stale definitions, declaration order, missing `.gp`
  registration). Ask the user for `task boot-game`, or `task boot-game-retail` for the Mods
  menu, before calling a gameplay change done.
- **Register every new `.gc` file** in `goal_src/jak[1-3]/game.gp`, dependent types first.
- **Saves and settings persist across boots.** A cold boot restores save slot 1
  (`%APPDATA%/OpenGOAL/jak[x]/saves/`), and toggled cheats and settings stay in
  `%APPDATA%/OpenGOAL/jak[x]/settings/pc-settings.gc`. Account for both when testing.

## 4. Golden rules for mods

1. **Consult the Lisp wiki first.** [`.agents/skills/goal-lisp/wiki/`](.agents/skills/goal-lisp/wiki/index.md)
   is the only place GOAL code examples live. Never invent an instruction.
2. **Native non-regression.** A mod must not change default game behavior unless asked: every
   change ships off by default, gated behind the mod's runtime toggle.
3. **In-game Mods toggle mandatory** for every `features/*` mod, switchable from a retail boot.
   - Jak 2 / Jak 3: the Mods menu opens with L3 + SELECT. See
     [`docs/modding/guides/mods_menu.md`](docs/modding/guides/mods_menu.md) and
     [`docs/modding/templates/mod_menu.template.gc`](docs/modding/templates/mod_menu.template.gc);
     the registration call is in the Lisp wiki.
   - Never edit shared menu files, and never mark your menu file debug-only (a debug segment is
     not linked in a retail boot).
   - Jak 1: the toggle is debug-only. Prefix submenus with the mod slug and say so in the mod
     README.
4. **Mandatory in-code comments.** Comment every function, method, state, hook and type change in
   `.gc` (purpose, arguments, return values, side effects).
5. **Non-destructive changes.** Never delete or wipe original `.gc` files; prefer surgical
   overrides and modular extensions. Never reformat a whole upstream `.gc` file: it trips the
   `og:preserve-this` lint and buries the real diff.
6. **Traceability.** Log every change in the mod's root `README.md` ("Modding Changes Log"); put
   deeper technical notes in `docs/modding/current_mod/<slug>_readme.md`.

## 5. Recording verified discoveries

A verified GOAL pattern, language trap, engine behavior or crash fix that could help another mod
goes into the knowledge base, never into a separate memory or scratch file. Follow the `kb` skill:
find the existing entry, edit it in place, cite the evidence, then commit and push from the
`.agents/skills` submodule. Notes about the current mod alone stay in its `README.md` and
`docs/modding/current_mod/`.

## 6. Documentation standards

English only; concise and tutorial-toned; one scope per document, stated in its first paragraph;
no decorative icons (GitHub admonitions are fine); GOAL code only in the Lisp wiki, except `.gc`
templates meant to be copied; verified facts only. The `documentalist` skill is the full
checklist.

## 7. Commands and CI

`task --list` shows every task, and
[`docs/modding/guides/task_scripts_reference.md`](docs/modding/guides/task_scripts_reference.md)
explains them. The ones agents need most:

```bash
task set-game-jak2          # select the active game (jak1, jak2, jak3)
task compile-check          # headless GOAL compile of the active game
task build-release-game     # rebuild gk + goalc after C++ changes
task build-release-decomp   # rebuild the decompiler after decompiler/ changes
task modding-sync-branch    # merge master-dev into the current mod branch
```

Workflows live in `.github/workflows/`;
[`docs/modding/guides/github_workflows.md`](docs/modding/guides/github_workflows.md) documents
their triggers and access control. Workflows that only make sense in the mother repository are
guarded with `github.repository == 'whozghiar/jak-project'`.

## 8. Git

How the mother repository, the mod repositories and the knowledge base fit together, with the
day-to-day commands: [`docs/modding/guides/repository_workflow.md`](docs/modding/guides/repository_workflow.md).

- `master` mirrors `open-goal/jak-project`. Never commit to it.
- `master-dev` is the modding base. Every mod starts from it.
- **One repository per mod:** `whozghiar/<game>-<slug>`, the slug being the mod's launcher
  catalog key. In this clone it is the branch `mods/<name>`: switch with
  `task modding-switch -- <name>` (not a bare `git switch`), `git push` goes to its `main`, and
  `task modding-sync-branch -- --push` merges the latest `master-dev` into it.
- `task modding-new-mod -- --new jak2/<slug>` creates a mod repository;
  `-- --from-branch <branch>` moves a mod branch into one. No branch is ever deleted.
- Mods not moved yet live on branches named `jak[N]/[type]/[slug]`.
- A mod has two documentation tiers: the root `README.md` for players (from
  [`docs/modding/templates/MOD_README.template.md`](docs/modding/templates/MOD_README.template.md))
  and `docs/modding/current_mod/<slug>_readme.md` for developers and agents.

## 9. Contributing

- Append `(AI-assisted)` to every commit, PR, issue or comment written with AI.
- Never delete or overwrite existing source files without explicit agreement.
- Never open an issue or PR on your own. When asked to, state in it that an AI agent made it and
  that a human may not have reviewed it.
