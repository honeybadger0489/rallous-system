# Pack scripts

```bash
# Author Old World content into cf-overrides/ (quests, datapack jar, lang, configs)
python3 scripts/author_old_world.py

# Rebuild zip from the existing CurseForge manifest + current overrides.
# Does not re-resolve fileIDs.
python3 scripts/pack-zip.py --version 0.2.2
# or: python3 scripts/build-cf-pack.py --pack-only

# Full CurseForge pin refresh (the dependency agent owns fileIDs — do not race it)
python3 scripts/build-cf-pack.py

# Older Modrinth pin refresh (0.1 prototype)
python3 scripts/generate-pack.py
./scripts/download-pack.sh --starter
```

`build-cf-pack.py` pins CurseForge `projectID`/`fileID` via CFWidget and bundles official Modrinth files only when CF has no usable 1.20.1 file. Content/glue updates should use `pack-zip.py`. Output: `dist/rallous-warhammer-fantasy-0.2.2.zip`.
