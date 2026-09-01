# SERVER-SMOKE-0.3.13 — Forge dedicated boot

**Done: YES.** `Done (1.884s)!` and **no** `ModLoadingException`.

Date: 2026-09-01. Runtime: Java 17.0.20, Minecraft 1.20.1, Forge **47.4.10**. JVM `-Xms4G -Xmx6G`. Reused `/tmp/rallous-smoke-039` after the 0.3.12 smoke. ModernFix: dedicated server took 18.027s.

This zip is the leftover-court cut after **0.3.12** passed (`Done (2.306s)`, 0 function parse fails). Same dedicated park (ETF / Oculus / Embeddium / EMF / AppleSkin / Controlling / Mouse Tweaks / EntityCulling).

## Zip / pin

| Check | Result |
| --- | --- |
| Zip | `dist/rallous-warhammer-fantasy-0.3.13.zip` (24 803 245 bytes) |
| Manifest | `minecraft 1.20.1`, `forge-47.4.10`, version `0.3.13`, **76** CF files |
| Refresh | Overwrote all 14 Rallous jars from the 0.3.13 zip. `rallous-old-world-1.0.0.jar` 22 077 → 16 296. |
| Leftover court | No CNPC `rallous_lords` letters. No `give_*_letter`, Kislev commission recipes, or `advancements/lords/*`. Faction camps still in `rallous_factions`. First-join court not restored. |

## Boot

Puzzles Lib: **Loading 86 mods**. `rallous_recruits_bridge 1.0.0` (`will found Recruits hosts after Warp-crash assign`).

```
[Server thread/INFO] [net.minecraft.server.dedicated.DedicatedServer/]: Done (1.884s)! For help, type "help"
[Server thread/WARN] [ModernFix/]: Dedicated server took 18.027 seconds to load
```

`ModLoadingException` count: **0**. `Failed to load function` count: **0**.

Full log: [`SERVER-SMOKE-0.3.13.latest.log`](SERVER-SMOKE-0.3.13.latest.log)

## Verdict

| | |
| --- | --- |
| **Boot / Done** | **yes** |
| Remaining function parse errors | **none** |
| New missing deps | **none** |
| New zip | **0.3.13** (leftover-court cut after 0.3.12 smoke) |
