# Dedicated smoke — 0.3.16

**Client:** not this report. CurseForge / GPU / `wiki/TEST.md` unrun. **SHIP_READY no.**

**Date:** 2026-09-01  
**Host:** Cloud Agent, Java 17, Forge 1.20.1-47.4.16  
**Zip:** `rallous-warhammer-fantasy-0.3.16.zip` (24 843 882 bytes)  
**Raw:** https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.16.zip  
**Run dir:** `/tmp/rallous-smoke-039` (fresh world — old smoke worlds deleted; **not** the Beastmen leftover)

Client-only parked: ETF, EMF, Oculus, Embeddium, AppleSkin, Controlling, MouseTweaks, EntityCulling.

## Boot

- `Done (28.890s)! For help, type "help"`
- Puzzles Lib: **Loading 86 mods**
- `Failed to load function`: **0**
- `ModLoadingException`: **0**

RCON `127.0.0.1:25575`. Piecewise functions (not one-tick `headless_proof`) to avoid watchdog.

## Fresh-world mix (not the leftover world)

**Ring pass at `0,80,0` (spawn chunks, no full ±220 forceload):** 5 camps / 5 lords, **5 unique races**, rotation 0–4:

| Lord | Race |
|---|---|
| Markus Wulfhart | Empire |
| Gashnag | Vampire Counts |
| Gor-Rok | Lizardmen |
| Gorebull Redhorn | Beastmen |
| Gorfang Rotgut | Greenskins |

Missing Dwarfs / Skaven / Khorne. `forceload add -256 -256 256 256` failed (`Too many chunks … maximum 256`). Outer mix spots sit outside loaded land / ocean `spreadplayers`. That is a **chunk/terrain cap**, not biome-prefer Beastmen stacking.

**Pad proof (stone fill `-80..80` y=70, eight `place_mix` at 40-block offsets, `#next_race` reset to 0):**

`[rallous.mix] OK eight races on this fresh field`  
`count: 8` camps.

| Lord | Race |
|---|---|
| Grand Theogonist Volkmar the Grim | empire |
| The Red Duke | vampire |
| Prophet of Sotek Tehenhauin | lizardmen |
| Great Bray-Shaman Malagor the Dark Omen | beastmen |
| Orc Warboss Azhag the Slaughterer | greenskins |
| King of Karak Eight Peaks Belegar Ironhammer | dwarfs |
| Deathmaster Deathmaster Snikch | skaven |
| Khorne’s Champion Skulltaker | khorne |

Rotation + `$mix_only` skip works when every spot resolves on land.

## 12 crash slots

`/function rallous_warp_crash:debug/prove_slots`  
`[rallous.slots] OK 12 distinct slots` — pile-up among probes **0**. Ring radii 4200 / 6800; reject `@e[tag=rallous.crater,distance=..900]`.

## LM/BM beasts

Pad mix (one LM camp + one BM camp): `temple_beast` **3**, `herd_beast` **3** (`fossil:triceratops` / `tameablebeasts:crested_gecko` / turtle; `fossil:smilodon` / `tameablebeasts:tameable_racoon` / goat). Other races: no dinos. Tame difficulty still global.

## Honesty

Dedicated boot + RCON counts. **Not** CurseForge first-person: no GPU, no Recruits **U** team name, no 1-hour walk, no `wiki/TEST.md`. Goal stays OPEN. SHIP_READY stays no.

Log: `content/SERVER-SMOKE-0.3.16.latest.log`
