#!/usr/bin/env python3
"""Rebuild the CurseForge zip from the existing manifest + current overrides.

Does not resolve or rewrite CurseForge fileIDs. Use this after content/glue
changes, or after another agent updates pack/curseforge/manifest.json.
"""

from __future__ import annotations

import argparse
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "pack"
DIST = ROOT / "dist"
OVERRIDES_SRC = PACK / "cf-overrides"
MANIFEST = PACK / "curseforge" / "manifest.json"
MODLIST = PACK / "curseforge" / "modlist.html"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", default="0.3.0", help="Pack version stamped into the zip manifest")
    args = parser.parse_args()

    if not MANIFEST.exists():
        raise SystemExit(f"Missing {MANIFEST}. Run build-cf-pack.py once, or wait for the pin agent.")

    manifest = json.loads(MANIFEST.read_text())
    manifest["version"] = args.version
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")

    if MODLIST.exists():
        text = MODLIST.read_text()
        for old in ("0.2.0", "0.2.1", "0.2.2", "0.3.0", "0.3.1", "0.3.2", "0.3.3"):
            text = text.replace(old, args.version)
        MODLIST.write_text(text)

    DIST.mkdir(parents=True, exist_ok=True)
    zip_path = DIST / f"rallous-warhammer-fantasy-{args.version}.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.write(MANIFEST, "manifest.json")
        if MODLIST.exists():
            zf.write(MODLIST, "modlist.html")
        if OVERRIDES_SRC.exists():
            for path in sorted(OVERRIDES_SRC.rglob("*")):
                if path.is_file():
                    zf.write(path, f"overrides/{path.relative_to(OVERRIDES_SRC).as_posix()}")
    print(f"wrote {zip_path} ({zip_path.stat().st_size} bytes) files={len(manifest.get('files') or [])}")


if __name__ == "__main__":
    main()
