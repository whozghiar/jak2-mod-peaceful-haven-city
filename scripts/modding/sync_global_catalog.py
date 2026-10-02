#!/usr/bin/env python3
"""
Aggregates all published mod releases into a unified global catalog (index.json)
at the repository root on master-dev.
Compliant with OpenGOAL Launcher Mod Source Schema v1:
https://github.com/open-goal/launcher/tree/main/schemas/mod-source/v1

This enables players to add a SINGLE catalog URL in the OpenGOAL Launcher:
    https://raw.githubusercontent.com/<user>/<repo>/master-dev/index.json
to see and install ALL published mods from this repository.

Usage:
    python scripts/modding/sync_global_catalog.py
    python scripts/modding/sync_global_catalog.py --repo <owner>/jak-project
    python scripts/modding/sync_global_catalog.py --offline
"""

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import urllib.error
import urllib.request

if hasattr(sys.stdout, "reconfigure"):
  sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
  sys.stderr.reconfigure(encoding="utf-8", errors="replace")

REPO_ROOT = Path(__file__).resolve().parents[2]
BRANCH_RE = re.compile(r"raw\.githubusercontent\.com/[^/\s]+/[^/\s]+/(jak([123])/.+?)/docs/")


def run_cmd(cmd: str) -> str:
  try:
    res = subprocess.run(
        cmd,
        shell=True,
        text=True,
        capture_output=True,
        cwd=REPO_ROOT,
        check=False,
    )
    return res.stdout.strip()
  except Exception:
    return ""


def get_default_repo() -> str:
  url = run_cmd("git config --get remote.origin.url")
  match = re.search(r"github\.com[:/]([^/]+/[^/.]+?)(?:\.git)?$", url)
  if match:
    return match.group(1)
  return os.environ.get("GITHUB_REPOSITORY", "")


def get_token() -> str:
  return (os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or "").strip()


def fetch_json(url: str, token: str):
  req = urllib.request.Request(
      url,
      headers={
          "Accept": "application/vnd.github+json",
          "User-Agent": "OpenGOAL-GlobalCatalogSync",
          **({"Authorization": f"Bearer {token}"} if token else {}),
      },
  )
  with urllib.request.urlopen(req, timeout=20) as resp:
    return json.loads(resp.read().decode("utf-8"))


def fetch_all_releases(repo: str, token: str):
  """All releases of repo, or None when GitHub could not be asked."""
  releases = []
  page = 1
  while True:
    url = f"https://api.github.com/repos/{repo}/releases?per_page=100&page={page}"
    try:
      batch = fetch_json(url, token)
    except urllib.error.HTTPError as err:
      print(f"Warning: HTTP {err.code} fetching releases (page {page}): {err}", file=sys.stderr)
      return None if page == 1 else releases
    except Exception as err:
      print(f"Warning: Failed to fetch releases: {err}", file=sys.stderr)
      return None if page == 1 else releases
    if not batch:
      break
    releases.extend(batch)
    if len(batch) < 100:
      break
    page += 1
  return releases


# Topic that marks a mod repository (one GitHub repository per mod, created from master-dev
# by scripts/modding/create_mod_repo.py). Its releases join the catalog next to this repository's.
MOD_REPO_TOPIC = "opengoal-mod"


def discover_mod_repos(owner: str, token: str) -> list[dict]:
  repos = []
  page = 1
  while True:
    try:
      batch = fetch_json(f"https://api.github.com/users/{owner}/repos?per_page=100&page={page}", token)
    except Exception as err:
      print(f"Warning: could not list {owner}'s repositories: {err}", file=sys.stderr)
      break
    if not batch:
      break
    repos.extend(r for r in batch if MOD_REPO_TOPIC in (r.get("topics") or []))
    if len(batch) < 100:
      break
    page += 1
  return repos


def mod_repo_entry(full_name: str, token: str) -> tuple[str | None, dict]:
  """The catalog key a mod repository publishes and its entry: the single mod of its own
  index.json, or just the `<slug>` of its `<game>-mod-<slug>` name when it has none yet."""
  try:
    mods = fetch_json(f"https://raw.githubusercontent.com/{full_name}/HEAD/index.json", token).get("mods") or {}
  except Exception:
    mods = {}
  if len(mods) == 1:
    return next(iter(mods.items()))
  m = re.match(r"^jak[123]-(?:mod-)?(.+)$", full_name.split("/")[-1])
  return (m.group(1) if m else None), {}


def get_git_remote_branches() -> list[str]:
  """List known remote branches for origin/jak*."""
  out = run_cmd("git branch -r")
  branches = []
  for b in out.splitlines():
    b = b.strip()
    if "origin/jak" in b and "HEAD" not in b:
      branches.append(b.replace("origin/", ""))
  return branches


def find_branch_for_slug(slug: str, remote_branches: list[str]) -> str | None:
  """Resolve the git branch associated with a mod slug."""
  clean_slug = slug.lower().replace("_", "-")
  # 1. Exact match on final path segment
  for b in remote_branches:
    last_seg = b.split("/")[-1].lower().replace("_", "-")
    if last_seg == clean_slug:
      return b

  # 2. Match on multi-segment suffix (e.g. transport-ag/alert -> transport-ag-alert)
  for b in remote_branches:
    parts = b.split("/")
    if len(parts) >= 3:
      var_part = "-".join(parts[2:]).lower().replace("_", "-")
      if var_part == clean_slug:
        return b

  # 3. Partial match
  for b in remote_branches:
    clean_b = b.lower().replace("_", "-")
    if clean_slug in clean_b or clean_b.split("/")[-1] in clean_slug:
      return b

  return None


def load_catalog_from_branch(branch: str) -> dict | None:
  """Load index.json from a git branch (origin/branch or local branch)."""
  if not branch:
    return None
  out = run_cmd(f"git show origin/{branch}:index.json")
  if not out.strip():
    out = run_cmd(f"git show {branch}:index.json")
  if out.strip():
    try:
      return json.loads(out)
    except Exception:
      pass
  return None


def load_catalog_from_release_asset(rel, token: str) -> dict | None:
  """Attempts to load index.json attached as an asset of the release."""
  for asset in rel.get("assets", []):
    if asset.get("name") == "index.json":
      url = asset.get("browser_download_url")
      if url:
        try:
          return fetch_json(url, token)
        except Exception as e:
          print(f"  Warning: failed to download index.json asset from {rel.get('tag_name')}: {e}", file=sys.stderr)
  return None


def get_offline_released_mods(remote_branches: list[str], repo: str):
  """Identify released mods strictly using git release tags (never arbitrary branches)."""
  print("Resolving published releases from git release tags (offline mode)...")
  res = subprocess.run(["git", "tag", "-l", "*-v*"], capture_output=True, text=True, cwd=REPO_ROOT)
  tags = [t.strip() for t in res.stdout.splitlines() if t.strip() and not t.startswith("v0.")]

  # Group by mod branch
  found_branches = {}
  for t in tags:
    m = re.match(r"^([a-zA-Z0-9_\-]+?)-v(\d+.*)$", t)
    if m:
      slug = m.group(1).replace("_", "-")
      branch = find_branch_for_slug(slug, remote_branches)
      if branch:
        found_branches.setdefault(branch, []).append(t)

  synthetic_releases = []
  for branch, tag_list in sorted(found_branches.items()):
    parts = branch.split("/")
    slug = "-".join(parts[2:]).replace("_", "-") if len(parts) >= 3 else parts[-1].replace("_", "-")
    sorted_tags = sorted(tag_list, reverse=True)
    latest_tag = sorted_tags[0]
    synthetic_releases.append({
        "tag_name": latest_tag,
        "name": latest_tag,
        "body": f"https://raw.githubusercontent.com/{repo}/{branch}/docs/img/mod/mod_cover.png",
        "published_at": datetime.now(timezone.utc).isoformat(),
        "assets": [],
        "inferred_branch": branch,
        "inferred_slug": slug,
    })

  return synthetic_releases


def collect_mods_from_releases(repo: str, token: str, offline: bool = False):
  """Collects published mods strictly by inspecting GitHub Releases and their catalogs."""
  remote_branches = get_git_remote_branches()
  releases = None

  if not offline:
    print(f"Fetching published releases for {repo}...")
    try:
      releases = fetch_all_releases(repo, token)
    except Exception as e:
      print(f"Warning: GitHub API call failed: {e}", file=sys.stderr)
      releases = None

  if releases is None:
    releases = get_offline_released_mods(remote_branches, repo)

  mod_repos = [] if offline else discover_mod_repos(repo.split("/")[0], token)
  for mod_repo in mod_repos:
    print(f"Fetching published releases for mod repository {mod_repo['full_name']}...")
    for rel in fetch_all_releases(mod_repo["full_name"], token) or []:
      rel["_repo"] = mod_repo["full_name"]
      releases.append(rel)

  print(f"Found {len(releases)} published release(s). Aggregating catalogs...")

  aggregated_mods = {}
  aggregated_texture_packs = {}

  for rel in sorted(releases, key=lambda r: r.get("published_at") or ""):
    if rel.get("draft"):
      continue

    tag = rel.get("tag_name", "")
    body = rel.get("body") or ""

    # Resolve branch and canonical slug
    branch_match = BRANCH_RE.search(body)
    branch = None
    if branch_match:
      branch = branch_match.group(1)
    elif "inferred_branch" in rel:
      branch = rel["inferred_branch"]

    canonical_slug = None
    if branch:
      m = re.match(r"^jak[123]/(?:features|config)/(.+)$", branch)
      if m:
        canonical_slug = m.group(1).replace("/", "-").replace("_", "-")
      else:
        canonical_slug = branch.split("/")[-1].replace("_", "-")
    elif "inferred_slug" in rel:
      canonical_slug = rel["inferred_slug"]
      branch = find_branch_for_slug(canonical_slug, remote_branches)
    else:
      m_tag = re.match(r"^([a-zA-Z0-9_\-]+?)-v\d+", tag)
      if m_tag:
        canonical_slug = m_tag.group(1).replace("_", "-")
        # A mod repository's release carries its own catalog; its old branch here is history.
        branch = None if "_repo" in rel else find_branch_for_slug(canonical_slug, remote_branches)

    # 1. Load data from release asset (if available)
    rel_catalog = load_catalog_from_release_asset(rel, token)

    # 2. Load data from mod branch (if available in git)
    branch_catalog = load_catalog_from_branch(branch) if branch else None

    # Available asset names on the release
    rel_asset_names = {a.get("name") for a in rel.get("assets", [])}

    if not rel_catalog and not branch_catalog:
      print(f"  - {tag}: no catalog found (neither in release asset nor branch), skipping")
      continue

    # Merge mods
    source_mod_data = {}
    if rel_catalog and "mods" in rel_catalog and isinstance(rel_catalog["mods"], dict):
      source_mod_data.update(rel_catalog["mods"])
    if branch_catalog and "mods" in branch_catalog and isinstance(branch_catalog["mods"], dict):
      for m_k, m_v in branch_catalog["mods"].items():
        if m_k not in source_mod_data:
          source_mod_data[m_k] = m_v
        else:
          # Merge versions
          existing_versions = {v.get("version"): v for v in source_mod_data[m_k].get("versions", [])}
          for v in m_v.get("versions", []):
            ver_num = v.get("version")
            if ver_num and ver_num not in existing_versions:
              source_mod_data[m_k].setdefault("versions", []).append(v)

    for mod_key, mod_info in source_mod_data.items():
      target_key = canonical_slug or mod_key
      if target_key not in aggregated_mods:
        aggregated_mods[target_key] = json.loads(json.dumps(mod_info))
      else:
        existing_versions = {v.get("version"): v for v in aggregated_mods[target_key].get("versions", [])}
        for v in mod_info.get("versions", []):
          ver_num = v.get("version")
          if ver_num and ver_num not in existing_versions:
            aggregated_mods[target_key].setdefault("versions", []).append(v)
        for t in mod_info.get("tags", []):
          if t not in aggregated_mods[target_key].setdefault("tags", []):
            aggregated_mods[target_key]["tags"].append(t)
        for g in mod_info.get("supportedGames", []):
          if g not in aggregated_mods[target_key].setdefault("supportedGames", []):
            aggregated_mods[target_key]["supportedGames"].append(g)
        for a in mod_info.get("authors", []):
          if a not in aggregated_mods[target_key].setdefault("authors", []):
            aggregated_mods[target_key]["authors"].append(a)
        for attr in ["displayName", "description", "coverArtUrl", "thumbnailArtUrl", "websiteUrl"]:
          if mod_info.get(attr):
            aggregated_mods[target_key][attr] = mod_info[attr]

    # Merge texture packs
    # Priority order: branch catalog has the up-to-date texture pack registered by package_texture_pack.py!
    source_tp_data = {}
    if branch_catalog and "texturePacks" in branch_catalog and isinstance(branch_catalog["texturePacks"], dict):
      source_tp_data.update(branch_catalog["texturePacks"])

    if rel_catalog and "texturePacks" in rel_catalog and isinstance(rel_catalog["texturePacks"], dict):
      for tp_k, tp_v in rel_catalog["texturePacks"].items():
        # Check if asset actually exists in release
        has_valid_asset = False
        for v in tp_v.get("versions", []):
          assets = v.get("assets", {})
          for url in assets.values():
            if url:
              zip_fname = url.split("/")[-1]
              if not rel_asset_names or zip_fname in rel_asset_names:
                has_valid_asset = True
                break
        if has_valid_asset:
          if tp_k not in source_tp_data:
            source_tp_data[tp_k] = tp_v

    for tp_key, tp_info in source_tp_data.items():
      # Ensure releasing mod slug is included in tags for clean affiliation
      if canonical_slug:
        tags = tp_info.setdefault("tags", [])
        if canonical_slug not in tags:
          tags.append(canonical_slug)
        if branch and not tp_info.get("websiteUrl"):
          tp_info["websiteUrl"] = f"https://github.com/{repo}/tree/{branch}"

      if tp_key not in aggregated_texture_packs:
        aggregated_texture_packs[tp_key] = json.loads(json.dumps(tp_info))
      else:
        # Merge tags so all declaring mod affiliations are preserved
        for t in tp_info.get("tags", []):
          if t not in aggregated_texture_packs[tp_key].setdefault("tags", []):
            aggregated_texture_packs[tp_key]["tags"].append(t)

        # Merge supported games
        for g in tp_info.get("supportedGames", []):
          if g not in aggregated_texture_packs[tp_key].setdefault("supportedGames", []):
            aggregated_texture_packs[tp_key]["supportedGames"].append(g)

        # Merge authors
        for a in tp_info.get("authors", []):
          if a not in aggregated_texture_packs[tp_key].setdefault("authors", []):
            aggregated_texture_packs[tp_key]["authors"].append(a)

        # Merge versions by comparing asset URLs to support releases from multiple mods
        existing_versions = aggregated_texture_packs[tp_key].setdefault("versions", [])
        existing_asset_urls = {
            url
            for ev in existing_versions
            for url in (ev.get("assets") or {}).values()
            if url
        }
        for v in tp_info.get("versions", []):
          v_urls = [u for u in (v.get("assets") or {}).values() if u]
          if not any(u in existing_asset_urls for u in v_urls):
            existing_versions.append(v)
            existing_asset_urls.update(v_urls)

        for attr in ["displayName", "description", "coverArtUrl", "thumbnailArtUrl", "websiteUrl"]:
          if tp_info.get(attr):
            aggregated_texture_packs[tp_key][attr] = tp_info[attr]

    print(f"  ✓ {tag}: aggregated successfully")

  # A mod repository's own index.json is the source of truth for its name and description,
  # and players are sent to the repository, even before its first release from there.
  for mod_repo in mod_repos:
    slug, entry = mod_repo_entry(mod_repo["full_name"], token)
    if slug in aggregated_mods:
      for attr in ("displayName", "description"):
        if entry.get(attr):
          aggregated_mods[slug][attr] = entry[attr]
      aggregated_mods[slug]["websiteUrl"] = mod_repo["html_url"]

  return aggregated_mods, aggregated_texture_packs


def generate_global_catalog(mods, texture_packs, source_name: str):
  """Builds the final OpenGOAL Launcher Mod Source Schema v1 document."""
  now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

  # Sort mods alphabetically by displayName
  sorted_mods = {}
  for k in sorted(mods.keys(), key=lambda x: (mods[x].get("displayName") or x).lower()):
    mod_info = dict(mods[k])
    # Sort versions newest to oldest
    if "versions" in mod_info and isinstance(mod_info["versions"], list):
      mod_info["versions"] = sorted(
          mod_info["versions"],
          key=lambda v: v.get("publishedDate") or "",
          reverse=True,
      )
    sorted_mods[k] = mod_info

  # Sort texture packs alphabetically
  sorted_tps = {}
  for k in sorted(texture_packs.keys(), key=lambda x: (texture_packs[x].get("displayName") or x).lower()):
    tp_info = dict(texture_packs[k])
    if "versions" in tp_info and isinstance(tp_info["versions"], list):
      tp_info["versions"] = sorted(
          tp_info["versions"],
          key=lambda v: v.get("publishedDate") or "",
          reverse=True,
      )
    sorted_tps[k] = tp_info

  return {
      "schemaVersion": "1.0.0",
      "sourceName": source_name,
      "lastUpdated": now_iso,
      "mods": sorted_mods,
      "texturePacks": sorted_tps,
  }


def main():
  parser = argparse.ArgumentParser(
      description="Generate or sync the master-dev global index.json catalog for OpenGOAL Launcher."
  )
  parser.add_argument(
      "--repo",
      default=get_default_repo(),
      help="GitHub repository in 'owner/repo' format (default: auto-detect)",
  )
  parser.add_argument(
      "--output",
      type=Path,
      default=REPO_ROOT / "index.json",
      help="Path to write index.json (default: <repo_root>/index.json)",
  )
  parser.add_argument(
      "--source-name",
      help="Display sourceName in Launcher (default: '<Owner> OpenGOAL Mods Hub')",
  )
  parser.add_argument(
      "--offline",
      action="store_true",
      help="Force collecting strictly from git release tags without GitHub API calls",
  )
  parser.add_argument(
      "--dry-run",
      action="store_true",
      help="Print summary without modifying index.json file",
  )

  args = parser.parse_args()
  if not args.repo:
    raise SystemExit("Cannot tell the GitHub repository: pass --repo <owner>/jak-project.")
  if not args.source_name:
    args.source_name = f"{args.repo.split('/')[0].capitalize()} OpenGOAL Mods Hub"
  token = get_token()

  mods, texture_packs = collect_mods_from_releases(args.repo, token, offline=args.offline)

  print(f"\nTotal distinct published mods found: {len(mods)}")
  for k, v in mods.items():
    v_count = len(v.get("versions", []))
    name = v.get("displayName", k)
    game = (v.get("supportedGames") or ["?"])[0]
    print(f"  • [{game}] {name} ({k}) — {v_count} version(s)")

  if texture_packs:
    print(f"\nTotal distinct published texture packs found: {len(texture_packs)}")
    for k, v in texture_packs.items():
      v_count = len(v.get("versions", []))
      name = v.get("displayName", k)
      game = (v.get("supportedGames") or ["?"])[0]
      tags = v.get("tags", [])
      print(f"  • [{game}] {name} ({k}) — {v_count} version(s) [tags: {', '.join(tags)}]")

  catalog = generate_global_catalog(mods, texture_packs, args.source_name)
  # Nothing new since the last run: keep its timestamp, so the file stays as it is and the daily
  # workflow commits nothing.
  try:
    previous = json.loads(Path(args.output).read_text(encoding="utf-8"))
    if ({k: v for k, v in previous.items() if k != "lastUpdated"}
        == {k: v for k, v in catalog.items() if k != "lastUpdated"}):
      catalog["lastUpdated"] = previous.get("lastUpdated", catalog["lastUpdated"])
  except (OSError, ValueError):
    pass
  catalog_json = json.dumps(catalog, indent=2, ensure_ascii=False) + "\n"

  if args.dry_run:
    print("\n[Dry Run] Generated index.json preview:")
    print(catalog_json[:600] + "...\n")
    return

  args.output.parent.mkdir(parents=True, exist_ok=True)
  with open(args.output, "w", encoding="utf-8") as f:
    f.write(catalog_json)

  print(f"\n[OK] Successfully wrote global catalog to {args.output}")


if __name__ == "__main__":
  main()
