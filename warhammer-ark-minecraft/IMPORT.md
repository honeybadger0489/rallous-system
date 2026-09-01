# How to import Rallous Frontier

All jars come from **Modrinth’s official CDN** (or CurseForge if you add Magistu’s Epic Knights). No third-party “mod sites.”

## A. Prism Launcher (best)

1. Install [Prism Launcher](https://prismlauncher.org/).
2. **Add Instance → Import** and choose `warhammer-ark-minecraft/pack/rallous-frontier-0.1.0.mrpack`.
3. If import of a metadata-only mrpack is picky, create a vanilla-style instance:
   - Minecraft **1.20.1**
   - Loader **Forge 47.4.0** (47.4.10 is fine)
   - Java **17**
   - Then **Edit → Mods → Download mods** and add each slug from `pack/mods.json` → `default`.
4. Copy resource packs / shader from the instance folders after download, or run the script below.
5. Settings → Java → max memory **8192 MiB** or more.

### packwiz (optional)

If you have [packwiz](https://packwiz.infra.link/) installed:

```bash
cd warhammer-ark-minecraft/pack
packwiz serve          # local HTTP pack, Prism can subscribe
# or
packwiz modrinth export
```

`pack.toml` + `index.toml` + `mods/*.pw.toml` are already generated.

## B. Modrinth App

Create a 1.20.1 Forge profile and import the `.mrpack`, or search each `slug` in `pack/mods.json`.

## C. CurseForge App

Use `curseforge_slug` / `curseforge_id` in `pack/mods.json`. Projects that exist only on CurseForge:

- **Epic Knights: Shields, Armor and Weapons** — slug `epic-knights-armor-and-weapons`, id `509041`

Do **not** add Hammercraft / Tacz40k / Sons of the Empire unless you have read `LEGAL-NOTES.md` and accept the IP risk. They are **not** in the default mrpack.

## D. Manual / CLI download

```bash
python3 warhammer-ark-minecraft/scripts/generate-pack.py   # refresh pins
./warhammer-ark-minecraft/scripts/download-pack.sh --starter
./warhammer-ark-minecraft/scripts/download-pack.sh           # full default set
```

Files land in `warhammer-ark-minecraft/downloads/{mods,resourcepacks,shaderpacks}/`. Copy them into your instance folders. Jars are gitignored.

`--starter` pulls a tiny set (JEI, Jade, Cloth Config, AppleSkin, Grimdark Sky, Gothic font, Complementary Unbound) so you can verify the pipeline without waiting on Fossils/Cataclysm.

## Resource pack order (top = highest priority)

1. Gothic RPG Font  
2. Grimdark Sky Pack  
3. Grimdark Battlepack  
4. Fresh Animations  
5. Faithful 32x  

Shader: **Complementary Unbound r5.8.1** via Oculus (Forge). Unbound is the darker profile; Reimagined is the brighter sibling.

## Server

Use the same Forge version. Omit client-only mods (Embeddium, Oculus, ETF, EMF, resource packs, shaders). Keep GeckoLib, Citadel, Curios, creature mods, LSO, Create, etc. on the server.
