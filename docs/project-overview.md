# OpenGOAL — Project Overview

## Summary
- [1. `goalc` (Compiler & REPL)](#1-goalc-compiler--repl)
- [2. `decompiler` (Asset & Code Extraction)](#2-decompiler-asset--code-extraction)
- [3. `goal_src/` (Game Source Code)](#3-goal_src-game-source-code)
- [4. `game` runtime (C++ Engine & Kernel)](#4-game-runtime-c-engine--kernel)

---

There are four main components to the project:

1. `goalc` — the GOAL compiler for x86-64 and interactive REPL.
2. `decompiler` — our decompiler for extracting retail game assets and code.
3. `goal_src/` — the directory containing all OpenGOAL / GOOS source code.
4. `game` — the C++ game runtime kernel simulating PS2 Emotion Engine RAM.

Let's break down each component.

---

## 1. `goalc` (Compiler & REPL)

Our implementation of GOAL is called **OpenGOAL**.

All of the compiler source code is located in `goalc/`. The compiler is controlled through an interactive prompt which can be used to:
- Enter commands to compile `.gc` source files.
- Connect to a running GOAL program for live interaction.
- Run the OpenGOAL debugger.
- Act as an interactive REPL (`(mi)`, etc.) to evaluate code on the fly in the running game memory.
- Pack and build binary data files.

### Running the Compiler

- **Environment Agnostic (Recommended):**
  If you have installed `task`, run:
  ```bash
  task repl
  ```
- **Linux:**
  Run the script: `scripts/shell/gc.sh`
- **Windows:**
  Run `scripts/batch/gc.bat` (Jak 1), `gc2.bat` (Jak 2) or `gc3.bat` (Jak 3).

---

## 2. `decompiler` (Asset & Code Extraction)

The second component of the project is the decompiler.

The decompiler outputs disassemblies, types, and human-readable GOAL source code in the `decompiler_out/` directory. Files in this folder are intended for inspection and are not directly consumed by the compiler.

### Running the Decompiler

You must possess a legitimate retail copy of the PS2 game and place all files from the DVD inside the corresponding folder within `iso_data/` (`jak1` for Jak 1 Black Label, `jak2`, `jak3`), as shown below:

![](./img/iso_data-help.png)

The decompiler extracts assets to the `assets/` folder. These assets will be used by the compiler when building the native port:
- **Environment Agnostic (Recommended):**
  ```bash
  task extract
  ```
  *(or `task decomp` for decompilation only)*
- **Linux:**
  `scripts/shell/decomp.sh`
- **Windows:**
  `scripts/batch/decomp-jak1.bat`

---

## 3. `goal_src/` (Game Source Code)

The game source code, written in OpenGOAL LISP, is located in `goal_src/`. All GOAL and GOOS code is organized by game:
- `goal_src/jak1/`
- `goal_src/jak2/`
- `goal_src/jak3/`

---

## 4. `game` runtime (C++ Engine & Kernel)

The final component is the **runtime**, located in `game/`. This is the native x86-64 executable written in C++ that emulates PS2 hardware structures and provides the environment for GOAL code to execute.

In the port, this includes:
- **The C Kernel (`game/kernel/`):** Contains the GOAL linker, memory heap allocators (`global`, `debug`), symbol table, type system, and low-level kernel dispatcher. It also handles TCP communication with the `goalc` compiler.
- **Sony Standard Library (`game/sce/`, `game/system/`):** Implements or stubs Sony PS2 SDK functions for file access, memory cards, controllers, and threading.
- **OVERLORD IOP Driver (`game/overlord/`):** The PS2 had a dedicated I/O Processor (IOP). Naughty Dog authored an IOP driver called OVERLORD for asynchronous DVD streaming and sound loading.
- **Sound Engine (`game/sound/`):** Implementation of Sony's `989SND` library and PC audio output backends (Cubeb).
- **PC Graphics Renderer (`game/graphics/`):** An OpenGL 4.3 pipeline that translates PS2 GS (Graphics Synthesizer) draw calls into modern PC shaders and render passes (TFRAG, TIE, MERC, SHRUB, etc.).
- **Extra Assets (`game/assets/`):** Supplemental PC port assets, icons, fonts, and configuration files.
