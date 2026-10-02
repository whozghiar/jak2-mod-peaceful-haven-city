#!/usr/bin/env python3
"""
Create a mod repository: one GitHub repository per mod, derived from master-dev.

    python scripts/modding/create_mod_repo.py            # asks for game, name, description, visibility
    python scripts/modding/create_mod_repo.py --new jak2/my-mod --description "One sentence." [--private]
    python scripts/modding/create_mod_repo.py --from-branch jak2/features/blue-krimzon-guard
    python scripts/modding/create_mod_repo.py --from-branch jak2/features/a jak2/features/b
    python scripts/modding/create_mod_repo.py --from-branch jak2/features/a --prepare-only

The repository is named <game>-mod-<slug>, the slug being the mod's launcher catalog key kept
verbatim (jak3-jetBoard keeps its capital B), so the launcher keeps seeing the same mod. In this
clone, the mod repository is the remote <name> and its main branch is the local branch
mods/<name>: switch to it with `task modding-switch -- <name>`. Nothing is ever deleted: the
source mod branch and mods/<name> both stay.

Each mod goes through two steps, so a failed run can simply be re-run:

1. Prepare (local only). A temporary worktree in the system temp folder (outside any editor
   workspace, so no IDE scans its checkout) builds mods/<name>: the
   mod (an existing mod branch, or master-dev with a README from the template), merged with
   master-dev under the mod-repository rules (sync_branch_with_master_dev.py --mod-repo), plus
   one commit with the repository-specific changes (README, catalog name and websiteUrl). On a
   re-run, a prepared branch that misses master-dev commits gets them merged in.
2. Publish. Creates the GitHub repository <owner>/<name> (public unless --private) with the
   opengoal-mod topic, which is how sync_global_catalog.py finds it, pushes mods/<name> as its
   main branch, and sets mods/<name> to track and push to it. Needs gh, authenticated with
   `gh auth login`. A private repository stays out of the launcher catalog: players cannot
   download its releases until it is made public.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import sync_common
from update_mod_catalog import sanitize_source_name

MOTHER_ROOT = Path(__file__).resolve().parents[2]
WORKTREES = Path(tempfile.gettempdir()) / "og-mod-worktrees"
TEMPLATE = MOTHER_ROOT / "docs" / "modding" / "templates" / "MOD_README.template.md"
SYNC_SCRIPT = MOTHER_ROOT / "scripts" / "modding" / "sync_branch_with_master_dev.py"
GAME_LABELS = {"jak1": "Jak 1", "jak2": "Jak 2", "jak3": "Jak 3"}
# Must match MOD_REPO_TOPIC in sync_global_catalog.py, which finds mod repositories by it.
MOD_REPO_TOPIC = "opengoal-mod"


def git(*args: str, cwd: Path = MOTHER_ROOT, check: bool = True) -> str:
    res = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                         encoding="utf-8", errors="replace")
    if check and res.returncode:
        sys.exit(f"git {' '.join(args)} failed:\n{res.stderr.strip()}")
    return res.stdout.strip()


def ref_exists(ref: str) -> bool:
    return subprocess.run(["git", "rev-parse", "--verify", "--quiet", ref],
                          cwd=MOTHER_ROOT, capture_output=True).returncode == 0


def is_ancestor(ancestor: str, ref: str) -> bool:
    return subprocess.run(["git", "merge-base", "--is-ancestor", ancestor, ref],
                          cwd=MOTHER_ROOT, capture_output=True).returncode == 0


def owner() -> str:
    return sync_common.github_owner(MOTHER_ROOT)


def catalog_mods(ref: str) -> dict:
    res = subprocess.run(["git", "show", f"{ref}:index.json"], cwd=MOTHER_ROOT,
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
    try:
        return (json.loads(res.stdout).get("mods") or {}) if res.returncode == 0 else {}
    except ValueError:
        return {}


def title(slug: str) -> str:
    return " ".join(w if any(c.isupper() for c in w) else w.capitalize() for w in re.split(r"[-_]", slug))


def tool_written_name(name: str | None, slug: str) -> bool:
    """True for a display name a script derived from a slug or branch name (e.g.
    `transport-ag/alert`, `killable_yakow`) rather than one a human chose."""
    return not name or name == slug or re.fullmatch(r"[a-z0-9_/.-]+", name) is not None


def released_entry(slug: str) -> dict:
    """The mod's entry in the mother repository's global catalog (empty if unreleased)."""
    try:
        return json.loads((MOTHER_ROOT / "index.json").read_text(encoding="utf-8"))["mods"].get(slug) or {}
    except (OSError, ValueError, KeyError):
        return {}


def short_description(text: str) -> str:
    """GitHub repository descriptions are one line: keep the first sentence, plain text."""
    text = re.sub(r"[`*_]", "", " ".join((text or "").split()))
    first = re.split(r"(?<=\.)\s", text, maxsplit=1)[0]
    return first[:300]


class Mod:
    def __init__(self, game: str, slug: str, start_ref: str, source_branch: str | None):
        self.game, self.slug, self.start_ref, self.source_branch = game, slug, start_ref, source_branch
        self.name = f"{game}-mod-{slug}"
        self.branch = f"mods/{self.name}"
        self.remote = self.name
        self.worktree = WORKTREES / self.name
        self.full_name = f"{owner()}/{self.name}"
        self.url = f"https://github.com/{self.full_name}"
        self.marker = f"chore: create the {slug} mod repository"

    @classmethod
    def from_branch(cls, branch: str) -> "Mod":
        m = re.match(r"^jak([123])/[^/]+/(.+)$", branch)
        if not m:
            sys.exit(f"{branch} is not a mod branch (jak[1-3]/<type>/<slug>)")
        ref = f"origin/{branch}" if ref_exists(f"origin/{branch}") else branch
        if not ref_exists(ref):
            sys.exit(f"branch {branch} not found")
        slug_from_name = m.group(2).replace("/", "-").replace("_", "-")
        mods = catalog_mods(ref)
        slug = next(iter(mods)) if len(mods) == 1 else slug_from_name
        return cls(f"jak{m.group(1)}", slug, ref, branch)

    @classmethod
    def new(cls, spec: str) -> "Mod":
        m = re.match(r"^(jak[123])/([A-Za-z0-9][A-Za-z0-9_-]*)$", spec)
        if not m:
            sys.exit(f"--new expects <game>/<slug>, e.g. jak2/my-mod (got {spec})")
        return cls(m.group(1), m.group(2), "master-dev", None)

    def prepared(self) -> bool:
        return ref_exists(self.branch) and self.marker in git("log", "--format=%s", self.branch)

    def published(self) -> bool:
        return bool(git("config", "--get", f"branch.{self.branch}.remote", check=False))


def run_sync(mod: Mod) -> None:
    """Merge the local master-dev into the worktree's branch under the mod-repository rules."""
    res = subprocess.run([sys.executable, str(SYNC_SCRIPT), "--local-source", "--mod-repo"],
                         cwd=mod.worktree, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res.returncode:
        print(res.stdout[-3000:], res.stderr[-2000:], sep="\n", file=sys.stderr)
        sys.exit(f"Merging master-dev into {mod.branch} needs a manual fix in {mod.worktree}")


def open_worktree(mod: Mod, *add_args: str) -> None:
    # Leftovers of an interrupted run: this script's own temporary worktree.
    if mod.worktree.exists():
        git("worktree", "remove", "--force", str(mod.worktree))
    WORKTREES.mkdir(exist_ok=True)
    git("worktree", "add", "-q", *add_args)


def close_worktree(mod: Mod) -> None:
    # A worktree holding a submodule (.agents/skills) can only be removed with --force;
    # everything in it is committed by then.
    git("worktree", "remove", "--force", str(mod.worktree))


def prepare(mod: Mod, description: str, youtube: str, redo: bool = False) -> None:
    if redo and ref_exists(mod.branch):
        if mod.published():
            sys.exit(f"--redo refused: {mod.branch} is already published to {mod.url}")
        git("branch", "-D", mod.branch)  # this script's own build, never published
    if mod.prepared():
        if is_ancestor("master-dev", mod.branch):
            print(f"[skip] {mod.branch} is prepared and up to date with master-dev")
            return
        print(f"Updating {mod.branch} with master-dev ...")
        open_worktree(mod, str(mod.worktree), mod.branch)
        run_sync(mod)
        close_worktree(mod)
        print(f"[OK] updated {mod.branch}")
        return

    print(f"Preparing {mod.branch} from {mod.start_ref} in {mod.worktree} ...")
    open_worktree(mod, "-B", mod.branch, str(mod.worktree), mod.start_ref)
    if mod.source_branch:
        run_sync(mod)
        adjust_migrated(mod)
        body = (f"Moved from the {mod.source_branch} branch of {owner()}/jak-project, "
                "merged with master-dev under the mod-repository rules.")
    else:
        adjust_new(mod, description, youtube)
        body = f"Created from {owner()}/jak-project master-dev."

    git("add", "-A", cwd=mod.worktree)
    git("commit", "-q", "-m", f"{mod.marker} (AI-assisted)", "-m", body,
        "-m", "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>", cwd=mod.worktree)
    close_worktree(mod)
    print(f"[OK] prepared {mod.branch}")


def adjust_migrated(mod: Mod) -> None:
    root = mod.worktree
    readme = root / "README.md"
    lines = readme.read_text(encoding="utf-8").splitlines(keepends=True)
    lines = [l for l in lines if "img.shields.io/badge/Branch-" not in l]
    note = (f"> [!NOTE]\n> This mod moved from the `{mod.source_branch}` branch of "
            f"[{owner()}/jak-project](https://github.com/{owner()}/jak-project) to this repository. "
            "Earlier releases stay installable from the launcher catalog.\n\n")
    first_section = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    lines.insert(first_section, note)
    readme.write_text("".join(lines), encoding="utf-8")

    # docs/modding/ outside current_mod/ is shared documentation: a mod repository mirrors
    # master-dev's, so a file only the mod branch carries is a stale copy.
    shared = set(git("ls-tree", "-r", "--name-only", "master-dev", "--", "docs/modding").splitlines())
    for path in git("ls-files", "--", "docs/modding", cwd=root).splitlines():
        if not path.startswith("docs/modding/current_mod/") and path not in shared:
            git("rm", "-q", "--", path, cwd=root)

    index = root / "index.json"
    catalog = json.loads(index.read_text(encoding="utf-8"))
    entry = catalog["mods"].get(mod.slug) or {}
    # One repository, one mod: drop stale keys so the repository names exactly one mod.
    catalog["mods"] = {mod.slug: entry}
    # Older branch syncs overwrote the name with the slug or branch name: prefer the name players
    # see in the published catalog, then a title made from the slug.
    released = released_entry(mod.slug).get("displayName")
    if not tool_written_name(released, mod.slug):
        entry["displayName"] = released
    elif tool_written_name(entry.get("displayName"), mod.slug):
        entry["displayName"] = title(mod.slug)
    entry["websiteUrl"] = mod.url
    catalog["sourceName"] = sanitize_source_name(entry["displayName"])
    index.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def adjust_new(mod: Mod, description: str, youtube: str) -> None:
    root = mod.worktree
    # The mother's global catalog and mother-only files do not belong in a mod repository;
    # the mod's own index.json is created by its first release.
    git("rm", "-q", "--ignore-unmatch", "index.json", *sync_common.MASTER_DEV_ONLY_PATHS, cwd=root)
    for wf in sync_common.stray_workflow_files(str(root), sync_common.ALLOWED_MOD_REPO_WORKFLOWS):
        git("rm", "-q", wf, cwd=root)

    youtube_id = ""
    if youtube:
        m = re.search(r"(?:youtu\.be/|v=)([A-Za-z0-9_-]{6,})", youtube)
        youtube_id = m.group(1) if m else ""
    label = GAME_LABELS[mod.game]
    values = {
        "{MOD_TITLE}": title(mod.slug),
        "{TARGET_GAME}": label,
        "{GAME_BADGE}": label.replace(" ", "%20"),
        "{REPO_PATH}": mod.full_name,
        "{BASE_REPO_PATH}": f"{owner()}/{sync_common.MOTHER_NAME}",
        "{REPO_NAME}": mod.name,
        "{TASK_SET_GAME}": f"task set-game-{mod.game}",
        "{GAME_DIR}": mod.game,
        "{MOD_SLUG}": mod.slug,
        "{MOD_DESCRIPTION}": description or "Brief, simple description of what this mod introduces or modifies in the game.",
        "{YOUTUBE_ID}": youtube_id or "{YOUTUBE_ID}",
    }
    text = TEMPLATE.read_text(encoding="utf-8")
    for key, value in values.items():
        text = text.replace(key, value)
    (root / "README.md").write_text(text, encoding="utf-8")


def publish(mod: Mod, description: str, private: bool = False) -> None:
    gh = shutil.which("gh")
    if not gh:
        sys.exit("gh not found: install it (scoop install gh) and run gh auth login")
    if subprocess.run([gh, "repo", "view", mod.full_name], capture_output=True).returncode != 0:
        if not description:
            description = short_description(released_entry(mod.slug).get("description", "")) or \
                f"OpenGOAL {GAME_LABELS[mod.game]} mod: {title(mod.slug)}."
        visibility = "--private" if private else "--public"
        subprocess.run([gh, "repo", "create", mod.full_name, visibility, "--description", description],
                       check=True)
    subprocess.run([gh, "repo", "edit", mod.full_name, "--homepage", mod.url,
                    "--add-topic", MOD_REPO_TOPIC, "--add-topic", "opengoal", "--add-topic", mod.game],
                   check=True)

    # In this clone the repository is a remote named after it, and mods/<name> tracks and
    # pushes to its main branch: `git push` and `task modding-switch` work like on a branch.
    if not git("remote", "get-url", mod.remote, check=False):
        git("remote", "add", mod.remote, f"{mod.url}.git")
    subprocess.run(["git", "push", mod.remote, f"{mod.branch}:main"], cwd=MOTHER_ROOT, check=True)
    git("fetch", "-q", mod.remote)
    git("branch", f"--set-upstream-to={mod.remote}/main", mod.branch)
    git("config", f"remote.{mod.remote}.push", f"refs/heads/{mod.branch}:refs/heads/main")
    print(f"[OK] published {mod.url} (switch to it with: task modding-switch -- {mod.name})")


def ask(prompt: str, default: str = "", pattern: str = "", hint: str = "") -> str:
    while True:
        answer = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip() or default
        if not pattern or re.fullmatch(pattern, answer):
            return answer
        print(f"  {hint}")


def ask_new_mod(args: argparse.Namespace) -> None:
    """Interactive creation, used when the task is run without arguments."""
    if not shutil.which("gh"):
        sys.exit("gh not found: install it (scoop install gh) and run gh auth login")
    print("New mod repository, created from master-dev.\n")
    game = ask("Game (jak1, jak2, jak3)", "jak2", r"jak[123]", "Answer jak1, jak2 or jak3.")
    slug = ask(f"Mod name, letters, digits, - or _ (the repository becomes {game}-mod-<name>)", "",
               r"[A-Za-z0-9][A-Za-z0-9_-]*", "Use letters, digits, - and _, starting with a letter or digit.")
    # The repository name carries the "mod-" part itself: "mod-foo" means "foo".
    if slug.lower().startswith("mod-"):
        slug = slug[len("mod-"):]
    name = f"{owner()}/{game}-mod-{slug}"
    if subprocess.run(["gh", "repo", "view", name], capture_output=True).returncode == 0:
        sys.exit(f"{name} already exists: switch to it with task modding-switch -- {game}-mod-{slug}")
    args.description = ask("One sentence for players (README overview and repository description)")
    args.youtube = ask("Demo video URL (optional)")
    visibility = ask("Visibility (public, private)", "public", r"public|private", "Answer public or private.")
    args.private = visibility == "private"
    args.new = f"{game}/{slug}"
    print(f"\nRepository  : {name} ({visibility})"
          f"\nLocal branch: mods/{game}-mod-{slug}"
          f"\nCatalog key : {slug}")
    if args.private:
        print("Private: players cannot install it from the launcher until you make it public.")
    if ask("Create it? (y, n)", "y", r"[yYnN]", "Answer y or n.").lower() != "y":
        sys.exit("Cancelled.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--from-branch", nargs="+", metavar="BRANCH",
                        help="move existing mod branches (jak[1-3]/<type>/<slug>) to their own repositories")
    source.add_argument("--new", metavar="GAME/SLUG", help="start a new mod, e.g. jak2/my-mod")
    parser.add_argument("--description", default="", help="one-line description (new mod, or repository description)")
    parser.add_argument("--youtube", default="", help="demo video URL (new mod)")
    parser.add_argument("--private", action="store_true",
                        help="create private repositories (kept out of the launcher catalog until made public)")
    parser.add_argument("--prepare-only", action="store_true", help="build the local branches, publish nothing")
    parser.add_argument("--redo", action="store_true",
                        help="rebuild prepared branches that were never published")
    args = parser.parse_args()

    if git("status", "--porcelain", "--ignore-submodules=all"):
        sys.exit("Commit or stash your changes first: the mod repositories are built from master-dev.")
    if not args.from_branch and not args.new:
        if not sys.stdin.isatty():
            sys.exit("Give --new <game>/<slug> or --from-branch <branch> (no terminal to ask in).")
        ask_new_mod(args)

    mods = [Mod.from_branch(b) for b in args.from_branch] if args.from_branch else [Mod.new(args.new)]
    for mod in mods:
        print(f"\n=== {mod.full_name} (catalog key {mod.slug}) ===")
        prepare(mod, args.description, args.youtube, args.redo)
        if not args.prepare_only:
            publish(mod, args.description, args.private)
    if args.prepare_only:
        print("\nPrepared only. Publish with the same command without --prepare-only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
