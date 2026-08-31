# Faction, kingdom, diplomacy, siege, lord, and army-AI mods

Live research for **Rallous Frontier** diplomacy / war layer. **Not a pack rewrite.** The default assortment stays in `pack/` (`pack.toml` pins **Minecraft 1.20.1 + Forge 47.4.0**). This file is a **candidate overlay**: what to add if we want Civ-style treaties and TWW3-style lords as a soldier on the ground. See `FACTIONS-AND-DIPLOMACY.md` for the design those mods should serve.

**Accessed:** 2026-08-31.

**Method:** WebSearch, WebFetch (Modrinth project pages), and Modrinth API `https://api.modrinth.com/v2/project/{slug}` and `/v2/search`. Bright Data `search_engine` / `scrape_as_markdown` returned **HTTP 401** (token not injected) in this environment, so those tools were not usable.

**Do not commit jars.** CurseForge is often Cloudflare-gated to scrapers; where a CurseForge URL is listed, it was confirmed via search snippets or known project slugs on 2026-08-31.

**Already in the default pack pin (do not duplicate):** Open Parties and Claims, Towns and Towers. Recruits / MineColonies / Custom NPCs are **not** in `pack/mods.json` at time of writing — campaign docs already assume them as the army/town/NPC layer.

**Overlap:** `QUEST-AND-WORLD-MODS.md` is the broader campaign overlay (quests, maps, sieges). This file goes deeper on **diplomacy, vassals, lords, and army AI** and should not replace that list.

---

## How to read this

| Pillar | What we need for the soldier+Civ+TWW3 loop |
| --- | --- |
| Factions / claims | Named polities, ranks, land, banners |
| Diplomacy | Ally / enemy / war / peace as data, not villager gossip |
| Vassal / tribute | Feudal hierarchy, not just “team color” |
| Siege | Breach, occupy, bell/keep, artillery |
| Named lords | Authored NPCs with dialogue, not random villagers |
| Army AI | Recruits/guards that march, hold, and fight without the player clicking every unit |

Recommended **first overlay** (Forge 1.20.1), on top of the existing pin, without replacing OPAC:

1. **Villager Recruits** (armies + built-in ally/enemy/siege).
2. **Vassal & Suzerains** + **Ranks and Titles** (feudal Civ verbs).
3. **Siege Weapons** and/or **Medieval Siege Machines** (artillery the soldier hears in the next valley).
4. **CustomNPCs-Unofficial** or **Easy NPC** + **InteractEntity** (lords in camps/courts).
5. **MineColonies** + **War 'N Taxes** *or* skip colonies and let Recruits claims be the only occupation layer (performance).
6. **Guard Villagers** + **MCA Reborn** only if we want living towns *and* can afford the AI cost next to Recruits.

Faction Friction is a strong **standalone** war system but **overlaps OPAC** (already pinned). Pick one claim brain.

---

## 1. Factions, kingdoms, diplomacy

### Villager Recruits: Claim and Siege Update!

- **Role:** Core **army + faction + diplomacy + siege** loop. Hire villagers, command groups, vanilla-team GUI, ally / neutral / enemy, claim land, siege to capture. Diplomacy changelog (1.13.0): leaders set ally/neutral/enemy; friendly fire off for allies; auto-enemy after significant damage; takeover for team leaders.
- **Loader / version:** Forge **1.20.1** (Modrinth loaders: `forge` only; game version 1.20.1). Latest Modrinth update **2026-06-29**. Downloads ~416k.
- **Pack fit:** Best single mod for “I am a captain in a host.” Compat listed with Small Ships, Epic Knights, Corpse. Optional Siege Weapons.
- **Citations:**
  - Villager Recruits. https://modrinth.com/mod/villager-recruits — 2026-08-31
  - Villager Recruits: Claim and Siege Update! https://www.curseforge.com/minecraft/mc-mods/recruits — 2026-08-31
  - Villager Recruits 1.13.0 changelog (diplomacy). https://modrinth.com/mod/villager-recruits/version/C4ZunsI9 — 2026-08-31

### Vassal & Suzerains: Villager Recruits Addon

- **Role:** Persistent **suzerain–vassal** hierarchy, titles, tribute contracts, rebellion cooldowns, hierarchy UI. This is the Civ **vassalize / tribute** verb Recruits does not fully own.
- **Loader / version:** Forge **1.20.1**. Modrinth updated **2026-04-10**.
- **Citations:**
  - Vassal & Suzerains: Villager Recruits Addon. https://modrinth.com/mod/vassal-suzerains-villager-recruits-addon — 2026-08-31
  - Vassal & Suzerains: Villager Recruits Addon. https://www.curseforge.com/minecraft/mc-mods/vassal-suzerains-villager-recruits-addon — 2026-08-31

### Ranks and Titles (Recruits Addon)

- **Role:** Faction ranks/titles, co-leader permissions for members, claims, **diplomacy**, tab-list roles. Supports “conscript vs champion vs agent” *presentation* even if rank logic also lives in quests.
- **Loader / version:** Forge (author Knightmare_Broke; 1.20.1 Recruits addon family).
- **Citations:**
  - Ranks and Titles (Recruits Addon). https://modrinth.com/mod/ranks-and-titles-(recruits-addon) — 2026-08-31
  - Author page (addon family). https://modrinth.com/user/Knightmare_Broke — 2026-08-31

### Faction Friction

- **Role:** Standalone factions: Team → Colony → Country tiers, ranks (Creator → Leader → … → Member), **war justification timer**, targeted **chunk sieges**, capitals (lose capital → war ends, land penalty), colors on chunk map / Xaero. **Does not require** OPAC or FTB Teams.
- **Loader / version:** Forge **1.20.1** (`factionfriction-1.5.0R-1.20.1-FORGE.jar` listed 16 Aug 2026) and NeoForge 1.21.1.
- **Pack fit:** Conflicts conceptually with **Open Parties and Claims** (already pinned). Use as an *alternative* claim/war brain, not a stack on OPAC, unless a later test proves peaceful coexistence.
- **Citations:**
  - Faction Friction (1.20.1 Forge files). https://modpacks.ch/mods/minecraft/1545398/faction-friction — 2026-08-31
  - Faction Friction 1.3.0R 1.20.1 Forge file card. https://modpacks.ch/mods/minecraft/1545398/faction-friction/versions/8552424 — 2026-08-31

### FactionCore

- **Role:** Lightweight factions for 1.20.1 Forge 47.4.10: invites, ally/break ally, **vote to declare war or peace**, friendly-fire rules.
- **Loader / version:** Forge 1.20.1. Smaller / newer than Recruits; useful if we want *player* politics without NPC armies.
- **Citation:** FactionCore. https://www.modpackindex.com/mod/172950/factioncore — 2026-08-31

### Kingdoms & Sieges

- **Role:** Place a **bell + banner** → kingdom + crown item; expand claim with emeralds; siege when outsiders push engines / projectiles in; win by breaking the bell, wiping attackers, or surrender. Hunger during sieges; death = out. Siege engines built like iron golems; manuscripts in outposts/mansions/villages. Designed to pair with **Knights & Heraldry**, not required.
- **Loader / version:** Fabric / Forge / NeoForge; **1.20.1 and 1.21.1**. Modrinth updated **2026-07-07**.
- **Pack fit:** Excellent “occupy the keep” fantasy. Overlaps Recruits sieges — pick **one** siege resolution for player-facing war, or gate Kingdoms to NPC capitals only.
- **Citations:**
  - Kingdoms & Sieges. https://modrinth.com/mod/kingdoms-sieges — 2026-08-31
  - Knights & Heraldry (companion). https://modrinth.com/mod/knights-and-heraldry — 2026-08-31

### Open Parties and Claims

- **Role:** Chunk claim + forceload + parties; API hooks for FTB Teams / Argonauts / LuckPerms. **Already pinned** in `pack/mods.json` (forge 1.20.1-0.30.3).
- **Loader / version:** Fabric / Forge / NeoForge / Quilt; 1.20.x including **1.20.1**. Modrinth updated **2026-08-20**. Downloads ~21.4M.
- **Pack fit:** Land + tribe (ARK). Not Civ treaties. Keep as the **player land** layer; let Recruits own **war**.
- **Citations:**
  - Open Parties and Claims. https://modrinth.com/mod/open-parties-and-claims — 2026-08-31
  - Open Parties and Claims. https://www.curseforge.com/minecraft/mc-mods/open-parties-and-claims — 2026-08-31

### FTB Teams (NeoForge project naming; Forge 1.20.1 files exist)

- **Role:** Party/team identity; War 'N Taxes lists it as optional integration; OPAC can use it as party backend.
- **Loader / version:** `ftb-teams-forge-2001.3.2.jar` published 21 Jan 2026 for 1.20.1 Forge (modpacks.ch file card).
- **Pack fit:** Optional. Only add if FTB Quests chapters need team-shared completion (`CAMPAIGN.md` §6.4).
- **Citations:**
  - FTB Teams 1.20.1 Forge file. https://modpacks.ch/mods/minecraft/404468/ftb-teams-neoforge/versions/7499810 — 2026-08-31

### Village Diplomacy

- **Role:** Per-village **reputation ranks** (HERO→VILLAIN), named villagers with personalities, named villages, golem memory. Commands: `/diplomacy info`.
- **Loader / version:** Fabric / Forge / NeoForge / Quilt; **1.20.1** (Forge 47.4.10+). Modrinth updated **2026-08-21**. Small (~1.6k dl).
- **Pack fit:** **Hamlet-scale** manners, not civilization treaties. Fine as flavor under Elector League towns. Do not mistake it for Civ VI.
- **Citation:** Village Diplomacy. https://modrinth.com/mod/village-diplomacy — 2026-08-31

### MineColonies + Minecolonies: War 'N Taxes

- **Role:** Living towns (workers, guards, raids). War 'N Taxes adds **tax, raid, `/wnt wagewar`, `/wnt besiege`, `/wnt vassalize`, peace/reparations, tribute %** — the closest **Civ vassal/tribute command set** on Forge 1.20.1. Optional Recruits / FTB Teams / JourneyMap hooks.
- **Loader / version:** MineColonies **1.20.1 Forge** (CurseForge still shipping Aug 2026 files; Modrinth project page is stale — **use CurseForge**). War 'N Taxes: Forge 1.20.1 and NeoForge 1.21.1; `WarNTaxes-Forge-1.20.1-v5.0.3.jar` listed 29 Jul 2026.
- **Pack fit:** `CAMPAIGN.md` already assigns MineColonies = living town, Recruits = field army. Do not enable both as “player capital” without a performance pass.
- **Citations:**
  - MineColonies. https://www.curseforge.com/minecraft/mc-mods/minecolonies — 2026-08-31
  - Minecolonies: War 'N Taxes. https://www.curseforge.com/minecraft/mc-mods/minecolonies-war-n-taxes — 2026-08-31

---

## 2. Siege engines and army AI

### Siege Weapons (talhanation)

- **Role:** Build and fire medieval engines; Recruits’ recommended war partner (“Prepare for war…”).
- **Loader / version:** Forge **1.20.1**. Modrinth updated **2026-04-10**.
- **Citation:** Siege Weapons. https://modrinth.com/mod/siegeweapons — 2026-08-31  
  Also: https://www.curseforge.com/minecraft/mc-mods/siegeweapons — 2026-08-31

### Medieval Siege Machines (magistu)

- **Role:** Mortar, catapult, ballista, ram, trebuchet (culverin / ladder on some versions). GeckoLib. Recruits compatibility addon exists so **bowmen operate engines**.
- **Loader / version:** Fabric / Forge / NeoForge; **1.20.1** among others. Modrinth updated **2026-01-15**.
- **Citations:**
  - Medieval Siege Machines. https://modrinth.com/mod/medieval-siege-machines — 2026-08-31
  - Medieval Siege Machines. https://www.curseforge.com/minecraft/mc-mods/medieval-siege-machines — 2026-08-31
  - Recruits–Medieval Siege Machine compat. https://www.curseforge.com/minecraft/mc-mods/recruits-medieval-siege-machine-mod-compat-addon — 2026-08-31

### Recruits Siege Fix / Morale / Horns / Raise Your Banner / QoL

Author **Knightmare_Broke** (Forge 1.20.1 addon family). Use as **quality** on Recruits, not as extra factions.

| Addon | Why it matters on the ground | URL |
| --- | --- | --- |
| Recruits Siege Fix | Core-chunk capture so sieges are a **place**, not a timer exploit | https://modrinth.com/mod/recruits-siege-fix |
| Recruits Morale Addon | Retreat / formation break — hosts can **rout**, not deathball | https://modrinth.com/mod/recruits-morale-addon |
| Recruits- Horns of War Addon | Horn = army-wide order (soldier fantasy) | https://modrinth.com/mod/recruits-horns-of-war-addon |
| Raise your banner! Recruits addon | Pack a group into a **placeable banner** to cut entity lag — required for “continent-scale” impression | https://modrinth.com/mod/raise-your-banner-recruits-addon |
| Recruits QoL Fix | Commands, map helpers, mount/claim fixes | https://modrinth.com/user/Knightmare_Broke |
| RTS Map Command Recruits | Map click-to-move for groups. **Optional.** Useful for captains; keep default UX first-person | https://modrinth.com/user/Knightmare_Broke |

All rows: Modrinth / author page — **2026-08-31**.

### Guard Villagers

- **Role:** Named-ish village guards, patrol, follow with Hero of the Village, shield AI, equipment GUI. Makes **occupied / allied towns** feel garrisoned when Recruits are off-chunk.
- **Loader / version:** Forge / NeoForge; **1.20.1**. Modrinth updated **2026-08-30**. Downloads ~12.6M.
- **Citation:** Guard Villagers. https://modrinth.com/mod/guard-villagers — 2026-08-31  
  Also: https://www.curseforge.com/minecraft/mc-mods/guard-villagers — 2026-08-31

### Ancient Warfare 3 NPCs

- **Role:** AW2-style workers + fighter/archer/siege engineer, townhall, armory, strategy table.
- **Loader / version:** CurseForge files checked 2026-08-31 show **1.21 / 1.21.1 NeoForge**, not a current 1.20.1 pin. **Do not add** to the 1.20.1 Forge pack unless a 1.20.1 file reappears.
- **Citation:** Ancient Warfare 3 NPCs. https://www.curseforge.com/minecraft/mc-mods/ancient-warfare-3-npcs — 2026-08-31

### Epic Knights: Shields, Armor and Weapons

- **Role:** Not a faction mod. **Kit** so Recruits and lords look like state troops / knights. Recruits lists Epic Knights compat.
- **Loader / version:** Fabric / Forge / NeoForge; **1.20.1**. Modrinth ~1.53M dl; updated 2026-03-24.
- **Citation:** Epic Knights: Shields Armor and Weapons. https://modrinth.com/mod/epic-knights-shields-armor-and-weapons — 2026-08-31  
  Also: https://www.curseforge.com/minecraft/mc-mods/epic-knights-armor-and-weapons — 2026-08-31

### Small Ships

- **Role:** Corsair Coast / Star-Sailed Quays travel; Recruits compat. Not diplomacy.
- **Loader / version:** Fabric / Forge / NeoForge; **1.20.1**.
- **Citation:** Small Ships. https://modrinth.com/mod/small-ships — 2026-08-31

---

## 3. Named NPCs, lords, authored courts

### CustomNPCs-Unofficial

- **Role:** The actual **TWW3 lord/hero** tool: skins, AI, faction ids, dialogue, quest hooks. Unofficial port with Noppes’ permission; **Forge and Fabric 1.20.1**.
- **Loader / version:** 1.20.1 (and later). Prefer this over the stale Modrinth `customnpcs_` project (last update 2024-11-06, empty `game_versions` in API).
- **Citations:**
  - CustomNPCs-Unofficial. https://www.curseforge.com/minecraft/mc-mods/customnpcs-unofficial — 2026-08-31
  - CustomNPCs-Unofficial (Modrinth). https://modrinth.com/project/vFAmwl6B — 2026-08-31

### Easy NPC

- **Role:** Lighter authored NPCs (dialogs, trading, skins) for map-makers. Bundle/core split in later versions. Forge **1.20.1**. Modrinth updated **2026-08-31**. ~1.1M dl.
- **Pack fit:** Faster to staff a court than full Custom NPCs. Weaker faction-war AI.
- **Citations:**
  - Easy NPC. https://modrinth.com/mod/easy-npc — 2026-08-31
  - Easy NPC. https://www.curseforge.com/minecraft/mc-mods/easy-npc — 2026-08-31

### interactEntity

- **Role:** JSON dialogues/quests/reputation/**factions** on any mob; auto-spawn on zone enter; KubeJS hooks; `custom_npc` type for important characters. **This is the warrant-seal / rumor / treaty-letter layer.**
- **Loader / version:** Forge **1.20.1** only. Small project (API ~209 dl); updated 2026-07-05. Treat as **prototype-grade**, high design value.
- **Citations:**
  - interactEntity. https://modrinth.com/mod/interactentity — 2026-08-31
  - AshPapi/minecraft_interactEntity. https://github.com/AshPapi/minecraft_interactEntity — 2026-08-31

### MCA Reborn

- **Role:** Named humans, personality, village rank toward “king,” relationship sim. **Not** a civilization. Use for Heartland **peasantry**, never for Elector-Count Hildemar.
- **Loader / version:** Fabric / Forge / NeoForge / Quilt; **1.20.1**. Updated 2026-08-29. ~3.9M dl.
- **Citation:** MCA Reborn. https://modrinth.com/mod/minecraft-comes-alive-reborn — 2026-08-31  
  Also: https://www.curseforge.com/minecraft/mc-mods/minecraft-comes-alive-reborn — 2026-08-31

### Towns and Towers / Integrated Villages

- **Role:** Architecture so a “capital” is not a vanilla plains village. **Towns and Towers is already pinned.** Integrated Villages: 1.20.1 Forge/Fabric/NeoForge, optional Recruits/Guard hooks; updated 2026-05-28.
- **Citations:**
  - Towns and Towers. https://modrinth.com/mod/towns-and-towers — 2026-08-31
  - Integrated Villages. https://modrinth.com/mod/integrated-villages — 2026-08-31

---

## 4. Plugins and dead ends (do not drop in the Forge pack)

| Project | Why it showed up | Verdict |
| --- | --- | --- |
| **Medieval Factions** (Spigot/Paper) | Alliances, wars, **vassalage**, swear fealty — closest *plugin* to Civ | **Server plugin**, not Forge. Ignore unless a future hybrid server. https://www.spigotmc.org/resources/medieval-factions.79941/ — 2026-08-31 |
| **Millenaire rewrite** (GitHub WangMioG) | Classic culture-villages on 1.20.1 Forge | **Dev rewrite**, not a trusted CurseForge/Modrinth release pin. https://github.com/WangMioG/Millenaire-rewrite — 2026-08-31 |
| **Ancient Warfare 2 nations** | 45 NPC nations, lords in structures | Legacy 1.12-era content; AW3 NPCs not on 1.20.1 |
| **RTS Map Command Recruits** | Map army UI | Allowed as *optional captain camera*; default play stays first-person in the host |

---

## 5. Suggested stack vs conflicts

| Need | Use | Avoid stacking with |
| --- | --- | --- |
| Player land / tribe | **OPAC** (already in pack) | Second claim mod (FTB Chunks, Faction Friction) until tested |
| Field army + ally/enemy | **Recruits** + morale + siege fix + banner-pack | Two siege-resolution mods as default win condition |
| Vassal / tribute | **Vassal & Suzerains** and/or **War 'N Taxes** | Both plus Faction Friction votes — three diplomatic brains |
| Authored lords | **CustomNPCs-Unofficial** *or* Easy NPC + InteractEntity | MCA Reborn as “the Elector” |
| Living capital | MineColonies **or** Recruits claim + Guard Villagers | Both + Integrated Villages + MCA on one spawn chunk |
| Siege spectacle | Siege Weapons **or** Medieval Siege Machines (+ Recruits compat) | Both engine mods until GeckoLib/entity caps are measured |

**Singleplayer simulated wars** are **not** fully solved by any one mod. Recruits NPC teams + MineColonies raids + a KubeJS/scoreboard tick (`FACTIONS-AND-DIPLOMACY.md` §6) is the honest architecture.

---

## 6. Version lock

Other agents locked **1.20.1 Forge 47.4.0** in `pack/pack.toml`. All **recommended** mods above have a 1.20.1 Forge path **except** Ancient Warfare 3 NPCs (skip) and Medieval Factions (plugin). If the pack later moves to NeoForge 1.21.1, re-check Recruits (Forge-only on Modrinth as of 2026-08-31) before following.
