# OpenGOAL Documentation Hub

Welcome to the documentation tree for the OpenGOAL project and modding framework (`jak-project`).

> ### Summary
>
> [1. Structure Overview](#1-structure-overview) · [2. Key Entry Points](#2-key-entry-points) · [3. Environment & Toolchain](#3-environment--toolchain-setup) · [4. Engine Architecture & Historical Notes](#4-engine-architecture--historical-notes)

---

## 1. Structure Overview

```text
docs/
├── modding/                # Complete modding documentation, verified references & tool guides
├── setup/                  # Environment, toolchain & IDE setup (VSCode, VS, Linux, Windows, macOS)
├── progress-notes/         # Upstream decompilation logs, assembly notes & reverse-engineering records
├── scratch/                # Upstream developer scratchpad and temporary notes
└── project-overview.md     # Architecture overview of OpenGOAL compiler, runtime & decompiler
```

---

## 2. Key Entry Points

### Modding & AI-Assisted Development
- **[Lisp Wiki (`.agents/skills/goal-lisp/wiki/`)](../.agents/skills/goal-lisp/wiki/index.md)**: verified Lisp instructions in the knowledge-base submodule — patterns and engine model shared by the three games in `common.md`, each game's specifics in `jak1.md`, `jak2.md` and `jak3.md`.
- **[AI Agent & Developer Guide (`AGENTS.md`)](../AGENTS.md)**: central rules, Taskfile command reference, REPL hot-reload cycle, ghost memory verification, and git branching standards.
- **[GitHub Actions Workflows Guide](modding/guides/github_workflows.md)**: detailed pedagogical guide to repository CI/CD, upstream synchronization, releases, and issue triaging.
- **[Task Commands & Modding Scripts Reference](modding/guides/task_scripts_reference.md)**: pedagogical reference for all Taskfile commands and `scripts/modding/*.py` automations.
- **[Modular Skills (`.agents/skills/`)](../.agents/skills/)**: high-density engineering skills loaded on demand:
  - [`goal-lisp`](../.agents/skills/goal-lisp/SKILL.md): GOAL syntax, state machines, types & macros.
  - [`engine-internals`](../.agents/skills/engine-internals/SKILL.md): C++ runtime, heaps & REPL workflow.
  - [`custom-actors-levels`](../.agents/skills/custom-actors-levels/SKILL.md): 3D models, Blender `.glb` exports, armatures & levels.
  - [`texture-modding`](../.agents/skills/texture-modding/SKILL.md): custom texture injection & replacement.
  - [`documentalist`](../.agents/skills/documentalist/SKILL.md): documentation standards enforcement.

---

## 3. Environment & Toolchain Setup

- **[Setup Guides (`docs/setup/`)](setup/)**:
  - **Operating Systems:** [Windows](setup/system/windows.md) · [Linux](setup/system/linux.md) · [macOS](setup/system/macos.md) · [Docker](setup/system/docker.md)
  - **IDEs & Editors:** [VSCode](setup/dev/vscode.md) · [Visual Studio](setup/dev/vs.md) · [Zed](setup/dev/zed.md)

---

## 4. Engine Architecture & Historical Notes

- **[Project Overview (`docs/project-overview.md`)](project-overview.md)**: Upstream architecture and component roles.
- **[Progress Notes (`docs/progress-notes/`)](progress-notes/)**: Decompilation notes, bone systems, joint decompression, and VU assembly documentation.
