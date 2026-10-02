# Jak 2 — Peaceful Haven City (`peaceful-haven-city`)

> **Mod Readme**
>
> - **Repository:** [`whozghiar/jak2-mod-peaceful-haven-city`](https://github.com/whozghiar/jak2-mod-peaceful-haven-city)
> - **Type:** `features`
> - **Depends on:** the existing `build-actor` custom-actor pipeline
>   (`goal_src/jak2/lib/project-lib.gp`, `goalc/build_actor/`)

---

## 1. What this is

A blue-recolored Crimson Guard, added as its **own standalone GOAL entity** (`crimson-blue-guard`)
rather than a global texture replacement — the stock red `crimson-guard` keeps spawning
unmodified. The blue variant shares `crimson-guard`'s animations, sounds and collision; its main
difference is that it is passive toward Jak by default, and only becomes
personally hostile toward him if he attacks it directly (no city-wide alarm either way) — see §5.
It also has its own health (8 HP), weapon loadout, combat tuning and death sequence (§6, §8).
A separate, manually-triggered function makes it fight another guard on purpose (also §5). It is
mixed into Haven City's ambient guard traffic.

The source asset is `custom_assets/jak2/models/custom_levels/crimson-blue-guard.glb` (also copied
to `custom_assets/jak2/models/common/crimson-blue-guard-lod0.glb`, see §4.3): the decompiled native
`crimson-guard` skeleton + all 40 of its animations, re-skinned with a recolored texture set in
Blender, then re-exported.

## 2. The core problem: animation slot indices

`crimson-guard`'s ~3650 lines of AI/state-machine code (`guard.gc`,
`goal_src/jak2/levels/city/traffic/citizen/guard.gc`) reference its animations almost entirely by **numeric
slot index** into its art-group's element array — either through overridable fields
(`anim-walk`, `anim-run`, `anim-get-up-front`, ...) set once in `init-enemy!`, or, in a handful of
methods (`enemy-method-77`, `enemy-method-78`, `set-behavior!`), as **raw literals** baked
directly into the method body (`(-> this draw art-group data 42)` and friends).

The native `crimson-guard-ag` art-group has a fixed layout (see
`decompiler/config/jak2/ntsc_v1/art-group-info.min.json`, key `crimson-guard-ag`):

| Slot | Content |
|---|---|
| 0 | `crimson-guard-lod0-jg` (skinned mesh) |
| 1 | `crimson-guard-lod0-mg` |
| 2 | `crimson-guard-lod2-mg` |
| 3 | `crimson-guard-shadow-mg` |
| 4..43 | 40 animations, in a fixed order (`idle`@4, `walk`@5, `run`@6, ..., `get-up-front`@33, `get-up-back`@34, ...) |

The existing `build-actor` tool (`goalc/build_actor/jak2/build_actor.cpp`) does **not** reproduce
this layout for a standalone custom actor: it always emits a 2-slot header (`jgeo`, one dummy
null slot) before the animations, and it orders animations by their order in the source `.glb`'s
`animations` array — which a normal Blender/glTF export sorts alphabetically. Building the blue
guard "as-is" would have put `crimson-blue-guard-ag`'s `idle` at slot 2 instead of 4, `get-up-back`
at some alphabetically-derived slot instead of 34, etc. — silently playing the *wrong* animation
in every hardcoded-index code path, breaking the "identical behavior" requirement in subtle,
hard-to-notice ways (e.g. only the vehicle-knockout or yellow-eco-hit reactions, which use raw
literals, would be wrong).

## 3. The fix — two additive, opt-in pieces

### 3.1 `build-actor :native-header #t`

`goal_src/jak2/lib/project-lib.gp`'s `build-actor` macro gained a new `&key (native-header #f)`
parameter, threaded through to the `build-actor2` data-compiler tool
(`goalc/make/Tools.cpp::BuildActor2Tool`) and finally to
`jak2::BuildActorParams2::native_anim_header` (`goalc/build_actor/jak2/build_actor.h`). When set,
`run_build_actor` (`goalc/build_actor/jak2/build_actor.cpp`) emits **two extra null placeholder
slots** after the mesh, padding the header from 2 to 4 slots — matching the native layout exactly.
Default is `#f`, so every existing custom actor (`test-actor`, the jetboard, etc.) is completely
unaffected.

```lisp
(build-actor "crimson-blue-guard" :force-run #t :native-header #t)
```

### 3.2 Reordering the source `.glb`'s animation array

A one-off Python script reordered `crimson-blue-guard.glb`'s `animations` JSON array (pure
reordering of array elements — no accessor/bufferView/mesh data touched) to match the 40-name
canonical order from `art-group-info.min.json` above. Combined with the 4-slot native header,
this makes `crimson-blue-guard-ag`'s slot N hold the *same* animation as `crimson-guard-ag`'s slot
N, for every N. If you ever need to rebuild the `.glb` from a fresh Blender export, re-run
`python scripts/modding/reorder_crimson_guard_glb_anims.py <in.glb> <out.glb>` before running
`build-actor`, or your animation indices will drift again.

With both pieces in place, `crimson-blue-guard` needs only to override
`init-enemy!` (`goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc`) to point at its
own skeleton-group by name — every other inherited method/state from `crimson-guard` keeps
working with the exact same numeric indices, unmodified.

```lisp
(deftype crimson-blue-guard (crimson-guard)
  ((knocked-fatal? symbol)
   (squad-count    int8)
   (squad-index    int8)
   (squad-leader   handle)
   (squad-members  handle 3)
   (squad-offset   vector :inline)))

(def-art-elt crimson-blue-guard-ag crimson-blue-guard-lod0-jg 0)
(def-art-elt crimson-blue-guard-ag crimson-blue-guard-lod0-mg 1)

(defskelgroup skel-crimson-blue-guard crimson-blue-guard crimson-blue-guard-lod0-jg -1
              ((crimson-blue-guard-lod0-mg (meters 999999)))
              :bounds (static-spherem 0 0 0 5)
              :origin-joint-index 3)

(defmethod init-enemy! ((this crimson-blue-guard))
  ;; identical to crimson-guard's init-enemy!, except the skeleton-group name, 8 HP and the squad fields
  ...)
```

## 4. Getting it into the world

- **Code residency:** `crimson-blue-guard.gc` compiles to `crimson-blue-guard.o`, added next to
  `guard.o` in `goal_src/jak2/dgos/cwi.gd` (the always-resident common DGO that already carries
  `crimson-guard`'s own code).
- **Art residency:** `crimson-blue-guard-ag.go` was added next to every existing
  `crimson-guard-ag.go` entry (append-only, nothing removed) in the 10 level DGOs that carry it:
  `cas.gd`, `dg1.gd`, `fdb.gd`, `fea.gd`, `fob.gd`, `fra.gd`, `lwidea.gd`, `lwideb.gd`, `lwidec.gd`,
  `pae.gd`. This guarantees the blue variant's assets are loaded everywhere the stock guard's are,
  so it can never be picked for a spawn without its art being resident.
- **Ambient traffic spawning:** `traffic-manager.gc::traffic-object-spawn` is the single place
  where the traffic simulation turns a `(traffic-type crimson-guard-1)` /
  `(traffic-type crimson-guard-0)` pick into a concrete process, via
  `(citizen-spawn arg0 crimson-guard arg1)`. Both call sites now pick between `crimson-blue-guard`
  and `crimson-guard` with an id-parity test, `(and *mod-city-peaceful?* (logtest? (-> arg1 id) 1))`:
  the `crimson-guard-1` / `crimson-guard-2` arm asks `*mod-city-guard-spawn-blue-hook*`, which this
  mod points at `mod-city-hook-guard-spawn-blue?` (`mod-city-hooks.gc`), and the `crimson-guard-0`
  arm runs the same test inline. With the mod on, a spawn whose `(-> arg1 id)`
  (`traffic-object-spawn-params`'s per-spawn counter) is odd builds a `crimson-blue-guard`, so about
  half of each guard pool is blue; with it off, every spawn is a stock `crimson-guard`.
  `*crimson-blue-guard-ratio*` is still defined in `traffic-manager.gc` (value `2`), but nothing
  reads it any more. While the mod is on, `activate-from-params` (`traffic-engine.gc`) also pulls a
  blue process out of the pool first, through `*mod-city-guard-activate-hook*`
  (`mod-pea-guard-activate`, which falls back to any process when no blue one is free). Apart from
  these two hooks, the `traffic-type` enum, the
  `guard-type-info-array` weighting table, and everything else about how/when/where a guard slot
  gets picked is completely untouched — `crimson-blue-guard` is just an alternate concrete type
  for an existing spawn decision, so all traffic-engine bookkeeping (nav mesh, alert state,
  population counts) behaves identically whichever variant lands in that process slot.
- `(declare-type crimson-blue-guard crimson-guard)` was added near the top of `traffic-manager.gc`
  so the reference above compiles independent of file ordering (same idiom as `crimson-guard`'s
  own forward declaration in `traffic-engine.gc`).

### 4.3 A second, easy-to-miss piece: the actual drawable geometry ("Circuit 2")

`build-actor` (Circuit 1, §3) only produces the skeleton/animations art-group. The actual triangles
+ textures the PC renderer draws (Circuit 2) come from a completely separate system: the
decompiler bakes them into `.fr3` files, looked up **by name** at runtime. See
§4 of `.agents/skills/custom-actors-levels/SKILL.md` for the full mechanism.
`build-actor`'s own merc-ctrl output is a placeholder (`generate_dummy_merc_ctrl` in
`build_actor.cpp` literally reuses a hardcoded dummy mesh) — without Circuit 2, the guard spawns,
moves and makes sound normally, but is **invisible**.

The fix: a second copy of the same `.glb`, renamed to match the placeholder merc-ctrl's own name
(`<art-group-name>-lod0`, here `crimson-blue-guard-lod0.glb`), dropped in
`custom_assets/jak2/models/common/`. The decompiler's `add_custom_model_to_level`
(`decompiler/level_extractor/extract_merc.cpp`) auto-scans that folder at `task extract` time — no
config needed — and bakes the model + all its textures into `GAME.fr3` (`common` → always
resident, regardless of level). This is a one-time step (or after any `.glb` model change); it
does **not** need to be repeated after ordinary `(mi)` GOAL-code iteration.

## 5. Faction behavior

`crimson-blue-guard`'s **faction difference from `crimson-guard`**: it does not fight *for* the
Crimson Guard side against Jak by default. Collision, animations, movement and spawn weighting are
whatever `crimson-guard` already does; its health, weapon loadout, combat tuning and death sequence
are overridden separately (see §6 and §8). The faction overrides, in
`goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc`, are:

- **`citizen-init!` override** — forces the "not targeting Jak" `focus collide-with` collide-spec
  unconditionally (crimson-guard's own version picks it based on the *shared*, city-wide
  `traffic-alert-flag target-jak` flag, which can't be used to keep just one variant passive). The
  guard keeps its `enemy` collide-as bit (so it's still a valid target for others), it just never
  opportunistically treats Jak as a target on its own.
- **`general-event-handler` override**:
  - `'hit`/`'hit-flinch`/`'hit-knocked`: a hit from another blue guard (or from a projectile one
    fired), or with no resolvable attacker, is dropped (`crimson-blue-guard-friendly-attacker?`).
    Any other attacker, Jak or not, is remembered as the guard's target
    (`traffic-target-status handle` + focus) and passed to the rest of its squad
    (`crimson-blue-guard-alert-squad`) instead of calling `trigger-alert`, so
    the city-wide alarm never raises. It then falls through to
    `(method-of-type nav-enemy general-event-handler)`, the exact same call stock crimson-guard
    makes — so the actual flinch/knockback/get-up/hostile transition is stock.
  - `'panic`/`'clear-path`: identical to stock, except danger attributed to Jak (gunfire near the
    guard, not necessarily a direct hit — see `traffic-engine::update-danger-from-target`, which
    always stores Jak's handle as the source) never raises the alert either. Without this, firing a
    weapon near the guard would still sound the alarm even with the `'hit` fix above.
  - `'alert-begin` (along with `'alert-end` and `'end-pursuit`) is turned into a deliberate no-op: stock crimson-guard's version targets whoever
    triggered the alert (almost always Jak) and goes hostile toward them — exactly the "attacks Jak
    during a general alert" behavior this variant must not have.
- **`crimson-blue-guard-attack-guards`** (plain `defun`, not a method, not called from anywhere
  automatically) — the one way to make this guard fight another guard on purpose. Finds the nearest
  red `crimson-guard` within ~60m via `find-nearest-enemy-guard` (`guard.gc`, which scans the
  traffic engine's trackers), excludes `crimson-blue-guard` itself via `type-type?` so blue
  guards can't be made to target each other, then sets the target, alerts its squad and calls
  `go-hostile` — same mechanism stock crimson-guard's `'alert-begin` uses. Call it from the REPL once you have a handle on the guard
  (e.g. `(define g (spawn-crimson-blue-guard-debug 0))`, then
  `(crimson-blue-guard-attack-guards (the-as crimson-blue-guard g))`).

These overrides live in `crimson-blue-guard.gc`; `guard.gc` itself only gains the mod's hooks,
`find-nearest-enemy-guard` and one guard-vs-guard rule (below). **Caveat on the manual trigger:** it reuses
crimson-guard's combat state machine (with this variant's `hostile`/`gun-shoot`/`close-attack` overrides), which is generic about *what* the current
target is (it reads `(-> this focus handle)`/`traffic-target-status handle`, not a hardcoded
`*target*` check) — but stock `crimson-guard` never actually has occasion to point that machinery at
another guard, only at Jak, so this exact combination (guard vs. guard) has no native precedent to
verify against. A red guard that gets hit by a blue guard does fight back: `crimson-guard`'s `'hit`
case in `guard.gc` targets the blue attacker directly and goes hostile instead of calling
`trigger-alert`.

## 6. Engine Changes Made on This Branch

| File | Change | Why |
|---|---|---|
| `goalc/build_actor/jak2/build_actor.h` | `BuildActorParams2` gained `bool native_anim_header = false;` | carries the new opt-in flag |
| `goalc/build_actor/jak2/build_actor.cpp` | `run_build_actor` emits 2 extra null header slots when the flag is set | matches the native 4-slot art-group header so reskins can reuse original anim indices |
| `goalc/make/Tools.cpp` | `BuildActor2Tool::needs_run`/`::run` accept a 9th `:in` element, parsed into `native_anim_header`; max input count raised from 8 to 9 | plumbs the flag from the GOAL macro through to the tool |
| `goal_src/jak2/lib/project-lib.gp` | `build-actor` macro gained `&key (native-header #f)`, appended to the `:in` list | GOAL-side opt-in switch, defaults preserve all existing custom actors |
| `goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc` (new) | `deftype`, `def-art-elt` x2, `defskelgroup`, `init-enemy!` override | the new entity itself |
| `goal_src/jak2/game.gp` | `(build-actor "crimson-blue-guard" ...)` + `(goal-src ...)` registration | builds the art-group, registers the new source file |
| `goal_src/jak2/dgos/cwi.gd` | `"crimson-blue-guard.o"` added next to `"guard.o"` | code residency |
| `goal_src/jak2/dgos/{cas,dg1,fdb,fea,fob,fra,lwidea,lwideb,lwidec,pae}.gd` | `"crimson-blue-guard-ag.go"` added next to each `"crimson-guard-ag.go"` | art residency, matching the stock guard's footprint exactly |
| `goal_src/jak2/levels/city/traffic/traffic-manager.gc` | `(declare-type crimson-blue-guard crimson-guard)`, `*crimson-blue-guard-ratio*` (still defined as `2`, no longer read), id-parity substitution in the `crimson-guard-1`/`crimson-guard-2` arm (through `*mod-city-guard-spawn-blue-hook*`) and the `crimson-guard-0` arm of `traffic-object-spawn`, `spawn-crimson-blue-guard-debug` REPL helper | mixes the blue variant into ambient city traffic, without touching the traffic-type enum or any weighting table; gives a one-liner to force-spawn one for testing |
| `custom_assets/jak2/models/common/crimson-blue-guard-lod0.glb` (new) | copy of the build-actor `.glb`, renamed | Circuit 2 — see §4.3 |
| `goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc` | `citizen-init!`, `general-event-handler` overrides + standalone `crimson-blue-guard-attack-guards` function | passivity toward Jak + manual guard-vs-guard trigger — see §5 |
| `goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc` | `crimson-guard-method-214` override (weapon fire) | grenade-launcher guards (`guard-type 2`) lob a `vehicle-grenade` on a parabolic arc from joint 14 ("blast"); every other guard type falls through to stock `crimson-guard-method-214`. `crimson-blue-guard.glb` keeps the native joint indices (14/15 "blast"/"dirblast"), so the stock line-of-sight probe and taser lightning need no override |
| `goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc` | `die` state + `crimson-blue-guard-dissolve-sequence` + `enemy-method-78` override | Robust custom actor death dissolution: skips standing die animation if `knocked-fatal?` so guard stays flat on the ground, plays `"enemy-fizz"`, launches purple dissolution particles (`merc-death-spawn 73`) across joints for 60 frames with jitter, and hides mesh on frame 5. Replaces `do-effect 'death-default` to prevent the C++ `generic_merc_death` crash (`exit status 5`) on dummy `build-actor` geometry |
| `goal_src/jak2/engine/ai/traffic-h.gc` | `(define-extern *mod-city-peaceful?* symbol)` / `(define-extern *mod-city-insurrection?* symbol)` | forward declarations, same idiom as the pre-existing `*traffic-alert-level-force*` a few lines above, so engine code and the menu file can reference the flags regardless of compile order |
| `goal_src/jak2/levels/city/traffic/citizen/mod-city-hooks.gc` | `*mod-city-peaceful?*` / `*mod-city-insurrection?*` globals, both default `#f` | mod-wide flags — defined in this CWI-resident non-debug file so gameplay code reads them unconditionally (the menu file only `define-extern`s them). `*mod-city-peaceful?*` is now the **master enable** for this branch. |
| `goal_src/jak2/pc/features/crimson-blueguard-peaceful-menu.gc` *(new)* | `mod-crimson-blueguard-peaceful-build-menu` + `mod-crimson-blueguard-peaceful-enable-toggle` + `mod-crimson-blueguard-peaceful-flush-guards`, registered with `(mods-menu-register "crimson-blueguard-peaceful" …)` | the mandatory Mods-menu toggle (retail-safe popup menu, L3 + SELECT). **Replaces** the old hand-rolled "Mods" root-menu block in `default-menu-pc.gc` (now reverted to stock — the shared menu files must never be edited by a branch). Wired in `game.gd` after `mods-menu.o`. |
| `goal_src/jak2/dgos/game.gd` | `"crimson-blueguard-peaceful-menu.o"` after `"mods-menu.o"` | menu-file residency in GAME.CGO |
| `goal_src/jak2/levels/city/traffic/traffic-manager.gc` | `*mod-city-peaceful?*` gate added to: the `crimson-guard-0` blue-pick, `traffic-want-counts` slots 18/19 (`(if *mod-city-peaceful?* 8 4)` / `… 8 3)`) | native non-regression — OFF restores retail spawning and vehicle counts |
| `goal_src/jak2/levels/city/traffic/citizen/mod-city-hooks.gc` | `mod-city-hook-guard-spawn-blue?` now returns `(and *mod-city-peaceful?* (logtest? id 1))` | OFF ⇒ the ambient guard pool builds a stock red `crimson-guard` every time |
| `goal_src/jak2/levels/city/traffic/citizen/guard.gc` | `*mod-city-peaceful?*` gate on the `dead` traffic-target drop in `hostile` `:trans` | OFF restores the stock `inactive`/`disable`-only test |
| `goal_src/jak2/engine/ui/minimap-h.gc` | `(blue-guard-frustum 71)` and `(blue-guard 72)` appended to the `minimap-class` enum + `(define-extern *minimap-class-list* ...)` | gives blue guards their own minimap class ids instead of reusing the red `guard-frustum` (32, guards on foot) and `guard` (14, guard vehicles) |
| `goal_src/jak2/engine/ui/minimap.gc` | `*minimap-class-list*` grown 71 -> 73 with a `blue-guard-frustum` node (clone of `guard-frustum` 32) and a `blue-guard` node (clone of `guard` 14). Each keeps its original's `icon-xy`, `scale` and flags; only `:color` differs (`r 0 / g #x40 / b #xff`) | the icon blip and the view-cone are both tinted from `(-> arg1 class color)` (`draw-frustum-1` / the icon draw path), so a blue class is all it takes to make a guard, or a guard vehicle, read blue on the minimap |
| `goal_src/jak2/levels/city/traffic/citizen/crimson-blue-guard.gc` | `citizen-init!` claims the minimap slot with `blue-guard-frustum` **before** delegating to `crimson-guard`; `die` `:enter` fades the icon out | the parent only adds the red icon while `minimap` is still `#f`, so taking the slot first is what overrides the color; the `die` fade-out mirrors what the stock `inactive` state does |
| `goal_src/jak2/engine/ai/traffic-h.gc` | `(define-extern *mod-city-guard-vehicle-icon-hook* (function uint))` | one more `*mod-city-*-hook*`, so `vehicle-guard.gc` never tests a mode flag inline |
| `goal_src/jak2/levels/city/traffic/citizen/mod-city-hooks.gc` | `mod-city-hook-guard-vehicle-icon` (stock: `guard` 14) + `mod-city-pea-guard-vehicle-icon` (`blue-guard` 72 while `*mod-city-peaceful?*`), installed into the new hook | the exact counterpart of `mod-city-pea-guard-rider-type`: the dot follows whoever the rider hook put in the cockpit |
| `goal_src/jak2/levels/city/traffic/vehicle/vehicle-guard.gc` | `vehicle-method-128` registers `(*mod-city-guard-vehicle-icon-hook*)` instead of the hardcoded class 14 | hellcats and guard-bikes show a blue dot while the mod is on (the third `vehicle-guard` subtype, `paddywagon` in `meet-brutter.gc`, overrides `vehicle-method-128` and is unaffected) |
| `goal_src/jak2/engine/ai/traffic-h.gc` | `(define-extern *mod-city-vehicle-alert-blocked-hook* (function process-focusable symbol))` | lets a city mode veto the city-wide alert a guard vehicle raises when Jak attacks it |
| `goal_src/jak2/levels/city/traffic/citizen/mod-city-hooks.gc` | `mod-city-hook-vehicle-alert-blocked?` (stock `#f`) + `mod-city-pea-vehicle-alert-blocked?` (returns `*mod-city-peaceful?*`), installed into the new hook | City Peaceful: attacking a gunship is a private quarrel, not a city-wide manhunt |
| `goal_src/jak2/levels/city/traffic/vehicle/vehicle-guard.gc` | `vehicle-method-134` wraps only its `vehicle-method-111` call in the new hook; `pursuit-target` and the `alert` flag are still set unconditionally | those two lines ARE the vehicle's own reaction (`active:post` — `vehicle-guard-method-150` — `vehicle-method-108` — `hostile` — `stop-and-shoot`), so the attacked vehicle retaliates exactly as in retail while nothing is broadcast to the rest of the city |
| `goal_src/jak2/pc/features/crimson-blueguard-peaceful-menu.gc` | the toggle's flush is now `'kill-all` + `'spawn-all` instead of five `'deactivate-by-type` | the traffic engine allocates each pool's processes once at city load and then reuses them, so a parked `crimson-guard` comes back red; only a destroy + rebuild re-runs the red/blue pick. Removes the "reload a save to see blue guards" step |

**Native non-regression:** with `*mod-city-peaceful?*` `#f` (the shipped default) Haven City is
byte-for-byte stock Jak 2 — no `crimson-blue-guard` is ever constructed, want-counts are retail,
and every `*mod-city-*-hook*` resolves to its stock-equivalent branch. The only always-on deltas
are cosmetic/harmless: the `crimson-blue-guard` art-group logs in at city load (unused), a
`citizen` skips its look-at when the focus is `dead`/`inactive` (`citizen.gc`), a dormant
`blue-guard-frustum` / `blue-guard` pair sits at the end of `*minimap-class-list*` (`minimap.gc`
— with the flag off `citizen-init!` never asks for the first and
`*mod-city-guard-vehicle-icon-hook*` returns the stock class 14 for the second), and the custom
art-group link path in `joint.gc`/`level.gc` is inert (empty registration list). The C++
`build-actor`/`Tools.cpp` changes are opt-in (`native-header #f` default).

## 7. How to Test

1. `task build-release-game` (or `build-debug-game`) — only needed after a C++ change
   (`build_actor.cpp`/`Tools.cpp`); not needed for GOAL-only iteration.
2. `task extract` — required once (or after the `.glb` model changes) to bake Circuit 2, see §4.3.
   Check the log for `Adding custom model crimson-blue-guard-lod0 to common` and no
   `merc failed to find texture` for it.
3. `task repl`, then `(mi)` — must reach "Successfully built all N targets" with no
   `could not find a master slot to link` / `link-art` errors.
4. `task boot-game` (or `(r)` from the REPL), reach Haven City.
4b. **Enable the mod:** press **L3 + SELECT** to open the Mods menu, then `crimson-blueguard-peaceful ▸ Enable` (works in a retail boot too). OFF by default —
    verify first that with it OFF the city shows **only red guards** and retail traffic density.
    Toggling it re-rolls the ambient guards immediately (`mod-crimson-blueguard-peaceful-flush-guards`).
5. With the mod ON, at the REPL
   `(spawn-crimson-blue-guard-debug 0)` / `(...  1)` to force-spawn a baton/gun guard in front of you (in the city it takes an inactive blue guard from the traffic pool);
   confirm it's textured and its idle/walk/run/notice/hostile/knocked/get-up/die animations all
   play correctly and match a regular guard's timing and sound cues 1:1.
6. **Passivity:** with no alert active, walk up to / bump a blue guard — it should not attack.
7. **No alarm on a general alert:** trigger a real city alert some other way (shoot a red guard,
   commit a crime). A nearby blue guard should stay passive toward Jak — it must not join the
   alert against him.
8. **Personal retaliation, no alarm:** hit/shoot a blue guard directly. It should react exactly
   like a red guard would (flinch/knockback/get-up animation, then fight back at normal range),
   but the city-wide alert (top-right alarm indicator) should **not** trigger from this.
9. **Death, collision, everything else:** kill a blue guard, get it hit by a vehicle, shocked
   (yellow hit), etc. It must look and animate like a red guard — same
   death animation, no different collision (its health, weapons and combat ranges are this mod's own, see §1). Any other difference here is a bug (most likely
   an animation-index drift — see the native-header/reorder pitfall in §2–§3).
10. **Manual guard-vs-guard trigger:** `(define g (spawn-crimson-blue-guard-debug 0))` then
    `(crimson-blue-guard-attack-guards (the-as crimson-blue-guard g))` near a red guard — it should
    go hostile and fight. This combination has no native precedent (stock guards never fight each
    other), so pay attention to whether the approach/attack range looks normal.
11. With the mod ON and no REPL spawns, confirm blue guards keep showing up in ambient traffic,
    mixed with red ones.
12. Regression: boot a couple of other, untouched levels/cities and confirm no new spawn/link-art
    errors in `log/jak2.<ts>.log`.

## 8. Status

| Item | State |
|---|---|
| `build-actor :native-header #t` (C++ + GOAL macro) | ✅ done, compiled and boot-tested |
| `.glb` animation reordering | ✅ done, verified programmatically and in-game (correct animations play) |
| `crimson-blue-guard` entity (`deftype`/`defskelgroup`/`init-enemy!`) | ✅ done, compiled and boot-tested |
| DGO residency (code + art, 11 files) | ✅ done |
| Ambient traffic mixing | ✅ done, boot-tested |
| Circuit 2 (`models/common` + `task extract`) | ✅ done — guard renders fully textured |
| Passivity toward Jak + personal retaliation, no alarm | ✅ done, verified in-game |
| `crimson-blue-guard-attack-guards` manual trigger | ✅ done, verified in-game |
| Death dissolve sequence (`die` state override + `merc-death-spawn 73` + `knocked-fatal?`) | ✅ done, verified in-game: solves the C++ `generic_merc_death` exit status 5 crash via direct GOAL purple particle dissolution loop, plays `"enemy-fizz"`, hides mesh, and keeps knocked-down guards flat on the ground |
| City Peaceful patrol squads (2-3 members, formation navigation, adaptive speed, leader promotion) | ✅ done, verified in-game: dynamic wing offsets, smooth squad pacing, clean automatic promotion if leader dies |
| Squad mutual defense & Faction friendly-fire immunity | ✅ done, verified in-game: squad responds as a unit without city sirens; blue members & projectiles are fully immune to friendly fire |
| Squad weapon loadout diversity | ✅ done, verified in-game: 3-man squads always have 1 Taser, 1 Rifle, 1 Grenade Launcher; 2-man squads have 2 distinct weapons |
| Faithful Crimson Guard combat AI | ✅ done, verified in-game: standoff distance (~6.5m–9m), reactive laser bursts/parabolic grenades once LOS is acquired (up to 50m), evasive sideways rolls, emergency-only close attack (< 2.5m) followed by evasive recovery roll |
| Mods menu toggle (`crimson-blueguard-peaceful ▸ Enable`, L3 + SELECT, retail-safe popup menu) | ✅ done: one flag, `*mod-city-peaceful?*` (City Peaceful); each toggle flushes & respawns the city guards so the new rules apply immediately |
| City Insurrection (district zoning, configurable war zone, inter-faction combat, alert-free zones) | not in this mod — it ships in [`whozghiar/jak2-mod-haven-city-rebellion`](https://github.com/whozghiar/jak2-mod-haven-city-rebellion) |

## 9. "Mods" Menu Toggle & Features

The Mods menu (a retail-safe popup menu opened with **L3 + SELECT** in a normal launcher boot,
`goal_src/jak2/pc/features/mods-menu.gc`) has a `crimson-blueguard-peaceful` entry with one toggle,
`Enable (blue guards + neutral patrol squads)`, which flips `*mod-city-peaceful?*` (**City
Peaceful**). It is off by default and freely reversible.

### 9.1 City Peaceful (✅ Fully Implemented)
When toggled on in the Mods menu:
- **Ambient Patrol Squads:** blue guards spawn in tight 2-to-3 member squads walking Haven City in
  formation (wingmen offset relative to the leader's rotation quaternion). Followers dynamically
  accelerate (up to 1.5×) or slow down (0.85×) to keep rank, and automatically promote follower 1
  to squad leader if the leader dies.
- **Weapon Diversity:** every 3-man squad features exactly one Taser guard (`guard-type 0`), one
  Rifle guard (`guard-type 1`), and one Grenade Launcher guard (`guard-type 2`). Every 2-man squad
  has two distinct weapons.
- **Mutual Defense:** if any squad member is attacked by Jak or another enemy, the entire squad
  retaliates together in self-defense, without triggering the city-wide alarm or calling red guards.
- **Friendly-Fire Immunity:** projectiles and attacks originating from blue guards are filtered out
  within the faction, preventing infighting or fratricidal aggro.
- **Guard Vehicles Fight Alone:** shooting or ramming a hellcat / guard-bike no longer puts the
  whole city on alert. The attacked gunship takes Jak as its own pursuit target and opens fire
  by itself, exactly as it would in retail; every other guard in Haven City keeps patrolling.
  Destroying it is already silent too — `crimson-blue-guard-rider`'s `knocked-off` handler
  skips the `'increase-alert-level` the stock red rider sends.
- **Instant Toggle:** flipping `Enable` runs a full `'kill-all` + `'spawn-all` on the traffic
  manager, so blue guards, blue pilots and blue map dots appear within a second or two — no
  save reload needed.
- **Faithful Combat AI:** ranged guards maintain standoff engagement distance, fire bursts or
  grenades upon acquiring LOS (up to 50m), and execute evasive sideways rolls (`roll-left` /
  `roll-right`). Melee rifle-butts are strictly an emergency counter (< 2.5m) immediately followed
  by an evasive roll to resume a firing stance.

### 9.2 City Insurrection (not in this mod)
City Insurrection, the three-front territorial civil-war mode, is not part of this repository:
none of its code (`mod-city-insurrection.gc`, its war-zone picker) is on this mod's branch, and
`*mod-city-insurrection?*` stays `#f`. It ships in
[`whozghiar/jak2-mod-haven-city-rebellion`](https://github.com/whozghiar/jak2-mod-haven-city-rebellion),
whose technical README documents it.

---
*(AI-assisted)*

