#!/usr/bin/env python3
"""
Merge the latest master-dev into every mod repository and push it: what
`task modding-sync-branch -- --push` does for the mod you are on, for all of them at once.

    task modding-sync-all                          # every mod repository
    task modding-sync-all -- jak2-mod-a jak2-mod-b # only these
    task modding-sync-all -- --dry-run             # report what would happen, merge and push nothing

The mod repositories are the local mods/<name> branches plus, when gh is installed, the
repositories of the same GitHub account that carry the opengoal-mod topic. For each one:
1. fetch it (adding it as a remote and a mods/<name> branch on first use);
2. skip it when its main already contains origin/master-dev, when mods/<name> holds commits
   that are not pushed (push them first: the merge starts from what is published), when
   mods/<name> is the branch checked out here (sync that one in place with
   `task modding-sync-branch -- --push`), or when its worktree has uncommitted changes;
3. merge origin/master-dev into it under the mod-repository rules of
   sync_branch_with_master_dev.py: in the mod's own worktree (.worktrees/<name>.jak-project)
   when it has one, otherwise in a temporary worktree outside this directory;
4. push the merge to the repository's main; mods/<name> follows.
A merge that hits a real conflict is abandoned and reported, and nothing is pushed for that
mod. Your working directory, its current branch and its uncommitted changes are not touched.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import switch_mod

REPO_ROOT = Path(__file__).resolve().parents[2]
SYNC_SCRIPT = REPO_ROOT / "scripts" / "modding" / "sync_branch_with_master_dev.py"
WORKTREES = Path(tempfile.gettempdir()) / "og-mod-worktrees"
SOURCE = "origin/master-dev"


def run(*args: str, cwd: Path = REPO_ROOT) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def count(commits: str) -> int:
    """Number of commits in a range such as a..b."""
    res = run("rev-list", "--count", commits)
    return int(res.stdout.strip()) if res.returncode == 0 else 0


def mod_names(selected: list[str]) -> list[str]:
    if selected:
        return selected
    names = {b[len("mods/"):] for b in run("for-each-ref", "--format=%(refname:short)",
                                            "refs/heads/mods/").stdout.split()}
    if shutil.which("gh"):
        res = subprocess.run(["gh", "repo", "list", switch_mod.owner(), "--topic", switch_mod.MOD_REPO_TOPIC,
                              "--limit", "200", "--json", "name", "--jq", ".[].name"],
                             capture_output=True, text=True)
        if res.returncode == 0:
            names |= set(res.stdout.split())
        else:
            print("(gh could not list the GitHub repositories: syncing the local mods/* branches only)")
    return sorted(names)


def checked_out_at(branch: str) -> Path | None:
    """The working directory that has branch checked out: this one, a worktree, or None."""
    path = None
    for line in run("worktree", "list", "--porcelain").stdout.splitlines():
        if line.startswith("worktree "):
            path = Path(line[len("worktree "):])
        elif line == f"branch refs/heads/{branch}":
            return path
    return None


def sync(name: str, dry_run: bool) -> tuple[bool, str]:
    """Bring one mod repository up to date. Returns (ok, what happened)."""
    branch, published = f"mods/{name}", f"{name}/main"
    try:
        switch_mod.mod_branch(name)  # remote, fetch, tracking branch
    except SystemExit as err:
        return False, f"not synced: {err}"
    unpushed = count(f"{published}..{branch}")
    if unpushed:
        return False, f"skipped: {branch} has {unpushed} commit(s) that are not pushed; push them, then run again"
    # A mod with its own worktree (.worktrees/<name>.jak-project) is merged in that worktree, since
    # git checks a branch out in one place only; the working directory this runs from is left alone.
    home = checked_out_at(branch)
    if home and home.resolve() == REPO_ROOT.resolve():
        return False, "skipped: checked out here; sync it in place with task modding-sync-branch -- --push"
    if home and run("status", "--porcelain", "--ignore-submodules=all", cwd=home).stdout.strip():
        return False, f"skipped: {home} has uncommitted changes; commit or stash them, then run again"
    if count(f"{branch}..{published}") and not dry_run:
        # fast-forward to what is published; in a worktree, move its files along with the branch
        if home:
            run("merge", "-q", "--ff-only", published, cwd=home)
        else:
            run("update-ref", f"refs/heads/{branch}", published)
    missing = count(f"{published}..{SOURCE}")
    if not missing:
        return True, "up to date"
    if dry_run:
        return True, f"would merge {missing} master-dev commit(s) and push"

    worktree = home or WORKTREES / name
    if not home:
        if worktree.exists():  # leftover of an interrupted run
            run("worktree", "remove", "--force", str(worktree))
        WORKTREES.mkdir(exist_ok=True)
        added = run("worktree", "add", "-q", str(worktree), branch)
        if added.returncode:
            return False, f"not synced: {added.stderr.strip()}"
    try:
        res = subprocess.run([sys.executable, str(SYNC_SCRIPT), "--remote", "origin", "--mod-repo", "--push"],
                             cwd=worktree, capture_output=True, text=True, encoding="utf-8", errors="replace")
        if res.returncode == 0:
            return True, f"merged {missing} master-dev commit(s), pushed to {published}"
        if run("rev-parse", "-q", "--verify", "MERGE_HEAD", cwd=worktree).returncode == 0:
            run("merge", "--abort", cwd=worktree)
            files = next((l.split(":", 1)[1].strip() for l in res.stderr.splitlines()
                          if l.startswith("Conflicting files:")), "see the merge output")
            return False, (f"conflict in {files}; nothing pushed. Resolve it by hand: "
                           f"task modding-switch -- {name}, then task modding-sync-branch -- --push")
        if count(f"{published}..{branch}"):
            return False, f"merged here but the push failed; retry with: git push {name}"
        lines = (res.stderr or res.stdout).strip().splitlines()
        return False, f"not synced: {lines[-1] if lines else 'the sync script failed'}"
    finally:
        if not home:
            run("worktree", "remove", "--force", str(worktree))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("mods", nargs="*", help="mod repository names (default: all of them)")
    parser.add_argument("--dry-run", action="store_true", help="report what would happen, merge and push nothing")
    args = parser.parse_args()

    if run("fetch", "-q", "origin", "master-dev").returncode:
        sys.exit("Could not fetch origin/master-dev: check the network and your access to origin.")
    print(f"master-dev: {run('log', '-1', '--format=%h %s', SOURCE).stdout.strip()}\n")
    results = []
    for name in mod_names(args.mods):
        ok, what = sync(name, args.dry_run)
        results.append(ok)
        print(f"{'  ' if ok else '! '}{name}: {what}")
    if not results:
        print("No mod repository found (task modding-switch -- --list).")
    return 0 if all(results) else 1


if __name__ == "__main__":
    sys.exit(main())
