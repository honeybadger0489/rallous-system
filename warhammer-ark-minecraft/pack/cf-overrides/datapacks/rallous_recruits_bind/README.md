# rallous_recruits_bind

Minecraft **1.20.1** datapack (`pack_format` **15**). After Warp-crash assign, Recruits is the army of **the compiled camp you crashed next to**, not a generic “Team 2”.

This folder only. Zip agent may ingest it (jar **or** world datapack, not both). Do not rebuild the dist zip for this change.

## Honesty: Recruits has no create / name / hire / ally command API

Researched **Villager Recruits 1.20.1 1.15.x** (talhanation, Claim and Siege / Diplomacy):

| Surface | What it actually does |
| --- | --- |
| Wiki command screen (R) | GUI orders: Follow, Hold, Aggressive, Raid, **Team** (opens team menu). Not chat commands. |
| Team menu (U) | **Found a Banner**, inspect, Diplomacy Ally / Neutral / Enemy, claims. This is how a host is named. |
| Hire | Right-click a recruit → hire GUI. No `/recruits hire`. |
| `/recruits spawn recruitPatrol <tiny\|small\|medium\|large\|huge\|caravan>` | Admin (op 2). Spawns a **generic** patrol, not the crash-camp faction. |
| `/recruits admin factionManager` | get/set NPC count, get/set leader, **delete**. **No create.** Looks up `RecruitsFactionManager` by existing team id. |
| `/recruits admin diplomacyManager setRelations <A> <B> Ally\|Neutral\|Enemy` | Admin (op 2). Requires **two Recruits banners that already exist**. Cannot found the crash-camp host. |
| `/recruits admin unitsManager` / `claimManager` / `nobleVillagerManager` / `debugManager spawnFromEgg` | Admin bookkeeping. Not first-contact bind. |
| Vanilla `/team add` | Recruits **warns this names hosts Team 1 / Team 2 and breaks banners** (`chat.recruits.team_creation.warnVanillaCommand`). Continuity and `recruits-server.toml` forbid it. A scoreboard team is **not** a Recruits faction (`getFactionByStringID` returns null). |

Sources (2026-08-31): [Villager Recruits Wiki](https://github.com/talhanation/wiki/wiki/Villager-Recruits-Wiki), `talhanation/recruits` `RecruitsAdminCommands.java` + `PatrolSpawnCommand.java`, Modrinth 1.13.0 diplomacy changelog, Continuity `assets/recruits/lang/en_us.json`.

**No new Java mod.** There is no datapack-only trick that writes `RecruitsFaction` saved data. The strongest bridge without that is **scores + storage + book + lang**.

## Mechanical (this datapack does it)

`/function rallous_recruits_bind:on_contact` — hooked after `rallous_factions:contact/assign`.

1. Reads the nearest `rallous.camp` / `rallous_contact` marker: `rallous.fac.id`, `rallous.fac.race`, `rallous.fac.stance`.
2. Copies onto the player: `rallous.rec.id`, `rallous.rec.race`, `rallous.rec.stance`, `rallous.contact_id`.
3. Writes `storage rallous_recruits_bind:contact` `{id,name,slug,lord,race,stance,rel}` from the compiled display name (Reikland, Clan Mors, … — **129 names**, same order as `compile_factions.py`).
4. Tags the player `rallous.rec.bound` and nearby Recruits entities `#rallous_recruits_bind:levy` as `rallous.rec.host`.
5. Gives a written book **once** (`rallous.rec.book`) and tellraws the crash-camp **display name**.
6. Dispatches `ally` or `war` from camp stance.

`/function rallous_recruits_bind:ally` — stance **help (1)** or **joined (5)**. Sets `rallous.rec.rel` 1, tags `rallous.rec.ally`.

`/function rallous_recruits_bind:war` — stance **hostile (3)** or **war (6)**. Sets `rallous.rec.rel` 2, tags `rallous.rec.war`.

Prove (2) and daemon-suspicion (4) bind the **name** only; they do not set Ally or Enemy scores.

Path hooks (compile_factions): `help_camp` → `ally` only if camp stance is now help (1) or joined (5); `join_camp` → `ally`; `betray_camp` → `war`.

## Open this GUI (Recruits will not move without it)

**Found / name the banner**

`Options → Controls → Hosts of the Old World → Open Elector / Waaagh / Under-Empire Screen` (default **U**, Continuity `key.recruits.team_screen_key`) → **Found a Banner**. Type the crash-camp name from chat. Dye a cloth banner first.

**Ally / Enemy**

Same U screen → **Diplomacy** → **Ally** or **Enemy**.

**Hire**

Right-click a Levy → **Levy for**.

**Orders**

`Options → Controls → Hosts of the Old World → Open Host Command` (default **R**, `key.recruits.command_screen_key`).

## Scores Recruits configs can read

Recruits’ own toml does **not** subscribe to scoreboards. These are the ids a later Recruits addon, KubeJS, or datapack should read:

| Objective | Meaning |
| --- | --- |
| `rallous.rec.id` | Compiled `rallous.fac.id` of the crash camp (1–129) |
| `rallous.rec.race` | 1 empire … 8 khorne |
| `rallous.rec.stance` | Camp `rallous.fac.stance` |
| `rallous.rec.rel` | 0 unbound / 1 ally / 2 war |
| `rallous.contact_id` | Same id (factions pack) |

`storage rallous_recruits_bind:contact.name` is the display string to type in **Found a Banner**.

Lang: `Rallous Continuity` `assets/rallous_recruits_bind/lang/en_us.json` (tellraw fallbacks still print if the pack is off).

Smoke: stand next to a `rallous.camp` marker, `/function rallous_recruits_bind:on_contact`. Chat must say **Reikland** (or whichever camp), never Team 2.
