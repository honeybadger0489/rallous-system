# HONESTY-0.3.17 — real-terrain mix + stance bite

SHIP_READY: **no**. Client `wiki/TEST.md` was not run. CurseForge / GPU client boot is unverified. Goal stays OPEN.

**0.3.17 gameplay (not essays):**

| Point | What changed |
| --- | --- |
| Mix on real terrain | Ring probes stay at the crash (no teleport into unloaded cells). Each ring cell forceloads a 3x3 (72 chunks, under the 256 cap). `spreadplayers` hunts land on ~120 and ~220 rings; ocean/unloaded falls inward. Rotation increments only when a camp lands. |
| Stance bites | Hostile camps (Skaven / Beastmen / Khorne, stance 3/6) spawn always-hostile raid mobs on approach and on greet. Help-leaning camps do not. Daemon-suspicion still gets no free kit until a path. |
| Waaagh | Mid-session host spawns at the nearest camp gate (12–28), not a far unloaded roll. |

Dedicated smoke of this zip: see `content/SERVER-SMOKE-0.3.17.md` after the run. Pad-only 8/8 from 0.3.16 is **not** the proof line.
