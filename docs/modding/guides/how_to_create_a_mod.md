# How to Create a Mod

The whole procedure for a new mod, from an empty repository to a release players install from
the OpenGOAL Launcher: which commands to run, which resources to read, and how to feed the
knowledge base. How the repositories fit together is explained in
[`repository_workflow.md`](repository_workflow.md).

## 0. One-time setup

Done once per machine, in a clone of `whozghiar/jak-project`.

1. **Clone with the knowledge base** (a submodule):
   ```bash
   git clone --recurse-submodules https://github.com/whozghiar/jak-project.git
   ```
   In an existing clone, `task kb-update` initialises it.
2. **Install the tools:** the C++ toolchain from [`docs/setup/system/windows.md`](../../setup/system/windows.md)
   (or `linux.md` / `macos.md`), [Task](https://taskfile.dev/), Python 3, and the GitHub CLI
   (`scoop install gh`, then `gh auth login`). `sccache` is optional and makes rebuilds after a
   switch near-instant.
3. **Build the tools:**
   ```bash
   task gen-cmake-release
   task build-release
   ```
4. **Extract each game you mod.** Copy the content of your own game disc into
   `iso_data/<game>/` (for example `iso_data/jak2/`), then:
   ```bash
   task set-game-jak2
   task extract
   ```
   `iso_data/`, `decompiler_out/` and `out/` are shared by every mod you switch to in this clone.

## 1. Create the mod repository

```bash
task modding-switch -- master-dev
task modding-new-mod
```

The task asks for:

| Question | What it decides |
| :--- | :--- |
| Game | `jak1`, `jak2` or `jak3`: the first part of the repository name. |
| Mod name | The repository name (`<game>-<name>`) and the mod's launcher catalog key. Players' launchers know the mod by this key, so pick it for good. |
| One sentence | The README overview and the repository description. |
| Demo video | Optional YouTube link embedded in the README. |
| Visibility | `public` (default) or `private`. A private mod stays out of the launcher catalog until you make it public (see section 9). |

It then creates `whozghiar/<game>-<name>` from `master-dev`, with a README from
[`MOD_README.template.md`](../templates/MOD_README.template.md), and the local branch
`mods/<game>-<name>`. Switch to it and select its game:

```bash
task modding-switch -- jak2-my-mod
task set-game-jak2
```

## 2. Learn the rules and find the code

Read these before writing code:

| Resource | Why |
| :--- | :--- |
| [`AGENTS.md`](../../../AGENTS.md), section 4 | The golden rules: every change off by default behind a runtime toggle, no edits to shared menu files, comments, change log. |
| [`mods_menu.md`](mods_menu.md) | How the in-game Mods menu (L3 + SELECT) works and how a mod registers in it. |
| The Lisp wiki, [`.agents/skills/goal-lisp/wiki/`](../../../.agents/skills/goal-lisp/wiki/index.md) | Verified GOAL syntax and engine behavior: `common.md`, then the file of your game. The only place GOAL code examples live. |
| `goal_src/<game>/` | The decompiled game code you hook into. Search it for the system you change. |
| `decompiler_out/<game>/` | Extracted assets (textures, levels) to find names and IDs. |

The knowledge base in `.agents/skills/` also holds focused guides, which an AI agent loads by
itself when the task matches:

| Skill | Use it for |
| :--- | :--- |
| `goal-lisp` | GOAL syntax, types, processes, states, macros and their traps. |
| `engine-internals` | The C++ runtime, the compiler, the decompiler, the build layers. |
| `custom-actors-levels` | Custom models, animations, sound banks, FR3 injection, custom levels. |
| `texture-modding` | Texture replacement, merging, texture packs. |
| `kb` | Recording a discovery (section 7). |
| `verification-before-completion` | Proof before any "done". |

## 3. Wire the toggle and register your files

1. **Put your code in your own files.** Touch vanilla files only where a hook is unavoidable,
   and mark each touch point with a `;; MOD <slug> --` comment so it stays easy to find and
   to merge.
2. **Register in the Mods menu** (Jak 2 and Jak 3): copy
   [`mod_menu.template.gc`](../templates/mod_menu.template.gc) into your mod's menu file,
   for example `goal_src/jak2/pc/features/<slug>-menu.gc`. Never make that file debug-only: a
   debug segment is not linked in a launcher boot. Names: config variables and helpers prefixed
   with the slug, builder named `mod-<slug>-build-menu` (see `mods_menu.md`). Jak 1 has no
   unified Mods menu yet: use a debug submenu prefixed with the slug and say so in the README.
3. **Register every new `.gc` file:** its `.o` in a `.gd` list
   (`goal_src/<game>/dgos/*.gd`, a menu file after `"mods-menu.o"`), plus a compile step in
   `goal_src/<game>/game.gp`. Jak 2 and Jak 3 also need the file pre-marked so the build does not
   look for it in the decompiler's index. The exact lines are in the Lisp wiki,
   [Registering a new source file](../../../.agents/skills/goal-lisp/wiki/common.md#registering-a-new-source-file).

## 4. Iterate

You run the game; an AI agent never launches it.

```bash
task run-game     # terminal 1: the game, waiting for the REPL
task repl         # terminal 2: then (mi) after each edit to hot-reload
```

| Check | When |
| :--- | :--- |
| `task compile-check` | After each change: compiles the GOAL code headless, no game window. This is what agents run. |
| `task boot-game` | Before calling a change done: a cold boot catches what hot reload hides (old definitions left in memory, declaration order, a missing registration). |
| `task boot-game-retail` | Before a release: checks the Mods menu in the boot players get (L3 + SELECT). |
| `task build-release-game` | After a change to `game/`, `goalc/` or `common/` C++. |
| `task build-release-decomp`, then `task extract` | After a change to `decompiler/` or `decompiler/config/`. |

Two traps when testing: a cold boot loads save slot 1, and toggled cheats and settings persist
in `%APPDATA%/OpenGOAL/<game>/settings/pc-settings.gc`.

## 5. Custom assets (optional)

- **Models, animations, sounds, levels:** sources under `custom_assets/<game>/`; the
  `custom-actors-levels` skill walks through the Blender export and the build steps.
- **Textures:** PNGs under `custom_assets/<game>/texture_replacements/`, baked by
  `task extract`; the `texture-modding` skill has the layout and format rules. A standalone
  texture pack is exported with the
  [OpenGOAL Texture Pack Generator](https://github.com/whozghiar/open-goal-texture-pack-generator)
  into `docs/modding/current_mod/texture_packs/`, then registered with
  `task modding-package-texture-pack`.

## 6. Document the mod

| File | For | Content |
| :--- | :--- | :--- |
| `README.md` at the root | Players | Overview, features, controls, demo video, and the "Modding Changes Log". |
| `docs/modding/current_mod/<slug>_readme.md` | Developers and agents | Architecture, the hooks you placed and why, memory and performance notes. Link to the Lisp wiki instead of pasting GOAL code. |
| `docs/img/mod/mod_cover.png` | The launcher | Optional cover thumbnail. |

## 7. Record what you learned in the knowledge base

When you verify something another mod could reuse (a GOAL pattern, a trap, an engine behavior,
the cause of a crash), it goes into the knowledge base, not into the mod. A fact is verified
when it compiled, when you saw it in game, or when it is read in `goal_src/`.

With an AI agent, ask it to record the fact: it follows the `kb` skill. By hand:

```bash
git -C .agents/skills switch main
git -C .agents/skills pull --ff-only
# edit the entry that covers the topic, or add one in the right file
git -C .agents/skills add -A
git -C .agents/skills commit -m "jak2: <topic>"
git -C .agents/skills push
```

- Search first (`grep -rniE "<keywords>" .agents/skills`) and edit the existing entry rather
  than adding a second one.
- When a new fact contradicts an entry, replace the old statement and say so in the commit.
- End each entry with its evidence: `Verified: <game>, <file>, <date>.`

Every repository picks the change up at its next Claude Code session, or with
`task kb-update`.

## 8. Commit, push and keep up with the base

- `git push` on `mods/<name>` goes to the mod repository's `main`.
- When the mod needs something newer from the base, run `task modding-sync-branch -- --push`: it
  merges `master-dev` and pushes.
- An improvement every mod should get (an engine patch, the Mods menu framework, a script)
  belongs in `master-dev`: switch to it, commit, push, then sync the mods that need it. If you
  wrote it in a mod first, bring it over with `git cherry-pick`.

## 9. Release

1. **Check:** the compliance checklist at the end of the mod's README (toggle off by default,
   retail Mods menu, prefixed symbols, comments), then a cold `task boot-game-retail`.
2. **Make it public** if you created it private:
   ```bash
   gh repo edit whozghiar/jak2-my-mod --visibility public --accept-visibility-change-consequences
   ```
3. **Run the release** from the repository's Actions tab (`release.yml`), or:
   ```bash
   gh workflow run release.yml -R whozghiar/jak2-my-mod --ref main \
     -f mod_name="My Mod" -f mod_description="One sentence." -f tag_name="v1.0.0"
   ```
   It rebuilds Windows and Linux (30 to 60 minutes), tags `<slug>-v1.0.0`, and publishes the
   archives and the mod's `index.json`. See [`mod_distribution_guide.md`](mod_distribution_guide.md).
4. **Catalog:** the global catalog on `master-dev` lists the release within a day, or at once
   with `gh workflow run sync-global-catalog.yml -R whozghiar/jak-project --ref master-dev`.

## 10. Working with an AI agent

What is already in place in every mod repository:

- The agent loads `AGENTS.md`, the golden rules and the commands, at the start of each session.
- The skills above load when the task matches; the knowledge base refreshes itself.
- The agent may compile (`task compile-check`, `task build-release-game`) but never launch the
  game: a hook blocks it. It gives you the command to run and asks what you see.

Requests that work well:

- "Add <feature> to this mod, off by default behind a Mods menu toggle; run compile-check and
  give me the cold-boot command."
- "This crash happens when <steps>; find the cause in goal_src before changing anything."
- "Record what we verified about <topic> with the kb skill."
