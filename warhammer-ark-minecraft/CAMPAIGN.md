# Open-world campaign design — grimdark fantasy total-war

This document is the **campaign layer** for the Minecraft overhaul. It is additive to pack/mod research in this folder. Tone references: *Warhammer Fantasy* / *Total War: Warhammer* / *ARK: Survival Evolved* / *Red Dead Redemption* / *New World*. **In-world names in this file are original analogues.** Official Games Workshop and Creative Assembly names appear only as designer tone-refs in parentheses. See `IP-FANTASY.md`.

**Target runtime (locked with pack research):** Minecraft **1.20.1 + Forge 47.4.x**. Recruits, CustomNPCs-Unofficial, and Epic Fight are strongest on that line. Quest graphs in this file stay version-agnostic. Survival/taming pillars already in v0.1 (`CURATED-PACK.md` / `RESEARCH.md`): Legendary Survival Overhaul, Serene Seasons, Fossils and Archeology: Revival, Alex’s Mobs, Open Parties and Claims, Epic Fight. This campaign layer **adds** questing, provincial war, and NPC story — it does not replace that pack.

The player is **not a tourist**. They are a **warband**: hungry, mounted, indebted, and politically small until they are not.

---

## 1. How a Total War campaign map becomes first-person Minecraft

A Total War campaign is a **graph of provinces**. Each province has a capital, a few minor settlements, a biome identity, a garrison, and a “who owns this right now” flag. In Minecraft that graph has to be **walkable**.

### 1.1 Scale

| Total War object | Minecraft object | Typical travel |
| --- | --- | --- |
| Campaign map | One Overworld (plus optional “north” / “under-hold” dimensions as late-game *regions*, not sci-fi 40k) | Hours, not loading screens |
| Province | A **region**: 2–8 km across, bounded by rivers, ridges, and biome belts | 10–40 minutes mounted |
| Capital | A **named hub**: overhauled village / castle / MineColonies colony / Custom NPC city | Destination, not spawn |
| Minor settlement | Hamlet, mill, watchtower, inn, logging camp, shrine | Side-quest nodes |
| Frontier fort | Recruits claim, Guard Villager keep, pillager analogue fortress | Contested |
| Sea / river | Small Ships routes, fords, ferry NPCs | Optional shortcut |
| Chaos Wastes / badlands | Far-north or far-east biome belt with escalating night spawns | Endgame travel, never “safe” |

Do **not** model the whole Old World at TW scale. Model a **campaign corridor** of five acts (Heartland → Marcher Principalities → Night Counties → Hold-Road → Howling North) plus **optional off-axis cultures** the player can ride into at any time. That is how RDR keeps a story without a corridor shooter, and how New World keeps territories without a linear MMO.

### 1.2 Province anatomy (every region uses this template)

1. **Biome belt** — what you *feel* as you cross the border (plains+villages vs swamp+crypts vs taiga+holds). Terralith / Regions Unexplored / Biomes O' Plenty / Oh The Biomes We've Gone provide the paint; structure mods provide the architecture.
2. **Capital hub** — quest board, faction NPCs, trade, barracks, rumor-giver. Always reachable. Never despawned by campaign flags.
3. **Two or three minor nodes** — inn, shrine, mill, mine, ferry. New World-style “something to do if you wander.”
4. **A contested piece** — outpost, ruin, dragon nest, raid camp. ARK-style risk that is also a campaign beat.
5. **A frontier** — the road *out* toward the next act. Rumors live here, not walls.

### 1.3 Fog of war, not map-lock

The campaign map in Total War hides enemy armies in the fog. In Minecraft:

- **Unexplored chunks stay blank** (Antique Atlas 4 + Surveyor, or Xaero’s World Map with exploration-only reveal).
- **Capitals are rumors until visited** (quest waypoint, cartographer map, or NPC rumor — not a teleport).
- **Game Stages hide quests, vendors, and siege contracts**, not geography. The player can always ride north. The *campaign* does not follow them until they pick up the rumor.

This is the RDR rule: the mountains exist before the chapter that *matters* there.

---

## 2. RDR-style chapters that never lock the map

*Red Dead Redemption* is a **directed open world**: you can ignore Dutch and go hunting, but the next *named chapter* still waits at a camp. Minecraft should copy that, not a gated MMORPG expansion.

### 2.1 Three tracks, one world

| Track | What it is | What it must never do |
| --- | --- | --- |
| **Main** | Five acts. Chapter quests in FTB Quests (or Heracles). NPC dialogue in CustomNPCs / InteractEntity. | Delete biomes, disable travel, wipe the player’s colony |
| **Regional** | New World-style standing, gathering nodes, local bounties, town boards | Require the current main act |
| **Warband** | ARK survival: food, mounts, tribe/guild, base, tames | Pause because a cutscene “needs” you in the capital |

**Commit or wander.** Completing Act I’s last quest *unlocks Act II rumors* (stage `act2_open`). It does not close Act I’s side content. Side quests remain completable in any order after their region is *visited*.

### 2.2 Chapter state machine

```
SPAWN → Act I available
Act N last beat → grant stage act{N+1}_rumor
Player talks to rumor NPC or reads a letter → grant stage act{N+1}_open
Act N+1 quests appear in the journal
Map, mounts, colonies, and old quests stay
```

Optional **soft** pressure (never hard locks):

- Night spawn tables get worse as you go north (`born_in_chaos` / graveyard density configs by biome, not by “you skipped a quest”).
- Siege contracts and elite vendors require standing + stage.
- Waystones in a region stay uncraftable until you *discover* that region’s capital (Waystones already spawn in the world — do not remove them; just don’t gift a teleport in the quest book).

### 2.3 Failure is local

If the player’s colony falls in a MineColonies raid, **the campaign does not reset**. They lose the colony, not the act. If they fail a siege, the capital stays enemy-held and the quest stays active. Total War’s “you lost a settlement” is the model, not a game-over screen.

---

## 3. New World-style regional living world

Each region should answer: **what do I do if I ignore the main quest for two hours?**

### 3.1 Activity loops per region

| Activity | Minecraft hook | Campaign meaning |
| --- | --- | --- |
| Gathering | Region-tagged resources (iron in heartland, silver/marble in holds, blighted wood in night counties) | Provincial economy; quest turn-ins |
| PvE | Biome mobs, dungeons (When Dungeons Arise, YUNG’s, IDAS, Mowzie’s), night raids | Standing and loot, not only XP |
| Faction standing | InteractEntity factions, CustomNPC faction points, or a KubeJS/scoreboard analogue of DawnCraft reputation | Prices, quests, who shoots first |
| Town hubs | CTOV / Towns and Towers / Medieval Buildings + Guard Villagers | Jobs, recruits, rumors |
| Bounties | Bountiful boards in inns | Optional cash + standing |
| Territory | Cadmus / Open Parties and Claims / Recruits claims | “This is *our* stretch of road” |
| Events | MineColonies raids, Illager Invasion, Recruits enemy teams | The world fights whether you show up or not |

### 3.2 Standing, not alignment meters

Keep **three durable standings** (more is noise):

1. **Settled peoples** — elector towns, marcher freeholds, hold-kings (allied-ish).
2. **The dead and the night** — Night Counties courts. High standing here *lowers* settled standing.
3. **The howling powers** — north cults. High standing is a late-game temptation, not a win.

Optional fourth: **Greenhost / horned woods** as “you can trade with monsters if you are monster enough.”

DawnCraft is the closest existing pack for “villager quests change prices and unlock guild contracts.” Copy the *idea*, not the Korok/Ender-Dragon plot.

### 3.3 Hubs are verbs

A hub is not a pretty village. It must sell at least four verbs: **sleep, trade, recruit, take a job**. Bonus verbs: stable a mount, donate to a shrine, read a rumor, launch a siege.

---

## 4. ARK-style survival inside the campaign

ARK works because the map is a **survival habitat** that also contains bosses. The campaign here must never become a quest UI with a Minecraft skin.

### 4.1 You are a warband

- **Tribe** = Open Parties and Claims (already in v0.1) plus FTB Teams when FTB Quests lands. Recruits teams are the field army. Solo is a one-person warband, not a chosen one.
- **Base** = a camp that can become a MineColonies supply town *or* a claimed Recruits fort. It is allowed to be ugly. ARK thatch is canon.
- **Tames** = horses first, then **Fossils and Archeology: Revival** warbeasts (v0.1 default Ark loop) and Alex’s Mobs. Ice and Fire is optional later (pack research: 1.20.1 still a 2024 beta). Apex tames are Act IV–V power, not Act I taxis.
- **Food, weather, seasons** = Legendary Survival Overhaul + Serene Seasons (v0.1). Winter in the frost marches should hurt.
- **Death** = keep it punishing enough that riding out undergeared is a story, not a respawn commute. Pack agent owns the exact death rules.

### 4.2 Survival actions *are* campaign actions

| ARK action | Campaign reading |
| --- | --- |
| Tame a flyer | Scout the next province; skip a siege wall |
| Starve on the road | Why inns exist; why you take the miller’s flour quest |
| Get raided at home | Provincial war; Recruits defensive contract |
| Breed a line of warbeasts | Warband identity; optional side chapter |
| Claim a resource node | New World gathering + TW province income analogue |

If a quest can be completed without leaving spawn with a full belly and a mount, it is a tutorial, not a campaign beat.

---

## 5. Example 5-act open campaign

Working title: **The Rallous Marches**. Player starts as a dispossessed sergeant / hedge knight / escaped levy — not an elector.

Tone-refs in parentheses are **design only**. In-game strings use the analogue names.

### Act I — Elector Heartland (tone: Reikland / Empire)

**Region feel:** Cultivated plains, rivers, timbered towns, state-troop analogue militia, coach roads.

**Capital:** **Altdorf analogue → “Vellbruck, Seat of the Elector.”** Hub with barracks, chapel-forge, quest board.

**Main beats**

1. Survive the first night on the road (ARK loop). Reach any hamlet.
2. Take the miller’s flour / missing patrol bounty (Bountiful + NPC).
3. Defend a CTOV town from a raid (vanilla raid / Illager Invasion / Recruits). Earn **settled standing**.
4. Audience with a captain: the Elector’s road south is cut. You are hired as a **free company**, not a hero.
5. **Win the home province:** clear the river fort (quest dungeon + optional Recruits assault) so grain moves again.

**Optional side**

- Chapel heresy (small undead crypt — preview of Act III).
- Tournament / duel (Better Combat / Epic Fight skill check).
- Tame a horse and a warhound; refuse the dragon rumor.
- Found a **tiny** camp. Do not found a capital yet.

**Unlock:** rumor of mercenary work in the **Broken Principalities**. Map already allowed you to walk there.

### Act II — Broken Principalities (tone: Border Princes)

**Region feel:** Badlands-adjacent hills, rival warlords, burned villages, no one law. New World territorial PvP energy even in PvE (NPC warlords).

**Capital:** none. **Three rival hubs** (Red Keep, Ford-Market, Hill-Banner). Player picks a patron or plays them against each other.

**Main beats**

1. Arrive starving. Sell your sword to *someone*.
2. First **field battle**: Recruits squad vs a rival’s squad on a ridge. This is the Total War “army” fantasy in first person.
3. Take or found a **colony** (MineColonies supply camp *or* Recruits claim). This is “settle a province.”
4. Siege a warlord’s keep (Siege Weapons + Recruits claim/siege, or Kingdoms & Sieges bell).
5. Choose: crown a puppet, keep the fort yourself, or burn it and move on. **Any choice completes the act.** Standing with settled peoples shifts.

**Optional side**

- Greenhost mercenary camp (greenskin analogue) — trade or fight.
- Chivalric knight errant from the west (Bretonnia analogue cameo).
- Smuggler river (Small Ships).
- First Ice and Fire nest on the horizon — **do not require killing it**.

**Unlock:** letters from the east: the dead are walking the **Night Counties**. Also: Hold-Road traders mention a grudge.

### Act III — Night Counties (tone: Sylvania / Vampire Counts)

**Region feel:** Swamps, graveyards, walled peasant towns that bar the gate at dusk. The Graveyard, Born in Chaos, swamp biomes, crypt structures.

**Capital:** **Mournhold-on-the-Fen** (living) vs **the Black Keep** (dead court). Two hubs, one province.

**Main beats**

1. Enter as a warband with a fort behind you. Night is the boss.
2. Peasant contract: escort a coffin that must *not* arrive. Or must.
3. Standing split: help the living (raid the keep) or accept a dead prince’s bargain (power, tames that are “wrong”).
4. **Province win (living):** siege the Black Keep at dawn with recruits + siege engines.  
   **Province win (dead):** deliver a living captain to the court; your old Heartland standing drops.
5. Either ending opens the mountain road: the Hold-Kings will not talk to a warband that smells of graves — unless you bring proof.

**Optional side**

- Strigoi analogue hunting lodge (Mowzie’s / Ice and Fire undead-adjacent).
- Kislev analogue frost-merchant caravan stuck in the fen.
- A vampire-count analogue wants your **dragon egg**. Refuse is valid.

**Unlock:** Hold-Road pass. Howling North rumors appear as graffiti, not a quest marker.

### Act IV — Hold-Road (tone: World’s Edge Mountains / Dwarfs)

**Region feel:** Extreme hills, deepslate, fortified stone towns (Medieval Buildings, YUNG’s Better Strongholds as “lost hold,” Hopo mineshafts as under-hold). Slow travel. Worth the iron.

**Capital:** **Karaz analogue → “Khuzum-Dur, the Open Gate.”** Interior halls, grudge-book NPC.

**Main beats**

1. The gate is shut to “umgi.” Prove yourself: clear a troll/dragon approach (Ice and Fire / Alex’s Caves adjacent threat).
2. **Grudge quest:** recover a named relic from a fallen hold (dungeon crawl, not a fetch from a chest next to the NPC).
3. Hold-Kings hire your warband as **mercenary artillery**. First use of siege weapons *with* NPC allies.
4. Optional civil split: help traditionalists vs a reckless engineer analogue (Create is allowed here as *dwarf* tech, not a kitchen-sink factory).
5. **Province win:** the Open Gate names you **oath-friend** (standing) and opens the north road. You do not become a dwarf.

**Optional side**

- Woodland court (Wood Elf analogue) will snipe you for cutting their border pines.
- High-court emissary (High Elf analogue) offers a sea route that **skips** Act V. Taking it is a valid wander — Act V still exists.
- Tame a dragon *properly*. This is the ARK apex tame, gated by power not by a locked door.

**Unlock:** The Howling North is no longer a rumor. It is weather.

### Act V — Howling North (tone: Chaos Wastes)

**Region feel:** Terralith/volcanic/snow extremes, Born in Chaos, mutated fauna, no towns — only warbands, shrines, and one last fortress of the settled world (Kislev analogue **frost-march holdfast**).

**Capital:** **Pavlenholt** (last city) and **the Wound** (a crater/structure, not a dimension you must enter to “finish Minecraft”).

**Main beats**

1. Escort a convoy to Pavlenholt. If it dies, the city still exists; standing and prices suffer.
2. Choose three of five optional warband trials (tame, siege, standing, relic, duel). The campaign does not require all five.
3. **Climax (commit):** a siege of a north fortress *or* a defense of Pavlenholt against a scripted Recruits/MineColonies-scale invasion. This is the Total War “final battle” as a *place you can walk away from and come back to*.
4. **Epilogue that is not an ending:** the Wound remains. New Game+ is “your warband is now a power on the map.” Side content in Acts I–IV stays open.

**Optional side (the wanderer’s ending)**

- Join the howling powers. The map does not close. Heartland towns become hostile. That is a *campaign outcome*, not a deleted save.
- Sail west with corsairs (Dark Elf analogue) and never finish Act V.
- Go home and run a colony. The journal marks Act V as “abandoned — the north still howls.”

### Off-axis regions (always optional)

These are **New World territories**, not extra acts. Seed them on the edges:

| Analogue (tone-ref) | In-world name | Hook |
| --- | --- | --- |
| Bretonnia | Lance-Duchies | Knightly vows, cavalry, peasants |
| Kislev | Frost Marches | Already the Act V doorstep |
| Greenskins | Greenhost Badlands | Recruits-hostile camps, waaagh-like raids (original slang) |
| Beastmen | Horned Woods | Forest ambushes, no towns |
| High Elves | Star-Sailed Quays | Sea, arrogance, elite gear |
| Wood Elves | Greenwood Court | Archery, hostility to loggers |
| Dark Elves | Corsair Coast | Slavery analogue: *prisoner escorts*, not real-world atrocities — keep it grim, not edgy |
| Chaos Dwarfs analogue | Ash-Foundries | Optional industrial evil, Act IV offshoot |

---

## 6. What “winning a province” means in Minecraft

Total War: occupy the settlement, install a governor, wait out public order. Minecraft cannot clone that UI. It **can** clone the *outcomes*. A province is **won** when **any two** of the following are true. The quest book should accept multiple combinations.

### 6.1 The four win keys

1. **Quest win** — complete the region’s FTB/Heracles chapter (story legitimacy).
2. **Siege win** — Recruits siege / Kingdoms & Sieges bell / scripted CustomNPC battle. The capital’s team color changes.
3. **Colony win** — a MineColonies colony (or equivalent) reaches a configured building level inside the region, and survives one raid.
4. **Reputation win** — settled (or dead, or howling) standing above a threshold. Merchants call you lord. Guards stop asking you to leave.

**Recommended default for the main campaign:** Quest + (Siege *or* Colony). Reputation is the wanderer’s path: you can “win” the Heartland by becoming beloved without ever taking the river fort.

### 6.2 What winning actually changes

| Change | Do | Don’t |
| --- | --- | --- |
| Flag | Recruits/vanilla team, claim overlay, banner on the atlas | Delete the enemy biome |
| Economy | Better trades, Bountiful refresh, recruit discounts | Infinite emeralds |
| Spawns | Slightly fewer night raids *near the capital* | Peaceful difficulty |
| Quests | Mark chapter complete; open rumor for next act | Remove side quests |
| Travel | Add a waypoint / cartographer map | Force a waystone in inventory |
| Failure later | Enemy can re-siege (Recruits / raid). Province can be *lost* | Ironman delete |

### 6.3 Occupying vs allying vs colonizing

- **Ally:** you never owned it. Standing win. TW “military access + alliance.”
- **Occupy:** siege win. You fly a banner. You owe a garrison (Recruits stay behind or the town falls again).
- **Colonize:** you built a new town in empty land. Border Princes energy. MineColonies is the analogue of “found a settlement” not “capture Altdorf.”
- **Vassal:** you put a puppet NPC in the keep (CustomNPC + quest flag). Best Act II ending.

### 6.4 Multiplayer

FTB Teams share quest completion. Cadmus/Open Parties share land. Recruits teams are the field army. A province won by the team is won for the team. PvP servers treat Act II+ as New World territory wars; PvE servers treat rival warlords as NPCs.

---

## 7. Implementation notes for the pack agent

- **Journal:** FTB Quests chapters named after acts; each chapter has a “Main” column and a “Warband / Region” column. Do not linearize the region column.
- **Rumors:** Game Stages + a single “Rumor” quest reward item (letter). Reading it grants the next stage.
- **NPCs:** CustomNPCs-Unofficial for authored characters; InteractEntity if you need JSON-on-any-mob; Blabber + Heracles-for-Blabber if you stay Fabric-side.
- **Armies:** Recruits is the Total War-in-first-person piece. MineColonies is the *living town* piece. They overlap; pick one as “player capital” and the other as “player army,” or accept the performance cost.
- **Do not ship jars in git.** CurseForge / Modrinth IDs belong in the pack manifest the other agent owns.

---

## See also

- `OPEN-WORLD-CAMPAIGN-LOOP.md` — a single day in the warband.
- `QUEST-AND-WORLD-MODS.md` — live-researched mods for 1.20.1 Forge.
- `IP-FANTASY.md` — why this world is an analogue, not a clone.
- `LEGAL-NOTES.md` — GW / Mojang / Wildcard field guide.
- `FACTIONS-AND-DIPLOMACY.md` — soldier’s-eye Civ/TW diplomacy overlay (if present).
