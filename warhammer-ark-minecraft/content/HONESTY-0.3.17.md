# HONESTY-0.3.17 — real-terrain mix + stance bite

SHIP_READY: **no**. Dedicated-server smoke **passed boot on 0.3.17** — `Done (29.576s)!`, 86 mods, 0 failed functions, **real-terrain mix 8/8 races** (not the stone pad), hostile raid spawned and killed a dummy, help camp did not bite, Waaagh within 48 of a camp (`content/SERVER-SMOKE-0.3.17.md`). Client `wiki/TEST.md` was not run. CurseForge / GPU client boot is unverified. Goal stays OPEN.

**0.3.17 gameplay (not essays):**

| Point | What changed |
| --- | --- |
| Mix on real terrain | Ring probes stay at the crash. Each ring cell forceloads a 3x3 (72 chunks, under 256), then `spreadplayers` hunts ~120 / ~220 land. Ocean/unloaded falls inward. Rotation increments only when a camp lands. Forceloads drop after probes finish. Dedicated: eight races including Dwarfs / Skaven / Khorne. |
| Stance bites | Hostile (Skaven / Beastmen / Khorne, stance 3/6) spawn always-hostile raid mobs on approach and greet (`AngryAt` on piglins). Smoke: raid spawned; Bite Dummy slain by Patrol; Bloodreaver slain by Zombified Piglin. Help-leaning Empire did not bite. Daemon-suspicion still gets no free kit until a path. |
| Waaagh | Spawns at the nearest camp gate (12–28). Smoke: host within 48 of a camp. `events/waaagh` still needs a player (`@p`); force from console should `spawn/waaagh` at the camp. |

12-slot proof **failed** on this busy mix world (`crater count != 12`). It passed on **0.3.16**. Recruits **U** / Team 2 unchanged. Client TEST is the success line.
