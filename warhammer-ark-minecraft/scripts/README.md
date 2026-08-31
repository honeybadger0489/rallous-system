# Pack scripts

```bash
# First-contact FTB book + rallous_contact scores/advancements + Continuity lang
python3 scripts/author_contact.py

# Warp-crash overlay + sibling ingest + zip (does not re-resolve fileIDs)
python3 scripts/compile_factions.py
python3 scripts/integrate-overrides.py --version 0.3.3

# Author Old World content into cf-overrides/ (then applies Warp-crash; never ships the court)
python3 scripts/author_old_world.py

# Rebuild zip from the existing CurseForge manifest + current overrides.
python3 scripts/pack-zip.py --version 0.3.3
# or: python3 scripts/build-cf-pack.py --pack-only

# Full CurseForge pin refresh (the dependency agent owns fileIDs — do not race it)
python3 scripts/build-cf-pack.py

# Older Modrinth pin refresh (0.1 prototype)
python3 scripts/generate-pack.py
./scripts/download-pack.sh --starter
```

`build-cf-pack.py` pins CurseForge `projectID`/`fileID` via CFWidget and bundles official Modrinth files only when CF has no usable 1.20.1 file. Content/glue updates should use `integrate-overrides.py` / `pack-zip.py`. `compile_factions.py` turns `content/factions/*.json` into the `rallous_factions` datapack (called by integrate). Output: `dist/rallous-warhammer-fantasy-0.3.3.zip`.
