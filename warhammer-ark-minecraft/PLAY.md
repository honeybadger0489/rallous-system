# Rallous Warhammer Fantasy — play this

**This is the only player doc.** Import **0.3.0** as a **new** CurseForge profile. Do not update 0.2.1 / 0.2.2.

**Download:**  
https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.0.zip

CurseForge app → Minecraft → Create Custom Profile → Import. Java **17**, ~8 GB RAM. **Minecraft 1.20.1 + Forge 47.4.10**. New world: Survival, Hard, cheats ON (smoke commands). Terralith default. Private pack — do not upload.

**Quest book identity:** **The Warp-Crash** — Crash (crater, then ~1 hour village *or* fight) → Paths (help / betray / join / align-and-leave; each sets `rallous.path` for the datapack) → First Hour (Empire, Vampire Counts, Lizardmen, Beastmen, Greenskins, Dwarfs, Skaven, Khorne) → The Winds (no starter spellbook; Colleges / Ice / death / Blood). **The Host** is optional Recruits. Smoke is a side checklist. There is no Reikland tutorial court.

A new world is a **Warp-crash**. You wake in a blackstone / crying-obsidian crater. There is **no** Karl Franz war council. A second player who joins this world crashes **somewhere else**.

---

## Authored vs borrowed

**We authored (in this zip’s overrides / LowCodeFML jar):**

- Warp-crash first join: crater, world spawn, per-player spawnpoint, wreckage chest, wreckage journal
- Friend-elsewhere scatter (and a solo demo function)
- Death: no bed → your crater; bed → bed
- Warp-Crash FTB book (Crash / Paths / First Hour / The Winds / optional Host) + Smoke (the 10 checks below)
- Recruits / OPAC lang: Levy, Elector, Waaagh, Under-Empire (resource pack **Rallous Continuity** — a lang overlay, **not** the Continuity connected-textures mod)
- Force functions: `/function rallous_old_world:force_roaming` and `/function rallous_old_world:lm_bm/summon`
- Strip of the 0.2.2 `summon_lords` first-join court

**We borrowed (engine):** Recruits, Iron’s Spells, Fossils and Archeology, Tameable Beasts, Epic Fight, Terralith, Towns and Towers, LSO, FTB Quests, Sons of the Empire kits, Faithful 32x, Grimdark Battlepack, Grimdark Sky, Gothic RPG Font, Complementary Unbound. **We did not sculpt Total War models.** Bodies stay Steve-like / villager.

**0.2.1 libraries stay.** Continuity (connected textures, Fabric-leaning) stays **out** so the instance boots.

---

## One-hour smoke (the 10 verify points)

Quest book **`` ` ``** (grave). Chapter **Warp-crash Smoke** ticks the same list.

1. **Crater** — Look down. Bowl of blackstone / crying obsidian, campfire, wreckage chest. No six named lords. Title says Warp-crash.
2. **Friend elsewhere** — Second player joins and is hundreds of blocks away in their own crater. Solo: `/function rallous_old_world:crash/demo_friend_elsewhere` then `/function rallous_old_world:crash/return_crater`.
3. **Village / fight** — Map `M`. Walk a Towns-and-Towers / village. Fight on the road. Combat mode `V`.
4. **Faction words** — Hire or inspect Recruits. UI should say **Levy** / **Elector** / **Waaagh** / **Under-Empire**, not “Recruit”. Enable **Rallous Continuity** if it does not.
5. **No starter magic** — Inventory and crater chest: bread, leather, stone. **No** Iron’s spellbook. Magic is in the pack for later; you do not start as a mage.
6. **LM / BM dinos** — `/function rallous_old_world:lm_bm/summon`. Turtle/goat/ravager proxies always. A Fossils triceratops (“Stegadon”) appears if that entity id is in the jar.
7. **Force roaming** — `/function rallous_old_world:force_roaming` spawns a Waaagh scout, a Beastmen herd, and a Khorne pack near you.
8. **Death crater / bed** — Die with no bed → back to **your** crater. Place a bed, sleep, die → the bed.
9. **Boot** — Grim sky, gothic font, Unbound, thirst/temp widgets. Forge 47.4.10. If it crashes, send `crash-*-fml.txt`.
10. **This file** — You are reading it. There is no second player guide.

---

## Keys

| Search | What |
| --- | --- |
| Epic Fight / `V` | Melee stance |
| Recruit / Faction | Host + Elector banners (after you walk to a town) |
| Parties / OPAC | Warband land |
| Quests / `` ` `` | Warp-Crash + Smoke |
| World map / `M` | Towns |
| Spell wheel / `R` | Iron’s — **later**, not the crater |

Useful (cheats ON):

```
/function rallous_old_world:force_roaming
/function rallous_old_world:lm_bm/summon
/function rallous_old_world:crash/demo_friend_elsewhere
/function rallous_old_world:crash/return_crater
```

`/function rallous_old_world:summon_lords` is a refuse line. It does **not** rebuild the 0.2.2 court.

Forge must be **1.20.1 / 47.4.10**. Sons of the Empire and grim packs live in the zip `overrides/`.
