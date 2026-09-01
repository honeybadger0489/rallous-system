#!/usr/bin/env python3
"""Resolve Modrinth versions for Rallous Frontier and write packwiz + mrpack metadata."""

from __future__ import annotations

import hashlib
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
CATALOG = PACK / "catalog.json"
UA = "RallousFrontierPack/0.1 (github.com/honeybadger0489/rallous-system)"
API = "https://api.modrinth.com/v2"
MC = "1.20.1"
LOADER = "forge"


def http_get_json(url: str, retries: int = 4):
    delay = 1.0
    last = None
    for _ in range(retries):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": UA, "Accept": "application/json"}
            )
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


def pick_version(project: dict, versions: list[dict]) -> dict | None:
    """Prefer a Forge 1.20.1 file that actually targets 1.20.1, not a mis-tagged 1.20.4+."""
    if not versions:
        return None
    ptype = project.get("project_type") or project.get("type")

    def score(v: dict) -> tuple:
        gv = set(v.get("game_versions") or [])
        loaders = set(v.get("loaders") or [])
        fn = (v.get("files") or [{}])[0].get("filename") or ""
        vn = v.get("version_number") or ""
        blob = f"{fn} {vn}".lower()
        has_mc = "1.20.1" in gv
        # Penalize clearly-newer filenames tagged onto 1.20.1
        mismatch = any(x in blob for x in ("1.20.2", "1.20.4", "1.20.5", "1.20.6", "1.21"))
        forge_ok = "forge" in loaders or "minecraft" in loaders or "iris" in loaders or "optifine" in loaders
        return (
            0 if has_mc else 1,
            0 if not mismatch else 1,
            0 if forge_ok else 1,
            v.get("date_published") or "",
        )

    ranked = sorted(versions, key=score)
    # date_published is last in score so we need newest among good scores:
    good = [v for v in versions if score(v)[0] == 0 and score(v)[1] == 0]
    if good:
        good.sort(key=lambda v: v.get("date_published") or "", reverse=True)
        return good[0]
    if ranked:
        ranked.sort(key=lambda v: (score(v)[0], score(v)[1], score(v)[2], ""), reverse=False)
        # newest among least-penalized
        best_prefix = score(ranked[0])[:3]
        pool = [v for v in versions if score(v)[:3] == best_prefix]
        pool.sort(key=lambda v: v.get("date_published") or "", reverse=True)
        return pool[0]
    return versions[0]


def fetch_versions(slug: str, ptype: str) -> list[dict]:
    if ptype == "mod":
        q = urllib.parse.urlencode(
            {
                "game_versions": json.dumps([MC]),
                "loaders": json.dumps([LOADER]),
            }
        )
        url = f"{API}/project/{slug}/version?{q}"
    elif ptype == "shader":
        q = urllib.parse.urlencode({"game_versions": json.dumps([MC])})
        url = f"{API}/project/{slug}/version?{q}"
        data = http_get_json(url)
        if data:
            return data
        return http_get_json(f"{API}/project/{slug}/version")[:8]
    else:
        q = urllib.parse.urlencode({"game_versions": json.dumps([MC])})
        url = f"{API}/project/{slug}/version?{q}"
        data = http_get_json(url)
        if data:
            return data
        return http_get_json(f"{API}/project/{slug}/version")[:8]
    return http_get_json(url)


def primary_file(version: dict) -> dict:
    files = version.get("files") or []
    for f in files:
        if f.get("primary"):
            return f
    return files[0]


def toml_escape(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def write_pw_toml(path: Path, rec: dict) -> None:
    side = rec.get("side") or "both"
    if rec["type"] in ("resourcepack", "shader"):
        side = "client"
    lines = [
        f'name = "{toml_escape(rec["title"])}"',
        f'filename = "{toml_escape(rec["filename"])}"',
        f'side = "{side}"',
        "",
        "[download]",
        'hash-format = "sha1"',
        f'hash = "{rec["sha1"]}"',
        f'mode = "url"',
        f'url = "{rec["url"]}"',
        "",
        "[update]",
        "[update.modrinth]",
        f'mod-id = "{rec["project_id"]}"',
        f'version = "{rec["version_id"]}"',
        "",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def folder_for(ptype: str) -> str:
    return {"mod": "mods", "resourcepack": "resourcepacks", "shader": "shaderpacks"}[ptype]


def main() -> int:
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    pack_meta = catalog["pack"]
    resolved = []
    errors = []

    for entry in catalog["projects"]:
        slug = entry["slug"]
        ptype = entry["type"]
        try:
            proj = http_get_json(f"{API}/project/{slug}")
            versions = fetch_versions(slug, ptype)
            ver = pick_version({**entry, "project_type": ptype}, versions)
            if not ver:
                errors.append({"slug": slug, "error": "no versions"})
                print(f"NOVER {slug}", file=sys.stderr)
                continue
            f = primary_file(ver)
            rec = {
                **entry,
                "title": entry.get("title") or proj.get("title"),
                "project_id": proj["id"],
                "license": (proj.get("license") or {}).get("id"),
                "modrinth_url": f"https://modrinth.com/{proj.get('project_type')}/{proj.get('slug')}",
                "version_id": ver["id"],
                "version_number": ver["version_number"],
                "version_date": ver.get("date_published"),
                "loaders": ver.get("loaders"),
                "game_versions": ver.get("game_versions"),
                "filename": f["filename"],
                "url": f["url"],
                "size": f.get("size"),
                "sha1": (f.get("hashes") or {}).get("sha1"),
                "sha512": (f.get("hashes") or {}).get("sha512"),
                "dependencies": ver.get("dependencies") or [],
            }
            resolved.append(rec)
            flag = "DEFAULT" if entry.get("include_in_default") else "LISTED"
            print(f"{flag:7} {ptype:13} {slug:42} {rec['version_number']}")
            time.sleep(0.04)
        except Exception as e:
            errors.append({"slug": slug, "error": str(e)})
            print(f"ERR {slug}: {e}", file=sys.stderr)

    default = [r for r in resolved if r.get("include_in_default")]
    starter = [r for r in resolved if r.get("starter")]

    # packwiz files
    for sub in ("mods", "resourcepacks", "shaderpacks"):
        d = PACK / sub
        if d.exists():
            for p in d.glob("*.pw.toml"):
                p.unlink()

    index_files = []
    for rec in default:
        rel = f"{folder_for(rec['type'])}/{rec['slug']}.pw.toml"
        path = PACK / rel
        write_pw_toml(path, rec)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        index_files.append((rel.replace("\\", "/"), digest))

    index_files.sort()
    index_lines = ['hash-format = "sha256"', ""]
    for rel, digest in index_files:
        index_lines += ["[[files]]", f'file = "{rel}"', f'hash = "{digest}"', "metafile = true", ""]
    index_text = "\n".join(index_lines)
    (PACK / "index.toml").write_text(index_text, encoding="utf-8")
    index_hash = hashlib.sha256(index_text.encode()).hexdigest()

    pack_toml = f"""name = "{toml_escape(pack_meta['name'])}"
author = "{toml_escape(pack_meta['author'])}"
version = "{pack_meta['version']}"
pack-format = "packwiz:1.1.0"
description = "{toml_escape(pack_meta['description'])}"

[index]
file = "index.toml"
hash-format = "sha256"
hash = "{index_hash}"

[versions]
minecraft = "{pack_meta['minecraft']}"
forge = "{pack_meta['loader_version']}"
"""
    (PACK / "pack.toml").write_text(pack_toml, encoding="utf-8")

    # mrpack index (default files only)
    mr_files = []
    for rec in default:
        dest = f"{folder_for(rec['type'])}/{rec['filename']}"
        env = {"client": "required", "server": "required"}
        if rec["type"] in ("resourcepack", "shader") or rec.get("role") == "visual" and rec["type"] != "mod":
            env = {"client": "required", "server": "unsupported"}
        if rec["type"] == "mod" and rec.get("role") in ("visual", "performance") and rec["slug"] in {
            "embeddium",
            "oculus",
            "entitytexturefeatures",
            "entity-model-features",
        }:
            # still needed on dedicated? embeddium/oculus client
            if rec["slug"] in {"embeddium", "oculus", "entitytexturefeatures", "entity-model-features"}:
                env = {"client": "required", "server": "unsupported"}
        mr_files.append(
            {
                "path": dest,
                "hashes": {"sha1": rec["sha1"], "sha512": rec["sha512"]},
                "downloads": [rec["url"]],
                "fileSize": rec["size"],
                "env": env,
            }
        )

    mr_index = {
        "formatVersion": 1,
        "game": "minecraft",
        "versionId": pack_meta["version"],
        "name": pack_meta["name"],
        "summary": pack_meta["description"],
        "files": mr_files,
        "dependencies": {
            "minecraft": pack_meta["minecraft"],
            "forge": pack_meta["loader_version"],
        },
    }
    (PACK / "modrinth.index.json").write_text(json.dumps(mr_index, indent=2) + "\n", encoding="utf-8")

    snapshot = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "minecraft": MC,
        "loader": LOADER,
        "loader_version": pack_meta["loader_version"],
        "default_count": len(default),
        "starter_count": len(starter),
        "resolved": resolved,
        "errors": errors,
        "manual_curseforge_only": catalog.get("manual_curseforge_only", []),
        "conflicts": catalog.get("conflicts", []),
    }
    (PACK / "resolved.json").write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")

    # slim mods.json for humans / other tools
    slim = {
        "pack": pack_meta,
        "default": [
            {
                "slug": r["slug"],
                "title": r["title"],
                "type": r["type"],
                "tier": r["tier"],
                "role": r["role"],
                "modrinth_id": r["project_id"],
                "modrinth_url": r["modrinth_url"],
                "version": r["version_number"],
                "version_id": r["version_id"],
                "filename": r["filename"],
                "sha1": r["sha1"],
                "download": r["url"],
                "curseforge_slug": r.get("curseforge_slug"),
                "curseforge_id": r.get("curseforge_id"),
                "license": r.get("license"),
                "notes": r.get("notes"),
            }
            for r in default
        ],
        "listed_not_default": [
            {
                "slug": r["slug"],
                "title": r["title"],
                "type": r["type"],
                "tier": r["tier"],
                "modrinth_url": r["modrinth_url"],
                "version": r["version_number"],
                "curseforge_slug": r.get("curseforge_slug"),
                "curseforge_id": r.get("curseforge_id"),
                "notes": r.get("notes"),
            }
            for r in resolved
            if not r.get("include_in_default")
        ],
        "manual_curseforge_only": catalog.get("manual_curseforge_only", []),
        "conflicts": catalog.get("conflicts", []),
        "starter_slugs": [r["slug"] for r in starter],
    }
    (PACK / "mods.json").write_text(json.dumps(slim, indent=2) + "\n", encoding="utf-8")

    print(
        f"\nWrote {len(default)} default files, {len(resolved)} resolved, {len(errors)} errors",
        file=sys.stderr,
    )
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
