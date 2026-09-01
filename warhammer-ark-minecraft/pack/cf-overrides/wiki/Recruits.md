# Recruits (The Host)

Recruits is the army engine. We bind it to **the compiled camp you crashed next to**, not a generic Team 2.

## Honest banner

Villager Recruits still has **no chat create / hire / ally command**. Hire, orders, and Ally / Enemy live in Recruits’ GUIs. `/recruits admin factionManager` can get/set NPC count, get/set leader, and **delete** — that admin path still lacks a create *subcommand*.

**The crash-camp host is not automatic.** `rallous-recruits-bridge` **tries** Recruits’ own `FactionEvents.createTeam(false, …)` — the same server path as **U → Found a Banner** — after assign. If that sticks, chat / **U** say **Reikland** or **Clan Mors**. If the bridge misses (`rallous.rec.bridge_fail`, or **U** still says Team 2), Found a Banner yourself and type the name from chat.

| You want | What actually works |
| --- | --- |
| Found / name a host | Bridge **tries** the crash-camp name after assign. If **U** is still Team 2: **Found a Banner**. Dye a cloth banner first. |
| Ally / Enemy | Same **U** screen → Diplomacy. Needs two banners that already exist. |
| Hire | Right-click a Levy → hire GUI. No `/recruits hire`. |
| Orders | **R** (Host Command): Follow, Hold, Aggressive, Raid. |
| Admin patrol | `/recruits spawn recruitPatrol tiny` — generic, **not** the crash-camp faction. Roaming Waaagh / herd / Blood Host use this. |
| Vanilla `/team add` | Recruits **warns this names hosts Team 1 / Team 2 and breaks banners**. Do not. |

## What we do anyway

1. `rallous_recruits_bind` copies the crash-camp display name onto scores / storage / a book. Chat should say **Reikland** or **Clan Mors**.
2. `rallous-recruits-bridge` (Java) **tries** to found the Recruits host to that name. If you already have Team 1 / Team 2, it tries to burn that and found the compiled name. This was not clicked in a client on the 0.3.10 smoke. If **U** is still Team 2, Found a Banner.

Hire, orders, and Ally / Enemy still use Recruits’ GUIs. The datapack cannot write Recruits saved data by itself.

## If you still see Team 2

1. Walk to the contact camp. Chat must name it (bind tellraw).
2. **U** → inspect. If it is still Team 2, Found a Banner and type the name from chat.
3. Enable **Rallous Continuity** if the UI still says “Recruit” instead of Levy ([Install](Install.md)). That pack does **not** rename Team 2.
4. Do **not** `/team add`.

## Keys

| Key | Screen |
| --- | --- |
| **U** | Elector / Waaagh / Under-Empire (Found a Banner, Diplomacy) |
| **R** | Host Command (levy orders) — not Iron’s wheel until you have a book |

The Host chapter in the quest book is **optional**.
