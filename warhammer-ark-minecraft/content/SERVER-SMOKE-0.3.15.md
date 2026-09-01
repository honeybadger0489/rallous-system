# Dedicated smoke — 0.3.15

**Client:** not this report. CurseForge / GPU / `wiki/TEST.md` unrun. **SHIP_READY no.**

**Date:** 2026-09-01  
**Host:** Cloud Agent, Java 17.0.17, Forge 1.20.1-47.4.16  
**Zip:** `rallous-warhammer-fantasy-0.3.15.zip` (24 827 106 bytes after mix-ring rebuild)  
**Raw:** https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.15.zip  
**Run dir:** `/tmp/rallous-smoke-039` (same instance as 0.3.14, mods folder overwritten)

## What this boot is

Same 0.3.14 dedicated recipe (client-only parked, EULA true, Recruits + rallous-recruits-bridge present). Jar refresh mid-run: `rallous_factions-1.0.0.jar` 358 045 → 358 602 after `place_mix` (biome-prefer stacked Beastmen; mix now rotates eight races).

## Boot

- `Done (2.029s)! For help, type "help"`
- ModernFix: dedicated server took **18.29s**
- Puzzles Lib: **Loading 86 mods**
- rallous-recruits-bridge: `will found Recruits hosts after Warp-crash assign`
- `Failed to load function`: **0**
- `ModLoadingException`: **0**
- `has no associated item`: **0**

## Headless field proof (RCON, spawn chunks)

`/function rallous_factions:debug/headless_proof` + `place_rings` at `0,80,0` (loaded). Far `4000,80,4000` is not a valid unloaded-chunk test — entities there are not in the ticking set.

After mix-ring rebuild + rings:

| Check | Result |
|---|---|
| `rallous_camp` markers | **7** |
| named `rallous_lord` | **7** |
| Recruits `AbstractRecruitEntity` (`rallous_soldier`) | **42** (6 per camp: 2 named summons + 4 patrol) |
| `rallous_levy` (same soldiers after levy tag) | **42** |
| `rallous_host` | 0 (marker is killed after patrol) |
| `#placed` | 8 |
| `#camps` `#far` | 0 (rings use `#placed`, not `#camps`) |
| Path functions (`help`, `burn_welcome`, `waaagh`, `on_death`, `offer`) | executed; no `Unknown function` |

Lords at this forest spawn (mix after prefer leftover): Markus Wulfhart (Empire), Mazdamundi (Lizardmen), Taurox / Morghur / Malagor / Khazrak / Shadowgor (Beastmen). A **fresh world** should rotate eight races; this instance already had prefer-stacked Beastmen camps.

First RCON pass (pre-mix jar): 5 camps / 5 lords / 30 soldiers / 30 levy, all Beastmen+Lizardmen — that is why `place_mix` shipped.

## Honesty

This is dedicated boot + function/RCON counts. It is **not** CurseForge first-person: no GPU, no Recruits U team name seen, no 1-hour walk, no wiki/TEST.md. Goal stays OPEN. SHIP_READY stays no.

Log: `content/SERVER-SMOKE-0.3.15.latest.log`
