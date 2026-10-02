# How the Repository Works

How the mother repository, the mod repositories and the knowledge base fit together, what
switching between them in one working directory implies, and the commands for day-to-day work.
For CI triggers and permissions see [`github_workflows.md`](github_workflows.md); for every task
option see [`task_scripts_reference.md`](task_scripts_reference.md); to start a mod from scratch
see [`how_to_create_a_mod.md`](how_to_create_a_mod.md).

`<owner>` below is the GitHub account that holds the mother repository: the original project's,
or yours in a fork (see [section 7](#7-working-from-a-fork)).

## 1. Three kinds of repositories

| Repository | Holds | Default branch |
| :--- | :--- | :--- |
| `<owner>/jak-project`, the mother | `master`: a mirror of `open-goal/jak-project`, synced daily. `master-dev`: the modding base every mod starts from (engine and compiler patches, the Mods menu framework, scripts, `Taskfile.yml`, CI, `AGENTS.md`, templates, and the global launcher catalog `index.json`). | `master-dev` |
| `<owner>/<game>-mod-<slug>`, one per mod | The mod: `master-dev` plus the mod's own changes, its README, releases and issues. `<slug>` is the mod's launcher catalog key, kept verbatim. Tagged with the `opengoal-mod` topic. | `main` |
| `opengoal-modding-kb`, the knowledge base | Agent skills and the verified Lisp wiki, mounted as the `.agents/skills` submodule in the mother and in every mod repository. Its URL is in `.gitmodules`. | `main` |

```text
open-goal/jak-project --daily--> jak-project master --> jak-project master-dev --+--> jak2-mod-a (main)
                                                                                 +--> jak2-mod-b (main)
                                                                                 +--> ... one repository per mod

opengoal-modding-kb (main) --submodule .agents/skills--> every repository above
```

## 2. One working directory for every repository

A mod repository shares its history with the mother, so one clone of `jak-project` holds every
mod, the way it held mod branches:

| Branch in the clone | What it is |
| :--- | :--- |
| `master-dev` | The modding base. |
| `mods/<name>` | The `main` branch of the mod repository `<name>`, which is a remote of the clone. `git push` on it goes to that repository's `main`. |
| `archive/jak[1-3]/<type>/<slug>` (tags) | The old mod branches, archived: those of the moved mods, and the mods not moved yet. See [Archived branches](#archived-branches). |

### Switching

```bash
task modding-switch -- --list                     # the mod repositories
task modding-switch -- jak2-mod-my-mod            # a mod repository, fetched on first use
task modding-switch -- master-dev                 # back to the modding base
```

Use `task modding-switch` rather than a bare `git switch`: on `master-dev` and in mod
repositories `.agents/skills` is the knowledge-base submodule, while an old mod branch restored
from its archive carries a plain copy of the skills at the same path, and git refuses to put one
in place of the other. The task parks the submodule first (after checking it holds no unpushed
knowledge-base work) and refreshes the knowledge base and the skill links after switching. Old
branches predate the task: to leave one, run `git switch master-dev` (or
`git switch mods/<name>`), then `task kb-update`.

#### From the IDE

In VS Code, and in editors built on it, select the branch name in the status bar (or run
**Git: Checkout to** from the Command Palette) and pick `mods/<name>`, for example
`mods/jak2-mod-peaceful-haven-city`, or `master-dev`. Between those branches this does the same
as the task, except two things: it does not fetch a mod repository that is not in the clone yet
(run `task modding-switch -- <name>` once for it), and it leaves the knowledge base as it was
(run `task kb-update`, or let the next Claude Code session do it). Uncommitted changes follow
you, or VS Code offers to stash them: commit before switching mods.

### What a switch changes

A switch replaces the tracked files (game code, engine, scripts, `Taskfile.yml`, docs, agent
configuration) with the target's. Everything git ignores stays as it was: `iso_data/`,
`decompiler_out/`, `out/` (the C++ build and the compiled game), the sccache cache, and the game
selected with `task set-game-*`. No mod needs its own extraction, but the build outputs are the
previous mod's until you rebuild what differs:

| The two mods differ in | Run after the switch |
| :--- | :--- |
| Game code (`goal_src/`) | `task compile-check`, or `(mi)` in the REPL: changed files recompile. |
| C++ (`game/`, `goalc/`, `common/`) | `task build-release-game`; sccache, when installed, serves the objects it compiled before. |
| The decompiler (`decompiler/`, `decompiler/config/`) | `task build-release-decomp`, then `task extract`. |
| Texture replacements (`custom_assets/<game>/texture_replacements/`) | `task extract`: textures are baked at extraction. |
| The game | `task set-game-jak1`, `-jak2` or `-jak3`. |

### Limits

| Limit | Why | What to do |
| :--- | :--- | :--- |
| One mod at a time | A working directory has one checkout and one `out/`. | For two mods side by side, add a second working directory (see [Two mods side by side](#two-mods-side-by-side)). |
| A clean tree to switch | The task refuses to switch over uncommitted changes or untracked files, so nothing is carried into the wrong mod. | Commit, or `git stash -u` and `git stash pop` when you come back. |
| Extracted data lags behind | Textures and decompiler output stay as the last `task extract` made them. | Run `task extract` after switching to or from a mod that changes them; it takes minutes, not a full rebuild. |
| Saves and settings are shared | `%APPDATA%/OpenGOAL/<game>/` holds the saves (a cold boot loads slot 1) and `pc-settings.gc` for every mod and for the stock game. | Before testing a mod, think about what the previous one saved: start a new game, or move the save files aside. |
| One agent memory for every mod | Claude Code keeps its auto memory per folder, so every mod of the working directory shares it. | Keep a mod's notes in its `docs/modding/current_mod/`, and verified general facts in the knowledge base. |
| The knowledge base moves on its own | Each repository pins a knowledge-base commit, and the session hook fast-forwards `.agents/skills` to the latest, so `git status` can show `.agents/skills` as modified. | Commit it with your next change, or leave it: the next sync with `master-dev` brings the base's pointer. |

### Two mods side by side

Switching is enough for one mod at a time. To keep a second mod open in its own window, give it
a second working directory, a git worktree, outside this folder:

1. In VS Code: **Source Control**, **Source Control Repositories** view, the repository's
   **More Actions (...)** menu, **Worktrees**, **Create Worktree**. Pick `mods/<name>` and a
   folder next to this one, such as `..\jak-project-<name>`. From a terminal:
   `git worktree add ../jak-project-<name> mods/<name>`.
2. Open it with **Open Worktree in New Window** (right-click it in Source Control Repositories),
   or `code ../jak-project-<name>`.
3. In the new folder: `task kb-update` for the knowledge base, copy your game files into its
   `iso_data/<game>/`, then `task set-game-<game>`, `task gen-cmake-release`,
   `task build-release` and `task extract`: `iso_data/`, `decompiler_out/` and `out/` are per
   folder.

A branch can be checked out in only one working directory, and each folder has its own Claude
Code memory. Remove one with `git worktree remove ../jak-project-<name>` (the branch stays).

## 3. Everyday tasks

### Start a new mod

```bash
task modding-switch -- master-dev
task modding-new-mod
```

The task asks for the game, the mod name (it names the repository `<game>-mod-<name>`), one sentence
for players and the visibility, then creates the repository from `master-dev` with a README from
[`MOD_README.template.md`](../templates/MOD_README.template.md), the `opengoal-mod` topic, and the
local branch `mods/<game>-mod-<name>`. The whole procedure, through to the release, is in
[`how_to_create_a_mod.md`](how_to_create_a_mod.md).

### Work on a mod

On `mods/<name>`: edit, verify with `task compile-check`, ask for a cold boot
(`task boot-game-retail` checks the Mods menu), commit, then `git push`. The golden rules are in
[`AGENTS.md`](../../../AGENTS.md): runtime toggle, native non-regression, comments, change log
(in the mod's technical README, not in its player README).

`git push` on `mods/<name>` goes to that repository's `main`: the branch tracks `<name>/main`,
and the remote `<name>` carries the push rule `refs/heads/mods/<name>:refs/heads/main`. VS
Code's Push and Sync buttons follow the same tracking. Only a typed `git push origin` would go
elsewhere, creating a `mods/<name>` branch in the mother repository: the pre-push hook that
`task git-hooks` installs refuses it.

### Bring the latest modding base into the current mod

```bash
task modding-sync-branch -- --push
```

On `mods/<name>` this merges `origin/master-dev` under the mod-repository rules and pushes to the
mod repository:

| Path | Rule |
| :--- | :--- |
| `README.md`, `index.json` | Always the mod's. |
| `docs/modding/current_mod/` | The mod's version wins a conflict. |
| `AGENTS.md`, `CLAUDE.md`, `.claude/`, `.gemini/`, `.agents/` (the knowledge-base pointer), `scripts/ai/`, the other `docs/modding/` files, issue templates | `master-dev`'s version wins a conflict. |
| Workflows | `release.yml`, `lint.yml` and `build.yml` only; the mother-only ones are removed. |
| `master-dev`-only files (`.github/dependabot.yml`, the mod-suggestion issue form) | Removed. |
| Everything else, game code included | A normal merge. A real conflict stops the sync for you to resolve. |

In a clone of the mod repository alone, the same task adds a `mother` remote pointing at
`<owner>/jak-project` on first use and merges its `master-dev`.

### Bring it into every mod at once

```bash
task modding-sync-all -- --dry-run   # what would happen
task modding-sync-all                # do it
task modding-sync-all -- jak2-mod-a jak2-mod-b   # only these
```

For each mod repository (the `mods/*` branches, plus the `opengoal-mod` repositories of the
account when `gh` is installed), the task fetches it, merges `origin/master-dev` with the same
rules in a temporary worktree outside your working directory, and pushes the result to its `main`.
It never touches your working directory, so it can run while you work. It skips a mod that is
already up to date, one whose `mods/<name>` has commits you have not pushed (push them first),
and the one you have checked out (sync that one with `task modding-sync-branch -- --push`). A mod
that hits a real conflict is left as it was, nothing pushed, and the summary says which files to
resolve by hand.

Nothing syncs a mod on its own: a released mod can stay on the base it was built with until it
needs something newer.

### Change the modding base

Engine and compiler patches, the Mods menu framework, tooling and shared docs are committed on
`master-dev` and pushed; the mods pick them up at their next sync. Reusable code first written in
a mod goes to `master-dev` with `git cherry-pick`, since the repositories share their history.

### Release a mod

Run `release.yml` from the mod repository: the steps are in
[`how_to_create_a_mod.md`](how_to_create_a_mod.md#9-release), the pipeline and the inputs in
[`mod_distribution_guide.md`](mod_distribution_guide.md). The release is tagged
`<slug>-vX.Y.Z`, and the global catalog on `master-dev` lists it within a day. Releases
published before a mod moved to its repository stay in `jak-project`, and the launcher keeps
installing them.

### Record a discovery

Verified knowledge that would help another mod goes into the knowledge base, never into a mod
repository or a memory file. Follow the `kb` skill: find the topic, edit its entry in place, cite
the evidence, then commit and push from `.agents/skills`. Every repository picks it up at its
next Claude Code session, or with `task kb-update`.

### Move an archived mod into its own repository

```bash
task modding-new-mod -- --from-branch jak2/features/<slug>
```

It works from the branch or from its archive tag. Add `--prepare-only` to build and inspect
`mods/<game>-mod-<slug>` before publishing it. A mod that was never released gets no
`index.json`: its first release creates it.

### Private repositories

Answer `private` when `task modding-new-mod` asks for the visibility, or pass `--private`. To
change an existing repository, use its GitHub settings (Danger Zone, Change visibility) or:

```bash
gh repo edit <owner>/<name> --visibility private --accept-visibility-change-consequences
```

| | Public | Private |
| :--- | :--- | :--- |
| Your work in this clone (`task modding-switch`, `git push`, `task modding-sync-all`) | Same | Same |
| Who sees the code, issues and releases | Everyone | You and the collaborators you invite |
| New releases in the launcher | Listed by the global catalog | Not listed: players cannot download them |
| Releases published before the mod moved to its repository | Installable | Still installable: they belong to `jak-project` |
| GitHub Actions minutes (lint on each push, releases) | Free | Taken from the account's monthly free minutes; Windows runners count double |

Making a private mod public is the same command with `--visibility public`; the catalog lists its
releases at its next daily run. The mother repository stays public: it is a fork of a public
repository.

### List every mod repository

Every mod repository carries the `opengoal-mod` topic:

```bash
gh repo list <owner> --topic opengoal-mod
```

On GitHub, search `user:<owner> topic:opengoal-mod`.

### Why the mod repositories are not GitHub forks

A GitHub account holds at most one repository per fork network ("you can only have one fork in a
repository's network of forks", GitHub support), and `<owner>/jak-project` is already the
account's fork of `open-goal/jak-project`. The mod repositories are therefore created by push.
They share the mother's history the way forks do, so `git merge` syncs them the same way, and
`task modding-sync-all` stands in for GitHub's Sync fork button. What a fork would add is the
"forked from" link and pull requests between the mother and a mod on GitHub's web interface.

### Archived branches

The mother repository keeps only `master` and `master-dev`. Every old mod branch is archived as
the tag `archive/<branch>`, at the commit the branch pointed to, so nothing is lost and the
branch list stays short. Releases made from those branches stay: they belong to their own tags.

```bash
git tag --list "archive/*"                                          # what is archived
git switch -c jak2/features/<slug> archive/jak2/features/<slug>     # restore a branch
```

To archive a branch yourself: `git tag -a archive/<branch> -m "Archived" origin/<branch>`,
`git push origin archive/<branch>`, then `git push origin --delete <branch>`.

## 4. Where things live

| Path | What | Source |
| :--- | :--- | :--- |
| `AGENTS.md`, `CLAUDE.md` | Agent instructions; `CLAUDE.md` imports `AGENTS.md` | `master-dev`, inherited by every mod |
| `.agents/skills/` | The knowledge base | Submodule of `opengoal-modding-kb` |
| `.claude/settings.json`, `.claude/hooks/` | Claude Code permissions and hooks | `master-dev` |
| `.claude/skills/` | Links to `.agents/skills/*` made by `task ai-link`, not versioned | Local |
| `.gemini/settings.json` | Makes Gemini CLI read `AGENTS.md` | `master-dev` |
| `docs/modding/guides/`, `docs/modding/templates/` | Tooling guides and templates | `master-dev`, mirrored in mods |
| `docs/modding/current_mod/` | A mod's own technical notes | Each mod repository |
| `README.md`, `index.json` | Mother: hub README and global catalog. Mod: player README and the mod's own catalog | Each repository |
| `scripts/modding/`, `scripts/ai/`, `Taskfile.yml` | Tooling | `master-dev` |

## 5. AI agents in this layout

- Every repository loads the same `AGENTS.md`: Claude Code through `CLAUDE.md`, Gemini CLI
  through `.gemini/settings.json`, Codex, Copilot and Cursor natively.
- Skills live in `.agents/skills/`, which Gemini CLI, Codex, Copilot and Cursor read natively. A
  Claude Code SessionStart hook refreshes the knowledge base and links each skill into
  `.claude/skills/`.
- Agents may compile (`task compile-check`, `task build-release-game`,
  `task build-release-decomp`) and never launch the game: a PreToolUse hook blocks `gk`,
  `task boot-game*`, `task run-game` and debugger attach.
- An agent works on whatever is checked out: switch before starting a session, and do not switch
  while an agent is working. Two agents on two mods need two working directories (see the limits
  in section 2).
- The archived mod branches predate this configuration; moving one to a repository brings it.

## 6. What runs on its own

| Automatic | When |
| :--- | :--- |
| Upstream into `master`, then `master-dev` | Daily at 10:00 UTC (`sync-upstream.yaml`) |
| Global catalog rebuilt from every repository's releases | Daily at 10:30 UTC, and after each release of the mother |
| Lint | On every push, in every repository |
| Knowledge base refreshed, skills linked | At the start of each Claude Code session |

Not automatic, on purpose: syncing mods with `master-dev` (`task modding-sync-all` does it on
demand), releases, the full build check (`build.yml`), and archiving branches.

## 7. Working from a fork

Nothing in the tooling names an account: scripts read the owner from the `origin` remote, and the
mother-only workflows run in any repository named `jak-project`. A fork of the mother therefore
works as is once you:

1. fork it under the name `jak-project`, enable its GitHub Actions, and clone it with
   `--recurse-submodules`;
2. publish your own mods with `task modding-new-mod`, which creates them under your account;
3. fork the knowledge base too if you want to record discoveries, and point `.agents/skills` at
   your fork.

The step-by-step procedure, with what the catalog and the launcher need, is in
[`how_to_create_a_mod.md`](how_to_create_a_mod.md#0-set-up-once).
