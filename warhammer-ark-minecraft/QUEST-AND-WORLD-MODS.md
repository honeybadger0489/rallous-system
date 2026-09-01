# Quest and world mods — campaign stack (1.20.1 Forge)

Researched **2026-08-31**. Target (locked with pack research): **Minecraft 1.20.1 + Forge 47.4.x**. **Do not pirate. Do not commit jars.** Download only from CurseForge, Modrinth, or the author’s GitHub.

This file is the **campaign overlay** on top of `CURATED-PACK.md` / `RESEARCH.md` / `pack/mods.json`. v0.1 already covers grimdark survival, Fossils tames, Epic Fight, Open Parties and Claims, Terralith, Born in Chaos, Cataclysm. **Not in v0.1, needed for the RDR/TW campaign:** FTB Quests (or Heracles), CustomNPCs, Recruits + sieges, MineColonies (optional colony-win), CTOV, a journal map, Game Stages, Bountiful.

Fantasy campaign rule: **TaCZ stays out of the journal.** v0.1 may ship original gunpacks; the five-act Fantasy war does not quest-reward firearms. Melee + Iron’s Spells (gated) + warbeasts.

---

## 0. Closest existing “open world campaign” packs (steal structure, not content)

| Pack | Version | Why it matters | What not to copy |
| --- | --- | --- | --- |
| **DawnCraft – Echoes of Legends** | Forge 1.18.2 | Closest *RDR-like* Minecraft pack: a main quest you can ignore, explorer maps, waypoints, **reputation with villagers**, guild trading scrolls, open-world bosses. ~10.4M CurseForge downloads. | Souls-Korok-Ender-Dragon plot; 1.18.2-only custom quest mod; don’t clone assets |
| **Craft to Exile 2** | Forge 1.20.1 | **5-act campaign + 250–650 quests** via **FTB Quests**, overworld → other dimensions, village mayor/invaders. Proof that a 1.20.1 Forge pack can ship a real campaign. | Path of Exile loot treadmill as the *fantasy*; 40k-adjacent sci-fi; VR-specific gunk |
| **Valhelsia 6** | Forge 1.20.1 | Kitchen-sink *world* quality (biomes, Twilight/Undergarden/Deeper Darker). Use as a **region paint** reference, not a campaign. | No directed story — the opposite of this brief |
| **Medieval / kingdom packs** (e.g. Wars of Westeros-style Recruits packs, Valoria Cloaks and Crowns, King’sCraft, SiegeCraft-SMP) | Mostly 1.20.1 Forge | Recruits + Epic Knights + siege weapons = the **Total War-in-first-person** cluster | Licensed Westeros; no Warhammer clone either |
| **RPG Series** (Better Combat + Paladins/Archers/Wizards/Rogues) | Multi-loader | Clean Fantasy class kit that is **not** 40k | Don’t require all class mods; keep warband identity over class menus |
| **RLCraft** | Older Forge | Tone-not-copy: lethal world, tames, “you are not the apex.” | Dragons-everywhere pacing; don’t copy the pack |

**DawnCraft loop to steal:** spawn → talk to a guide → atlas + village map → reputation-gated trades → open world with a main objective that does not freeze the map. See DawnCraft wiki *Getting Started* and *Progression*.

**Craft to Exile 2 loop to steal:** Prologue chapter → Main Campaign Acts → Side Quests that never block the acts. FTB Quests is the journal.

---

## 1. Questing and dialogue

### Recommended spine

**FTB Quests (Forge) + FTB Library + FTB Teams + Architectury API + FTB XMod Compat**

- Team-shared chapters map 1:1 to campaign acts.
- Tasks: items, kills, advancements, locations, Game Stages.
- ExtraQuests / KubeJS (via XMod Compat) for custom checks (“province won”).
- Latest 1.20.1 Forge file observed: `ftb-quests-forge-2001.4.22.jar` (CurseForge, 12 May 2026).

Use **Game Stages** so Act II quests *exist in the book as locked* or hidden until the rumor stage. FTB XMod Compat wires Quests ↔ Game Stages and re-checks tasks when a stage changes.

### Alternatives

| Mod | Loader / 1.20.1 | Role |
| --- | --- | --- |
| **Odyssey Quests (Heracles)** | Forge + Fabric 1.20–1.20.1 | Tree quests in config JSON. Odysseus converts FTB/HQM packs. Pair with **Heracles for Blabber** and **Heracles for Villagers**. Good if the pack goes Fabric-heavy. Last Heracles 1.1.13 around Jun 2024 — **less maintained than FTB Quests in 2026**. |
| **Better Questing** | Forge 1.20.1 exists (`BetterQuesting-Forge-1.20.1-4.0.71.jar`, alpha, 5 Mar 2025) | Legacy 1.12 king. **Do not pick as primary** unless someone is porting an old pack. |
| **Hardcore Questing Mode** | No healthy 1.20.1 Modrinth hit | Skip. |
| **CustomNPCs-Unofficial** | Forge/Fabric 1.20.1; NeoForge 1.21.1 | **Authored characters, shops, quests, factions, scripting.** Permissioned port by Goodbird. This is how towns *talk*. Use for named captains, electors, dead princes. |
| **interactEntity** | Forge 1.20.1 | JSON dialogues/quests/reputation on *any* mob. Journal + HUD. Tiny download count — treat as experimental, excellent for “the miller is a villager with a real quest.” |
| **Blabber** | Fabric-first, 1.20.1 | Dialogue graphs. Use with Heracles-for-Blabber. |
| **Bountiful** | Forge/Fabric/NeoForge 1.20.1 | Inn bounty boards. Regional living-world filler. |

**Pack recipe:** FTB Quests = campaign journal. CustomNPCs = faces and voiced (or text) scenes. Bountiful = New World job boards. InteractEntity optional for cheap regional NPCs.

---

## 2. Factions, reputation, guilds, tribes

| Mod | 1.20.1 | Campaign job |
| --- | --- | --- |
| **FTB Teams** | CurseForge `ftb-teams-forge` | Tribe for quests + FTB Chunks. `/ftbteams create`. Shared campaign progress. |
| **Open Parties and Claims** | Forge/Fabric, 21M+ Modrinth dl | Parties + chunk claims. Hooks FTB Teams / Argonauts. Warband land without FTB Chunks. |
| **Cadmus (Odyssey Claims)** | Forge/Fabric 1.20.1 | Admin regions + player/guild claims. Pair with **Argonauts** so a guild shares claims (Terrarium docs). |
| **Argonauts / Odyssey Guilds** | Terrarium; listed as Heracles companion | Guild layer if not using FTB Teams. |
| **Villager Recruits** | Forge 1.20.1 (1.15.2, 29 Jun 2026) | **Vanilla teams GUI, diplomacy (ally/neutral/enemy), takeovers, 500 NPC cap.** This is faction-as-army. |
| **Faction Friction** | Forge 1.20.1 | Team → Colony → Country, wars, sieges of chunks, Xaero colors. Standalone (conflicts with FTB Teams). Pick **either** this **or** FTB+Recruits. |
| **Botz Guild Manager** | Forge 1.20.1 | Guild wars, missions, FTB Chunks/Quests optional hooks. Heavy server plugin-energy. |
| **CustomNPCs factions** | via Unofficial | NPC-side standing (DawnCraft analogue without DawnCraft’s custom mod). |
| **interactEntity** | Forge 1.20.1 | JSON reputation + factions. |

**Recommendation:** FTB Teams (meta tribe) + Recruits (field diplomacy + siege) + CustomNPC faction points (story standing). Skip Faction Friction if FTB is in the pack.

**DawnCraft reputation analogue:** profession quests → standing → cheaper trades → guild contracts. Implement with NPC faction points + FTB quest rewards, not a 1.18-only coremod.

---

## 3. Settlements, sieges, raids, invasions

| Mod | 1.20.1 | Campaign job |
| --- | --- | --- |
| **MineColonies** | Forge 1.20.1 (active snapshots through 2026 on CurseForge; Modrinth page is stale 1.18) | Player **colony**: builders, guards, university, **biome-typed raids** (Barbarian / Nordic / Mummy / Pirate / Amazon). Raid wiki: nights-only, doors/walls breakable, difficulty scales with colony. **Colony win** for a province. Needs Structurize, BlockUI, Domum Ornamentum, MultiPiston. |
| **Villager Recruits** | Forge 1.20.1 | Hire armies, group commands, **claim and siege**, scout companions, horses. Compat: Small Ships, Epic Knights, Siege Weapons. **Siege win** for a province. |
| **Siege Weapons** | Forge 1.20.1 | Catapults, ballistae, physics. The Total War artillery button. |
| **Kingdoms & Sieges** | Forge/Fabric/NeoForge 1.20.1 | Kingdom claim, hunger during siege, break the bell to abolish the claim, siege engines from manuscripts. Smaller project (~3k dl) — optional overlay. |
| **Guard Villagers** | Forge/NeoForge 1.20.1 | Towns that fight. Pair with CTOV. |
| **Illager Invasion** | 1.20.1 | Extra raid pressure in heartlands. |
| **MineColonies raids** | config | `averagenumberofnightsbetweenraids` default 14; biome picks raider culture. Use as **living-world invasions**, not only a colony minigame. |

**Performance note:** MineColonies + Recruits + Ice and Fire on one server is heavy. Cap recruit counts; don’t found five colonies in Act I.

**Millenaire:** not a 1.20.1 Forge spine. Skip.

---

## 4. Structures and cultures as you travel

Goal: crossing a river should feel like crossing a Total War province border.

| Mod | Job |
| --- | --- |
| **Terralith** / **Regions Unexplored** / **Biomes O' Plenty** / **Oh The Biomes We've Gone** | Biome belts = province paint. Pick **one** primary biome overhaul + optional compat. |
| **ChoiceTheorem's Overhauled Village (CTOV)** | 23 village variants + 14 pillager-outpost variants, biome-fit. Hamlets vs walled towns. Compat wiki with Terralith/BOP/Towns and Towers. **Heartland / Frost / Desert cultures.** |
| **Towns and Towers** | Extra village/outpost cultures; exclusive structures when biome mods are present (e.g. Mediterranean village). Warning: overlap if stacked blindly. |
| **Medieval Buildings** (+ End/Nether editions) | Castles, churches, manors — elector and chivalric silhouettes. |
| **When Dungeons Arise** (+ Seven Seas) | Large adventure structures as provincial dungeons. |
| **YUNG's Better Dungeons / Strongholds** | Catacombs, undead forts — Night Counties / Hold-Road. |
| **Integrated Dungeons and Structures (IDAS)** | Lore-heavy structures; optional Quark/Alex’s/Create integration. |
| **Structory** + **Structory: Towers** | Wilderness camps, towers — frontier clutter. |
| **Explorify** | Small world-flavour structures. |
| **Repurposed Structures (Forge)** | Vanilla structures remixed per biome. |
| **Dungeons Enhanced** | Extra dungeon variety. |
| **The Graveyard** | Night Counties architecture. Confirm the Forge 1.20.1 file (several forks exist). |
| **Born in Chaos** | Grimdark night roster + structures. Better Combat compatible. Act III–V spawn tables. |
| **Mowzie’s Mobs** | Regional bosses (jungle, plains, etc.) as optional provincial champions. |
| **Friends & Foes** | Extra village personalities (use CTOV compat pack). |

**Culture mapping (analogue → generation):**

- Heartland: CTOV plains/taiga villages, Guard Villagers, Medieval churches.
- Principalities: Towns and Towers hill/mediterranean, burned Structory camps, Recruits warlord forts.
- Night Counties: Graveyard + swampier swamps + IDAS haunted manors.
- Hold-Road: stone Medieval Buildings, YUNG strongholds, Hopo Better Mineshaft.
- Howling North: Terralith frozen/volcanic, Born in Chaos, no CTOV density (empty on purpose).

Use **Structure Essentials** or **StructureOverlapless** if the pack agent stacks more than three structure mods.

---

## 5. Map, journal, waypoints, fog-of-war analogues

| Mod | Fog / reveal | Campaign use |
| --- | --- | --- |
| **Antique Atlas 4** + **Surveyor** | Hand-drawn tiles; structures marked only after you see them; share via `/surveyor share` | Best *diegetic* campaign map. Hold a renamed book. **Require atlas in inventory** via config for RDR-journal feel. Forge needs Connector + Forgified Fabric API. |
| **Xaero’s Minimap + World Map** | Explored chunks only on world map | Best *utility* map; waypoints (B / U); fair-play edition for PvP. Overlay FTB claims. |
| **JourneyMap** | Real-time; waypoint groups; web map | Server ops / streamers. JourneyMap Teams for warbands. |
| **FTB Chunks** | Claim overlay; optional `ftbchunks_mapping` **Game Stage** to *deny* the map until a tutorial quest | True fog-of-war analogue: **no minimap until Act I “buy a chart.”** Needs FTB XMod Compat + Game Stages. |
| **Waystones** | Fast travel after discovery | Discover-on-foot; Xaero waystone compat. Do not quest-reward teleports in Act I. |
| **FTB Quests UI** | Journal | Chapter = act. Pinned quest = current main beat. |

**Recommended:** Antique Atlas 4 as the in-world object + Xaero (or FTB Chunks) for tactics. Don’t ship Atlas + JourneyMap + Xaero + FTB map together.

**DawnCraft precedent:** Antique Atlas + compass + village explorer map on spawn; `M` waypoint list.

---

## 6. RPG combat that feels Total War–era Fantasy (not 40k)

Avoid guns, power armor, chainswords, bolters, 41st-millennium energy weapons.

| Mod | Feel | Notes |
| --- | --- | --- |
| **Epic Fight** | Souls-like stamina, skills, entity movesets | **v0.1 default** (pack research). DawnCraft’s combat cousin. Datapack Recruits / Fossils weapons. |
| **Better Combat** | Minecraft Dungeons swings, dual wield, sweep | Highest raw compatibility (Simply Swords, RPG Series). **Do not stack with Epic Fight** in v0.1 — pack research flags a extra compat mod. Only switch if Recruits AI fights Epic Fight badly. |
| **Epic Knights: Shields, Armor and Weapons** + Addon | Sallet, poleaxe, longsword, pavise | The *look* of Empire/Bretonnia analogues. Recruits optional compat. |
| **Simply Swords** | Fantasy weapons | Fast content; v0.1 already has it. Datapack for Epic Fight swings. |
| **Immersive Armors** | Distinct culture kits | Assign sets to regions. |
| **Tetra** | Modular weapons | Blacksmith fantasy; pair with Better Combat (Tetratic is older — check 1.20.1). |
| **Iron’s Spells ’n Spellbooks** | Lore-friendly magic (not lasguns) | Colleges-of-magic analogue. Restrict spell schools by Game Stage if needed. Ice and Fire: Spellbooks exists. |
| **RPG Series** (Archers, Paladins & Priests, Wizards, Rogues & Warriors, Jewelry, Arsenal) | Classes | Optional. Warband > class menu. |
| **Mowzie’s Mobs** | Animated Fantasy bosses | Provincial champions. |

**Recommendation (aligned with v0.1):** Epic Fight + Epic Knights + Simply Swords + Iron’s Spells (gated). No Better Combat until someone owns the compat datapack.

**Tames (campaign-critical):**

- **Fossils and Archeology: Revival** — v0.1 default Ark loop (DNA → embryo → ride). Provincial warbeasts.
- **Alex’s Mobs** — regional fauna; several rideable/tameable.
- **Ice and Fire: Dragons** — optional later. Pack research: 1.20.1 still `2.1.13-beta-5` (2024-08-15). Don’t require a dragon for any main-act complete.

---

## 7. Glue mods

| Mod | Why |
| --- | --- |
| **Architectury API** | FTB stack |
| **Resourceful Lib** | Heracles / Cadmus / Terrarium |
| **KubeJS** | Province flags, custom quest checks (1.20.1 is supported on Modrinth in 2026) |
| **Game Stages** | Act unlocks, map unlock, magic schools |
| **FTB XMod Compat** | Quests/Chunks ↔ Stages, JEI, Waystones on map |
| **Serene Seasons** | Frost Marches hurt in winter |
| **Sophisticated Backpacks** | Warband logistics (don’t let it delete survival) |
| **Small Ships** | Corsair / river / High Elf quay travel |
| **Geckolib** | Mowzie’s etc. |

---

## 8. Suggested campaign overlay (on top of v0.1)

v0.1 already has Epic Fight, Simply Swords, Terralith, Alex’s Mobs, Fossils, Open Parties, Born in Chaos, LSO, Serene Seasons. Add:

1. FTB Library / Teams / Quests / XMod Compat (Architectury is already in the pack)  
2. Game Stages  
3. CustomNPCs-Unofficial  
4. Recruits + Siege Weapons + Epic Knights (Knights may already be a CurseForge-only add)  
5. Guard Villagers + CTOV  
6. Antique Atlas 4 + Surveyor (or Xaero pair)  
7. Bountiful  
8. MineColonies (only if colony-win is a first-class goal)

Everything else is regional garnish.

---

## 9. Sources

Accessed **2026-08-31**.

1. FTB Quests (NeoForge/Forge) — https://www.curseforge.com/minecraft/mc-mods/ftb-quests-forge  
2. FTB Quests 1.20.1 file listing — https://modpacks.ch/mods/minecraft/289412/ftb-quests-neoforge/versions/8078538  
3. FTB Quests CHANGELOG (1.20.1, XMod Compat, team stages) — https://github.com/FTBTeam/FTB-Quests/blob/main/CHANGELOG.md  
4. FTB XMod Compat (Game Stages, mapping stage) — https://github.com/FTBTeam/FTB-XMod-Compat  
5. FTB Chunks — https://www.curseforge.com/minecraft/mc-mods/ftb-chunks-forge  
6. FTB Teams — https://www.curseforge.com/minecraft/mc-mods/ftb-teams-forge  
7. Odyssey Quests / Heracles — https://modrinth.com/mod/odyssey-quests  
8. Heracles source — https://github.com/terrarium-earth/Heracles  
9. Better Questing — https://www.curseforge.com/minecraft/mc-mods/better-questing  
10. CustomNPCs-Unofficial — https://www.curseforge.com/minecraft/mc-mods/customnpcs-unofficial  
11. CustomNPCs-Unofficial (Modrinth) — https://modrinth.com/mod/customnpcs-unofficial  
12. interactEntity — https://modrinth.com/mod/interactentity and https://github.com/AshPapi/minecraft_interactEntity  
13. Blabber — https://modrinth.com/mod/blabber  
14. Bountiful — https://modrinth.com/mod/bountiful  
15. Game Stages — https://modrinth.com/mod/game-stages  
16. Open Parties and Claims — https://www.curseforge.com/minecraft/mc-mods/open-parties-and-claims and https://modrinth.com/mod/open-parties-and-claims  
17. Cadmus / Odyssey Claims — https://www.curseforge.com/minecraft/mc-mods/odyssey-claims — docs: https://docs.terrarium.earth/docs/cadmus/intro — Argonauts integration: https://docs.terrarium.earth/docs/argonauts/guilds/cadmus  
18. Villager Recruits — https://modrinth.com/mod/villager-recruits — https://www.curseforge.com/minecraft/mc-mods/recruits  
19. Siege Weapons — https://modrinth.com/mod/siegeweapons  
20. Kingdoms & Sieges — https://modrinth.com/mod/kingdoms-sieges  
21. MineColonies CurseForge — https://www.curseforge.com/minecraft/mc-mods/minecolonies  
22. MineColonies raids wiki — https://minecolonies.com/wiki/systems/raid/  
23. MineColonies config wiki — https://minecolonies.com/wiki/misc/configfile/  
24. Guard Villagers — https://modrinth.com/mod/guard-villagers  
25. ChoiceTheorem's Overhauled Village — https://modrinth.com/mod/ct-overhaul-village — CurseForge: https://www.curseforge.com/minecraft/mc-mods/choicetheorems-overhauled-village  
26. Towns and Towers — https://www.curseforge.com/minecraft/mc-mods/towns-and-towers — https://modrinth.com/mod/towns-and-towers  
27. When Dungeons Arise — https://modrinth.com/mod/when-dungeons-arise  
28. YUNG's Better Dungeons — https://modrinth.com/mod/yungs-better-dungeons  
29. Integrated Dungeons and Structures — https://www.curseforge.com/minecraft/mc-mods/idas — https://modrinth.com/mod/idas  
30. Medieval Buildings — https://modrinth.com/mod/medieval-buildings  
31. Structory — https://modrinth.com/mod/structory  
32. Explorify — https://modrinth.com/mod/explorify  
33. Repurposed Structures (Forge) — https://modrinth.com/mod/repurposed-structures-forge  
34. Terralith — https://modrinth.com/mod/terralith  
35. Antique Atlas 4 — https://modrinth.com/mod/antique-atlas-4  
36. Surveyor Map Framework — https://modrinth.com/mod/surveyor  
37. Xaero's Minimap — https://www.curseforge.com/minecraft/mc-mods/xaeros-minimap — https://modrinth.com/mod/xaeros-minimap  
38. Xaero's World Map — https://modrinth.com/mod/xaeros-world-map  
39. JourneyMap — https://modrinth.com/mod/journeymap — waypoints docs: https://teamjm.github.io/journeymap-docs/latest/client/waypoints/  
40. Waystones — https://modrinth.com/mod/waystones  
41. Better Combat — https://modrinth.com/mod/better-combat  
42. Epic Fight — https://modrinth.com/mod/epic-fight  
43. Epic Knights: Shields, Armor and Weapons — https://modrinth.com/mod/epic-knights-shields-armor-and-weapons  
44. Iron's Spells 'n Spellbooks — https://modrinth.com/mod/irons-spells-n-spellbooks  
45. Simply Swords — https://modrinth.com/mod/simply-swords  
46. Ice and Fire: Dragons — https://www.curseforge.com/minecraft/mc-mods/ice-and-fire-dragons — https://modrinth.com/mod/ice-and-fire-dragons  
47. Alex's Mobs — https://www.curseforge.com/minecraft/mc-mods/alexs-mobs — https://modrinth.com/mod/alexs-mobs  
48. Mowzie's Mobs — https://www.curseforge.com/minecraft/mc-mods/mowzies-mobs — https://modrinth.com/mod/mowzies-mobs  
49. Born in Chaos — https://www.curseforge.com/minecraft/mc-mods/born-in-chaos  
50. Illager Invasion — https://modrinth.com/mod/illager-invasion  
51. Small Ships — https://modrinth.com/mod/small-ships  
52. Serene Seasons — https://modrinth.com/mod/serene-seasons  
53. KubeJS — https://modrinth.com/mod/kubejs  
54. Architectury API — https://modrinth.com/mod/architectury-api  
55. DawnCraft – Echoes of Legends — https://www.curseforge.com/minecraft/modpacks/dawn-craft  
56. DawnCraft Getting Started — https://dawncraft.fandom.com/wiki/Getting_Started  
57. DawnCraft Progression — https://dawncraft.fandom.com/wiki/Progression  
58. DawnCraft Quests / reputation — https://dawncraft.fandom.com/wiki/Quests  
59. Craft to Exile 2 — https://www.curseforge.com/minecraft/modpacks/craft-to-exile-2  
60. Valhelsia 6 — https://www.curseforge.com/minecraft/modpacks/valhelsia-6  
61. Botz Guild Manager — https://github.com/DepthDrako/BotzGuildManager  
62. ExtraQuests — https://modrinth.com/mod/extraquests  
63. Modrinth API project lookups for version/download metadata (1.20.1 facets), 2026-08-31  

Bright Data `search_engine` / `scrape_as_markdown` returned HTTP 401 in this environment; live checks used WebSearch, direct page fetches, and the public Modrinth API instead.
