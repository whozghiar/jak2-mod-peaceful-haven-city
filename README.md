# Crimson Blue Guard — Jak 2

<p align="center">
  <img src="https://img.shields.io/badge/OpenGOAL-Mod-blue.svg" alt="OpenGOAL Mod">
  <img src="https://img.shields.io/badge/Game-Jak%202-orange.svg" alt="Target Game">
  <img src="https://img.shields.io/badge/AI--assisted-Modding-purple.svg" alt="AI Assisted">
</p>

---

> [!NOTE]
> This mod moved from the `jak2/features/peaceful-haven-city` branch of [whozghiar/jak-project](https://github.com/whozghiar/jak-project) to this repository. Earlier releases stay installable from the launcher catalog.

## 📖 Overview
Adds a blue-recolored Crimson Guard as its own, standalone entity — a new GOAL type
(`crimson-blue-guard`) that reuses 100% of the stock `crimson-guard`'s behavior, animations and
sounds, only with a re-textured mesh. It appears in Haven City mixed into the normal ambient
guard traffic, alongside the regular red guards.

- **Target Game:** Jak 2
- **Repository:** [`whozghiar/jak2-mod-peaceful-haven-city`](https://github.com/whozghiar/jak2-mod-peaceful-haven-city) — base blue-guard traffic + the **City Peaceful**
  mode: ambient blue guards patrol as neutral 2-3 member squads.

### Branch family
| Branch | Adds |
|---|---|
| `jak2/features/blueguard-traffic` | base: `crimson-blue-guard` entity, faithful combat AI, ambient city-traffic spawning, modular hook layer |
| **`jak2/features/city-peaceful`** *(this one)* | neutral blue patrol **squads** — formation nav, adaptive follower speed, leader re-election, mutual defense, faction friendly-fire immunity |
| `jak2/features/city-insurrection` | three-front **territorial civil war** — district zoning, autonomous inter-faction combat, alert-free zones, debug-menu war-zone picker |
| `jak2/features/blueguard` | both modes together (mutually exclusive at runtime) |

**The mod ships OFF.** It is enabled in-game with **L3 + SELECT** under `Mods ▸ crimson-blueguard-peaceful ▸ Enable` (works in retail boot, no debug mode required).
With it **off, Haven City is byte-for-byte stock Jak 2** — no blue guards spawn, ambient
guard-vehicle counts are the retail values, alerts and civilians behave normally. Turning it
**on** enables the whole package at once: blue ambient guards **and** the neutral patrol-squad
behaviour. The choice re-rolls the ambient guards on the spot and persists across level reloads.

## ✨ Key Features
- **New standalone entity:** `crimson-blue-guard` is a real GOAL type (subtype of
  `crimson-guard`), not a global texture swap — regular red guards keep spawning too.
- **Identical to the stock guard in every other respect:** animations, sounds, death (including native purple particle dissolution and ground knockdown death), collision,
  weapon loadout — all inherited unchanged (same slot indices, see the technical doc); only the
  mesh/skeleton-group and the one behavior difference below are different.
- **Its own faction behavior:** unlike the stock guard, it is passive toward Jak by default and
  never joins a general city alert against him. If Jak personally attacks it, it fights back
  without raising the city-wide alarm. Enhanced resilience: 8 HP (double standard guard health)
  ensures durable tactical squad combat.
- **Manual "fight the other guards" trigger:** `crimson-blue-guard-attack-guards`, a small function
  that makes it go hostile toward the nearest red `crimson-guard` — never automatic, called
  explicitly (REPL or code).
- **Mixed into ambient city traffic:** the traffic manager spawns the blue variant for a
  configurable fraction of ambient guard spawns (`*crimson-blue-guard-ratio*`, default 1-in-2 of
  the id-parity pool), right alongside the stock guard.
- **Faithful Crimson Guard Combat AI:** rifle and grenade launcher guards maintain tactical standoff distance (engaging targets up to 50m away), fire reactive bursts or parabolic grenades, and execute evasive combat rolls (`roll-left` / `roll-right`). Melee rifle-butt strikes are strictly an emergency close-quarters counter (< 2.5m), followed immediately by an evasive roll to resume shooting. Taser guards charge and shock with high-voltage electric arcs.
- **City Peaceful mode** (`mod-city-peaceful.gc`, toggled from the Mods debug tab): when on, a
  freshly-activated ambient blue guard becomes a **squad leader** and pulls 1-2 followers behind
  it — tight formation navigation with adaptive follower speed, automatic leader re-election on
  death, distinct weapon loadouts across the squad, and mutual retaliatory defense (hit one, the
  whole squad turns on the attacker) — all without ever sounding the city alarm. Blue guards are
  completely immune to friendly fire from each other.
- **Blue Guard Vehicle Drivers (Peaceful mode):** Krimson Guard patrol cruisers (`vehicle-guard`)
  are piloted by blue guards (`crimson-blue-guard-rider`). If knocked off their vehicle, they
  deploy onto the street as blue guards on foot without triggering police alerts.
- **Civilian Protection / Alert Suppression (Peaceful mode):** attacking or killing civilian
  pedestrians in the street no longer triggers police alarms or raises the city alert level.
  Stock red guards still trigger alerts normally if directly engaged.
- **Modular `*mod-city-*-hook*` layer:** the shared traffic/guard engine files call ~10 named
  function-pointer hooks (declared in `engine/ai/traffic-h.gc`); `mod-city-peaceful.gc` and
  `mod-city-hooks.gc` wire the required behaviors, while the rest stay at their stock defaults.
  The engine files remain byte-identical across the branch family.

## 🚀 Step-by-Step Guide to Run the Mod

### 1. Select the Active Game
Make sure your environment is targeting Jak 2:
```bash
task set-game-jak2
```

### 2. Binary Compilation
- **Status:** `task build-release-game` (or `task build-debug-game`) — required. The
  `build-actor` tool (`goalc/build_actor/jak2/build_actor.cpp`) and the `goalc` data-compiler
  (`goalc/make/Tools.cpp`) both gained a new opt-in `:native-header` flag used to build this
  actor's art-group. See `docs/modding/build_and_iteration_workflow.md`.
- **Details:** engine/compiler C++ was modified (see the "Engine Changes" table in the technical
  doc below).
```bash
task build-release-game
```

### 3. Asset Extraction
- **Status:** Required, once — the guard's actual drawable geometry + textures ("Circuit 2", see
  the technical doc) are baked into `GAME.fr3` by the decompiler, from
  `custom_assets/jak2/models/common/crimson-blue-guard-lod0.glb`. Needs a legally-dumped Jak 2 ISO.
```bash
task extract
```
Check the log for `Adding custom model crimson-blue-guard-lod0 to common` and no
`merc failed to find texture` error for it. This step does **not** need to be repeated after a
pure GOAL-code change (`(mi)` is enough) — only after the `.glb` model itself changes.

### 4. Launch the Game
Run the game natively:
```bash
task boot-game
```
*(Or launch via the OpenGOAL REPL using `task repl`, then compile and run with `(mi)` and `(r)`).*
Roughly 1 in 8 ambient guard spawns in Haven City will be blue. To see it faster while testing,
set `(set! *crimson-blue-guard-ratio* 1)` at the REPL once booted — every ambient guard spawn
becomes blue until you reset it back to `8` (or any N you like). You can also spawn one right in
front of you regardless of the ratio with `(spawn-crimson-blue-guard-debug 0)` (baton guard) or
`(spawn-crimson-blue-guard-debug 1)` (gun-equipped guard).

## 🎥 Demonstration Video

[![Demonstration Video](https://img.youtube.com/vi/SppDFeEd4r8/maxresdefault.jpg)](https://youtu.be/SppDFeEd4r8)

▶️ **[Watch the demonstration video on YouTube](https://youtu.be/SppDFeEd4r8)**

---

## 📖 Technical Documentation
For the complete technical breakdown, architecture, and developer notes, refer to:
- 📄 [`docs/modding/current_mod/blue_guard_reskin_readme.md`](docs/modding/current_mod/blue_guard_reskin_readme.md)

---
*(AI-assisted)*
