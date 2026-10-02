# How the Repository Works

How `whozghiar/jak-project`, the mod repositories and the knowledge base fit together, and the
commands for day-to-day work. For CI triggers and permissions see
[`github_workflows.md`](github_workflows.md); for every task option see
[`task_scripts_reference.md`](task_scripts_reference.md).

## 1. Three kinds of repositories

| Repository | Holds | Default branch |
| :--- | :--- | :--- |
| [`whozghiar/jak-project`](https://github.com/whozghiar/jak-project), the mother | `master`: a mirror of `open-goal/jak-project`, synced daily. `master-dev`: the modding base every mod starts from (engine and compiler patches, the Mods menu framework, scripts, `Taskfile.yml`, CI, `AGENTS.md`, templates, and the global launcher catalog `index.json`). | `master-dev` |
| `whozghiar/<game>-<slug>`, one per mod | The mod: `master-dev` plus the mod's own changes, its README, releases and issues. `<slug>` is the mod's launcher catalog key, kept verbatim. Tagged with the `opengoal-mod` topic. | `main` |
| [`whozghiar/opengoal-modding-kb`](https://github.com/whozghiar/opengoal-modding-kb), the knowledge base | Agent skills and the verified Lisp wiki, mounted as the `.agents/skills` submodule in the mother and in every mod repository. | `main` |

```text
open-goal/jak-project --daily--> jak-project master --> jak-project master-dev --+--> jak2-blue-krimzon-guard (main)
                                                                                 +--> jak2-dark-jak-enhanced (main)
                                                                                 +--> ... one repository per mod

opengoal-modding-kb (main) --submodule .agents/skills--> every repository above
```

## 2. One working directory for everything

A mod repository shares its history with the mother, so one clone of `jak-project` holds every
mod, the way it held mod branches:

| Branch in the clone | What it is |
| :--- | :--- |
| `master-dev` | The modding base. |
| `mods/<name>` | The `main` branch of the mod repository `<name>`, which is a remote of the clone. `git push` on it goes to that repository's `main`. |
| `jak[1-3]/<type>/<slug>` | Mods not moved to a repository yet, and the original branches of the moved ones, which are kept. |

`iso_data/`, `decompiler_out/`, `out/` and the sccache cache stay shared by all of them, so no
mod needs its own extraction.

### Switching

```bash
task modding-switch -- --list                            # mod repositories, plus the mods still on a branch
task modding-switch -- jak2-blue-krimzon-guard           # a mod repository, fetched on first use
task modding-switch -- master-dev                        # back to the modding base
task modding-switch -- jak2/features/haven-city-chaos    # a mod still on a branch
```

Use `task modding-switch` rather than a bare `git switch`: on `master-dev` and in mod
repositories `.agents/skills` is the knowledge-base submodule, while the mods still on a branch
carry a plain copy of the skills at the same path, and git refuses to put one in place of the
other. The task parks the submodule first (after checking it holds no unpushed knowledge-base
work) and refreshes the knowledge base and the skill links after switching.

Those older branches predate the task. To leave one, run `git switch master-dev` (or
`git switch mods/<name>`), then `task kb-update`.

After switching, select the mod's game (`task set-game-jak2`, ...) and rebuild what differs:
`task compile-check` for GOAL code, `task build-release-game` when the mod or the base changes
C++.

A single mod can also be cloned on its own:
`git clone --recurse-submodules https://github.com/whozghiar/<name>.git`. That clone needs its own
`task extract`, and reaches `master-dev` through a `mother` remote that `task modding-sync-branch`
adds on first use.

## 3. Everyday tasks

### Start a new mod

```bash
task modding-switch -- master-dev
task modding-new-mod
```

The task asks for the game, the mod name (it names the repository `<game>-<name>`), one sentence
for players and the visibility, then creates the repository from `master-dev` with a README from
[`MOD_README.template.md`](../templates/MOD_README.template.md), the `opengoal-mod` topic, and the
local branch `mods/<game>-<name>`. The whole procedure, through to the release, is in
[`how_to_create_a_mod.md`](how_to_create_a_mod.md).

### Work on a mod

On `mods/<name>`: edit, verify with `task compile-check`, ask for a cold boot
(`task boot-game-retail` checks the Mods menu), commit, then `git push`. The golden rules are in
[`AGENTS.md`](../../../AGENTS.md): runtime toggle, native non-regression, comments, change log.

### Bring the latest modding base into a mod

```bash
task modding-sync-branch -- --push
```

On `mods/<name>` this merges `origin/master-dev` under the mod-repository rules (the mod's
`README.md`, `index.json` and `docs/modding/current_mod/` stay the mod's; shared docs and agent
configuration come from `master-dev`; mother-only workflows are dropped) and pushes to the mod
repository. Nothing syncs a mod automatically: a released mod can stay on the base it was built
with until it needs something newer.

### Change the modding base

Engine and compiler patches, the Mods menu framework, tooling and shared docs are committed on
`master-dev` and pushed; each mod picks them up at its next sync. Reusable code first written in
a mod goes to `master-dev` with `git cherry-pick`, since the repositories share their history.

### Release a mod

Run `release.yml` from the mod repository's Actions tab, or:

```bash
gh workflow run release.yml -R whozghiar/<name> --ref main \
  -f mod_name="Display Name" -f mod_description="One sentence." -f tag_name="v1.1.0"
```

The release is tagged `<slug>-vX.Y.Z`. The global catalog on `master-dev` picks it up within a
day, or at once with
`gh workflow run sync-global-catalog.yml -R whozghiar/jak-project --ref master-dev`. Releases
published before a mod moved to its repository stay in `jak-project`, and the launcher keeps
installing them. See [`mod_distribution_guide.md`](mod_distribution_guide.md).

### Record a discovery

Verified knowledge that would help another mod goes into the knowledge base, never into a mod
repository or a memory file. Follow the `kb` skill: find the topic, edit its entry in place, cite
the evidence, then commit and push from `.agents/skills`. Every repository picks it up at its
next Claude Code session, or with `task kb-update`.

### Move a mod still on a branch into its own repository

```bash
task modding-new-mod -- --from-branch jak2/features/<slug>
```

The branch stays. Add `--prepare-only` to build and inspect `mods/<game>-<slug>` before
publishing it.

### Private repositories

Answer `private` when `task modding-new-mod` asks for the visibility, or pass `--private`. To
change an existing repository, use its GitHub settings (Danger Zone, Change visibility) or:

```bash
gh repo edit whozghiar/<name> --visibility private --accept-visibility-change-consequences
```

A private mod works the same in this clone (`task modding-switch`, `git push`), but players
cannot download its releases, so the global catalog leaves it out until it is public again. Its
GitHub Actions runs count against the account's free minutes, which public repositories do not
use. `whozghiar/jak-project` itself stays public: it is a fork of a public repository.

### Group the repositories on GitHub

GitHub has no folders. Every mod repository carries the `opengoal-mod` topic, so
`https://github.com/whozghiar?tab=repositories&q=topic%3Aopengoal-mod` lists them all. For a
dedicated page, a free GitHub organization can hold the mother repository, the mod repositories
and the knowledge base; moving them there means updating the `whozghiar/jak-project` references
in workflows, scripts and docs, and regenerating the catalog.

### Retire an old branch

Nothing deletes branches. Once a mod's repository is confirmed, delete its original branch
yourself with `git push origin --delete <branch>` and `git branch -D <branch>`. Its releases stay:
they belong to tags, not to the branch.

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
- The mods still on a branch predate this configuration; moving them to a repository brings it.

## 6. What runs on its own

| Automatic | When |
| :--- | :--- |
| Upstream into `master`, then `master-dev` | Daily at 10:00 UTC (`sync-upstream.yaml`) |
| Global catalog rebuilt from every repository's releases | Daily at 10:30 UTC, and after each release of the mother |
| Lint | On every push, in every repository |
| Knowledge base refreshed, skills linked | At the start of each Claude Code session |

Not automatic, on purpose: syncing a mod with `master-dev`, releases, the full build check
(`build.yml`), and deleting branches.
