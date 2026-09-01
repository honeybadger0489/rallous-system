# SERVER-SMOKE-0.3.11 — Forge dedicated boot

**Done: YES.** `Done (1.987s)!` and **no** `ModLoadingException`.

Date: 2026-09-01. Runtime: Java 17.0.20, Minecraft 1.20.1, Forge **47.4.10**. JVM `-Xms4G -Xmx6G`. Reused `/tmp/rallous-smoke-039` from the 0.3.10 smoke (existing world). ModernFix: dedicated server took 18.509s.

## Zip / pin

| Check | Result |
| --- | --- |
| Zip | `dist/rallous-warhammer-fantasy-0.3.11.zip` (24 819 594 bytes) |
| Manifest | `minecraft 1.20.1`, `forge-47.4.10`, version `0.3.11` |
| Server dir | `/tmp/rallous-smoke-039` (Forge 47.4.10 installer already present) |
| Refresh | Overwrote all 14 `rallous_*` / `rallous-old-world` / `rallous-recruits-bridge` jars from the 0.3.11 zip. CF libs unchanged. |

Changed vs 0.3.10 install: rebuilt `rallous-recruits-bridge` (12 754 B vs 11 563 B), plus director-pass / leftover-ID jars (`rallous_factions`, `rallous_warp_crash`, `rallous_winds`, `rallous_kit`, `rallous_session`, `rallous_contact`, `rallous_roaming`, `rallous_temple_herd`, `rallous_recruits_bind`).

## Dedicated park (same as 0.3.10)

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
[Server thread/INFO] [net.minecraft.server.dedicated.DedicatedServer/]: Done (1.987s)! For help, type "help"
[Server thread/WARN] [ModernFix/]: Dedicated server took 18.509 seconds to load
```

`ModLoadingException` count: **0**. No new missing CurseForge / FML deps.

Full log: [`SERVER-SMOKE-0.3.11.latest.log`](SERVER-SMOKE-0.3.11.latest.log)  
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

The four 0.3.9 `ServerFunctionLibrary` failures stay absent.

## Remaining non-function leftovers (same class as 0.3.10)

These are **not** FML crashes and **not** function parse errors. They do not fail this smoke.

| Kind | Detail |
| --- | --- |
| Third-party | SoTE recipe unknown items; Malum JEED / Farmers Delight optional recipes; Siege Machines advancement icons |
| Architectury | `fossil:*` / `fossil:triceratops` “not realized” registry warnings |

## Verdict

| | |
| --- | --- |
| **Boot / Done** | **yes** |
| Remaining function parse errors | **none** |
| `triceratops` / `necronomicon` / `crater_hq:load` / `give_book` as function fails | **do not appear** |
| New missing deps | **none** |
| New zip | **none at smoke time** (0.3.11 was the zip under test) |
