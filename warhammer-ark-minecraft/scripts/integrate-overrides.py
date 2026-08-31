#!/usr/bin/env python3
"""Copy sibling content into the zip overrides, then rebuild the CF zip.

Looks at repo-root and warhammer-ark-minecraft/ for:
  content/factions/
  pack-src/datapacks/  pack-src/resourcepacks/  pack-src/quests/  pack-src/config/

Does not resolve CurseForge fileIDs. Does not add Fabric. Strips first-join court.
"""

from __future__ import annotations

import argparse
import json
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
PACK = ROOT / "pack"
OV = PACK / "cf-overrides"
CONTENT = PACK / "content" / "rallous_old_world"
DIST = ROOT / "dist"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from author_warp_crash import apply_warp_crash, rebuild_jar, strip_court_hooks  # noqa: E402


def search_roots() -> list[Path]:
    return [REPO, ROOT, Path("/workspace"), Path("/workspace/content").parent]


def find_dirs(rel: str) -> list[Path]:
    found: list[Path] = []
    seen: set[Path] = set()
    for base in search_roots():
        p = (base / rel).resolve()
        if p in seen or not p.is_dir():
            continue
        seen.add(p)
        found.append(p)
    return found


def copy_tree(src: Path, dest: Path) -> int:
    n = 0
    if not src.exists():
        return 0
    dest.mkdir(parents=True, exist_ok=True)
    if src.is_file():
        shutil.copy2(src, dest / src.name)
        return 1
    for path in src.rglob("*"):
        if path.is_file():
            target = dest / path.relative_to(src)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(path, target)
            n += 1
    return n


def ensure_lowcode_toml(src: Path) -> None:
    toml = src / "META-INF" / "mods.toml"
    if toml.exists() or src.name == "rallous_old_world":
        return
    if not (src / "pack.mcmeta").exists():
        return
    mod_id = src.name.replace("-", "_")[:64]
    w = toml
    w.parent.mkdir(parents=True, exist_ok=True)
    w.write_text(
        f"""modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="{mod_id}"
version="1.0.0"
displayName="{src.name}"
authors="Rallous System"
description='''Sibling datapack shipped as LowCodeFML so it loads without Open Loader.'''
"""
    )


def jar_datapack(src: Path) -> int:
    ensure_lowcode_toml(src)
    jar = OV / "mods" / f"{src.name}-1.0.0.jar"
    jar.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(jar, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(src.rglob("*")):
            if path.is_file() and path.name != "README.md":
                zf.write(path, path.relative_to(src).as_posix())
    print(f"extra jar {jar}")
    return 1


def merge_datapack(src: Path) -> int:
    """Ship sibling datapacks as their own LowCodeFML jars (no Open Loader).

    Do not copy their data/ into rallous_old_world — that double-fires tick tags.
    """
    if src.name == "rallous_old_world":
        return 0
    if (src / "data").is_dir() or (src / "pack.mcmeta").exists():
        return jar_datapack(src)
    return 0


def ingest_siblings() -> dict[str, int]:
    counts = {
        "factions": 0,
        "datapacks": 0,
        "resourcepacks": 0,
        "quests": 0,
        "config": 0,
    }
    for src in find_dirs("content/factions"):
        counts["factions"] += copy_tree(src, OV / "content" / "factions")
        counts["factions"] += copy_tree(src, PACK / "content" / "factions")
        if (src / "data").is_dir():
            counts["factions"] += copy_tree(src / "data", CONTENT / "data")
    for rel in (
        "pack-src/datapacks",
        "pack-src/overrides/datapacks",
        "content/datapacks",
    ):
        for src in find_dirs(rel):
            for pack in sorted(p for p in src.iterdir() if p.is_dir()):
                counts["datapacks"] += merge_datapack(pack)
    for rel in (
        "pack-src/resourcepacks",
        "pack-src/overrides/resourcepacks",
        "content/resourcepacks",
    ):
        for src in find_dirs(rel):
            for pack in sorted(p for p in src.iterdir() if p.is_dir() or p.suffix == ".zip"):
                dest = OV / "resourcepacks" / pack.name
                if pack.is_dir():
                    counts["resourcepacks"] += copy_tree(pack, dest)
                else:
                    dest.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(pack, dest)
                    counts["resourcepacks"] += 1
    for rel in (
        "pack-src/quests",
        "pack-src/overrides/config/ftbquests/quests",
        "content/ftbquests",
    ):
        for src in find_dirs(rel):
            chapters = src / "chapters" if (src / "chapters").is_dir() else src
            if chapters.name == "chapters" or any(chapters.glob("*.snbt")):
                dest = OV / "config" / "ftbquests" / "quests"
                if chapters.name == "chapters":
                    counts["quests"] += copy_tree(chapters, dest / "chapters")
                    if (src / "chapter_groups.snbt").exists():
                        shutil.copy2(src / "chapter_groups.snbt", dest / "chapter_groups.snbt")
                        counts["quests"] += 1
                else:
                    for snbt in chapters.glob("*.snbt"):
                        if snbt.name.startswith("chapter_groups"):
                            continue
                        target = dest / "chapters" / snbt.name
                        target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(snbt, target)
                        counts["quests"] += 1
    for src in find_dirs("pack-src/config"):
        counts["config"] += copy_tree(src, OV / "config")
    print("ingested", counts)
    return counts


def validate_json() -> int:
    errors = 0
    roots = [CONTENT, OV]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.json"):
            try:
                json.loads(path.read_text())
            except json.JSONDecodeError as e:
                print(f"INVALID JSON {path}: {e}")
                errors += 1
    if errors:
        raise SystemExit(f"JSON validation failed: {errors} file(s)")
    print("JSON ok")
    return 0


def assert_no_court_on_join() -> None:
    fj = CONTENT / "data" / "rallous_old_world" / "functions" / "first_join.mcfunction"
    text = fj.read_text() if fj.exists() else ""
    for bad in ("ensure_court", "summon_lords", "place_court"):
        if bad in text:
            raise SystemExit(f"first_join still calls {bad}")
    welcome = CONTENT / "data" / "rallous_old_world" / "functions" / "welcome.mcfunction"
    wt = welcome.read_text() if welcome.exists() else ""
    if "summon_lords" in wt or "ensure_court" in wt or "function rallous_old_world:summon" in wt:
        raise SystemExit("welcome still advertises the court")
    print("first-join court stripped")


def assert_no_fabric_files(manifest: dict) -> None:
    # Keep existing ETF project (slug contains 'fabric' but the pinned file is Forge).
    # Refuse any new loader besides forge.
    loaders = manifest.get("minecraft", {}).get("modLoaders", [])
    for loader in loaders:
        lid = str(loader.get("id", ""))
        if lid.startswith("fabric") or lid.startswith("quilt"):
            raise SystemExit(f"Fabric/Quilt loader in manifest: {lid}")
    if "fabric" in json.dumps(loaders).lower() and "forge-47.4.10" not in json.dumps(loaders):
        raise SystemExit("Unexpected non-Forge loader")
    print("manifest Forge-only", loaders)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="0.3.0")
    parser.add_argument("--skip-author", action="store_true", help="Do not rewrite crash functions")
    args = parser.parse_args()

    ingested = ingest_siblings()
    if not args.skip_author:
        apply_warp_crash()
    strip_court_hooks()
    rebuild_jar()
    assert_no_court_on_join()
    validate_json()

    script = Path(__file__).with_name("pack-zip.py")
    import subprocess

    subprocess.check_call([sys.executable, str(script), "--version", args.version])

    manifest = json.loads((PACK / "curseforge" / "manifest.json").read_text())
    assert_no_fabric_files(manifest)
    nfiles = len(manifest.get("files") or [])
    print(f"CF files pinned: {nfiles} version={manifest.get('version')}")
    print("sibling ingest", ingested)
    print("zip", DIST / f"rallous-warhammer-fantasy-{args.version}.zip")


if __name__ == "__main__":
    main()
