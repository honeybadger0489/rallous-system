# Dedicated smoke — 0.3.17

**Client:** not this report. CurseForge / GPU / `wiki/TEST.md` unrun. **SHIP_READY no.**

**Date:** 2026-09-01  
**Host:** Cloud Agent, Java 17, Forge 1.20.1-47.4.16 installer / 47.4.10 pack  
**Zip:** `rallous-warhammer-fantasy-0.3.17.zip` (24 848 124 bytes)  
**Raw:** https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.17.zip  
**Run dir:** `/tmp/rallous-smoke-039` (fresh world deleted before boot — **not** a stone pad)

Client-only parked: ETF, EMF, Oculus, Embeddium, AppleSkin, Controlling, MouseTweaks, EntityCulling.

## Boot

- `Done (29.576s)! For help, type "help"`
- Puzzles Lib: **Loading 86 mods**
- `Failed to load function`: **0**
- `ModLoadingException`: **0**

Console functions (RCON timed out on the first pass; tmux stdin to `nogui`).

## Fresh-world mix on real terrain (not the stone pad)

`execute positioned 0 80 0` → `gen/boot` + `place_near` + `place_rings`. No `fill` stone. Spawn overworld land.

**`[rallous.mix] OK eight races on this fresh field`** (twice — immediate + scheduled count).

| Race | Lords seen |
|---|---|
| Empire | Balthasar Gelt, Elspeth von Draken |
| Vampire Counts | Gashnag, The Red Duke |
| Lizardmen | Adohi-Tehga |
| Beastmen | Taurox the Brass Bull |
| Greenskins | Grimgor Ironhide, Wurrzag |
| Dwarfs | Thorek Ironbrow, Belegar Ironhammer |
| Skaven | Septik, Kreepus |
| Khorne | Skarbrand, Skulltaker |

Dwarfs / Skaven / Khorne landed. 0.3.16 raw 120/220 rings had missed those three.

## Stance bite

`debug/prove_bite` at `0,80,0`:

- `[rallous.bite] OK hostile raid spawned`
- `[rallous.bite] OK help camp did not bite` (Balthasar Gelt / Empire)
- `[rallous.bite] OK help dummy not facing camp pillagers`
- `Bite Dummy was slain by Patrol` — dummy at the hostile camp died
- `Bloodreaver was slain by Zombified Piglin` — Khorne raid actually hit

Help-leaning did not instantly murder.

## Waaagh at the gate

`execute positioned 0 80 0 run function rallous_roaming:spawn/waaagh` (events/waaagh needs `@p`; dedicated has no player).

`[smoke.waaagh] host within 48 of a camp`  
`[smoke.waaagh] waaagh entities present`

## 12 crash slots

This world, after mix + raid + Waaagh: **`[rallous.slots] FAIL crater count != 12`** (twice). 0.3.16 on a quieter world was **OK 12**. Ring 3x3 forceloads are now dropped after probes finish (`gen/ring_unload`) so the 256 cap is not held. Slots were not re-proved on a clean empty world this run.

## Honesty

Dedicated boot + real-terrain 8/8 + hostile bite that kills + Waaagh at a camp. **Not** CurseForge first-person. No GPU. Recruits **U** untested. Client TEST remains the success line. Goal stays OPEN. SHIP_READY stays no.

Log: `content/SERVER-SMOKE-0.3.17.latest.log`
