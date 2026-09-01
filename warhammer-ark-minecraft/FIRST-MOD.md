# First mod: Rallous Allegiance

**One-liner:** Craft and plant a **warband banner**, claim a camp, gain standing with analogue factions, talk to one data-driven envoy, and save a single **ally/war** flag on the world.

Mod id: `rallous_allegiance` · Maven group: `io.github.honeybadger0489` (or your domain) · MC **1.20.1** · **Forge 47.4.x** · Java **17**.

This is the **first ship**, not the dream. The dream is [CAMPAIGN.md](CAMPAIGN.md) + [FACTIONS-AND-DIPLOMACY.md](FACTIONS-AND-DIPLOMACY.md). Those files stay; this mod is a **ladder rung**.

---

## Why this, not a cool sword

A sword teaches `DeferredRegister<Item>` and a JSON model. You already have Simply Swords in the pack. It does not teach:

| Forge fundamental | Allegiance v1 use |
| --- | --- |
| **Items + blocks** | Banner item → placed camp marker |
| **Data generation** | Recipe, lang, tags, maybe a banner pattern |
| **Datapacks / data-driven JSON** | Faction list (`elector_league`, `hold_kings`, …) without recompiling |
| **SavedData** (world) | Who owns this camp; treaty table |
| **Capabilities** (player) | Per-player standing −100..100 (Forge 1.20.1 caps; NeoForge *attachments* are the 1.21 name for the same idea) |
| **Networking** | Sync standing + war flag to the client for HUD/chat |
| **One NPC interaction** | Envoy: right-click → “swear / defy” |

That set is the **whole** Minecraft-mod career in miniature. It is also the **ASA port lesson**: tribe claim, tribe rank, alliance bit, a replicating actor, a data table of factions. Dinosaur meshes do not port. **State machines do.**

---

## Why not a custom dinosaur first

Fossils and Archeology *already* gives you a tame loop on 1.20.1. A custom Crown-Beast means:

- Blockbench + GeckoLib (or entity renderer) + hitboxes + attributes + AI goals + spawn eggs + loot + animations + sounds + taming food + ride code.
- Weeks before *one* animal feels good.
- Zero practice at **world politics**, which is the fantasy you actually locked (soldier on the ground, lords, alliances).
- ASA later wants Unreal skeletal meshes anyway — Minecraft dino work is a **sunk art pipeline**, not a transferable systems lesson.

Make a dino in **v4**, when Allegiance’s faction id can own a pen.

## Why not a full quest pack first

FTB Quests / Heracles can overlay [CAMPAIGN.md](CAMPAIGN.md) **without your Java**. That is a **content** infinity (five acts × regional boards × warband chores). You will never “finish” it, and you will not learn Forge networking. Quest graphs are **ladder rung 3** (pack integration), after a jar exists that quests can *read* (`rallous:standing`, `rallous:at_war`).

## Why not colonies + guns + Ice and Fire on day one

The pack already tests *feel*. Your mod should not compete with Create and TaCZ. **One** new system. If it needs Epic Fight to exist, it is too big.

---

## Fantasy it *does* express

You are a **conscript who stole a colour**. Planting a banner is how a Total War minor faction *appears on the map*, except the map is a chunk in the Overworld. The envoy is a TWW3/Civ diplomat who **walks**. Ally/war is a treaty you can point at in the log, not a villager gossip meter.

**In-world names only** (see [IP-FANTASY.md](IP-FANTASY.md)):

| Data id | Display |
| --- | --- |
| `elector_league` | Elector League |
| `broken_principalities` | Broken Principalities |
| `night_counties` | Night Counties |
| `hold_kings` | Hold-Kings |
| `frost_marches` | Frost Marches |
| `player_warband` | *your* banner’s name (player-chosen, default “Nameless Company”) |

Do **not** put Empire, Kislev, Dawi, or “Warhammer” in `en_us.json`.

NO MOBA. No lane. No matchmaking. No hero roster UI.

---

## Hard scope (v1)

**In**

- One item: **Warband Banner** (craft: 6 wool + stick, shapeless or a 3×3 that looks like a flag).
- Place on a solid block → **Camp Banner** block (one per player until you add a “relocate” verb).
- World SavedData: camp `BlockPos`, owner UUID, `Map<factionId, Standing>`, `Map<factionId, Treaty>` where Treaty ∈ `{none, alliance, war}`.
- Two datapack JSON files under `data/rallous_allegiance/rallous/factions/*.json` (id, display name, default standing).
- One **Envoy** entity *or* a vanilla villager with a custom brain/profession *or* (fastest) a `PathfinderMob` that stands at the camp and opens a tiny screen. Prefer **data-driven dialogue JSON** over a 40-line hardcoded string.
- One verb: **Alliance** *or* **War** with `elector_league` (not both trees, one path with a deny).
- INFO logs on: claim, treaty change, standing crossing 0. **Not** per tick.
- Client packet: standing + treaty for the focused faction (chat line is enough; HUD is v1.1).

**Out of v1**

- Simulated continent AI, sieges, vassals, tribute wagons, five campaign acts, custom dimensions, guns, tames, quest trees, MineColonies integration, Recruits armies, Mixin into vanilla raids, dedicated server auth mods.

If a feature is not in the milestone list below, it is a **new mod version**, not a “quick add.”

---

## Milestones (days, not a season)

Do them **in order**. Each milestone ends with `./gradlew build` + a `lessons/` note.

### M0 — Hello MDK (day 3 of [BEFORE-YOU-BEGIN.md](BEFORE-YOU-BEGIN.md))

Examplemod title screen. You have not earned a banner yet.

### M1 — Hello item

- Mod id `rallous_allegiance`, creative tab “Rallous.”
- `WarbandBannerItem`. Texture: 16×16 original (Blockbench or GIMP). Lang: `item.rallous_allegiance.warband_banner`.
- `runData` writes the crafting recipe. Prove the JSON appears under `src/generated` or `src/main/resources`.
- **Lesson:** deferred registers, resources, data gen. **ASA transfer:** “engram = item with a recipe unlock.”

### M2 — Persistent world data

- Right-click block on ground → place camp (limit 1). Break = abandon.
- `AllegianceSavedData` on **overworld** `DimensionDataStorage` ([Forge Saved Data](https://docs.minecraftforge.net/en/1.20.1/datastorage/saveddata/)). `setDirty()` on every change.
- Restart the client. Camp still yours. `/kill` is irrelevant; **stop the JVM** to prove disk.
- Capability on the **player**: standing map; copy on `PlayerEvent.Clone` so death does not wipe politics ([Capabilities](https://docs.minecraftforge.net/en/1.20.1/datastorage/capabilities/)).
- Logger: `Rallous allegiance: claimed camp at x y z by uuid`.
- **Lesson:** server authority, NBT, dirty flags. **ASA transfer:** savegame `UObject` + `SaveGame` / tribe manager. Disk is a feature.

### M3 — One NPC interaction

- Spawn or walk-up **Envoy of Vellbruck** (display name only) at the camp when claimed — or summon with an item “Sealed Letter” to keep spawn simple.
- Right-click: four lines of text, two buttons: *Hear the Elector* / *Dismiss*.
- No shops. No quest IDs. A `Dialogue` JSON: `id`, `lines[]`, `options[]`.
- **Lesson:** entity or menu + `SimpleChannel` packet “open dialogue.” **ASA transfer:** interactable NPC pawn + Widget. The JSON file is the same idea as a DataTable row.

### M4 — One diplomacy verb (ally **or** war)

- Option on the envoy: **Swear open roads** (treaty=`alliance`) **or** **Defy the League** (`war`). One is enough; implement the other as a stub that logs `not in v1`.
- Persist on SavedData. Broadcast a chat message to the player. Log at INFO: `treaty elector_league alliance`.
- Optional: if `war`, make League-coloured team / vanilla `Player#setLastHurtByMob` irrelevant — even a `Mob#setTarget` on a dyed zombie is *too much*. **Chat + log + NBT is the verb.** Visual soldiers wait for Recruits overlay later.
- **Lesson:** enum state machine, never toggle 20 booleans. **ASA transfer:** `ETribeAlliance` byte on the tribe manager; replicate it.

**v1 is done** when a friend can clone the MDK, `runClient`, craft the banner, plant it, click the envoy, and after a restart still be at war or allied. Then you write `lessons/00x-allegiance-v1-shipped.md` and **stop coding for a day**.

---

## Suggested packages (do not bikeshed)

```text
io.github.honeybadger0489.rallousallegiance
  RallousAllegiance.java          // @Mod
  registry/ModItems.java
  registry/ModBlocks.java
  registry/ModEntities.java       // M3
  world/AllegianceSavedData.java  // M2
  cap/StandingCapability.java     // M2
  net/ModNetworking.java          // M3–M4
  data/FactionDefinition.java     // datapack JSON
  client/...                      // screens, only what M3 needs
```

Datapack:

```text
data/rallous_allegiance/rallous/factions/elector_league.json
```

Keep faction *design* in `FACTIONS-AND-DIPLOMACY.md`; keep faction *runtime ids* in JSON. When they drift, the JSON wins in-game, the markdown wins in the design review — then you sync them in a lesson, not in a silent rename.

---

## Pack integration (not v1, but the next rung)

After the jar builds:

1. Drop it in a **dedicated** Prism instance (mod + Forge, no kitchen sink).
2. Then a second instance: Frontier pack + your jar. Watch for ID conflicts (`rallous_allegiance` vs OPAC claims).
3. A datapack-only prototype of *standing as scoreboards* can exist **before** M2 as a throwaway — see ladder in [ORGANIZATION.md](ORGANIZATION.md). If you already know scoreboards, skip to Java; do not ship scoreboards as the final politics.

---

## Port sheet (pin this in every Allegiance lesson)

| Minecraft / Forge | ARK: Survival Ascended (later) | Other engines |
| --- | --- | --- |
| `SavedData` on overworld | Tribe / game-state subsystem, savegame | Unity `ScriptableObject` + save blob; Unreal `SaveGame` |
| Player capability / (NeoForge attachment) | Player state component, replicated | Unity component; Unreal Actor Component |
| `SimpleChannel` packet | Unreal RPC / NetUpdate | Mirror/Netcode / custom |
| Datapack JSON factions | UE DataTable / JSON in mod pak | Addressable JSON |
| Banner block as claim | Flag / totem / tribe totem actor | “Capture point” with an owner id |
| Envoy dialogue JSON | Widget + data rows | Yarn/Ink, then *throw away* the tool if it fights source control |

The transferable sentence: **owner id + standing int + treaty enum + a replicating talker.** Not the wool texture.

---

## Sources (accessed 2026-08-31)

- https://docs.minecraftforge.net/en/1.20.1/gettingstarted/
- https://docs.minecraftforge.net/en/1.20.1/items/
- https://docs.minecraftforge.net/en/1.20.1/datagen/
- https://docs.minecraftforge.net/en/1.20.1/datastorage/saveddata/
- https://docs.minecraftforge.net/en/1.20.1/datastorage/capabilities/
- https://docs.minecraftforge.net/en/1.20.1/networking/
- Design: [FACTIONS-AND-DIPLOMACY.md](FACTIONS-AND-DIPLOMACY.md) §1–§2, [CAMPAIGN.md](CAMPAIGN.md) §2
