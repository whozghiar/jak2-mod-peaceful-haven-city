#!/usr/bin/env python3
"""
Shared rules used when master-dev is merged into a mod: by
sync_branch_with_master_dev.py (a mod branch of this repository, or a mod
repository syncing from its `mother` remote) and by create_mod_repo.py.

Why this module exists
-----------------------
Every sync must resolve the same handful of paths the same way (the mod's own
README stays the mod's, the shared docs come from master-dev, stray workflow
files are dropped). Keeping that rule table in its own module gives the
scripts and the workflows that rely on it (build.yml, lint.yml, release.yml)
one place to point at.
"""

import os
import re
import subprocess

# Every account keeps its mother repository under this name: a mod repository finds it next to
# itself, at https://github.com/<owner>/jak-project.
MOTHER_NAME = "jak-project"


def github_repo(remote="origin", cwd=None):
    """(owner, name) of a remote's GitHub URL, or None when the remote is missing or not on GitHub."""
    res = subprocess.run(["git", "remote", "get-url", remote], cwd=cwd, capture_output=True, text=True)
    m = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?/?$", res.stdout.strip())
    return (m.group(1), m.group(2)) if m else None


def github_owner(cwd=None):
    """The GitHub account of this clone's origin, which owns the mother and every mod repository."""
    repo = github_repo("origin", cwd)
    if not repo:
        raise SystemExit("origin is not a GitHub repository: clone <owner>/jak-project, or one of its "
                         "mod repositories, from GitHub.")
    return repo[0]

# Files that make sense only on master-dev. A plain `git merge master-dev`
# would otherwise happily carry them onto every mod branch (they are not in
# conflict, master-dev just added/changed them) — so both sync scripts
# explicitly `git rm` them back out after merging. Keep this list short: it
# is a statement of "this file does not belong on a mod branch", not a
# general-purpose ignore list.
# dependabot.yml: version-update PRs for GitHub Actions belong to the mother repository only;
# in every mod repository it opened the same handful of PRs, one branch each.
MASTER_DEV_ONLY_PATHS = [".github/ISSUE_TEMPLATE/mod-suggestion.yml", ".github/dependabot.yml"]

# The only workflow files a mod branch is meant to carry (see
# classify_conflict_path's "drop" rule below and AGENTS.md for why this fork
# does not mirror upstream's own CI workflows onto every branch). Repo-wide
# automation that only makes sense running from master-dev (upstream sync,
# issue triage, the global catalog) stays off this list on purpose.
ALLOWED_MOD_BRANCH_WORKFLOWS = {
    "release.yml",
    "lint.yml",
    "build.yml",
}

# A mod repository (one GitHub repository per mod, synced from the mother
# repository's master-dev) carries the same three.
ALLOWED_MOD_REPO_WORKFLOWS = {
    "release.yml",
    "lint.yml",
    "build.yml",
}


def stray_workflow_files(repo_root, allowed=ALLOWED_MOD_BRANCH_WORKFLOWS):
    """.github/workflows/* files on disk that don't belong on a mod branch.

    classify_conflict_path's "drop" rule only ever runs on paths git reports as
    CONFLICTED. A workflow that master-dev merely *adds* (not yet present on the
    mod branch, so nothing to conflict with) sails through a clean merge untouched
    — silently violating the same policy. Call this after every merge, conflict or
    not, exactly like MASTER_DEV_ONLY_PATHS, so a brand-new master-dev-only
    workflow can never linger on a mod branch just because it happened not to
    collide with anything.
    """
    workflows_dir = os.path.join(repo_root, ".github", "workflows")
    if not os.path.isdir(workflows_dir):
        return []
    return [
        f".github/workflows/{name}"
        for name in sorted(os.listdir(workflows_dir))
        if name not in allowed
        and os.path.isfile(os.path.join(workflows_dir, name))
    ]


def classify_conflict_path(filepath, allowed=ALLOWED_MOD_BRANCH_WORKFLOWS):
    """
    One rule table, one place. Given a path that conflicted (or would
    conflict) while merging master-dev into a mod branch, returns how to
    resolve it:
        "ours"   - keep the mod branch's own version (its README, its Tier-2 docs)
        "theirs" - take master-dev's version (shared guidelines/skills/tools)
        "drop"   - delete it (any workflow file not in
                   ALLOWED_MOD_BRANCH_WORKFLOWS — see AGENTS.md for why this
                   fork does not mirror upstream's own CI workflows)
        None     - not a path this project auto-resolves; a real conflict.
    """
    if filepath == "README.md" or filepath == "index.json" or filepath.startswith("docs/modding/current_mod/"):
        return "ours"
    if filepath in MASTER_DEV_ONLY_PATHS:
        # Never actually kept on a mod branch: dropping it here handles the
        # rare case where it shows up as a genuine merge conflict; the
        # common case (no conflict, silently carried over) is handled by
        # each script explicitly `git rm`-ing MASTER_DEV_ONLY_PATHS after
        # every merge, conflict or not.
        return "drop"
    if filepath.startswith(".github/workflows/"):
        return "theirs" if filepath[len(".github/workflows/"):] in allowed else "drop"
    if (filepath in ("AGENTS.md", "CLAUDE.md", ".gitmodules")
            or filepath.startswith((".claude/", ".gemini/", "scripts/ai/"))
            or filepath.startswith(".agents/")
            or filepath.startswith(".github/ISSUE_TEMPLATE/")
            or (filepath.startswith("docs/modding/") and not filepath.startswith("docs/modding/current_mod/"))):
        return "theirs"
    return None
