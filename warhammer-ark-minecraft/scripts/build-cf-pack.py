#!/usr/bin/env python3
"""Resolve CurseForge file IDs and build an importable CF modpack zip.

Uses api.cfwidget.com (public CF mirror) plus Modrinth for projects that
exist only there. Does not pirate: only official project/file IDs and
Modrinth CDN for the one Fantasy armor overlay not listed on CF.
"""

from __future__ import annotations

import html
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
DIST = ROOT / "dist"
OVERRIDES_SRC = PACK / "cf-overrides"
UA = "RallousWarhammerFantasy/0.2.2 (github.com/honeybadger0489/rallous-system; private pack pin)"
MC = "1.20.1"
FORGE = "47.4.10"
PACK_NAME = "Rallous Warhammer Fantasy"
PACK_VERSION = "0.2.2"
AUTHOR = "Rallous System"

# Directed Old-World pack. Kitchen-sink (Create, TaCZ, Macaw's, Alex's Caves,
# Cataclysm) stays out. Hammercraft 40k stays out — wrong setting.
PROJECTS: list[dict] = [
    # --- libraries ---
    {"title": "Just Enough Items (JEI)", "kind": "mod", "slugs": ["jei"], "id": 238222},
    {"title": "Jade", "kind": "mod", "slugs": ["jade"]},
    {"title": "Cloth Config API", "kind": "mod", "slugs": ["cloth-config"], "id": 348521},
    {"title": "Architectury API", "kind": "mod", "slugs": ["architectury-api", "architectury"], "id": 419699},
    {"title": "GeckoLib", "kind": "mod", "slugs": ["geckolib"], "id": 388172},
    {"title": "Citadel", "kind": "mod", "slugs": ["citadel"], "id": 331936},
    {"title": "Curios API", "kind": "mod", "slugs": ["curios"], "id": 309927},
    {"title": "Player Animator", "kind": "mod", "slugs": ["playeranimator"]},
    {"title": "Kotlin for Forge", "kind": "mod", "slugs": ["kotlin-for-forge"]},
    {"title": "Moonlight Lib", "kind": "mod", "slugs": ["selene", "moonlight-lib", "moonlight"], "id": 499980},
    {"title": "Puzzles Lib", "kind": "mod", "slugs": ["puzzles-lib"]},
    {"title": "YUNG's API", "kind": "mod", "slugs": ["yungs-api"]},
    {"title": "Sophisticated Core", "kind": "mod", "slugs": ["sophisticated-core"], "id": 618298},
    {"title": "Searchables", "kind": "mod", "slugs": ["searchables"]},
    {"title": "FTB Library", "kind": "mod", "slugs": ["ftb-library-forge", "ftb-library"], "id": 404465},
    {"title": "FTB Teams", "kind": "mod", "slugs": ["ftb-teams-forge", "ftb-teams"], "id": 404468},
    {"title": "Item Filters", "kind": "mod", "slugs": ["item-filters"], "id": 309674, "optional": True},
    {"title": "Data Anchor", "kind": "mod", "slugs": ["data-anchor"], "id": 1203668},
    {"title": "CorgiLib", "kind": "mod", "slugs": ["corgilib"], "id": 693313},
    {"title": "GlitchCore", "kind": "mod", "slugs": ["glitchcore"], "id": 955399},
    {"title": "Fzzy Config", "kind": "mod", "slugs": ["fzzy-config"], "id": 1005914},
    {"title": "Simply Tooltips", "kind": "mod", "slugs": ["simply-tooltips"], "id": 1475755},
    {"title": "More Hitboxes", "kind": "mod", "slugs": ["more-hitboxes"], "id": 1115989},
    {"title": "TerraBlender (Forge)", "kind": "mod", "slugs": ["terrablender"], "id": 563928},
    {"title": "Lodestone", "kind": "mod", "slugs": ["lodestone"], "id": 616457},
    {"title": "Cristel Lib", "kind": "mod", "slugs": ["cristel-lib"], "id": 856996},
    {"title": "Iron's Lib", "kind": "mod", "slugs": ["irons-lib"], "id": 1492763},
    # --- performance ---
    {"title": "Embeddium", "kind": "mod", "slugs": ["embeddium"], "id": 908741},
    {"title": "Oculus", "kind": "mod", "slugs": ["oculus"], "id": 581495},
    {"title": "FerriteCore", "kind": "mod", "slugs": ["ferritecore"], "id": 429235},
    {"title": "ModernFix", "kind": "mod", "slugs": ["modernfix"]},
    {"title": "Entity Culling", "kind": "mod", "slugs": ["entityculling"], "id": 448233},
    # --- qol ---
    {"title": "AppleSkin", "kind": "mod", "slugs": ["appleskin"]},
    {"title": "Controlling", "kind": "mod", "slugs": ["controlling"]},
    {"title": "Mouse Tweaks", "kind": "mod", "slugs": ["mouse-tweaks"]},
    {"title": "Carry On", "kind": "mod", "slugs": ["carry-on"]},
    {"title": "Sophisticated Backpacks", "kind": "mod", "slugs": ["sophisticated-backpacks"]},
    {"title": "Entity Texture Features", "kind": "mod", "slugs": ["entity-texture-features-fabric", "entitytexturefeatures"]},
    {"title": "Entity Model Features", "kind": "mod", "slugs": ["entity-model-features"]},
    {"title": "Xaero's Minimap", "kind": "mod", "slugs": ["xaeros-minimap"]},
    {"title": "Xaero's World Map", "kind": "mod", "slugs": ["xaeros-world-map"]},
    # --- magic (WH battle magic + grim occult) ---
    {"title": "Iron's Spells 'n Spellbooks", "kind": "mod", "slugs": ["irons-spells-n-spellbooks"], "id": 855414},
    {"title": "Malum", "kind": "mod", "slugs": ["malum"]},
    # --- factions / war / alliance ---
    {"title": "Villager Recruits", "kind": "mod", "slugs": ["recruits"], "id": 523860},
    {
        "title": "Vassal & Suzerains",
        "kind": "mod",
        "slugs": ["vassal-suzerains-villager-recruits-addon"],
    },
    {
        "title": "Ranks and Titles (Recruits Addon)",
        "kind": "mod",
        "slugs": ["ranks-and-titles-recruits-addon", "ranks-and-titles"],
        "optional": True,
    },
    {"title": "Open Parties and Claims", "kind": "mod", "slugs": ["open-parties-and-claims"], "id": 636608},
    {"title": "Guard Villagers", "kind": "mod", "slugs": ["guard-villagers"]},
    {
        "title": "Siege Weapons",
        "kind": "mod",
        "slugs": ["siege-weapons", "medieval-siege-machines", "siegeweapons"],
        "optional": True,
    },
    {
        "title": "Custom NPCs Unofficial",
        "kind": "mod",
        "slugs": ["customnpcs-unofficial", "custom-npcs-unofficial", "customnpcs", "custom-npcs"],
        "optional": True,
    },
    # --- combat ---
    {"title": "Epic Fight", "kind": "mod", "slugs": ["epic-fight-mod"], "id": 405076},
    {"title": "Simply Swords", "kind": "mod", "slugs": ["simply-swords"], "id": 659887},
    {
        "title": "Epic Knights",
        "kind": "mod",
        "slugs": ["epic-knights-armor-and-weapons"],
        "id": 509041,
    },
    # --- ark-like survival / beasts ---
    {"title": "Fossils and Archeology Revival", "kind": "mod", "slugs": ["fossils"], "id": 223908},
    {"title": "Tameable Beasts", "kind": "mod", "slugs": ["tameable-beasts"], "id": 646425},
    {"title": "Legendary Survival Overhaul", "kind": "mod", "slugs": ["legendary-survival-overhaul"], "id": 840254},
    {"title": "Serene Seasons", "kind": "mod", "slugs": ["serene-seasons"], "id": 291874},
    {"title": "Farmer's Delight", "kind": "mod", "slugs": ["farmers-delight"], "id": 398521},
    # --- world / towns / sieges ---
    {"title": "Terralith", "kind": "mod", "slugs": ["terralith"], "id": 513688},
    {"title": "Towns and Towers", "kind": "mod", "slugs": ["towns-and-towers"]},
    {"title": "When Dungeons Arise", "kind": "mod", "slugs": ["when-dungeons-arise", "dungeons-arise"], "id": 442508},
    {"title": "YUNG's Better Dungeons", "kind": "mod", "slugs": ["yungs-better-dungeons"], "id": 510089},
    {"title": "YUNG's Better Nether Fortresses", "kind": "mod", "slugs": ["yungs-better-nether-fortresses"]},
    {"title": "YUNG's Better Strongholds", "kind": "mod", "slugs": ["yungs-better-strongholds"], "id": 465575},
    {"title": "Structory", "kind": "mod", "slugs": ["structory"]},
    {"title": "Explorify", "kind": "mod", "slugs": ["explorify"]},
    {"title": "Born in Chaos", "kind": "mod", "slugs": ["born-in-chaos"], "id": 686437},
    {"title": "Enhanced Celestials", "kind": "mod", "slugs": ["enhanced-celestials"], "id": 438447},
    {"title": "Supplementaries", "kind": "mod", "slugs": ["supplementaries"]},
    {"title": "Amendments", "kind": "mod", "slugs": ["amendments"]},
    {
        "title": "ChoiceTheorem's Overhauled Village",
        "kind": "mod",
        "slugs": ["choicetheorems-overhauled-village"],
        "optional": True,
    },
    {
        "title": "Lithostitched",
        "kind": "mod",
        "slugs": ["lithostitched"],
        "optional": True,
    },
    # --- questing ---
    {"title": "FTB Quests", "kind": "mod", "slugs": ["ftb-quests", "ftb-quests-forge"], "id": 289412},
    # --- look ---
    {"title": "Grimdark Sky Pack", "kind": "resourcepack", "slugs": ["grimdark-sky"]},
    {"title": "Grimdark Battlepack", "kind": "resourcepack", "slugs": ["grimdark-battlepack"], "optional": True},
    {"title": "Faithful 32x", "kind": "resourcepack", "slugs": ["faithful-32x"], "optional": True},
    {"title": "Fresh Animations", "kind": "resourcepack", "slugs": ["fresh-animations"], "optional": True},
    {"title": "Gothic RPG Font", "kind": "resourcepack", "slugs": ["gothic-rpg-font"]},
    {"title": "Complementary Shaders - Unbound", "kind": "shader", "slugs": ["complementary-unbound", "complementary-shaders-unbound"]},
]

# Official Modrinth CDN bundles (no usable CF file listing).
MODRINTH_BUNDLES = [
    {
        "title": "Warhammer: Sons of the Empire",
        "slug": "warhammer-sons-of-the-empire",
        "dest": "mods",
        "loaders": ["forge"],
        "reason": "Official Modrinth listing; no CurseForge project found. WH Fantasy faction armor (Empire, Bretonnia, Kislev, Dawi, Asur, Southern Realms).",
    },
    {
        "title": "Grimdark Battlepack",
        "slug": "battlepack",
        "dest": "resourcepacks",
        "loaders": None,
        "reason": "CF project exists but file list is empty on the pin API; official Modrinth 2.7 zip.",
    },
    {
        "title": "Faithful 32x",
        "slug": "faithful-32x",
        "dest": "resourcepacks",
        "loaders": None,
        "reason": "CF Faithful x32 listing has no 1.20.1 files; official Modrinth 1.20.1 zip.",
    },
    {
        "title": "Fresh Animations",
        "slug": "fresh-animations",
        "dest": "resourcepacks",
        "loaders": None,
        "reason": "No CurseForge 1.20.1 listing found; official Modrinth zip. Needs ETF + EMF (in the CF files list).",
    },
]


def http_json(url: str, retries: int = 4):
    delay = 1.0
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(delay)
            delay *= 2
    raise last


def http_bytes(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=90) as resp:
        return resp.read()


def head_ok(url: str) -> tuple[bool, int | None]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return True, resp.status
    except urllib.error.HTTPError as e:
        return e.code in (200, 301, 302, 303, 307, 308), e.code
    except Exception:
        return False, None


def cfwidget(path: str) -> dict | None:
    url = f"https://api.cfwidget.com/{path.lstrip('/')}"
    try:
        return http_json(url)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


def lookup_project(entry: dict) -> dict | None:
    if entry.get("id"):
        data = cfwidget(str(entry["id"]))
        if data:
            return data
    classes = {
        "mod": ["minecraft/mc-mods"],
        "resourcepack": ["minecraft/texture-packs", "minecraft/mc-mods"],
        "shader": ["minecraft/shaders", "minecraft/texture-packs", "minecraft/mc-mods"],
    }
    for slug in entry["slugs"]:
        for cls in classes[entry["kind"]]:
            data = cfwidget(f"{cls}/{slug}")
            if data:
                return data
            time.sleep(0.15)
    return None


def _tags(file_rec: dict) -> list[str]:
    return [str(x).lower() for x in (file_rec.get("versions") or [])]


def is_1201(file_rec: dict) -> bool:
    tags = _tags(file_rec)
    if "1.20.1" in tags:
        return True
    if file_rec.get("version") == "1.20.1":
        return True
    name = (file_rec.get("name") or "").lower()
    display = (file_rec.get("display") or "").lower()
    return "1.20.1" in name or "1.20.1" in display


def loader_bucket(file_rec: dict, kind: str) -> str:
    """Return 'forge', 'other-ok', or 'skip'."""
    tags = _tags(file_rec)
    name = (file_rec.get("name") or "").lower()
    if kind in ("resourcepack", "shader"):
        if "fabric" in name and "forge" not in name:
            return "skip"
        if "neoforge" in name and "forge" not in name.replace("neoforge", ""):
            return "skip"
        return "other-ok"
    fabric_only = "fabric" in tags and "forge" not in tags
    neo_only = "neoforge" in tags and "forge" not in tags
    if fabric_only or neo_only:
        return "skip"
    if "fabric" in name and "forge" not in name:
        return "skip"
    if name.endswith("-fabric.jar") or "-fabric-" in name:
        if "forge" not in name:
            return "skip"
    if "neoforge" in name and "forge" not in name.replace("neoforge", ""):
        return "skip"
    if "forge" in tags or "forge" in name:
        return "forge"
    # Some libraries tag only 1.20.1 without loader
    if not any(x in tags for x in ("fabric", "quilt", "neoforge")):
        return "other-ok"
    return "skip"


def pick_file(project: dict, kind: str) -> dict | None:
    pool = []
    versions = project.get("versions") or {}
    files = versions.get("1.20.1") or []
    if not files:
        files = [f for f in (project.get("files") or []) if is_1201(f)]
    for f in files:
        if not is_1201(f):
            continue
        bucket = loader_bucket(f, kind)
        if bucket == "skip":
            continue
        pool.append((0 if bucket == "forge" else 1, f))
    if not pool:
        return None
    pool.sort(key=lambda x: (x[0], x[1].get("uploaded_at") or ""), reverse=True)
    # After reverse: newest first among forge (0) — wait, reverse on tuple
    # (0, date) reversed puts forge last. Sort properly:
    forge = [f for score, f in pool if score == 0]
    generic = [f for score, f in pool if score == 1]
    chosen_pool = forge or generic
    chosen_pool.sort(key=lambda f: f.get("uploaded_at") or "", reverse=True)
    return chosen_pool[0]


def forgecdn_url(file_id: int, filename: str) -> str:
    return f"https://edge.forgecdn.net/files/{file_id // 1000}/{file_id % 1000}/{urllib.parse.quote(filename)}"


def resolve_all() -> list[dict]:
    resolved = []
    missing = []
    for entry in PROJECTS:
        print(f"resolve {entry['title']} ...", flush=True)
        try:
            proj = lookup_project(entry)
        except Exception as e:
            print(f"  ERROR lookup: {e}")
            proj = None
        time.sleep(0.2)
        if not proj:
            if entry.get("optional"):
                print("  skip (optional, not found)")
                continue
            missing.append(entry["title"])
            print("  MISSING")
            continue
        file_rec = pick_file(proj, entry["kind"])
        if not file_rec:
            if entry.get("optional"):
                print("  skip (optional, no 1.20.1 Forge file)")
                continue
            missing.append(entry["title"])
            print(f"  NO FILE id={proj.get('id')}")
            continue
        rec = {
            "title": entry["title"],
            "kind": entry["kind"],
            "projectID": int(proj["id"]),
            "fileID": int(file_rec["id"]),
            "filename": file_rec.get("name"),
            "display": file_rec.get("display"),
            "uploaded_at": file_rec.get("uploaded_at"),
            "versions": file_rec.get("versions"),
            "cf_url": proj.get("urls", {}).get("curseforge"),
            "file_url": file_rec.get("url"),
            "required": True,
        }
        rec["cdn"] = forgecdn_url(rec["fileID"], rec["filename"] or "file.jar")
        print(f"  {rec['projectID']}:{rec['fileID']} {rec['filename']}")
        resolved.append(rec)
    if missing:
        raise SystemExit("Missing required projects:\n- " + "\n- ".join(missing))
    # de-dupe project IDs
    seen = {}
    unique = []
    for rec in resolved:
        pid = rec["projectID"]
        if pid in seen:
            print(f"WARN duplicate project {pid} {seen[pid]} vs {rec['title']}")
            continue
        seen[pid] = rec["title"]
        unique.append(rec)
    return unique


def bundle_modrinth() -> list[dict]:
    out = []
    dest_root = OVERRIDES_SRC
    for item in MODRINTH_BUNDLES:
        slug = item["slug"]
        print(f"modrinth bundle {slug} ...", flush=True)
        params = {"game_versions": json.dumps([MC])}
        if item.get("loaders"):
            params["loaders"] = json.dumps(item["loaders"])
        versions = http_json(
            "https://api.modrinth.com/v2/project/"
            + slug
            + "/version?"
            + urllib.parse.urlencode(params)
        )
        if not versions:
            raise SystemExit(f"No Modrinth Forge 1.20.1 file for {slug}")
        versions.sort(key=lambda v: v.get("date_published") or "", reverse=True)
        ver = versions[0]
        files = ver.get("files") or []
        primary = next((f for f in files if f.get("primary")), files[0])
        filename = primary["filename"]
        url = primary["url"]
        folder = dest_root / item["dest"]
        folder.mkdir(parents=True, exist_ok=True)
        target = folder / filename
        if not target.exists():
            print(f"  download {url}")
            target.write_bytes(http_bytes(url))
        print(f"  wrote {target} ({target.stat().st_size} bytes)")
        out.append(
            {
                "title": item["title"],
                "slug": slug,
                "filename": filename,
                "version": ver.get("version_number"),
                "url": url,
                "sha1": (primary.get("hashes") or {}).get("sha1"),
                "path": f"overrides/{item['dest']}/{filename}",
                "reason": item["reason"],
            }
        )
    return out


def write_modlist(resolved: list[dict], bundles: list[dict]) -> str:
    rows = []
    for rec in resolved:
        url = rec.get("cf_url") or rec.get("file_url") or "#"
        rows.append(f'<li><a href="{html.escape(url)}">{html.escape(rec["title"])}</a> ({html.escape(rec["filename"] or "")})</li>')
    for b in bundles:
        rows.append(
            f'<li><a href="https://modrinth.com/mod/{html.escape(b["slug"])}">{html.escape(b["title"])}</a> (Modrinth {html.escape(b["version"])} bundled)</li>'
        )
    return (
        "<!DOCTYPE html><html><head><meta charset='utf-8'><title>"
        + html.escape(PACK_NAME)
        + "</title></head><body><h1>"
        + html.escape(PACK_NAME)
        + f" {PACK_VERSION}</h1><ul>\n"
        + "\n".join(rows)
        + "\n</ul></body></html>\n"
    )


def validate_ids(resolved: list[dict]) -> None:
    bad = []
    for rec in resolved:
        pid, fid = rec["projectID"], rec["fileID"]
        if not (10000 < pid < 10_000_000):
            bad.append(f"implausible projectID {pid} for {rec['title']}")
        if not (100000 < fid < 100_000_000):
            bad.append(f"implausible fileID {fid} for {rec['title']}")
        ok, code = head_ok(rec["file_url"])
        rec["file_page_ok"] = ok
        rec["file_page_status"] = code
        if not ok:
            # CF pages are often Cloudflare-gated; treat CFWidget record as source of truth
            print(f"  HEAD {rec['file_url']} -> {code} (cloudflare-ok if 403/503)")
        time.sleep(0.05)
    if bad:
        raise SystemExit("Validation failed:\n- " + "\n- ".join(bad))


def build_zip(resolved: list[dict], bundles: list[dict]) -> Path:
    DIST.mkdir(parents=True, exist_ok=True)
    manifest = {
        "minecraft": {
            "version": MC,
            "modLoaders": [{"id": f"forge-{FORGE}", "primary": True}],
        },
        "manifestType": "minecraftModpack",
        "manifestVersion": 1,
        "name": PACK_NAME,
        "version": PACK_VERSION,
        "author": AUTHOR,
        "overrides": "overrides",
        "files": [
            {"projectID": rec["projectID"], "fileID": rec["fileID"], "required": True}
            for rec in resolved
        ],
    }
    pack_dir = PACK / "curseforge"
    pack_dir.mkdir(parents=True, exist_ok=True)
    (pack_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    (pack_dir / "modlist.html").write_text(write_modlist(resolved, bundles))
    snapshot = {
        "pack": {
            "name": PACK_NAME,
            "version": PACK_VERSION,
            "minecraft": MC,
            "loader": "forge",
            "loader_version": FORGE,
        },
        "resolved": resolved,
        "modrinth_bundles": bundles,
    }
    (PACK / "curseforge-resolved.json").write_text(json.dumps(snapshot, indent=2) + "\n")

    zip_path = DIST / f"rallous-warhammer-fantasy-{PACK_VERSION}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(pack_dir / "manifest.json", "manifest.json")
        zf.write(pack_dir / "modlist.html", "modlist.html")
        if OVERRIDES_SRC.exists():
            for path in sorted(OVERRIDES_SRC.rglob("*")):
                if path.is_file():
                    zf.write(path, f"overrides/{path.relative_to(OVERRIDES_SRC).as_posix()}")
    print(f"wrote {zip_path} ({zip_path.stat().st_size} bytes)")
    return zip_path


def main() -> None:
    import subprocess
    import sys

    if "--pack-only" in sys.argv:
        # Do not re-resolve CurseForge fileIDs. Rebuild zip from the existing
        # manifest + current overrides (content/glue updates).
        script = Path(__file__).with_name("pack-zip.py")
        raise SystemExit(subprocess.call([sys.executable, str(script), "--version", PACK_VERSION]))
    resolved = resolve_all()
    bundles = bundle_modrinth()
    validate_ids(resolved)
    zip_path = build_zip(resolved, bundles)
    print("FILES", len(resolved), "BUNDLES", len(bundles), "ZIP", zip_path)


if __name__ == "__main__":
    main()
