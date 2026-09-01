# SERVER-SMOKE-0.3.9 — Forge dedicated boot

**Boot: YES.** `Done (35.871s)!` and **no** `ModLoadingException`. No 0.3.10 zip.

Date: 2026-09-01. Runtime: Java 17.0.20, Minecraft 1.20.1, Forge **47.4.10**. JVM `-Xms4G -Xmx6G`. World gen + load ~52s (ModernFix).

## Zip / pin

| Check | Result |
| --- | --- |
| Zip | `dist/rallous-warhammer-fantasy-0.3.9.zip` (24 820 513 bytes) |
| Manifest | `minecraft 1.20.1`, `forge-47.4.10`, version `0.3.9` |
| CF files | **76** fileIDs, identical to `pack/curseforge-resolved.json` |
| Of those 76 | 73 mods, 2 resource packs, 1 shader |
| Server skip | Grimdark Sky, Gothic RPG Font, Complementary Unbound (resource/shader) |

All 73 CF jars came from official `edge.forgecdn.net` (same fileIDs as the manifest). No piracy, no CF API 403 fallback needed. Override jars from the zip: 14 `rallous_*` / `rallous-old-world` / `rallous-recruits-bridge` + `sonsoftheempire-1.1.9`.

## Attempt 1 — ETF client mixin (not a missing lib)

Full pack mods including client visual jars. Died in mixin apply **before** FML common setup:

```
Attempted to load class net/minecraft/client/gui/screens/Screen for invalid dist DEDICATED_SERVER
...
ResourceLocation.handler$zmd000$etf$illegalPathOverride
```

That is Entity Texture Features 7.1 touching a client `Screen` on a dedicated server. **Not** a missing-dep / `ModLoadingException`. Client CurseForge import still wants ETF + EMF + Oculus + Embeddium. Dedicated smoke parked those client-only jars.

Log: [`SERVER-SMOKE-0.3.9.attempt1-etf.log`](SERVER-SMOKE-0.3.9.attempt1-etf.log)

Parked for attempt 2 (still in the zip for players):

- `entity_texture_features_1.20.1-forge-7.1.jar`
- `entity_model_features-3.2.4-1.20.1-forge.jar`
- `oculus-mc1.20.1-1.8.0.jar`
- `embeddium-0.3.31+mc1.20.1.jar`
- `appleskin-forge-mc1.20.1-2.5.1.jar`
- `Controlling-forge-1.20.1-12.0.2.jar`
- `MouseTweaks-forge-mc1.20.1-2.25.1.jar`
- `entityculling-forge-1.10.5-mc1.20.1.jar`

## Attempt 2 — success

Puzzles Lib: **Loading 86 mods** (Forge + MC + 73−8 CF + 15 overrides + jar-in-jar). All 14 Rallous LowCode/Java jars loaded, including `rallous_recruits_bridge 1.0.0` (`will found Recruits hosts after Warp-crash assign`).

```
[Server thread/INFO] [net.minecraft.server.dedicated.DedicatedServer/]: Done (35.871s)! For help, type "help"
[Server thread/WARN] [ModernFix/]: Dedicated server took 51.685 seconds to load
```

`ModLoadingException` count: **0**.

Full log: [`SERVER-SMOKE-0.3.9.latest.log`](SERVER-SMOKE-0.3.9.latest.log)  
Also at `/tmp/rallous-smoke-039/logs/latest.log` on the smoke host (server stopped after capture).

## Non-blocking datapack noise (server still reached Done)

These are **not** FML crashes. They do not fail this smoke. Honest leftovers:

| Kind | Detail |
| --- | --- |
| Function fail | `rallous_old_world:lm_bm/summon` — unknown entity `fossilsandarcheology:triceratops` (Fossils 9.3 id is `fossil:…`) |
| Function fail | `rallous_old_world:crash/strip_starter_magic` — unknown item `irons_spellbooks:necronomicon` |
| Function fail | `rallous_crater_hq:load` — parse error on `data set` (so `#minecraft:load` also cannot resolve `rallous_crater_hq:load`) |
| Function fail | `rallous_recruits_bind:give_book` — invalid `\n` in a quoted book string |
| Tag | `rallous_recruits_bind:levy` missing `recruits:commander` |
| Advancement | `rallous_temple_herd:lizardmen/loyal_beast` unknown `fossil:egg` |
| Third-party | SoTE recipe unknown items; Malum JEED / Farmers Delight optional recipes; Siege Machines advancement icons |

Core crash / contact / session / bind / winds / grow / kit paths were **not** in the “Failed to load function” list except the four rows above. `rallous_crater_hq:load` failing means the HQ scoreboard init on `#minecraft:load` did not register; `mark` is still called from warp-crash `store_crater` after land.

No pack rebuild. Those four functions are content bugs, not missing CurseForge libraries.

## Verdict

| | |
| --- | --- |
| **Boot** | **yes** |
| Log | `warhammer-ark-minecraft/content/SERVER-SMOKE-0.3.9.latest.log` |
| New zip | **none** (0.3.9 stays current; 0.3.10 not needed) |
