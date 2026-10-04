#!/usr/bin/env python3
"""
Builds the global catalog (index.json) at the root of master-dev from the mod repositories.
Compliant with OpenGOAL Launcher Mod Source Schema v1:
https://github.com/open-goal/launcher/tree/main/schemas/mod-source/v1

This enables players to add a SINGLE catalog URL in the OpenGOAL Launcher:
    https://raw.githubusercontent.com/<user>/<repo>/master-dev/index.json
to see and install ALL published mods.

Sources: the public repositories of the same owner that carry the opengoal-mod topic (one GitHub
repository per mod), and in each one only its most advanced release, the one with the highest
version in its tag. That release's index.json asset is the mod's catalog: release.yml writes it
with the mod's whole version history. Branches, the repositories' index.json files and the
releases of this repository are never read.

Usage:
    python scripts/modding/sync_global_catalog.py
    python scripts/modding/sync_global_catalog.py --repo <owner>/jak-project
    python scripts/modding/sync_global_catalog.py --dry-run
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


def fetch_paged(url: str, token: str) -> list:
  """Every item of a paginated GitHub API list. Raises when GitHub cannot be asked: a catalog
  built from a partial answer would drop mods until the next run."""
  items = []
  page = 1
  while True:
    batch = fetch_json(f"{url}{'&' if '?' in url else '?'}per_page=100&page={page}", token)
    if not batch:
      break
    items.extend(batch)
    if len(batch) < 100:
      break
    page += 1
  return items


# Topic that marks a mod repository (one GitHub repository per mod, created from master-dev
# by scripts/modding/create_mod_repo.py). Only these repositories feed the catalog.
MOD_REPO_TOPIC = "opengoal-mod"


def discover_mod_repos(owner: str, token: str) -> list[dict]:
  """The owner's public repositories with the opengoal-mod topic, sorted by name. A private
  repository is left out: players cannot download its releases."""
  repos = fetch_paged(f"https://api.github.com/users/{owner}/repos", token)
  return sorted(
      (r for r in repos if MOD_REPO_TOPIC in (r.get("topics") or []) and not r.get("private")),
      key=lambda r: r["full_name"].lower(),
  )


# Version at the end of a release tag: `<slug>-v1.2.3`, optionally `-rc1`.
TAG_VERSION_RE = re.compile(r"v(\d+(?:\.\d+)*)(?:-([0-9A-Za-z.]+))?$")


def release_rank(rel: dict) -> tuple:
  """Sort key of a release by the version in its tag, highest is the most advanced. As in
  semver, a pre-release suffix ranks below the same plain version (1.1.0-rc1 < 1.1.0); the
  publication date breaks ties, and ranks a tag without a version below every versioned one."""
  m = TAG_VERSION_RE.search(rel.get("tag_name") or "")
  numbers = tuple(int(n) for n in m.group(1).split(".")) if m else ()
  numbers += (0,) * (3 - len(numbers)) if m else ()
  is_final = 1 if m and not m.group(2) else 0
  return (numbers, is_final, (m.group(2) or "") if m else "", rel.get("published_at") or "")


def load_catalog_from_release_asset(rel: dict, token: str) -> dict | None:
  """The index.json attached to a release, or None when the release has none. Raises when the
  asset exists but cannot be downloaded."""
  for asset in rel.get("assets", []):
    if asset.get("name") == "index.json" and asset.get("browser_download_url"):
      return fetch_json(asset["browser_download_url"], token)
  return None


def latest_release_catalog(full_name: str, token: str) -> tuple[dict, dict] | None:
  """(release, catalog) of the most advanced published release of a mod repository that carries
  an index.json, or None when it has no such release. Drafts are skipped; a pre-release counts,
  ranked by its version like any other release."""
  releases = [r for r in fetch_paged(f"https://api.github.com/repos/{full_name}/releases", token)
              if not r.get("draft")]
  for rel in sorted(releases, key=release_rank, reverse=True):
    catalog = load_catalog_from_release_asset(rel, token)
    if catalog is not None:
      return rel, catalog
    print(f"  Warning: {rel.get('tag_name')} has no index.json asset, trying the next release",
          file=sys.stderr)
  return None


def merge_list(target: dict, key: str, values) -> None:
  """Appends to target[key] the values it does not hold yet, keeping their order."""
  existing = target.setdefault(key, [])
  for v in values or []:
    if v not in existing:
      existing.append(v)


def collect_mods_from_mod_repos(owner: str, token: str):
  """The mods and texture packs of every mod repository's most advanced release."""
  print(f"Looking for {owner}'s public repositories with the {MOD_REPO_TOPIC} topic...")
  mod_repos = discover_mod_repos(owner, token)
  print(f"Found {len(mod_repos)} mod repositor{'y' if len(mod_repos) == 1 else 'ies'}.")

  published = []
  for mod_repo in mod_repos:
    found = latest_release_catalog(mod_repo["full_name"], token)
    if not found:
      print(f"  - {mod_repo['full_name']}: no release with an index.json, not listed")
      continue
    rel, catalog = found
    mods = catalog.get("mods") if isinstance(catalog.get("mods"), dict) else {}
    if len(mods) != 1:
      # A mod repository's catalog names its mod alone (update_mod_catalog.mod_identity).
      print(f"  - {mod_repo['full_name']}: {rel.get('tag_name')} lists {len(mods)} mods instead of 1, "
            "not listed", file=sys.stderr)
      continue
    published.append((mod_repo, rel, catalog))

  aggregated_mods = {}
  aggregated_texture_packs = {}

  # Oldest release first: on a clash (the same mod key in two repositories, the same texture
  # pack version shipped by two mods) the most recently published one wins.
  for mod_repo, rel, catalog in sorted(published, key=lambda p: p[1].get("published_at") or ""):
    tag = rel.get("tag_name", "")
    mod_key, mod_info = next(iter(catalog["mods"].items()))
    mod_info = json.loads(json.dumps(mod_info))
    # Players are sent to the mod's repository.
    mod_info["websiteUrl"] = mod_repo["html_url"]
    if mod_key in aggregated_mods:
      print(f"  Warning: mod '{mod_key}' is published by several repositories; "
            f"keeping {mod_repo['full_name']}", file=sys.stderr)
    aggregated_mods[mod_key] = mod_info

    # Texture packs: only those whose archive is attached to this release.
    rel_asset_names = {a.get("name") for a in rel.get("assets", [])}
    texture_packs = catalog.get("texturePacks") if isinstance(catalog.get("texturePacks"), dict) else {}
    for tp_key, tp_info in texture_packs.items():
      versions = [
          v for v in tp_info.get("versions", [])
          if any(url and url.split("/")[-1] in rel_asset_names for url in (v.get("assets") or {}).values())
      ]
      if not versions:
        continue
      tp_info = json.loads(json.dumps(tp_info))
      # The mod key in the tags ties the pack to every mod that ships it.
      merge_list(tp_info, "tags", [mod_key])
      tp_info["websiteUrl"] = mod_repo["html_url"]

      if tp_key not in aggregated_texture_packs:
        aggregated_texture_packs[tp_key] = {**tp_info, "versions": versions}
        continue
      target = aggregated_texture_packs[tp_key]
      for key in ("tags", "supportedGames", "authors"):
        merge_list(target, key, tp_info.get(key))
      for attr in ("displayName", "description", "coverArtUrl", "thumbnailArtUrl", "websiteUrl"):
        if tp_info.get(attr):
          target[attr] = tp_info[attr]
      # One entry per version number.
      new_numbers = {v.get("version") for v in versions}
      target["versions"] = [v for v in target.get("versions", []) if v.get("version") not in new_numbers] + versions

    print(f"  ✓ {mod_repo['full_name']}: {tag}")

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
      description="Generate or sync the master-dev global index.json catalog for OpenGOAL Launcher "
                  "from the most advanced release of each mod repository."
  )
  parser.add_argument(
      "--repo",
      default=get_default_repo(),
      help="GitHub repository in 'owner/repo' format, whose owner holds the mod repositories "
           "(default: auto-detect)",
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
      "--dry-run",
      action="store_true",
      help="Print summary without modifying index.json file",
  )

  args = parser.parse_args()
  if not args.repo:
    raise SystemExit("Cannot tell the GitHub repository: pass --repo <owner>/jak-project.")
  owner = args.repo.split("/")[0]
  if not args.source_name:
    args.source_name = f"{owner.capitalize()} OpenGOAL Mods Hub"
  token = get_token()

  try:
    mods, texture_packs = collect_mods_from_mod_repos(owner, token)
  except (urllib.error.URLError, OSError, ValueError) as err:
    raise SystemExit(f"GitHub could not be asked ({err}): index.json left unchanged.")

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
