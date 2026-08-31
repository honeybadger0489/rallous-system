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
from compile_factions import compile_factions  # noqa: E402


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
    """Ship sibling datapacks as LowCodeFML jars plus inspectable override folders.

    Do not copy their data/ into rallous_old_world — that double-fires tick tags.
    Folders under overrides/datapacks do not auto-load without Open Loader.
    """
    if src.name == "rallous_old_world":
        return 0
    if not ((src / "data").is_dir() or (src / "pack.mcmeta").exists()):
        return 0
    n = jar_datapack(src)
    n += copy_tree(src, OV / "datapacks" / src.name)
    return n


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
    counts["quests"] += ingest_ftb_chapters()
    for src in find_dirs("pack-src/config"):
        counts["config"] += copy_tree(src, OV / "config")
    print("ingested", counts)
    return counts


COURT_CHAPTERS = (
    "reikland",
    "border_princes",
    "sylvania",
    "worlds_edge",
    "kislev",
    "chaos_wastes",
    "first_contact",
)

SIBLING_CHAPTERS = ("temple_and_herd",)


def ingest_ftb_chapters() -> int:
    """Copy FTB from pack-src / content. Never restore court chapters."""
    n = 0
    dest = OV / "config" / "ftbquests" / "quests"
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "chapters").mkdir(parents=True, exist_ok=True)
    for rel in (
        "pack-src/quests",
        "pack-src/overrides/config/ftbquests/quests",
        "content/ftbquests",
    ):
        for src in find_dirs(rel):
            chapters = src / "chapters" if (src / "chapters").is_dir() else src
            if chapters.name == "chapters":
                for snbt in chapters.glob("*.snbt"):
                    if snbt.stem in COURT_CHAPTERS:
                        continue
                    target = dest / "chapters" / snbt.name
                    shutil.copy2(snbt, target)
                    n += 1
                if (src / "chapter_groups.snbt").exists():
                    shutil.copy2(src / "chapter_groups.snbt", dest / "chapter_groups.snbt")
                    n += 1
                if (src / "data.snbt").exists():
                    shutil.copy2(src / "data.snbt", dest / "data.snbt")
                    n += 1
            else:
                for snbt in chapters.glob("*.snbt"):
                    if snbt.name.startswith("chapter_groups") or snbt.stem in COURT_CHAPTERS:
                        continue
                    target = dest / "chapters" / snbt.name
                    shutil.copy2(snbt, target)
                    n += 1
    for old in COURT_CHAPTERS:
        p = dest / "chapters" / f"{old}.snbt"
        if p.exists():
            p.unlink()
    return n


def restore_sibling_ftb() -> None:
    """author_contact rewrites the Warp-Crash book; keep sibling chapters."""
    dest = OV / "config" / "ftbquests" / "quests" / "chapters"
    dest.mkdir(parents=True, exist_ok=True)
    for name in SIBLING_CHAPTERS:
        for rel in (
            f"content/ftbquests/chapters/{name}.snbt",
            f"pack-src/quests/chapters/{name}.snbt",
        ):
            for base in search_roots():
                src = base / rel
                if src.is_file():
                    shutil.copy2(src, dest / f"{name}.snbt")
                    print(f"restored sibling FTB {name} from {src}")
                    break


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
    live = OV / "config" / "ftbquests" / "quests" / "chapters"
    for old in COURT_CHAPTERS:
        if (live / f"{old}.snbt").exists():
            raise SystemExit(f"court chapter still in overrides: {old}")
    wc_join = OV / "datapacks" / "rallous_warp_crash" / "data" / "rallous_warp_crash" / "functions" / "first_join.mcfunction"
    if wc_join.exists():
        wct = wc_join.read_text()
        for bad in ("ensure_court", "summon_lords", "place_court"):
            if bad in wct:
                raise SystemExit(f"warp_crash first_join still calls {bad}")
    print("first-join court stripped")


REQUIRED_JARS = (
    "rallous-old-world-1.0.0.jar",
    "rallous_contact-1.0.0.jar",
    "rallous_roaming-1.0.0.jar",
    "rallous_temple_herd-1.0.0.jar",
    "rallous_warp_crash-1.0.0.jar",
    "rallous_factions-1.0.0.jar",
)

REQUIRED_FTB = (
    "crash.snbt",
    "paths.snbt",
    "first_hour.snbt",
    "winds.snbt",
    "host.snbt",
    "smoke_test.snbt",
    "temple_and_herd.snbt",
)


def assert_zip_payload(zip_path: Path, file_ids_021: set[tuple[int, int]]) -> None:
    if not zip_path.exists():
        raise SystemExit(f"missing zip {zip_path}")
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
        manifest = json.loads(zf.read("manifest.json"))
        if manifest.get("version") != zip_path.stem.rsplit("-", 1)[-1]:
            raise SystemExit(f"zip manifest version {manifest.get('version')} != {zip_path.name}")
        loaders = manifest.get("minecraft", {}).get("modLoaders", [])
        if loaders != [{"id": "forge-47.4.10", "primary": True}]:
            raise SystemExit(f"zip loaders {loaders}")
        got = {(f["projectID"], f["fileID"]) for f in manifest.get("files") or []}
        if file_ids_021 and got != file_ids_021:
            raise SystemExit(f"fileIDs drifted from 0.2.1: +{got-file_ids_021} -{file_ids_021-got}")
        for jar in REQUIRED_JARS:
            if f"overrides/mods/{jar}" not in names:
                raise SystemExit(f"zip missing jar {jar}")
        for ch in REQUIRED_FTB:
            if f"overrides/config/ftbquests/quests/chapters/{ch}" not in names:
                raise SystemExit(f"zip missing FTB {ch}")
        for old in COURT_CHAPTERS:
            if f"overrides/config/ftbquests/quests/chapters/{old}.snbt" in names:
                raise SystemExit(f"zip still has court chapter {old}")
        for pack in ("rallous_warp_crash", "rallous_roaming", "rallous_temple_herd", "rallous_contact", "rallous_factions"):
            if f"overrides/datapacks/{pack}/pack.mcmeta" not in names:
                raise SystemExit(f"zip missing datapack folder {pack}")
        if "overrides/content/factions/races/empire.json" not in names:
            raise SystemExit("zip missing faction JSON")
        if "overrides/datapacks/rallous_factions/data/rallous_factions/functions/place/reikland.mcfunction" not in names:
            raise SystemExit("zip missing compiled faction place/reikland")
        if "overrides/datapacks/rallous_factions/data/rallous_factions/functions/crash/on_land.mcfunction" not in names:
            raise SystemExit("zip missing compiled crash/on_land")
        fac = zipfile.ZipFile(__import__("io").BytesIO(zf.read("overrides/mods/rallous_factions-1.0.0.jar")))
        fac_names = set(fac.namelist())
        if "data/rallous_factions/functions/place/karaz_a_karak.mcfunction" not in fac_names:
            raise SystemExit("factions jar missing karaz_a_karak place")
        if "data/rallous_factions/functions/pool/empire/pick_major.mcfunction" not in fac_names:
            raise SystemExit("factions jar missing empire major pool")
        wc = zipfile.ZipFile(__import__("io").BytesIO(zf.read("overrides/mods/rallous_warp_crash-1.0.0.jar")))
        hook = wc.read("data/rallous_warp_crash/functions/contact_hook.mcfunction").decode()
        if "rallous_factions:crash/on_land" not in hook:
            raise SystemExit("warp_crash contact_hook does not call compiled factions")
        if "tag_existing_contact" in hook:
            raise SystemExit("warp_crash still tags mute villagers as contact")
        if "overrides/resourcepacks/Rallous Continuity/pack.mcmeta" not in names:
            raise SystemExit("zip missing Rallous Continuity resource pack")
        if any("Continuity" in n and n.endswith(".jar") for n in names):
            raise SystemExit("zip contains Continuity jar")
        from io import BytesIO

        ow = zipfile.ZipFile(BytesIO(zf.read("overrides/mods/rallous-old-world-1.0.0.jar")))
        fj = ow.read("data/rallous_old_world/functions/first_join.mcfunction").decode()
        for bad in ("ensure_court", "summon_lords", "place_court"):
            if bad in fj:
                raise SystemExit(f"old_world jar first_join calls {bad}")
        wc = zipfile.ZipFile(BytesIO(zf.read("overrides/mods/rallous_warp_crash-1.0.0.jar")))
        wj = wc.read("data/rallous_warp_crash/functions/first_join.mcfunction").decode()
        for bad in ("ensure_court", "summon_lords", "place_court"):
            if bad in wj:
                raise SystemExit(f"warp_crash jar first_join calls {bad}")
    print("zip payload ok", zip_path.name)


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


def file_ids_from_021() -> set[tuple[int, int]]:
    z021 = DIST / "rallous-warhammer-fantasy-0.2.1.zip"
    if not z021.exists():
        return set()
    with zipfile.ZipFile(z021) as zf:
        manifest = json.loads(zf.read("manifest.json"))
    return {(f["projectID"], f["fileID"]) for f in manifest.get("files") or []}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="0.3.3")
    parser.add_argument("--skip-author", action="store_true", help="Do not rewrite crash functions")
    args = parser.parse_args()

    compile_factions()
    ingested = ingest_siblings()
    if not args.skip_author:
        apply_warp_crash()
    restore_sibling_ftb()
    strip_court_hooks()
    rebuild_jar()
    ingest_siblings()
    restore_sibling_ftb()
    assert_no_court_on_join()
    validate_json()

    play = ROOT / "PLAY.md"
    if play.exists():
        (OV / "PLAY.md").write_text(play.read_text())

    script = Path(__file__).with_name("pack-zip.py")
    import subprocess

    subprocess.check_call([sys.executable, str(script), "--version", args.version])

    manifest = json.loads((PACK / "curseforge" / "manifest.json").read_text())
    assert_no_fabric_files(manifest)
    zip_path = DIST / f"rallous-warhammer-fantasy-{args.version}.zip"
    assert_zip_payload(zip_path, file_ids_from_021())
    nfiles = len(manifest.get("files") or [])
    print(f"CF files pinned: {nfiles} version={manifest.get('version')}")
    print("sibling ingest", ingested)
    print("zip", zip_path)


if __name__ == "__main__":
    main()
