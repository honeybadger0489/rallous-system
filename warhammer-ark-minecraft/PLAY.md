# Rallous Warhammer Fantasy — play this

**This is the only player doc.** Import **0.3.4** as a **new** CurseForge profile. Do not update 0.2.1 / 0.2.2 / 0.3.0 / 0.3.1 / 0.3.2 / 0.3.3.

**Download:**  
https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.4.zip

CurseForge app → Minecraft → Create Custom Profile → Import. Java **17**, ~8 GB RAM. **Minecraft 1.20.1 + Forge 47.4.10**. New world: Survival, Hard, cheats ON (smoke commands). Terralith default. Private pack — do not upload. **Enable resource pack Rallous Continuity** (Options → Resource Packs) so Recruits / OPAC / Vassal UI says Elector / Waaagh / Under-Empire / von Carstein / Dawi / herd / temple-city / Bloodbound, not Team 2.

**Quest book identity:** **The Warp-Crash** — Crash (crater, then ~1 hour village *or* fight) → Paths (help / betray / join / align-and-leave; each sets `rallous.path` and shifts **that** contact faction’s stance) → First Hour (Empire, Vampire Counts, Lizardmen, Beastmen, Greenskins, Dwarfs, Skaven, Khorne) → The Winds (no starter spellbook; Colleges / Ice / death / Blood). **The Host** is optional Recruits. **Temple and Herd** is the Fossils / Tameable Beasts chapter. Smoke is a side checklist. There is no Reikland tutorial court.

A new world is a **Warp-crash**. You wake in a blackstone / crying-obsidian crater. There is **no** Karl Franz war council. A named lord from a **real table faction** (not a mute vanilla village) is the nearest camp: banner, lord villager from the JSON template, and a stance line. A second player who joins this world crashes **somewhere else**.

**Honest — living map vs Recruits:** `overrides/content/factions/*.json` is compiled at zip-build into `rallous_factions` (folder + jar). That pack **does** place camps, pick majors then minors, name lords, and fire `help_with_blade` / `prove_yourself` / `hostile` / `daemon_suspicion`. Recruits AI is **still not driven by that JSON** — hire lists, pathfinding, and team diplomacy stay the engine’s. Camps are the living map (banner + lord pickets), not Total War cities. First days cap about **16** sites so the world stays playable; walking farther can place more from the remaining pool (about **40** total, never all 129 at once). Beastmen / Waaagh / Khorne / some Skaven are roaming-style camps, not pretty capitals.

---

## Authored vs borrowed

**We authored (in this zip’s overrides / LowCodeFML jars):**

- Warp-crash first join: crater, world spawn, per-player spawnpoint, wreckage chest, wreckage journal (`rallous_warp_crash` + Old World fallback)
- Friend-elsewhere scatter (and a solo demo function)
- Death: no bed → your crater; bed → bed
- Compiled faction map (`rallous_factions`): mix of major+minor camps from the 8 v1 races, lords from templates, crash contact + stance, path scores change that faction
- Warp-Crash FTB book (Crash / Paths / First Hour / The Winds / optional Host / Temple and Herd) + Smoke (the 10 checks below)
- Recruits / OPAC / Vassal lang: Levy, Elector, Waaagh, Under-Empire, von Carstein, Dawi, herd, temple-city, Bloodbound (resource pack **Rallous Continuity** — a lang overlay, **not** the Continuity connected-textures mod). Enable it for banner names.
- Recruits / Vassal / OPAC defaultconfigs (grim host caps, tribute, warband-land note)
- First-contact path stance (`rallous_diplomacy`) and crater HQ hook (`rallous_crater_hq`)
- Force functions: `/function rallous_old_world:force_roaming` and `/function rallous_old_world:lm_bm/summon`
- Sibling jars: `rallous_roaming`, `rallous_temple_herd`, `rallous_contact`, `rallous_factions`, `rallous_diplomacy`, `rallous_crater_hq`
- Strip of the 0.2.2 `summon_lords` first-join court

**We borrowed (engine):** Recruits, Iron’s Spells, Fossils and Archeology, Tameable Beasts, Epic Fight, Terralith, Towns and Towers, LSO, FTB Quests, Sons of the Empire kits, Faithful 32x, Grimdark Battlepack, Grimdark Sky, Gothic RPG Font, Complementary Unbound. **We did not sculpt Total War models.** Bodies stay Steve-like / villager.

**0.2.1 libraries stay.** Continuity (connected textures, Fabric-leaning) stays **out** so the instance boots.

---

## One-hour smoke (the 10 verify points)

Quest book **`` ` ``** (grave). Chapter **Warp-crash Smoke** ticks the same list.

1. **Crater + reacting faction** — Look down. Bowl of blackstone / crying obsidian, campfire, wreckage chest. No six named lords. Title says Warp-crash. Walk toward the nearest bannered camp: a **named lord from a real faction** (Elector, High King, Beastlord, …) speaks a **stance** (blade gift, prove-yourself, brief raid, or daemon accusation). Not a mute village tagged “Faction Contact”.
2. **Friend elsewhere** — Second player joins and is hundreds of blocks away in their own crater. Solo: `/function rallous_old_world:crash/demo_friend_elsewhere` then `/function rallous_old_world:crash/return_crater`.
3. **Village / fight** — Map `M`. Walk a Towns-and-Towers / village **or** last an hour at the contact camp’s fight. Combat mode `V`.
4. **Faction words** — Hire or inspect Recruits. UI should say **Levy** / **Elector** / **Waaagh** / **Under-Empire**, not “Recruit”. Enable **Rallous Continuity** if it does not. That overlay is lang only. The **compiled camps** are the living faction map; Recruits hire lists are still the engine’s teams.
5. **No starter magic** — Inventory and crater chest: bread, leather, stone. **No** Iron’s spellbook. Magic is in the pack for later; you do not start as a mage.
6. **LM / BM dinos** — `/function rallous_old_world:lm_bm/summon`. Turtle/goat/ravager proxies always. A Fossils triceratops (“Stegadon”) appears if that entity id is in the jar.
7. **Force roaming** — `/function rallous_old_world:force_roaming` spawns a Waaagh scout, a Beastmen herd, and a Khorne pack near you. Mid-play, walking far from placed camps can also drop another compiled camp from the remaining pool.
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
/function rallous_factions:debug/force_contact
```

`/function rallous_old_world:summon_lords` is a refuse line. It does **not** rebuild the 0.2.2 court.

Forge must be **1.20.1 / 47.4.10**. Sons of the Empire and grim packs live in the zip `overrides/`.
