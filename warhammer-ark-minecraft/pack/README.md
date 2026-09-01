# Rallous Warhammer Fantasy

**Players: read [PLAY.md](../PLAY.md) only.** Import `../dist/rallous-warhammer-fantasy-0.3.6.zip` in the CurseForge app.

This `pack/` folder is the pin source:

- `curseforge/manifest.json` + `cf-overrides/` → the zip
- `curseforge-resolved.json` → projectID/fileID snapshot
- packwiz / `.mrpack` is the older 0.1 kitchen-sink prototype; do not import that if you want the directed Old World pack

Rebuild the zip:

```bash
python3 ../scripts/integrate-overrides.py --version 0.3.6
```
