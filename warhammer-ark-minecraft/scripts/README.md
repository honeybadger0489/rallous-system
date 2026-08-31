# Pack scripts

```bash
# CurseForge-importable zip (PLAY.md is the player doc)
python3 scripts/build-cf-pack.py

# Older Modrinth pin refresh (0.1 prototype)
python3 scripts/generate-pack.py
./scripts/download-pack.sh --starter
```

`build-cf-pack.py` pins CurseForge `projectID`/`fileID` via CFWidget and bundles official Modrinth files only when CF has no usable 1.20.1 file. Output: `dist/rallous-warhammer-fantasy-0.2.0.zip`.
