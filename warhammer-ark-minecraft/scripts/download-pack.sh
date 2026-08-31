#!/usr/bin/env bash
# Download Rallous Frontier files from Modrinth CDN using official hashes.
# Usage:
#   ./scripts/download-pack.sh              # default pack (mods + resource packs + shader)
#   ./scripts/download-pack.sh --starter    # tiny verification set
#   ./scripts/download-pack.sh --list       # print planned files, no download
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PACK="$ROOT/pack"
DEST="$ROOT/downloads"
INDEX="$PACK/modrinth.index.json"
MODS_JSON="$PACK/mods.json"

if [[ ! -f "$INDEX" ]]; then
  echo "Missing $INDEX — run: python3 $ROOT/scripts/generate-pack.py" >&2
  exit 1
fi

MODE="default"
if [[ "${1:-}" == "--starter" ]]; then
  MODE="starter"
elif [[ "${1:-}" == "--list" ]]; then
  MODE="list"
elif [[ -n "${1:-}" ]]; then
  echo "Unknown argument: $1" >&2
  exit 2
fi

python3 - "$INDEX" "$MODS_JSON" "$DEST" "$MODE" << 'PY'
import hashlib, json, os, sys, urllib.request

index_path, mods_path, dest, mode = sys.argv[1:5]
index = json.loads(open(index_path).read())
mods = json.loads(open(mods_path).read())
starter = set(mods.get("starter_slugs") or [])
slug_by_filename = {e["filename"]: e["slug"] for e in mods.get("default", [])}

files = index["files"]
if mode == "starter":
    files = [f for f in files if slug_by_filename.get(os.path.basename(f["path"])) in starter]
    if not files:
        sys.exit("No starter files matched. Was generate-pack.py run?")

print(f"{len(files)} file(s) [{mode}]")
for f in files:
    print(f"  {f['path']}  {f.get('fileSize', 0)} bytes")

if mode == "list":
    sys.exit(0)

ua = "RallousFrontierPack/0.1 (github.com/honeybadger0489/rallous-system)"
ok = fail = 0
for f in files:
    rel = f["path"]
    out = os.path.join(dest, rel)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    url = f["downloads"][0]
    expected = (f.get("hashes") or {}).get("sha1")
    if os.path.isfile(out) and expected:
        h = hashlib.sha1(open(out, "rb").read()).hexdigest()
        if h == expected:
            print(f"SKIP {rel}")
            ok += 1
            continue
    print(f"GET  {rel}")
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = resp.read()
    except Exception as e:
        print(f"FAIL {rel}: {e}", file=sys.stderr)
        fail += 1
        continue
    if expected:
        h = hashlib.sha1(data).hexdigest()
        if h != expected:
            print(f"FAIL {rel}: sha1 {h} != {expected}", file=sys.stderr)
            fail += 1
            continue
    with open(out, "wb") as fh:
        fh.write(data)
    print(f"OK   {rel} ({len(data)} bytes)")
    ok += 1

open(os.path.join(dest, "last-download.log"), "w").write(
    f"mode={mode} ok={ok} fail={fail}\n"
)
print(f"Done ok={ok} fail={fail} -> {dest}")
sys.exit(1 if fail else 0)
PY
