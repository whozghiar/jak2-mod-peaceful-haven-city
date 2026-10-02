#!/usr/bin/env python3
"""
Synchronize a mod with master-dev.

Works on the checkout you run it from:
- a mod repository checked out in the mother repository (<owner>/jak-project) as mods/<name>
  (merges origin/master-dev, pushes to the mod repository's main),
- a standalone clone of a mod repository (merges master-dev from its `mother` remote, added on
  first use), or
- a mod branch of the mother repository, restored from its archive tag (merges origin/master-dev).

By default, this script uses `git merge` (safe, non-destructive, preserves commit SHAs
for published branches). It also offers an explicit `--rebase` option for developers
who prefer a linear commit history on unshared/local branches.

Usage:
    python scripts/modding/sync_branch_with_master_dev.py                  # Merge master-dev into the current mod
    python scripts/modding/sync_branch_with_master_dev.py --rebase         # Rebase the current branch onto master-dev
    python scripts/modding/sync_branch_with_master_dev.py --push           # Merge and push to origin
    python scripts/modding/sync_branch_with_master_dev.py --branch jak2/features/foo  # Target a specific branch
"""

import argparse
import os
import re
import shutil
import subprocess
import sys

import sync_common

def run_cmd(cmd, check=True, capture=True):
    print(f">> Running: {cmd}")
    res = subprocess.run(
        cmd,
        shell=True,
        text=True,
        capture_output=capture,
        cwd=REPO_ROOT,
        encoding="utf-8",
        errors="replace"
    )
    if res.stdout and capture:
        print(res.stdout.strip())
    if res.stderr and res.returncode != 0:
        print(res.stderr.strip(), file=sys.stderr)
    if check and res.returncode != 0:
        sys.exit(res.returncode)
    return res


def find_repo_root():
    """The checkout this script runs against: the git toplevel of the current directory."""
    res = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
    if res.returncode != 0:
        print("Error: run this script from inside a git checkout.", file=sys.stderr)
        sys.exit(1)
    return res.stdout.strip()


REPO_ROOT = find_repo_root()


def git_quiet(*args):
    """Run git without a shell, ignoring failures. Shell redirections such as 2>/dev/null
    do not exist in cmd.exe, which Python uses for shell=True on Windows."""
    return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")


def drop_path(path):
    """Remove a path from the merge result, whether git still tracks it or not."""
    git_quiet("rm", "-r", "-q", "-f", "--", path)
    full = os.path.join(REPO_ROOT, path)
    if os.path.isdir(full) and not os.path.islink(full):
        shutil.rmtree(full)
    elif os.path.lexists(full):
        os.remove(full)
    git_quiet("add", "-A", "--", path)


def get_current_branch():
    res = run_cmd("git rev-parse --abbrev-ref HEAD", check=False)
    if res.returncode == 0:
        return res.stdout.strip()
    return None


def is_working_tree_clean():
    res = run_cmd("git status --porcelain --ignore-submodules=all", check=False)
    return len(res.stdout.strip()) == 0


def is_ancestor(ancestor_ref, target_ref):
    res = run_cmd(f"git merge-base --is-ancestor {ancestor_ref} {target_ref}", check=False)
    return res.returncode == 0


def default_remote():
    """origin in the mother repository itself, mother in a standalone clone of a mod repository."""
    url = git_quiet("remote", "get-url", "origin").stdout.strip()
    return "origin" if re.search(r"/jak-project(\.git)?/?$", url) else "mother"


def push_target(branch):
    """Where `branch` publishes: its upstream remote and branch (mods/<name> pushes to <name>/main)."""
    remote = git_quiet("config", "--get", f"branch.{branch}.remote").stdout.strip() or "origin"
    merge = git_quiet("config", "--get", f"branch.{branch}.merge").stdout.strip() or f"refs/heads/{branch}"
    return remote, merge.replace("refs/heads/", "", 1)


def ensure_remote(name):
    """A mod repository reaches master-dev through a `mother` remote; add it on first use."""
    if run_cmd(f"git remote get-url {name}", check=False).returncode != 0:
        if name != "mother":
            print(f"Error: remote '{name}' does not exist.", file=sys.stderr)
            sys.exit(1)
        # The mother repository sits next to the mod repository: <owner>/jak-project.
        owner = sync_common.github_owner(REPO_ROOT)
        run_cmd(f"git remote add mother https://github.com/{owner}/{sync_common.MOTHER_NAME}.git")


def main():
    parser = argparse.ArgumentParser(
        description="Synchronize the current (or specified) branch with master-dev."
    )
    parser.add_argument(
        "--branch",
        help="Target branch to synchronize (defaults to currently active branch)."
    )
    parser.add_argument(
        "--rebase",
        action="store_true",
        help="Use 'git rebase' instead of 'git merge' (rewrites commit history, use with caution on published branches)."
    )
    parser.add_argument(
        "--push",
        action="store_true",
        help="Push the synchronized branch to where it publishes (its upstream) after success."
    )
    parser.add_argument(
        "--source",
        default="master-dev",
        help="Source base branch to synchronize from (default: master-dev)."
    )
    parser.add_argument(
        "--remote",
        help="Remote that holds the source branch. Default: origin in the mother repository, "
             "mother (added automatically) in a standalone clone of a mod repository."
    )
    parser.add_argument(
        "--local-source",
        action="store_true",
        help="Merge the local source branch as-is, without fetching (used by create_mod_repo.py)."
    )
    parser.add_argument(
        "--mod-repo",
        action="store_true",
        help="Apply the mod repository rules (only release.yml, lint.yml and build.yml are kept). "
             "Implied for mods/<name> branches and when the remote is not origin."
    )
    args = parser.parse_args()
    remote = args.remote or default_remote()

    # Determine target branch
    target_branch = args.branch.strip() if args.branch else get_current_branch()
    if not target_branch or target_branch == "HEAD":
        print("Error: Could not determine current branch. Please specify with --branch <name>.", file=sys.stderr)
        sys.exit(1)

    mod_repo = args.mod_repo or remote != "origin" or target_branch.startswith("mods/")
    allowed_workflows = (sync_common.ALLOWED_MOD_REPO_WORKFLOWS if mod_repo
                         else sync_common.ALLOWED_MOD_BRANCH_WORKFLOWS)

    source_branch = args.source.strip()
    source_ref = source_branch if args.local_source else f"{remote}/{source_branch}"

    if target_branch == source_branch:
        print(f"Error: Target branch cannot be the source base branch '{source_branch}'.", file=sys.stderr)
        sys.exit(1)

    print(f"\n=== Synchronizing with {source_ref} ===")
    print(f"Checkout     : {REPO_ROOT}")
    print(f"Target Branch: {target_branch}")
    print(f"Source Base  : {source_ref}")
    print(f"Mode         : {'mod repository' if mod_repo else 'mod branch'}")
    print(f"Strategy     : {'REBASE (linear history)' if args.rebase else 'MERGE (safe, preserves SHAs)'}")

    # Check cleanliness
    if not is_working_tree_clean():
        print("\nError: Working tree has uncommitted modifications.", file=sys.stderr)
        print("Please commit or stash your changes before synchronizing:", file=sys.stderr)
        print("    git stash", file=sys.stderr)
        sys.exit(1)

    # Fetch source
    if not args.local_source:
        ensure_remote(remote)
        print(f"\nFetching latest {source_ref}...")
        run_cmd(f"git fetch {remote} {source_branch}")

    # Switch to target branch if not already on it
    current_branch = get_current_branch()
    if current_branch != target_branch:
        print(f"\nChecking out {target_branch}...")
        run_cmd(f"git checkout {target_branch}")

    # Check if already up to date
    if is_ancestor(source_ref, "HEAD"):
        print(f"\n[OK] Branch '{target_branch}' is already fully up-to-date with {source_ref}!")
        return

    if args.rebase:
        print(f"\nRebasing {target_branch} onto {source_ref}...")
        rebase_res = run_cmd(f"git rebase {source_ref}", check=False)
        if rebase_res.returncode != 0:
            print("\n⚠️ Conflict encountered during rebase!", file=sys.stderr)
            print("To resolve conflicts:", file=sys.stderr)
            print("  1. Resolve conflicted files in your editor.")
            print("  2. git add <resolved_files>")
            print("  3. git rebase --continue")
            print("Or abort with: git rebase --abort")
            sys.exit(rebase_res.returncode)
        print(f"\n[OK] Successfully rebased {target_branch} onto {source_ref}!")
        if args.push:
            push_remote, push_branch = push_target(target_branch)
            print(f"\nPushing (force-with-lease) {target_branch} to {push_remote}/{push_branch}...")
            run_cmd(f"git push --force-with-lease {push_remote} {target_branch}:{push_branch}")
            print(f"[OK] Pushed to {push_remote}/{push_branch} successfully.")
    else:
        print(f"\nMerging {source_ref} into {target_branch}...")
        # Ensure 'ours' merge driver is enabled for .gitattributes protection
        run_cmd("git config merge.ours.driver true", check=False)

        run_cmd(f'git merge {source_ref} --no-commit', check=False)

        # Auto-resolve the deterministic documentation and workflow rules
        # (see sync_common.classify_conflict_path)
        unmerged_res = run_cmd("git diff --name-only --diff-filter=U", check=False)
        unmerged = [l.strip() for l in unmerged_res.stdout.splitlines() if l.strip()]
        for f in unmerged:
            action = sync_common.classify_conflict_path(f, allowed_workflows)
            print(f"   conflict {f}: {action or 'manual'}")
            if action == "ours":
                git_quiet("checkout", "HEAD", "--", f)
                git_quiet("add", "--", f)
            elif action == "theirs":
                if git_quiet("checkout", "MERGE_HEAD", "--", f).returncode:
                    git_quiet("rm", "-q", "-f", "--", f)  # deleted on master-dev
                git_quiet("add", "-A", "--", f)
            elif action == "drop":
                drop_path(f)

        # CRITICAL: Always ensure the mod's root README.md is strictly preserved from HEAD
        # (prevents Git 3-way merge from silently splicing master-dev's hub README into the mod's)
        git_quiet("checkout", "HEAD", "--", "README.md")
        if mod_repo:
            # Same for a mod repository's catalog: it names this mod only, or does not exist
            # before the mod's first release, while master-dev's index.json is the global catalog.
            if git_quiet("cat-file", "-e", "HEAD:index.json").returncode == 0:
                git_quiet("checkout", "HEAD", "--", "index.json")
            else:
                drop_path("index.json")

            # The knowledge base is a submodule on master-dev. A mod that edited the plain copy its
            # old branch carried comes out of the merge without the submodule (a file/directory
            # conflict): put master-dev's pointer back in place of the old copy.
            kb = ".agents/skills"
            theirs = git_quiet("ls-tree", source_ref, kb).stdout.split()
            staged = git_quiet("ls-files", "-s", "--", kb).stdout.split()
            if theirs[:1] == ["160000"] and staged[:1] != ["160000"]:
                git_quiet("rm", "-r", "-q", "-f", "--cached", "--", kb)
                kb_dir = os.path.join(REPO_ROOT, kb)
                if os.path.isdir(kb_dir) and not os.path.exists(os.path.join(kb_dir, ".git")):
                    shutil.rmtree(kb_dir)
                git_quiet("update-index", "--add", "--cacheinfo", f"160000,{theirs[2]},{kb}")

        # master-dev-only files ride along on a clean, no-conflict merge too:
        # strip them back out (see sync_common).
        for mdo_path in sync_common.MASTER_DEV_ONLY_PATHS:
            if os.path.isfile(os.path.join(REPO_ROOT, mdo_path)):
                run_cmd(f'git rm -f -q "{mdo_path}"', check=False)

        # Same for any workflow this kind of mod does not carry: a clean merge brings
        # it in with no conflict to catch, so it is swept out explicitly.
        for wf_path in sync_common.stray_workflow_files(REPO_ROOT, allowed_workflows):
            run_cmd(f'git rm -f -q "{wf_path}"', check=False)

        run_cmd('git add README.md', check=False)

        # Refresh index.json's display metadata only — a routine sync is not a release,
        # so it must never fabricate a draft versions[] entry (see update_mod_catalog.py's
        # refresh_metadata_only).
        catalog_script = os.path.join(REPO_ROOT, "scripts", "modding", "update_mod_catalog.py")
        run_cmd(f'python "{catalog_script}" --branch "{target_branch}" --metadata-only', check=False)
        run_cmd('git add index.json', check=False)

        # Verify if real source code conflicts remain
        remaining_res = run_cmd("git diff --name-only --diff-filter=U", check=False)
        remaining = [l.strip() for l in remaining_res.stdout.splitlines() if l.strip()]
        if remaining:
            print("\n⚠️ Real code conflict encountered during merge!", file=sys.stderr)
            print(f"Conflicting files: {', '.join(remaining)}", file=sys.stderr)
            print("To resolve conflicts:", file=sys.stderr)
            print("  1. Resolve conflicted files in your editor.")
            print("  2. git add <resolved_files>")
            print('  3. git commit -m "fix: resolve merge conflicts with master-dev (AI-assisted)"')
            print("Or abort with: git merge --abort")
            sys.exit(1)

        run_cmd(f'git commit -m "chore(sync): merge {source_ref} into {target_branch} (AI-assisted)"')
        print(f"\n[OK] Successfully merged {source_ref} into {target_branch}!")
        if args.push:
            push_remote, push_branch = push_target(target_branch)
            print(f"\nPushing {target_branch} to {push_remote}/{push_branch}...")
            run_cmd(f"git push {push_remote} {target_branch}:{push_branch}")
            print(f"[OK] Pushed to {push_remote}/{push_branch} successfully.")

    print("\nSynchronization completed successfully!")


if __name__ == "__main__":
    main()
