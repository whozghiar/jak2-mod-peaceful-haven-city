# Crimson Blue Guard — Jak 2

<p align="center">
  <img src="https://img.shields.io/badge/OpenGOAL-Mod-blue.svg" alt="OpenGOAL Mod">
  <img src="https://img.shields.io/badge/Game-Jak%202-orange.svg" alt="Target Game">
  <img src="https://img.shields.io/badge/AI--assisted-Modding-purple.svg" alt="AI Assisted">
</p>

<p align="center">
  <a href="#-english-version"><b>🇬🇧 English Version</b></a> &nbsp;•&nbsp; <a href="#-version-française"><b>🇫🇷 Version Française</b></a>
</p>

---

# 🇬🇧 English Version

> [!NOTE]
> This mod moved from the `jak2/features/peaceful-haven-city` branch of [whozghiar/jak-project](https://github.com/whozghiar/jak-project) to this repository. Earlier releases stay installable from the launcher catalog.

## 📖 Overview
Adds a blue-recolored Crimson Guard as its own, standalone entity — a new GOAL type
(`crimson-blue-guard`) that reuses 100% of the stock `crimson-guard`'s behavior, animations and
sounds, only with a re-textured mesh. It appears in Haven City mixed into the normal ambient
guard traffic, alongside the regular red guards.

- **Target Game:** Jak 2
- **Active Branch:** `jak2/features/city-peaceful` — base blue-guard traffic + the **City Peaceful**
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

# 🇫🇷 Version Française

## 📖 Présentation du Mod
Ajoute un garde crimson recoloré en bleu comme une entité à part entière — un nouveau type GOAL
(`crimson-blue-guard`) qui réutilise à 100% le comportement, les animations et les sons du garde
crimson d'origine (`crimson-guard`), seul le mesh/la texture change. Il apparaît dans Haven City
mélangé au trafic ambiant normal, aux côtés des gardes rouges classiques.

- **Jeu Ciblé :** Jak 2
- **Branche Active :** `jak2/features/city-peaceful` — base blue-guard + le mode **City Peaceful** :
  les gardes bleus ambiants patrouillent en escouades neutres de 2 à 3 membres.

### Famille de branches
| Branche | Ajoute |
|---|---|
| `jak2/features/blueguard-traffic` | base : entité `crimson-blue-guard`, IA de combat fidèle, spawn dans le trafic ambiant, couche de hooks modulaire |
| **`jak2/features/city-peaceful`** *(celle-ci)* | **escouades** de patrouille bleues neutres — nav en formation, vitesse adaptative, réélection du chef, défense mutuelle, immunité aux tirs alliés |
| `jak2/features/city-insurrection` | **guerre civile territoriale** à trois fronts — zonage par quartier, combat inter-factions autonome, zones sans alerte, sélecteur de quartier de guerre |
| `jak2/features/blueguard` | les deux modes ensemble (mutuellement exclusifs au runtime) |

**Le mod est livré DÉSACTIVÉ.** Il s'active en jeu avec **L3 + SELECT** dans `Mods ▸ crimson-blueguard-peaceful ▸ Enable` (fonctionne en boot normal, sans mode debug).
Désactivé, **Abriville est identique au Jak 2 d'origine** — aucun garde bleu, les effectifs de
véhicules-gardes ambiants sont ceux du jeu d'origine, alertes et civils normaux. L'**activer**
enclenche tout le paquet d'un coup : gardes bleus ambiants **et** comportement d'escouades de
patrouille neutres. Le choix re-tire les gardes ambiants immédiatement et persiste au
rechargement des niveaux.

## ✨ Fonctionnalités Clés
- **Nouvelle entité à part entière :** `crimson-blue-guard` est un vrai type GOAL (sous-type de
  `crimson-guard`), pas un simple remplacement de texture global — les gardes rouges classiques
  continuent d'apparaître normalement.
- **Identique au garde classique en tout le reste :** animations, sons, mort (dissolution en particules violettes et maintien au sol après projection), collision, arsenal —
  tout est hérité sans modification (mêmes indices de slot, voir la doc technique) ; seuls le
  mesh/skeleton-group et la différence de comportement ci-dessous changent.
- **Sa propre logique de faction :** contrairement au garde classique, il est passif envers Jak par
  défaut et ne rejoint jamais une alerte générale de la ville contre lui. Si Jak l'attaque
  personnellement, il riposte sans déclencher l'alarme de la ville. Robustesse accrue : 8 PV
  (le double des gardes classiques) pour des affrontements tactiques prolongés.
- **Déclencheur manuel « combattre les autres gardes » :** `crimson-blue-guard-attack-guards`, une
  petite fonction qui le fait devenir hostile envers le `crimson-guard` rouge le plus proche —
  jamais automatique, appelée explicitement (REPL ou code).
- **Mélangé au trafic ambiant de la ville :** le traffic-manager fait apparaître la variante bleue
  pour une fraction configurable des spawns de gardes ambiants (`*crimson-blue-guard-ratio*`,
  1 sur 2 du pool parité-id par défaut), aux côtés du garde classique.
- **IA de Combat Fidèle aux Crimson Guards :** les gardes armés d'un fusil ou d'un lance-grenades maintiennent une distance d'engagement tactique (jusqu'à 50 m), tirent des rafales/projectiles avec visée réactive et enchaînent des roulades d'esquive latérales (`roll-left` / `roll-right`). Les coups de crosse sont strictement réservés au contact d'urgence (< 2,5 m) et sont immédiatement suivis d'une roulade d'esquive pour reprendre le tir à distance. Les gardes au taser foncent au contact pour électrocuter avec des arcs électriques.
- **Mode City Peaceful** (`mod-city-peaceful.gc`, basculé depuis l'onglet Mods) : quand il est
  actif, un garde bleu ambiant fraîchement activé devient **chef d'escouade** et fait apparaître
  1-2 suiveurs derrière lui — nav en formation serrée avec vitesse de suiveur adaptative,
  réélection automatique du chef à la mort, arsenal distinct par membre, et riposte mutuelle
  (frappe-en un, toute l'escouade se retourne contre l'attaquant) — le tout sans jamais déclencher
  l'alarme de la ville. Les gardes bleus sont totalement immunisés aux tirs alliés entre eux.
- **Conducteurs de véhicules en gardes bleus (mode Peaceful) :** les cruisers de patrouille
  de la garde (`vehicle-guard`) sont conduits par des gardes bleus (`crimson-blue-guard-rider`).
  En cas d'éjection du véhicule, ils atterrissent sur la chaussée en gardes bleus à pied sans
  déclencher d'alerte de police.
- **Protection des civils / Suppression de l'alerte (mode Peaceful) :** attaquer ou tuer des
  piétons civils dans les rues ne déclenche plus l'alarme de police et ne fait plus monter le
  niveau d'alerte de la ville. Les gardes rouges classiques déclenchent toujours l'alerte
  normalement s'ils sont directement provoqués.
- **Couche modulaire `*mod-city-*-hook*` :** les fichiers moteur partagés appellent ~10 hooks
  nommés (déclarés dans `engine/ai/traffic-h.gc`) ; `mod-city-peaceful.gc` et `mod-city-hooks.gc`
  câblent les comportements requis, tandis que le reste conserve les valeurs d'origine. Les
  fichiers moteur restent identiques sur toute la famille de branches.

## 🚀 Guide Pas à Pas pour Lancer le Mod

### 1. Sélectionner le Jeu Actif
Assurez-vous que l'environnement cible Jak 2 :
```bash
task set-game-jak2
```

### 2. Compilation des Binaires
- **Statut :** `task build-release-game` (ou `task build-debug-game`) — requise. L'outil
  `build-actor` (`goalc/build_actor/jak2/build_actor.cpp`) et le compilateur de données `goalc`
  (`goalc/make/Tools.cpp`) ont tous deux reçu un nouveau flag optionnel `:native-header` utilisé
  pour construire l'art-group de cet acteur. Voir `docs/modding/build_and_iteration_workflow.md`.
- **Détails :** du C++ moteur/compilateur a été modifié (voir le tableau « Changements Moteur »
  dans la doc technique ci-dessous).
```bash
task build-release-game
```

### 3. Extraction des Données (Assets)
- **Statut :** Requise, une fois — la géométrie de rendu + textures réelles du garde
  (« Circuit 2 », voir la doc technique) sont cuites dans `GAME.fr3` par le décompilateur, à partir
  de `custom_assets/jak2/models/common/crimson-blue-guard-lod0.glb`. Nécessite un ISO Jak 2
  légalement dumpé.
```bash
task extract
```
Vérifiez dans le log la ligne `Adding custom model crimson-blue-guard-lod0 to common` et l'absence
d'erreur `merc failed to find texture` pour lui. Cette étape n'est **pas** à refaire après un
simple changement de code GOAL (`(mi)` suffit) — seulement quand le `.glb` lui-même change.

### 4. Lancer le Jeu
Lancez le jeu nativement :
```bash
task boot-game
```
*(Ou via le REPL OpenGOAL avec `task repl`, puis `(mi)` et `(r)`).*
Environ 1 spawn de garde ambiant sur 8 sera bleu dans Haven City. Pour le voir plus vite pendant
les tests, faites `(set! *crimson-blue-guard-ratio* 1)` au REPL une fois le jeu lancé — chaque
garde ambiant spawné devient bleu jusqu'à ce que vous remettiez `8` (ou la valeur de votre choix).
Vous pouvez aussi en faire apparaître un directement devant vous, sans dépendre du ratio, avec
`(spawn-crimson-blue-guard-debug 0)` (garde matraque) ou `(spawn-crimson-blue-guard-debug 1)`
(garde armé d'un fusil).

---

## 🎥 Démonstration Vidéo

[![Démonstration Vidéo](https://img.youtube.com/vi/SppDFeEd4r8/maxresdefault.jpg)](https://youtu.be/SppDFeEd4r8)

▶️ **[Regarder la vidéo de démonstration sur YouTube](https://youtu.be/SppDFeEd4r8)**

---

## 📖 Documentation Technique
Pour l'audit technique approfondi, l'architecture et les détails d'implémentation, consultez :
- 📄 [`docs/modding/current_mod/blue_guard_reskin_readme.md`](docs/modding/current_mod/blue_guard_reskin_readme.md)

---
*(AI-assisted)*
