# SERVER-SMOKE-0.3.10 — Forge dedicated boot

**Done: YES.** `Done (1.918s)!` and **no** `ModLoadingException`. The four 0.3.9 function parse failures are gone.

Date: 2026-09-01. Runtime: Java 17.0.20, Minecraft 1.20.1, Forge **47.4.10**. JVM `-Xms4G -Xmx6G`. Reused `/tmp/rallous-smoke-039` from the 0.3.9 smoke (existing world). ModernFix: dedicated server took 20.756s.

## Zip / pin

| Check | Result |
| --- | --- |
| Zip | `dist/rallous-warhammer-fantasy-0.3.10.zip` (24 825 254 bytes) |
| Manifest | `minecraft 1.20.1`, `forge-47.4.10`, version `0.3.10` |
| Server dir | `/tmp/rallous-smoke-039` (Forge 47.4.10 installer already present) |
| Refresh | Overwrote all 14 `rallous_*` / `rallous-old-world` / `rallous-recruits-bridge` jars from the 0.3.10 zip. CF libs unchanged. |

Changed vs 0.3.9 install: `rallous_crater_hq`, `rallous-old-world`, `rallous_recruits_bind`, `rallous_temple_herd` (thicker temple/herd NBTs). Other Rallous jars same size.

## Dedicated park (same as 0.3.9 attempt 2)

Still in the zip for clients. Not loaded on this dedicated smoke:

- `entity_texture_features_1.20.1-forge-7.1.jar`
- `entity_model_features-3.2.4-1.20.1-forge.jar`
- `oculus-mc1.20.1-1.8.0.jar`
- `embeddium-0.3.31+mc1.20.1.jar`
- `appleskin-forge-mc1.20.1-2.5.1.jar`
- `Controlling-forge-1.20.1-12.0.2.jar`
- `MouseTweaks-forge-mc1.20.1-2.25.1.jar`
- `entityculling-forge-1.10.5-mc1.20.1.jar`

## Boot

Puzzles Lib: **Loading 86 mods**. All 14 Rallous LowCode/Java jars loaded, including `rallous_recruits_bridge 1.0.0` (`will found Recruits hosts after Warp-crash assign`).

```
[Server thread/INFO] [net.minecraft.server.dedicated.DedicatedServer/]: Done (1.918s)! For help, type "help"
[Server thread/WARN] [ModernFix/]: Dedicated server took 20.756 seconds to load
```

`ModLoadingException` count: **0**. No new missing CurseForge / FML deps. **No 0.3.11 zip.**

Full log: [`SERVER-SMOKE-0.3.10.latest.log`](SERVER-SMOKE-0.3.10.latest.log)  
Also at `/tmp/rallous-smoke-039/logs/latest.log` on the smoke host (server stopped after capture).

## Function parse errors (grep `latest.log`)

| Grep | Count |
| --- | --- |
| `Failed to load function` | **0** |
| `fossilsandarcheology` | **0** |
| `necronomicon` | **0** |
| `crater_hq:load` | **0** |
| `give_book` | **0** |
| `triceratops` | 28 — Architectury `Registry entry listened … was not realized` for `fossil:triceratops` items/entity only. **Not** a function parse. |

The four 0.3.9 `ServerFunctionLibrary` failures are absent:

| 0.3.9 fail | 0.3.10 |
| --- | --- |
| `rallous_old_world:lm_bm/summon` (`fossilsandarcheology:triceratops`) | gone (`fossil:triceratops` in jar) |
| `rallous_old_world:crash/strip_starter_magic` (`irons_spellbooks:necronomicon`) | gone (that item id removed) |
| `rallous_crater_hq:load` (pathless `data set`) | gone (`data merge storage …`) |
| `rallous_recruits_bind:give_book` (bare `\n`) | gone (`\\n` in SNBT) |

## Remaining non-function leftovers (same class as 0.3.9)

These are **not** FML crashes and **not** function parse errors. They do not fail this smoke.

| Kind | Detail |
| --- | --- |
| Tag | `rallous_recruits_bind:levy` missing `recruits:commander` |
| Advancement | `rallous_temple_herd:lizardmen/loyal_beast` unknown `fossil:egg` |
| Third-party | SoTE recipe unknown items; Malum JEED / Farmers Delight optional recipes; Siege Machines advancement icons |
| Architectury | `fossil:*` / `fossil:triceratops` “not realized” registry warnings |

## Verdict

| | |
| --- | --- |
| **Boot / Done** | **yes** |
| Remaining function parse errors | **none** |
| `triceratops` / `necronomicon` / `crater_hq:load` / `give_book` as function fails | **do not appear** |
| New missing deps | **none** |
| New zip | **none** (0.3.10 stands; 0.3.11 not needed) |
