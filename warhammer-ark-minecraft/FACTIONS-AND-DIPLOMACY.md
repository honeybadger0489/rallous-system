# Factions, lords, and Civ-style diplomacy (soldier’s-eye)

Additive design for **Rallous Frontier**. This is not a pack list and not a rewrite of campaign acts. Pair with `CAMPAIGN.md` (provinces, five acts, win keys) and `FACTION-MODS.md` (live mod research).

**Locked runtime:** Minecraft **1.20.1 Forge 47.4.x** (`pack/pack.toml`). In-world names are **original analogues**. Games Workshop / Creative Assembly names appear only as designer tone-refs in parentheses. The player is a body on a road, not a general on a map.

---

## The loop (soldier + Civ + Total War)

You wake as a **conscript** in someone else’s war: a banner you did not choose, a ration you did not cook, a road already full of dust from a host that marched before dawn. Civilizations are **met on the ground** — a patrol challenge, a court tent, a occupied mill flying a new color — the way *Civilization VI* first-contact and treaty language works, except there is no globe to click. Inside each civilization sit **lords and heroes** (*Total War: WARHAMMER 3* style): you find them in camps, throne-halls, and the wreck of a battlefield, not as portraits on a campaign UI. You can **swear, ally, pay tribute, vassalize, or burn**, then watch the **continent keep fighting without you**. Rank is earned in the mud: conscript → champion → a lord’s agent carrying sealed letters → a **warband leader** with your own banner, still small next to the Elector’s columns.

---

## 1. Civ VI diplomacy in first-person Minecraft

*Civilization VI* diplomacy is a **relationship graph** (meet → agenda friction → deals → alliance / war → peace / vassal). Minecraft must keep that graph and **throw away the map screen**. Every diplomatic verb is a **place, a body, and a prop**.

### 1.1 First contact (Meet)

You do not get a popup. You get:

- A **border patrol** that halts the road and demands a banner, a pass, or a bribe.
- A **herald camp** half a kilometer off the coach road (banner, cookfire, two guards, one clerk).
- A **first-audience** at a capital hub already named in `CAMPAIGN.md` (Vellbruck, Khuzum-Dur, Pavlenholt, Mournhold-on-the-Fen).

**State change:** `faction_X_met`. Atlas rumor pin. Town criers in *already visited* hubs mention the name. Unmet factions still exist and still wage simulated war (see §6).

### 1.2 Embassy, agenda, grievances

Civ leaders have **agendas**. Lords here have the same, but you learn them by **being in the room**:

| Civ VI idea | Grounded Minecraft |
| --- | --- |
| Agenda | Lord gossip + a visible habit (the Hold-King counts grudges; the Dead Prince never signs in daylight) |
| Grievance | A **deed** you can point at: burned mill, stolen tribute wagon, murdered envoy, occupied shrine |
| Access level | How close you may stand: gate only → courtyard → hall → private tent |
| Delegation | You are not the Elector. You are a **soldier or agent**. High deals require a lord *or* a sealed warrant |

### 1.3 Treaty table (every deal is a scene)

Treaties are **signed objects**: a waxed letter, a banner-swap, a hostage, a wagon of grain. Copies go on **town boards**. Breaking a treaty is visible (ripped proclamation, new enemy color on the atlas).

| Deal | What the soldier sees | Typical cost |
| --- | --- | --- |
| **Open roads** (open borders) | Allied/neutral patrols wave you through; enemy patrols still stop you | Gift + standing |
| **Trade** | A marked caravan route; you can escort it for pay | Luxury analogue: salt, silver, frost-furs, hold-iron |
| **Defensive pact** | If *their* capital is sieged, messengers spawn on *your* road asking for a relief column | You may refuse; standing drops |
| **Alliance** | Shared camp access, no friendly fire, joint war calls | Mutual; breaking it is a grievance everywhere |
| **Research / faith pact analogue** | College-mage or chapel-forge unlocks a vendor or a recruit type | Story-gated, not a tech tree UI |
| **Denounce** | Town crier + bounty on *your* banner in their hubs | Cheap; starts a timer toward war |
| **Declare war** | Horns, then columns. Not a checkbox. A **herald** can declare in a capital square, or a **raid** can declare by burning a mill | Casus belli optional but NPCs remember sneak attacks |
| **White peace** | Both banners stay; roads reopen; nobody pays | Exhaustion after simulated or played battles |
| **Tribute peace** | Wagon schedule (emeralds / grain / iron / captives-as-prisoner-escorts — grim, not atrocity porn) | Recurring; see vassals |
| **City cession** | The **claim color and keep banner change**. You walk the occupied street | Siege win or treaty clause |
| **Vassalage / suzerainty** | Two banners on the gate: overlord large, vassal small. Tax wagons leave on a clock | Feudal contract (mod hook: Vassal & Suzerains) |
| **Liberation** | You return a keep to a third faction; they owe you | High standing, no land |

### 1.4 Who may sign

| Rank (see §5) | May negotiate | May bind a faction |
| --- | --- | --- |
| Conscript | Nothing. You carry packs. | No |
| Champion | Local truce (one road, one night) | No |
| Lord’s agent | Full treaty *if* you hold a **warrant seal** | Yes, as the lord’s hand |
| Warband leader | Your **own** banner’s deals; you may **swear fealty** or **demand vassalage** of someone smaller | Yes, for *your* warband, not for Vellbruck unless they named you |

This is the Civ rule *and* the TWW3 rule: **the Elector is not you**. You can become a minor power. You should never start as the map.

### 1.5 What this must never feel like

- A diplo screen that pauses the world.
- Villager trading as “meeting a civilization.”
- Instant global alliance because you dropped emeralds on one NPC.
- One “good vs evil” meter. Use the three durable standings in `CAMPAIGN.md` §3.2 **plus** per-civilization met/treaty flags.

---

## 2. TWW3-inspired faction roster (inspiration vs analogue)

Use **in-world names** in quests, NPC speech, banners, and journal. Tone-refs are designer-only.

Aligns with `CAMPAIGN.md` acts and off-axis table. Extra rows fill the *Total War: WARHAMMER 3* roster so the **living war** has more than five colors.

### 2.1 Core campaign civilizations

| Tone-ref (design only) | In-world civilization | Typical lords / court | Soldier’s first meet | Campaign hook |
| --- | --- | --- | --- | --- |
| The Empire / Reikland | **Elector League** (Heartland; capital **Vellbruck**) | Elector-Count, warrior-chaplain, college-mage, road-captain | State-troop patrol, coach-road checkpoint | Act I home banner |
| Border Princes | **Broken Principalities** (Red Keep, Ford-Market, Hill-Banner) | Rival warlords, mercenary captains | Paid sword, no law | Act II; easiest vassal playground |
| Sylvania / Vampire Counts | **Night Counties** (Mournhold-on-the-Fen vs **the Black Keep**) | Dead prince, banshee-herald, living mayor | Gate slammed at dusk | Act III split standing |
| Dwarfs / Karaz Ankor | **Hold-Kings of the Hold-Road** (**Khuzum-Dur**) | Hold-King, slayer-oath, grudgemaster, engineer | Shut gate, “umgi” tax | Act IV |
| Kislev / Chaos Wastes doorstep | **Frost Marches** (**Pavlenholt**) | Ice-tsarevna, bear-priest, wing-lancer captain | Convoy escort in snow | Act V last city |
| Chaos Wastes | **Howling Hosts** (the Wound; not one tidy nation) | Ruinous warlords, cult champions | Shrine on a dead road | Act V; joining them is a *campaign outcome* |

### 2.2 Off-axis civilizations (always optional, always at war with *someone*)

| Tone-ref (design only) | In-world civilization | Soldier’s first meet |
| --- | --- | --- |
| Bretonnia | **Lance-Duchies** | Knight-errant on a listed road; peasant levy hiding from their own lord |
| High Elves / Ulthuan | **Star-Sailed Quays** | Arrogant quay-envoy; sea-route that can skip Act V (`CAMPAIGN.md`) |
| Wood Elves | **Greenwood Court** | Arrow from a tree-line you were logging |
| Dark Elves | **Corsair Coast** | Prisoner-escort contract; black sails |
| Greenskins | **Greenhost** | Mercenary camp in Act II; raid horns at night |
| Beastmen | **Horned Woods** | No town. Herdstone analogue: a hung banner of skulls |
| Chaos Dwarfs | **Ash-Foundries** | Slave-furnace road; Act IV industrial offshoot |
| Grand Cathay | **Jade Mandate** | Far-east caravan, dragon-gate diplomats, gunpowder wagons |
| Skaven | **Under-Clans** | You meet them *under* a capital; surface lords deny they exist |
| Tomb Kings | **Sunken Dynasties** | Desert/badlands necropolis; silent herald with a scroll older than Vellbruck |
| Lizardmen | **Temple-Spawn** | Jungle temple that “negotiates” by omen and ambush |
| Ogre Kingdoms | **Maw Tribes** | Gut-king feast-truce: pay in meat or be the meat |
| Vampire Coast | **Drowned Admiralty** | Fog, wreck-banners, press-gang of the already-dead |
| Norsca | **Reaver Tribes** | North of Pavlenholt; they raid the Frost Marches whether you are there or not |
| Warriors of Chaos | **Northern Host** | Armored columns, not random cultists — a *civilization of warbands* |
| Khorne | **Blood Host** | No treaties. Only skull-tithe or flight |
| Nurgle | **Rot Courts** | Plague-hospital “alliance” that poisons Heartland standing |
| Tzeentch | **Changing Cabal** | Treaties that rewrite themselves; agent-on-agent layer |
| Slaanesh | **Velvet Host** | Beautiful camp, ruinous gifts; never a “romance sim” |
| Tilea / Estalia | **Merchant Republics** | Condottieri contracts; buy an alliance for a season |
| Araby analogue | **Desert Caliphates** | Spice road, horse-archers, scholar-mages |
| Hobgoblin / east steppes | **Wolf-Banner Khans** | Steppe host between Jade Mandate and Maw Tribes |

**Pack note:** you do not need a unique mob mod per row. Banner color + named lord NPC + biome belt + simulated war AI is enough for a first pass. Unique models are polish.

### 2.3 What a “faction” is in data

Keep this boring and implementable:

```
faction_id          e.g. elector_league
display_name        Elector League
banner_pattern      (vanilla banner + team color)
met                 bool
standing            -100..100 (per player / per warband)
treaty              none | open_roads | defensive | alliance | war | vassal | overlord
overlord_id         optional
lords[]             named NPC ids
heroes[]            named NPC ids (agents, captains, priests)
at_war_with[]       faction ids (simulated, even in SP)
```

Vanilla teams + Recruits diplomacy + InteractEntity/CustomNPC faction ids should **mirror** this table, not invent a second politics.

---

## 3. Lords and heroes (TWW3, on the ground)

In *Total War: WARHAMMER 3*, a faction is a **roster**: legendary lords, generic lords, heroes, and units. The player here never clicks a lord card. They **walk up to a person**.

### 3.1 Three encounter stages (camps, courts, battlefields)

**Camps** — the default. A lord on campaign is a **moving village**: command tent, smith, cook, pickets, banner pole, prisoner cage, tribute chest. You may:

- Take a contract (champion path).
- Deliver a letter (agent path).
- Steal the chest (grievance).
- Challenge a champion in the ring (Epic Fight / Simply Swords skill check — still not a “match”).

**Courts** — capitals only. Elector hall, Hold-King’s gate, Dead Prince’s night audience, Ice-tsarevna’s frost-keep. Treaties that bind a *civilization* happen here. Guards check standing. Wrong banner = arrest or duel, not a shrug.

**Battlefields** — during or after a siege / field fight. You may:

- Spot the lord’s **bodyguard knot** (better armor, unique banner, hero nearby).
- Receive a **parley flag** (white banner item) if you are an agent.
- Loot a **fallen hero’s seal** (quest item) if they died in simulated or played battle.
- Rescue or capture: a captured lord is a **peace clause**, not a cute pet.

Lords **despawn from camp and appear on the field** when their province is contested. If the player is elsewhere, the battle still resolves (§6) and the camp may be gone, captured, or mourning.

### 3.2 Named roster (original names, designer tone-refs in parentheses)

These are **authored NPCs** (CustomNPCs-Unofficial / Easy NPC / InteractEntity). Not villager professions.

| Civilization | Lord (legendary analogue) | Heroes you actually bump into |
| --- | --- | --- |
| Elector League | **Elector-Count Hildemar Vellbruck** (Empire LL energy) | Warrior-chaplain **Otto Twin-Hammer**; college-mage **Elsbeth Greyquill**; road-captain **Marta Kehl** |
| Lance-Duchies | **Dame Isolde of the High Lists** | Peasant-vow knight **Ser Gerren**; damsel-analogue **Sister Bramble** |
| Frost Marches | **Ice-Tsarevna Milena Pavlen** | Bear-priest **Yaromir**; wing-lancer **Captain Ostrik** |
| Hold-Kings | **Hold-King Thrumgar of Khuzum-Dur** | Slayer-oath **Karak Drin**; grudgemaster **Bram Oak-Ledger**; engineer **Nissa Steam-Spite** |
| Night Counties (dead) | **Prince-in-the-Coffin Vasalric** | Banshee-herald **Lys**; grave-captain **Helm of Nine Nails** |
| Night Counties (living) | **Mayor-Warden Annel of Mournhold** | Watch-sergeant **Piotr**; coffin-smuggler **Red Juna** |
| Broken Principalities | **Warlord Cess of Red Keep**; **Lady Toll of Ford-Market**; **Banner-King Halvo** | Sellsword champion **Brick**; spy **Quill** |
| Star-Sailed Quays | **High-Envoy Caelith Starwake** | Sea-guard **Ithlin**; mage-envoy **Vael** |
| Greenwood Court | **Glade-Regent Thorn-That-Watches** | Way-singer **Nim**; arrow-saint **Cal** |
| Corsair Coast | **Admiral-in-Chains Sable Vex** | Assassin-hero **Needle**; beastmaster **Kresh** |
| Greenhost | **Warboss-analogue Gruk Dump-Banner** | Shaman **Wizzgit** (original slang only); boar-boss **Tusk** |
| Horned Woods | **Beast-lord Cindergor** | Bray-shaman analogue **Moth-Eye**; gore-captain **Split-Hoof** |
| Ash-Foundries | **Hashut analogue refused — use Ash-Overlord Varnak Furnace-Tithe** | Daemonsmith analogue **Pyre-Scribe**; overseer **Chain-Count** |
| Jade Mandate | **Jade-Commissar Shen of the West Gate** | Alchemist-hero **Li Four-Fires**; crow-mage **Yue** |
| Under-Clans | **Warlock-Take Skritch Two-Crowns** | Assassin **Fingermark**; plague-deacon **Rikk** |
| Sunken Dynasties | **Pharaoh-Who-Wakes Khetep-Ra** | Liche-priest analogue **Scroll-That-Walks**; tomb prince **Ushabti-Voice** |
| Temple-Spawn | **Oracle-Saurian Quetz-of-the-Third-Sun** | Skink diplomat **Tikli**; kroxigor-captain (no speech, only the diplomat) |
| Maw Tribes | **Gut-King Ogga the Toll** | Butcher-priest **Grease**; hunter **Maw-Daughter Brakka** |
| Drowned Admiralty | **Drowned Admiral Salt-Caron** | Gunnery wight **Nine-Fathom**; siren-herald **Wail** |
| Reaver Tribes | **Jarl-of-the-Red-Hull Inga** | Skin-wolf analogue **Hrim**; seer **Bone-Lot** |
| Howling / Northern Host | **Warlord of the Wound, name revealed in Act V** | Four **ruinous champions** as optional patrons, never as a “class select” |

**Generic lords** (repeatable): Elector marshal, hold thane, princeling, corsair captain, gut-chief. Same jobs, different names, spawned per province.

**Hero types** (TWW3 jobs, first-person tasks):

| Hero job | What you *do* with them |
| --- | --- |
| Agent / spy | Carry letters, plant grievances, open a gate from inside |
| Warrior-priest / chaplain | Camp buffs, undead-hate, public sermons that change standing |
| Mage | Court advisor; optional battlefield ritual (keep it rare) |
| Assassin | “Remove this captain” contracts — player may *be* the knife |
| Engineer | Siege-train escort; Create-as-dwarf-tech in Act IV only |
| Diplomat | The NPC who actually holds the treaty quill |

### 3.3 Killing a lord

Lords are **not bosses with unique dimensions**. They are hard NPCs with bodyguards. If they die:

- The faction does **not** vanish (TWW3: another lord takes the faction).
- A **succession camp** spawns within a few in-game days.
- Your standing and grievances persist.
- If *you* killed them in parley, every court hears it. Sneak-war grievance.

---

## 4. Continent-scale war, felt by one soldier

The fantasy is **MMORPG-scale faction conflict in one world**, experienced as a person who can only see a ridge at a time.

### 4.1 Always-on signs (even when you are chopping wood)

- **Banners on towers and gatehouses** match the current occupier. When simulated war flips a province, the banner **changes** before you arrive.
- **Marching hosts:** Recruits columns or packed **banner-items** (see Raise Your Banner addon in `FACTION-MODS.md`) moving on roads. Dust, horn, supply wagons, camp followers. You can hide, join, or get conscripted.
- **Occupied towns:** two sets of guards; curfew; prices; a proclamation board with the new lord’s name.
- **Refugee files** on the coach road: NPC groups with the *loser’s* banner in a sack.
- **Burned mill / intact mill** as a province health read. You do not need a UI pie chart.
- **Distant artillery:** Siege Weapons / Medieval Siege Machines sound from the next valley. Follow it or don’t.
- **Dead horses and broken pavise** on a field you did not fight. Loot is meager; the *story* is the point.

### 4.2 What “large-scale” means without a thousand entities

Minecraft will melt if every war is 400 loaded NPCs. Design for **impression**:

1. **On-chunk:** 20–60 Recruits + player + siege piece is a “battle.”
2. **Off-chunk:** simulated resolution (§6). Next visit shows aftermath dressing (banners, rubble schematics, fewer vendors).
3. **Road theater:** small patrols (6–12) constantly. They imply the host.
4. **Pack-and-place banners** for armies the player owns so the world can breathe.

This is New World territory war + ARK tribe raid energy.

### 4.3 Occupied town checklist (designers)

When a capital changes hands, all of this should update:

1. Team / claim color (Recruits, Open Parties and Claims — already in the pack pin).
2. Guard outfit and banner.
3. Quest board issuer (living mayor vs dead prince vs Hold-King’s factor).
4. One vendor locked, one vendor opened.
5. A **grave or a feast**, depending on who won.
6. Journal rumor: “Khuzum-Dur has closed the north road” / “Red Keep flies Hill-Banner’s cloth.”

---

## 5. Player paths: conscript → champion → lord’s agent → warband leader

Ranks are **diegetic**. They are titles other NPCs use, plus a few flags. They are not a class-select screen.

### 5.1 Conscript

**How you start (Act I default):** a levy sergeant shoves a spear and a cheap banner into your hands. You march, haul flour, stand a night watch, and do not get a name in the Elector’s book.

**Verbs:** follow, carry, survive, desert (standing hit), complete a patrol.

**Exit:** one notable deed (defend the mill, save the captain, win a duel in camp).

### 5.2 Champion

**You are named in camp.** Better kit. You may lead a **small** Recruits group. Civilians call you by epithet (“the mill-saver”).

**Verbs:** field battle in Act II, take bounties, refuse a stupid order, pick a patron warlord.

**You still cannot sign a civilization-level alliance.**

### 5.3 Lord’s agent

A lord gives you a **warrant seal** (item). You are their **hand**, not their heir.

**Verbs (the Civ layer lives here):**

- Carry peace / war / tribute letters between courts.
- Escort a hostage or a tribute wagon.
- Open a gate from inside.
- Sit in the *back* of a treaty tent and watch the quill. Sometimes *you* are told to sign.

**Risk:** if you betray the warrant, that lord’s heroes hunt you. This is TWW3 hero-on-hero, first person.

### 5.4 Warband leader

You plant **your** banner (Recruits faction create / Kingdoms & Sieges bell / OPAC party — pick one stack in `FACTION-MODS.md`). You are a **minor civilization**.

**Verbs:**

- Ally with, or vassalize under, Elector League / Hold-Kings / a Principalities warlord.
- Demand tribute from a hamlet you actually occupy.
- Get called into *their* wars (defensive pact).
- Lose the warband and fall back to champion (the campaign does not reset — same rule as `CAMPAIGN.md` §2.3).

**You are still not the map.** Vellbruck’s columns should make your warband look like a free company. That is the point.

### 5.5 Optional late titles (not a fifth required rank)

- **Oath-friend of Khuzum-Dur** (Act IV standing win).
- **Puppet-crowned** (Act II vassal ending).
- **Howling convert** (Act V join — Heartland towns hostile).

---

## 6. Simulated ongoing wars (including singleplayer)

The world must **keep fighting** when the player is fishing. This is the MMORPG-scale promise with one human.

### 6.1 Tick

Every **N in-game days** (default 3), for every pair of factions with `treaty = war` or a rolled casus belli:

1. Score each contested province: garrison + nearby lords + terrain + recent player meddling.
2. Resolve **one** battle off-screen unless the player is in that region (then: spawn the live fight or a “join or flee” horn).
3. Apply occupation / exhaustion / tribute.
4. Spawn **news**: messenger NPC, board poster, or camp gossip.

KubeJS, Game Stages, or a tiny custom datapack can own the tick. Recruits NPC teams and MineColonies raids are the *muscles*; they should not be the only brain.

### 6.2 Casus belli the player can cause without meaning to

- Killing a herald.
- Looting a tribute wagon.
- Chopping Greenwood pines.
- Bringing Night Counties stink into Khuzum-Dur.
- Joining a siege “for loot” on the wrong side.

Civ VI grievances, but you **did the crime with your own hands**.

### 6.3 What the player can do to a war they did not start

| Action | Effect |
| --- | --- |
| Join a column | Temporary alliance flag with that host; loot share; standing |
| Run supplies | Faster simulated resolution for the side you fed |
| Assassinate a generic lord | −score for that side on next tick |
| Sign a separate peace as warband leader | You drop out; the *civilizations* may continue |
| Vassalize a loser | You inherit their wars unless the treaty says otherwise |

### 6.4 Singleplayer honesty

No fake “online population.” The **factions** are the other players. Their lords move, their towns flip, their refugees clog *your* favorite road. If the player never leaves Act I, they should still **hear** that Red Keep fell and that Pavlenholt is starving.

---

## 7. Fit with existing campaign docs (do not rewrite acts)

| Campaign beat (`CAMPAIGN.md`) | Diplomacy / lord beat (this file) |
| --- | --- |
| Act I audience with a captain | Conscript → champion; you are **not** at Hildemar’s high table yet |
| Act II pick a patron / puppet | First **vassal or alliance** you actually author |
| Act III living vs dead court | Two civilizations, one province; treaties with one tank standing with the other |
| Act IV oath-friend | Defensive pact with Hold-Kings, not citizenship |
| Act V join the howling | Civilization switch; Heartland **declare war** on you |
| Province win keys | Siege / colony / quest / reputation — diplomacy is how **ally vs occupy vs vassal** is chosen (`CAMPAIGN.md` §6.3) |

Implementation leftovers for the pack agent stay in `CAMPAIGN.md` §7. Mod candidates, versions, and citations live in `FACTION-MODS.md`. Do not duplicate pack pins here.
