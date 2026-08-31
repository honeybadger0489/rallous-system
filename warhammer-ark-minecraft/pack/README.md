Packwiz + Modrinth metadata for **Rallous Frontier 0.1.0**.

- `catalog.json` — human-curated list (tiers, conflicts, CF ids)
- `mods.json` — resolved pins for the default set
- `modrinth.index.json` / `rallous-frontier-0.1.0.mrpack` — launcher import
- `pack.toml` + `index.toml` + `*.pw.toml` — [packwiz](https://packwiz.infra.link/)
- `resolved.json` — full API snapshot (hashes, dates)

Regenerate:

```bash
python3 ../scripts/generate-pack.py
```
