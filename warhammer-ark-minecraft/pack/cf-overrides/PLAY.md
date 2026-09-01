# Rallous Warhammer Fantasy — play this

**Player wiki:** [wiki/Home.md](wiki/Home.md) · two-hour test: [wiki/TEST.md](wiki/TEST.md)

**This is the only player doc.** Import **0.3.7** as a **new** CurseForge profile. Do not update 0.2.1 / 0.2.2 / 0.3.0 / 0.3.1 / 0.3.2 / 0.3.3 / 0.3.4 / 0.3.5 / 0.3.6.

**Download:**  
https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.7.zip

CurseForge app → Minecraft → Create Custom Profile → Import. Java **17**, ~8 GB RAM. **Minecraft 1.20.1 + Forge 47.4.10**. New world: Survival, Hard, cheats ON (smoke commands). Terralith default. Private pack — do not upload.

**Rallous Continuity is on in `options.txt` pack order** (last in the list). That overlay is lang only — Elector / Waaagh / Under-Empire / von Carstein / Dawi / herd / temple-city / Bloodbound — **not** the Fabric Continuity connected-textures mod. If a profile resets packs, move **Rallous Continuity** up again or Recruits still says Team 2.

**Quest book identity:** **The Warp-Crash** — Crash (crater, then ~1 hour village *or* fight) → Paths (help / betray / join / align-and-leave; each sets `rallous.path` and shifts **that** contact faction’s stance) → First Hour (Empire, Vampire Counts, Lizardmen, Beastmen, Greenskins, Dwarfs, Skaven, Khorne) → The Winds (no starter spellbook; Colleges / Ice / death / Blood). **The Host** is optional Recruits. **Temple and Herd** is the Fossils / Tameable Beasts chapter. Smoke is a side checklist. There is no Reikland tutorial court.

A new world is a **Warp-crash**. You wake in a blackstone / crying-obsidian crater. There is **no** Karl Franz war council. A named lord from a **real table faction** (not a mute vanilla village) is the nearest camp: palisade, banners, campfires, site props, the lord villager from the JSON template, two Recruits soldiers, and a stance line. A second player who joins this world crashes **somewhere else**.

**Honest remaining limits:**

- **Camps vs Recruits.** `rallous_factions` places thicker war-host pickets, names lords, and fires stance lines. `rallous_recruits_bind` copies that camp’s display name onto scores / storage and hands you a book. This zip **includes** `rallous-recruits-bridge-1.0.0.jar` (sibling Forge 1.20.1 / 47.4.10). That Java mod founds or renames your Recruits host to the crash-camp name after assign. Hire lists, pathfinding, and team AI stay the engine’s. If the bridge fails on boot, send `crash-*-fml.txt` and use **U** → Found a Banner as the fallback.
- **Session night** is vanilla pillagers / zombies **named as that race’s enemies**, not a Recruits battle and not a Total War city fight.
- Camps are war-host pickets (palisade + banners + lord + two soldiers), not Total War cities. First days cap about **16** sites; walking farther can place more from the remaining pool (about **40** total, never all 129 at once). Beastmen / Waaagh / Khorne / some Skaven are roaming-style camps, not pretty capitals.
- Client is **not** booted in CI. If it crashes, send `crash-*-fml.txt`.

---

## Authored vs borrowed

**We authored (in this zip’s overrides / LowCodeFML jars):**

- Warp-crash first join: crater, world spawn, per-player spawnpoint, wreckage chest, wreckage journal (`rallous_warp_crash` + Old World fallback). After `store_crater`, `rallous_crater_hq:mark` plants a later-DLC HQ hook.
- Friend-elsewhere scatter (and a solo demo function)
- Death: no bed → your crater; bed → bed
- Compiled faction map (`rallous_factions`): mix of major+minor camps from the 8 v1 races, lords from templates, crash contact + stance, path scores change that faction
- First-contact path stance (`rallous_diplomacy`) — FTB Paths and the factions tick both call `apply_path`
- One-night session (`rallous_session`): `/function rallous_session:start` / `:win` — one village or one fight in the contact lord’s voice
- Recruits bind (`rallous_recruits_bind`): scores + book + crash-camp name after assign. Plus `rallous-recruits-bridge-1.0.0.jar` to found / rename the Recruits host to that camp (`FactionEvents.createTeam(false, …)`).
- Race levy kit on first-contact greet (`rallous_kit`)
- Camp growth (`rallous_grow`) — help / trade / session and the 7×7 gains huts (Millénaire loop, not MineColonies)
- Warp-Crash FTB book (Crash / Paths / First Hour / The Winds / optional Host / Temple and Herd) + Smoke
- Recruits / OPAC / Vassal lang overlay (**Rallous Continuity**) and grim defaultconfigs
- Force functions: `/function rallous_old_world:force_roaming` and `/function rallous_old_world:lm_bm/summon`
- Sibling jars: `rallous_roaming`, `rallous_temple_herd`, `rallous_contact`, `rallous_factions`, `rallous_diplomacy`, `rallous_crater_hq`, `rallous_session`, `rallous_recruits_bind`, `rallous_winds`, `rallous_grow`, `rallous_kit`, `rallous-recruits-bridge`
- Strip of the 0.2.2 `summon_lords` first-join court

**We borrowed (engine):** Recruits, Iron’s Spells, Fossils and Archeology, Tameable Beasts, Epic Fight, Terralith, Towns and Towers, LSO, FTB Quests, Sons of the Empire kits, Faithful 32x, Grimdark Battlepack, Grimdark Sky, Gothic RPG Font, Complementary Unbound. **We did not sculpt Total War models.** Bodies stay Steve-like / villager.

**0.2.1 libraries stay** (76 CurseForge fileIDs). Continuity (connected textures, Fabric-leaning) stays **out** so the instance boots.

---

## Two-hour test

Do **[wiki/TEST.md](wiki/TEST.md)** (copied into the instance folder as `wiki/TEST.md`). The grave-book list below is the short smoke.

## One-hour smoke

Quest book **`` ` ``** (grave). Chapter **Warp-crash Smoke** ticks the same list.

1. **Crash** — Look down. Bowl of blackstone / crying obsidian, campfire, wreckage chest. No six named lords. Title says Warp-crash. Forge 47.4.10. If it dies on boot, send `crash-*-fml.txt`.
2. **Named lord + stance** — Walk to the nearest bannered camp. A **named lord from a real faction** (Elector, High King, Beastlord, …) speaks a **stance** (blade gift, prove-yourself, brief raid, or daemon accusation). Not a mute village tagged “Faction Contact”. Chat should name the camp (Reikland, Clan Mors, …), never Team 2.
3. **Session start / win** — Cheats ON, stand at that camp: `/function rallous_session:start`. The lord speaks; a short wave or the camp raid begins. Clear it, or `/function rallous_session:win`. Night + walking to **that** camp can also auto-start once.
4. **Force roaming** — `/function rallous_old_world:force_roaming` spawns a Waaagh scout, a Beastmen herd, and a Khorne pack near you.
5. **Enable Rallous Continuity** — Options → Resource Packs → move **Rallous Continuity** up. Hire / inspect Recruits: **Levy** / **Elector** / **Waaagh** / **Under-Empire**, not “Recruit” / Team 2. That overlay is lang only.

Also worth a pass if you have time: second player (or `/function rallous_old_world:crash/demo_friend_elsewhere`) crashes elsewhere; wreckage chest has bread / leather / stone and **no** Iron’s spellbook; die with no bed → your crater; bed → bed.

---

## Keys

| Search | What |
| --- | --- |
| Epic Fight / `V` | Melee stance |
| Recruit / Faction / `U` | Found a Banner + Diplomacy (after you walk to a camp) |
| Host Command / `R` (Recruits) | Levy orders — not Iron’s wheel until later |
| Parties / OPAC | Warband land |
| Quests / `` ` `` | Warp-Crash + Smoke |
| World map / `M` | Towns |
| Spell wheel / `R` (Iron’s) | **Later**, not the crater |

Useful (cheats ON):

```
/function rallous_old_world:force_roaming
/function rallous_old_world:lm_bm/summon
/function rallous_old_world:crash/demo_friend_elsewhere
/function rallous_old_world:crash/return_crater
/function rallous_factions:debug/force_contact
/function rallous_session:start
/function rallous_session:win
/function rallous_recruits_bind:on_contact
/function rallous_winds:hint
/function rallous_grow:on_session
/function rallous_kit:on_greet
```

**The Winds (first hour):** no spellbook in the crater. Walk to a bannered camp, read the named lectern, take the letter. Camp barrels rarely hold Iron’s common ink. Dungeon and library chests already hide Iron’s ink and scrolls. Inscribe later. Spell wheel **R** waits. `/function rallous_winds:hint` restates this.

`/function rallous_old_world:summon_lords` is a refuse line. It does **not** rebuild the 0.2.2 court.

Forge must be **1.20.1 / 47.4.10**. Sons of the Empire and grim packs live in the zip `overrides/`.
