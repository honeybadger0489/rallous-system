# Factions

Eight races. Compiled from JSON, not hardcoded names. You meet a **named lord** at a **war-host picket**: palisade, banners, campfires, site props, two Recruits soldiers, a stance line.

Not Total War cities. Beastmen / Waaagh / Khorne / some Skaven are roaming-style camps, not pretty capitals.

## The eight

| Race | Settlement | Warp-stranger stance | Tames | Majors / minors |
| --- | --- | --- | --- | --- |
| **The Empire** | Settled cities | Help with a blade | Low | 5 / 9 |
| **Vampire Counts** | Keeps, crypt-towns | Prove yourself | Low | 5 / 9 |
| **Lizardmen** | Temple-cities | Daemon-suspicion | **High** | 7 / 7 |
| **Beastmen** | Roaming (no capitals) | Hostile | **Corrupt** | 4 / 8 |
| **Greenskins** | Mixed (crag or roam) | Prove yourself | Low | 6 / 27 |
| **Dwarfs** | Holds | Daemon-suspicion | Low | 6 / 10 |
| **Skaven** | Hidden under-capitals | Prove yourself | Low | 6 / 13 |
| **Khorne** | Roaming brass camps | Hostile | Low | 3 / 4 |

**129** factions in the pool (42 major / 87 minor). You will not see them all.

## Majors and minors

Worldgen mixes **majors and minors** of a race. Once every `tier: major` of that race is placed, further rolls for that race are **minor-only**.

Examples you might actually crash next to: Reikland, Clan Mors, Karaz-a-Karak, Hexoatl, Warherd of the One-Eye, Grimgor’s ’Ardboyz, Sylvania, Exiles of Khorne.

## Stances (first meet)

The race `warp_stranger_stance` plus the lord’s offer (`help` / `recruit` / `tribute` / `war` / `prove`) is the first-meet verb.

| Stance | What you hear / get |
| --- | --- |
| **Help with a blade** | Gift sword. They will use you. |
| **Prove yourself** | Last an hour in their fight or their village. |
| **Hostile** | Raid. You are meat or a scalp. |
| **Daemon-suspicion** | They will not name you clean until you prove it. |

Path quests later shift **that contact camp** only. See [Diplomacy](Diplomacy.md).

## 16 / 40 camps

- **First days:** about **16** sites.
- **Walk farther:** more from the remaining pool, cap about **40**.
- Never all 129 at once.

Bind chat names the camp (Reikland, Clan Mors, …). **U** may still say Team 2 if the bridge misses — **U** → Found a Banner and type that chat name. Continuity is lang only; it does not rename a host. See [Recruits](Recruits.md).
