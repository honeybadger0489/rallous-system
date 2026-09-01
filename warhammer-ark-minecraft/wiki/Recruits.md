# Recruits (The Host)

Recruits is the army engine. We bind it to **the compiled camp you crashed next to**, not a generic Team 2.

## Honest banner

**Villager Recruits has no create / name / hire / ally chat API.**

| You want | What actually works |
| --- | --- |
| Found / name a host | **U** → **Found a Banner**. Dye a cloth banner first. |
| Ally / Enemy | Same **U** screen → Diplomacy. Needs two banners that already exist. |
| Hire | Right-click a Levy → hire GUI. No `/recruits hire`. |
| Orders | **R** (Host Command): Follow, Hold, Aggressive, Raid. |
| Admin patrol | `/recruits spawn recruitPatrol …` — generic, **not** the crash-camp faction. |
| Vanilla `/team add` | Recruits **warns this names hosts Team 1 / Team 2 and breaks banners**. Do not. |

`/recruits admin factionManager` can get/set NPC count, get/set leader, **delete**. **No create.**

## What we do anyway

1. `rallous_recruits_bind` copies the crash-camp display name onto scores / storage / a book. Chat should say **Reikland** or **Clan Mors**.
2. `rallous-recruits-bridge` (Java) calls Recruits’ own Found-a-Banner server method so the **U** inspect should already show that name, not Team 2. If you already have Team 1 / Team 2, the bridge burns it and founds the compiled name.

Hire, orders, and Ally / Enemy still use Recruits’ GUIs. The datapack cannot write Recruits saved data by itself.

## If you still see Team 2

1. Enable **Rallous Continuity** (lang overlay — [Install](Install.md)).
2. Walk to the contact camp. Chat must name it.
3. **U** → inspect. If it is still Team 2, Found a Banner and type the name from chat.
4. Do **not** `/team add`.

## Keys

| Key | Screen |
| --- | --- |
| **U** | Elector / Waaagh / Under-Empire (Found a Banner, Diplomacy) |
| **R** | Host Command (levy orders) — not Iron’s wheel until you have a book |

The Host chapter in the quest book is **optional**.
