# HONESTY-0.3.16 — mix, greet, slots, beasts

SHIP_READY: **no**. Dedicated-server smoke **passed on 0.3.16** — `Done (28.890s)!`, 86 mods, 0 failed functions, pad mix **8/8 races**, 12 distinct crash slots, 3 temple + 3 herd beasts (`content/SERVER-SMOKE-0.3.16.md`). Client `wiki/TEST.md` was not run. CurseForge / GPU client boot is unverified.

**0.3.16 gameplay (not essays):**

| Point | What changed |
| --- | --- |
| Fresh mix | `$mix_only` skips biome prefer. `place_near` / `place_far` call `place_mix`. Pad on a **new** world: eight races (Empire through Khorne). Raw 120/220 rings can miss spots 6–8 if chunks are unloaded or ocean — vanilla forceload cap 256 chunks, not leftover Beastmen stacking. |
| First contact | Stance + greet copy differ by race. Empire / Greenskins `help_with_blade`; Dwarfs / Lizardmen / Vampire Counts `daemon_suspicion`; Skaven / Beastmen / Khorne `hostile`. Four clickable paths stay. Lead-in is not one shared sentence. |
| 12 crash slots | Scatter rings 4200 / 6800, 900-block crater reject. Probe: 12 distinct, pile=0. |
| LM/BM beasts | Temple / herd summons at those camps (Fossils + Tameable Beasts ids + vanilla proxy). Other races: no free dinos. Tame still global. |

Still true: camps are 7×7 pickets, not TW cities. Survival is LSO + Fossils / Tameable Beasts, not Ark. Recruits **U** may still say Team 2. Client TEST remains the success line.
