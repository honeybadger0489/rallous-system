# HONESTY-0.3.15 — living field

SHIP_READY: **no**. Dedicated-server smoke on 0.3.15 is recorded in `SERVER-SMOKE-0.3.15.md` when run. Client `wiki/TEST.md` was not run. CurseForge / GPU client boot is unverified.

**0.3.15 gameplay (not essays):**

| Point | What changed |
| --- | --- |
| Contact host | Named lord from the rolled template wears race plate (SoTE State Trooper on Empire). Two named Recruits stay. Plus `/recruits spawn recruitPatrol tiny` (same as roaming). Vanilla levy fallback if Recruits is missing. |
| Worldgen mix | Crash plants mixed-race pickets on inner (~96) and outer (~220) rings. Tick can still fill to 16 / explore to 40. After majors exhausted, minors only. |
| Recruits Team 2 | Bridge now syncs (`serverSideUpdateTeam` + broadcast) after `createTeam`, burns generic leadership, and joins an already-founded named host instead of failing “team exists”. Retry window ~90s, every 10 ticks. Still a try. |
| Diplomacy | Paths open after the crater, not after a prove hour. Clickable [Help] [Betray] [Join] [Leave] at greet. Flint the pad = burn welcome → that camp turns + Khorne. |
| Headless proof | `/function rallous_factions:debug/headless_proof` drives crash / rings / levy / greet / paths / roaming / death and prints entity counts. |

Still true: camps are 7×7 pickets, not TW cities. Survival is LSO + Fossils / Tameable Beasts, not Ark. Recruits **U** may still say Team 2. Client TEST remains the success line.
