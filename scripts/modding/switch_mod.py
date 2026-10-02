#!/usr/bin/env python3
"""
Switch this working directory between master-dev, the mod repositories and the mods still on a
branch, the way `git switch` moved between mod branches.

    task modding-switch -- jak2-blue-krimzon-guard          # a mod repository
    task modding-switch -- master-dev                       # the modding base
    task modding-switch -- jak2/features/haven-city-chaos   # a mod still on a branch
    task modding-switch -- --list                           # what you can switch to

Every mod repository shares its history with the mother repository (<owner>/jak-project), so one
clone holds them all:
each mod repository is a remote named after it, and its main branch is the local branch
mods/<name>, created and fetched on first use; `git push` on it goes to that repository's main.
iso_data/, decompiler_out/, out/ and the sccache cache stay shared by every mod.

Why not a bare `git switch`: on master-dev and in mod repositories, .agents/skills is the
knowledge-base submodule, while the mods still on a branch carry a plain copy of the skills at
the same path, and git refuses to put one in place of the other. Before switching to such a
branch, this script parks the submodule (after checking it holds no unpushed work). To come back
from one, run `git switch master-dev` (or `git switch mods/<name>`) then `task kb-update`: those
branches predate this script.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

import sync_common

if hasattr(sys.stdout, "reconfigure"):
    # Repository descriptions may hold characters a Windows console code page cannot encode.
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[2]
KB = ".agents/skills"
# Must match MOD_REPO_TOPIC in sync_global_catalog.py.
MOD_REPO_TOPIC = "opengoal-mod"


def git(*args: str, check: bool = True, cwd: Path = REPO_ROOT) -> str:
    res = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if check and res.returncode:
        sys.exit(f"git {' '.join(args)} failed:\n{res.stderr.strip()}")
    return res.stdout.strip()


def ref_exists(ref: str) -> bool:
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref], cwd=REPO_ROOT,
                          capture_output=True).returncode == 0


def owner() -> str:
    return sync_common.github_owner(REPO_ROOT)


def kb_is_submodule(ref: str) -> bool:
    """True when .agents/skills is the knowledge-base submodule at `ref` (a gitlink)."""
    return git("ls-tree", ref, KB, check=False).startswith("160000")


def kb_unpushed_work() -> str:
    kb = REPO_ROOT / KB
    if not (kb / ".git").exists():
        return ""
    edits = git("status", "--porcelain", check=False, cwd=kb)
    commits = git("log", "--oneline", "HEAD", "--branches", "--not", "--remotes", check=False, cwd=kb)
    return (edits + "\n" + commits).strip()


def mod_branch(name: str) -> str:
    """Make the mod repository <name> available here as the local branch mods/<name>."""
    branch = f"mods/{name}"
    if not git("remote", "get-url", name, check=False):
        git("remote", "add", name, f"https://github.com/{owner()}/{name}.git")
    print(f"Fetching {name} ...")
    if subprocess.run(["git", "fetch", "-q", name], cwd=REPO_ROOT).returncode:
        if not ref_exists(branch):
            sys.exit(f"{name}: no such mod repository or no network (see: task modding-switch -- --list)")
        print("warning: fetch failed, switching to the local copy")
    if not ref_exists(branch):
        git("branch", "-q", "--track", branch, f"{name}/main")
    elif not git("config", "--get", f"branch.{branch}.remote", check=False):
        git("branch", "-q", f"--set-upstream-to={name}/main", branch)
    git("config", f"remote.{name}.push", f"refs/heads/{branch}:refs/heads/main")
    return branch


def resolve(target: str) -> str:
    if target.startswith("mods/"):
        return mod_branch(target[len("mods/"):])
    if ref_exists(f"refs/heads/{target}") or ref_exists(f"refs/remotes/origin/{target}"):
        return target
    if re.fullmatch(r"jak[123]-[A-Za-z0-9_.-]+", target):
        return mod_branch(target)
    sys.exit(f"Unknown target '{target}': give a mod repository name (e.g. jak2-blue-krimzon-guard), "
             "master-dev, or a branch name (see: task modding-switch -- --list)")


def run_script(relative: str, *args: str) -> None:
    script = REPO_ROOT / relative
    if script.is_file():
        subprocess.run([sys.executable, str(script), "--quiet", *args], cwd=REPO_ROOT)


def switch(branch: str) -> None:
    if git("status", "--porcelain", "--ignore-submodules=all"):
        sys.exit("Commit or stash your changes first.")
    target_ref = branch if ref_exists(f"refs/heads/{branch}") else f"origin/{branch}"
    if kb_is_submodule("HEAD") and not kb_is_submodule(target_ref):
        work = kb_unpushed_work()
        if work:
            sys.exit(f"{KB} holds knowledge-base work that is not pushed yet:\n{work}\n"
                     "Commit and push it first (see the kb skill).")
        print(f"{branch} predates the knowledge-base submodule: parking {KB} ...")
        git("submodule", "deinit", "-q", "-f", KB)
        # Nothing ignores .claude/skills/ links on such a branch: drop them (task kb-update relinks).
        run_script("scripts/ai/link_skills.py", "--remove")
    git("switch", "-q", branch)
    if kb_is_submodule("HEAD"):
        run_script("scripts/ai/kb_sync.py")  # also refreshes the skill links
    print(f"Now on {branch} ({git('log', '-1', '--format=%h %s')})")
    if not (REPO_ROOT / "scripts" / "modding" / "switch_mod.py").is_file():
        print("This branch predates task modding-switch. To leave it: "
              "git switch master-dev (or mods/<name>), then task kb-update.")


def list_targets() -> None:
    local = {b[len("mods/"):] for b in git("for-each-ref", "--format=%(refname:short)", "refs/heads/mods/").split()}
    published = {}
    try:
        if shutil.which("gh"):
            out = subprocess.run(["gh", "repo", "list", owner(), "--topic", MOD_REPO_TOPIC, "--limit", "200",
                                  "--json", "name,description"], capture_output=True, text=True,
                                 encoding="utf-8", check=True).stdout
            repos = json.loads(out)
        else:
            req = urllib.request.Request(f"https://api.github.com/users/{owner()}/repos?per_page=100",
                                         headers={"Accept": "application/vnd.github+json", "User-Agent": "modding-switch"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                repos = [r for r in json.loads(resp.read().decode("utf-8"))
                         if MOD_REPO_TOPIC in (r.get("topics") or [])]
        published = {r["name"]: r.get("description") or "" for r in repos}
    except Exception as err:
        print(f"(could not list GitHub repositories: {err})")
    current = git("branch", "--show-current")
    print("Mod repositories (task modding-switch -- <name>):")
    for name in sorted(local | set(published)):
        mark = "*" if current == f"mods/{name}" else " "
        where = "here" if name in local else "on GitHub, fetched on first switch"
        print(f" {mark} {name:32} {where:36} {published.get(name, '')[:60]}")
    print("\nModding base: master-dev" + ("  (current)" if current == "master-dev" else ""))
    branches = sorted({b.split("origin/", 1)[-1] for b in git(
        "for-each-ref", "--format=%(refname:short)", "refs/heads/jak1", "refs/heads/jak2", "refs/heads/jak3",
        "refs/remotes/origin/jak1", "refs/remotes/origin/jak2", "refs/remotes/origin/jak3").split()})
    if branches:
        print("\nMod branches (kept; a mod moved to its own repository says where):")
        moved = {n.lower(): n for n in local | set(published)}
        for b in branches:
            m = re.match(r"^(jak[123])/[^/]+/(.+)$", b)
            repo = moved.get(f"{m.group(1)}-{m.group(2).replace('/', '-').replace('_', '-')}".lower()) if m else None
            note = f"moved to {repo}" if repo else ""
            print(f" {'*' if current == b else ' '} {b:40} {note}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("target", nargs="?", help="mod repository name, master-dev, or a branch name")
    parser.add_argument("--list", action="store_true", help="list what you can switch to")
    args = parser.parse_args()
    if args.list or not args.target:
        list_targets()
        return 0
    switch(resolve(args.target))
    return 0


if __name__ == "__main__":
    sys.exit(main())
