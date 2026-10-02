# OpenGOAL — Build & Iteration Workflow (Fast Mod Compilation)

> - **Applies to:** Jak 1 / Jak 2 / Jak 3 (OpenGOAL PC Port) — every mod
> - **Origin:** `master-dev`
> - **Related Guides:** [`github_workflows.md`](github_workflows.md) · [`task_scripts_reference.md`](task_scripts_reference.md)

> ### Summary
>
> [1. Why This Exists](#1-why-this-exists) · [2. Mental Model (3 Layers)](#2-the-mental-model--three-independent-layers) · [3. Day-to-Day Workflow](#3-the-day-to-day-workflow) · [4. First-Time Setup](#4-first-time-setup) · [5. Decompiler Modding](#5-modding-that-touches-the-decompiler) · [6. Troubleshooting](#6-troubleshooting)

---

## 1. Why this exists

A full `task build-release` compiles **~20 executables** — the game runtime (`gk`), the compiler
(`goalc`), the decompiler, the language server, dozens of standalone tools, the unit/offline test
suites, and every bundled third-party library (SDL, curl, draco, zydis, capstone…). On a typical
machine that is **10–20 minutes**. For day-to-day modding you almost never need most of it.

Three changes on `master-dev` make iteration dramatically faster. None of them change *what* is
built — only *how much* and *how fast*.

| Change | What it does | Typical gain |
|---|---|---|
| **`sccache` compiler cache** | Remembers the compiled output of every `.cpp`. After a branch switch or a small revert, unchanged files are served from cache instead of recompiled. | Rebuild after `git switch`: **~1–2 min instead of ~15** |
| **Uncapped `--parallel`** | The build tasks no longer force `--parallel 8`; the generator now uses **every CPU core**. | Clean build **~1.5–1.8× faster** |
| **Targeted `*-game` / `*-decomp` tasks** | Build only the binaries you actually need instead of all 20. | Iteration build **~40–55 % fewer files** |

There is also a correctness fix: the `build*` tasks now always pass `--config Release`/`--config
Debug`. With the project's normal Ninja setup this is a harmless no-op, but if a build directory
was ever configured with the Visual Studio generator, `cmake --build` silently defaults to a
**Debug** build even inside `out/build/Release`. Passing `--config` removes that trap.

## 2. The mental model — three independent layers

Understanding this is the key to never waiting for a build you don't need.

```
┌─────────────────────────────────────────────────────────────────────┐
│ LAYER 1 — C++ runtime & compiler   (gk, goalc)                       │
│   Source: game/  common/  goalc/  + third-party                      │
│   Rebuild with: task build-release-game                              │
│   Needed when: you edit engine C++, renderers, mips2c, the compiler  │
├─────────────────────────────────────────────────────────────────────┤
│ LAYER 2 — Decompiler & asset extraction   (decompiler)               │
│   Source: decompiler/  common/                                       │
│   Rebuild with: task build-release-decomp                            │
│   Needed when: you change how assets/types are extracted from the    │
│                original game (config JSON changes, mips2c ports,     │
│                new extraction features, texture/model injection)     │
│   After rebuilding, you must RE-RUN the extraction (see §5)          │
├─────────────────────────────────────────────────────────────────────┤
│ LAYER 3 — GOAL game code   (*.gc / *.gd / *.gp)                       │
│   Source: goal_src/jak[x]/                                           │
│   "Rebuild" with: the REPL — task repl  then  (mi)                   │
│   Needed when: you edit gameplay logic, states, types, HUD…          │
│   NO C++ compilation involved. Hot-reloads into a running game.      │
└─────────────────────────────────────────────────────────────────────┘
```

**Most mods only ever touch Layer 3.** For those, you never run a C++ build after the initial
setup — you use the REPL.

## 3. First-time setup (once per machine / after `task clean-cmake`)

```bash
# 1. Optional but strongly recommended — install the compiler cache.
#    Windows:
scoop install sccache
#    Linux (apt):        sudo apt install sccache      (or: cargo install sccache)
#    macOS (brew):       brew install sccache
#    (optionally) raise the cache budget so several branches fit:
#    Windows:  setx SCCACHE_CACHE_SIZE 25G       Linux/macOS: export SCCACHE_CACHE_SIZE=25G

# 2. Generate the build system. This is where sccache gets "baked in":
#    the Taskfile auto-detects sccache on PATH and wires it into CMake here.
task gen-cmake-release

# 3. One full build — needed to get the decompiler for asset extraction.
task build-release

# 4. Extract the assets from your legal ISO in ./iso_data (once, unless config changes).
task extract
```

> If you skip `sccache`, everything still works — the Taskfile simply omits it. But you lose the
> single biggest speed-up for branch-heavy mod work.

## 4. Everyday iteration loop

### 4a. Editing GOAL code (`.gc`) — the common case, no C++ build

```bash
task repl                 # starts goalc, connects to the game
# in the REPL:
(mi)                      # incrementally compile + hot-reload your changes into the running game
```
Keep the REPL open. Every `(mi)` after an edit takes seconds.

### 4b. Editing C++ engine or compiler code

```bash
task build-release-game   # builds ONLY gk + goalc (+ their libraries)
task boot-game            # or: task run-game
```
`build-release-game` skips: `decompiler`, `lsp`, `extractor`, all `tools/`, the test suites, and
standalone third-party binaries. With `sccache` warm, only the files you actually changed
recompile.

### 4c. Switching between mod branches

```bash
git switch jak2/features/my-other-mod
task build-release-game   # sccache serves the unchanged 95 %+ from cache — fast
```

## 5. What if my mod needs to modify the decompiler?

Some mods legitimately need decompiler changes — for example:

- adding an entry to `extra_art_groups_by_dgo` or another `decompiler/config/jak[x]/*.jsonc` key
  (custom model / `.fr3` injection, extra level extraction),
- porting a new `mips2c` function so a type extracts correctly,
- teaching the decompiler about a new type layout or a new asset format.

`task build-release-game` **will not** rebuild the decompiler — that is the whole point of the
targeted task. The workflow is:

```bash
# 1. Rebuild ONLY the decompiler (sccache still applies — only changed files recompile).
task build-release-decomp

# 2. Re-run the extraction so the decompiled output / assets are regenerated with your new
#    decompiler. Pick the one that matches your change:
task extract                       # full asset + level extraction (config JSON changes,
                                   #   texture/model/collision/level injection)
task decomp                        # re-decompile all GOAL code to reference output
task update-gsrc-file FILE=foo.gc  # re-decompile + fold one file back into goal_src/
task decomp-file FILE=foo          # decompile a single object without touching goal_src/

# 3. Then rebuild the game code as usual (REPL (mi), or task build-release-game if you also
#    changed engine C++).
```

Key point: **a decompiler change is inert until you re-extract.** The decompiler runs *offline*;
its output (in `decompiler_out/`, `goal_src/`, and the extracted asset packs) is what the game
actually loads. Rebuilding the binary without re-running it changes nothing in-game.

If you changed *both* engine C++ and the decompiler, run `task build-release-decomp` **and**
`task build-release-game` (or a single `task build-release` for everything).

Document any decompiler-config change in your mod's root `README.md` "Binary Compilation" step so
other users know they must run `task build-release` + `task extract`, not just the standard
binaries.

## 6. Task reference

| Task | Builds | Use when |
|---|---|---|
| `task gen-cmake-release` | *(configure only)* | first setup, after `task clean-cmake`, or to pick up a newly-installed `sccache` |
| `task build-release` | everything (~20 exes) | first build, CI-like full check, or you changed many layers at once |
| `task build-release-game` | `gk` + `goalc` | iterating on engine / compiler C++ |
| `task build-release-decomp` | `decompiler` | you changed `decompiler/` code or `decompiler/config/**` |
| `task repl` → `(mi)` | *(nothing — hot reload)* | iterating on GOAL `.gc` code |
| `task extract` | *(runs decompiler)* | first setup, or after a decompiler / config change |

`build-debug`, `build-debug-game`, `build-debug-decomp` are the `Debug` equivalents (paired with
`task gen-cmake-debug`).

## 7. Checking that sccache is working

```bash
sccache --show-stats
```
Look at the "Cache hits" vs "Cache misses" ratio. A rebuild after a branch switch should be
almost all hits. `sccache --zero-stats` resets the counters before a test build.
