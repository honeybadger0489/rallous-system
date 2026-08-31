# Curated pack — Rallous Frontier 0.1.0

**Target:** Minecraft **1.20.1** + **Forge 47.4.0** (47.4.x, Java 17)  
**Name:** Rallous Frontier (original setting; not Games Workshop, not Studio Wildcard)  
**Import:** [IMPORT.md](IMPORT.md) · files in [pack/](pack/)

## Why this version and loader

1. **Creature + combat overlap is unique to 1.20.1 Forge.** Fossils 9.3.4, Cataclysm 3.31, Epic Fight 20.14, TaCZ 1.1.8, Create 6.0.8, LSO 2.4.7, Hammercraft (if you ever risk it) all live here.
2. **Fabric** cannot run Epic Fight or Alex’s Caves; **1.21.1 NeoForge** still lags this exact creature mix.
3. **1.20.1 is still the overhaul sweet spot** in 2026 (C2E2, Hollowreach-style rebuilds, Chaos/Titan kitchen sinks). Details: [RESEARCH.md](RESEARCH.md).

Allocate **8 GB** RAM minimum; **10–12 GB** if you later add Ice and Fire or Ad Astra.

---

## Gameplay pillars (what every mod must serve)

| Pillar | In-game feel | Default mods |
| --- | --- | --- |
| Grimdark world | Ugly beauty, bad nights, cathedral ruins | Born in Chaos, Cataclysm, Dungeons Arise, YUNG’s, Enhanced Celestials, Terralith |
| Prehistoric / alien fauna | The island has a food chain above you | Fossils & Archeology, Alex’s Mobs, Alex’s Caves |
| Taming | You don’t craft a mount, you *earn* one | Fossils loop + Tameable Beasts |
| Tribes / factions | Named warbands, claimed land | Open Parties and Claims |
| Brutal survival | Heat, thirst, seasons, food that matters | LSO + Serene Seasons + Farmer’s Delight |
| Gothic / industrial bases | Hive-city masonry + brass machinery | Create, Chipped, Architect’s Palette, Macaw’s, Supplementaries |
| Weapons that feel 40k *or* fantasy-Warhammer | Weight of plate, roar of a heavy gun | Epic Fight, Simply Swords, TaCZ; add Magistu from CurseForge |

---

## How to import

See **[IMPORT.md](IMPORT.md)** for Prism, Modrinth App, CurseForge App, packwiz, and the CDN script.

Default pack is **69 files** (63 mods + 5 resource packs + 1 shader) pinned in `pack/modrinth.index.json`. Magistu’s Epic Knights is the one extra **CurseForge-only** add (id `509041`).

---

## Tiered list

Versions below are **Modrinth 1.20.1 Forge pins from 2026-08-31**. Refresh with `python3 scripts/generate-pack.py`.

### Must-have (boot these first)

**Libraries:** JEI `15.56.0.205` · Jade `11.13.3` · Cloth Config `11.1.136` · Architectury `9.2.14` · GeckoLib `4.8.4` · Citadel `2.6.3` · Curios `5.14.1` · Player Animator `1.0.2-rc1` · Kotlin for Forge `4.12.0` · Lionfish API `3.0` · Moonlight Lib `2.16.34` · YUNG’s API `4.0.6`

**Performance:** Embeddium `0.3.31` · Oculus `1.8.0` · FerriteCore `6.0.1` · ModernFix `5.27.83` · Entity Culling `1.10.5`

**Creatures / world:** Fossils and Archeology Revival `9.3.4.0` · Alex’s Mobs `1.22.9` · Alex’s Caves `2.0.2` · Born in Chaos `1.7.5` · L_Ender’s Cataclysm `3.31` · Terralith `2.5.4` · When Dungeons Arise `2.1.58`

**Combat / survival / tribes:** Epic Fight `20.14.17` · Simply Swords `1.70.2` · TaCZ `1.1.8-hotfix` · Legendary Survival Overhaul `2.4.7` · Serene Seasons `9.1.0.3` · Farmer’s Delight `1.20.1-1.3.4` · Open Parties and Claims `0.30.3`

**Bases:** Create `6.0.8` · Supplementaries `3.1.43` · Chipped `3.0.7`

**Look:** Grimdark Sky `1.1` · Grimdark Battlepack `2.7` · Complementary Unbound `r5.8.1`

### Strongly recommended (in the default mrpack)

Tameable Beasts `7.1.3` · Malum `1.6.7` · Enhanced Celestials `5.0.3.3` · YUNG’s Better Dungeons / Nether Fortresses / Strongholds · Towns and Towers `1.12` · Structory `1.3.5` · Explorify `v1.6.5` · Amendments `2.2.6` · Architect’s Palette `1.3.6.1` · Macaw’s Windows/Roofs/Bridges · Another Furniture `3.0.4` · Decorative Blocks `4.1.3` · ETF `7.1` + EMF `3.2.4` + Continuity `3.0.0` · Faithful 32x `1.20.1-june-2026` · Fresh Animations `1.10.4` · Controlling + Searchables + Mouse Tweaks + Carry On + AppleSkin · Sophisticated Core + Backpacks · Puzzles Lib · Gothic RPG Font

**CurseForge-only (add by hand):** Epic Knights (Magistu) — `epic-knights-armor-and-weapons` **509041**, 1.20.1 Forge 10.11 (2026-03-14).

### Optional (listed in catalog, **not** in default mrpack)

| Mod | Why wait |
| --- | --- |
| Immersive Engineering `10.2.0-183` | Noisy next to Create 6 |
| Create: Steam ’n Rails, Immersive Aircraft, Create Big Cannons | Transport/artillery after the loop is fun |
| Hardcore Torches, Spice of Life Apple Pie | Extra primitive friction |
| Iron’s Spellbooks `3.16.3` | Psyker fantasy; can steal the spotlight |
| Parcool | Already in default; disable if it fights Epic Fight |

### Later / separate instance

| Mod | Why not now |
| --- | --- |
| Ice and Fire `2.1.13-beta-5` | 2024 beta, dragon lag, worldgen fights |
| Prehistoric Fauna `2.3.3` | Time-travel dimensions ≠ Fossils revival |
| Jurassic Revived `0.215.0` | Park game; pick this *or* Fossils |
| Ad Astra, Deeper and Darker, Undergarden | Extra dimensions after the Overworld is deadly enough |
| Better Combat | Conflicts with Epic Fight |
| Tough As Nails / Cold Sweat | Conflicts with LSO |
| MineColonies | NPC city sim; CurseForge/FTB, not in this mrpack |

### IP overlay (**never** in default)

Hammercraft 40k `1.0.6` · Tacz40k `2.0.0` · Sons of the Empire `1.1.9` · create-warhammer · Ultimate warhammer 40k  

Read [LEGAL-NOTES.md](LEGAL-NOTES.md) before you even search these in a launcher.

---

## Compatibility notes

| Do not combine | Prefer |
| --- | --- |
| Fossils + Jurassic Revived + Jurassic Reborn + Prehistoric Fauna | **Fossils only** |
| LSO + Tough As Nails + Cold Sweat + Thirst Was Taken | **LSO only** |
| Epic Fight + Better Combat | **Epic Fight only** (or add a dedicated compat mod later) |
| Terralith + Biomes O’ Plenty + Oh The Biomes We’ve Gone | **Terralith only** |
| Grimdark Sky + Dramatic Skys | **Grimdark Sky** |
| TaCZ + Point Blank | **TaCZ only** |
| Create 6 + legacy Flywheel jar | Create 6 only |
| Oculus + OptiFine | **Oculus + Embeddium** |
| Tameable Beasts default config + Fossils dinos | Blacklist Fossils entities if taming becomes trivial |
| Magistu steel + other steel mods | Magistu claims it won’t conflict; still test recipes |
| ParCool vaulting + Epic Fight combat mode | Rebind or disable ParCool if animations desync |

Cataclysm needs **Lionfish API + Curios + GeckoLib**. Alex’s mods need **Citadel**. Supplementaries needs **Moonlight**. Sophisticated Backpacks needs **Sophisticated Core**. Controlling needs **Searchables**. Fresh Animations needs **ETF + EMF**.

First-boot checklist: JEI loads, a dinosaur egg recipe exists, a Cataclysm dungeon locates, thirst/temp HUD from LSO appears, TaCZ gun table works, shader compiles.

---

## Texture pack + shader pairing

**Stack (top = wins):**

1. Gothic RPG Font  
2. Grimdark Sky Pack  
3. Grimdark Battlepack  
4. Fresh Animations  
5. Faithful 32x  

**Shader:** Complementary **Unbound** r5.8.1 (darker, more “ash world”). Switch to **Reimagined** if Unbound is too muddy; **BSL 10.1.3** if you want a different contrast curve.

Tune Unbound: raise fog a little, drop bloom, keep shadows long. Pair with Enhanced Celestials blood moons.

Battlepack anvil variants want CIT. On Forge+Oculus that is weaker than OptiFine — expect the default Battlepack look, not every named variant.

Thalyrus II is a **replace Faithful** option (full medieval), not an overlay.

---

## Bridge to ARK: Survival Ascended

Conceptual only. Do not copy Ark assets into Minecraft or GW assets into ASA.

| Rallous Minecraft (now) | Rallous ASA (later) |
| --- | --- |
| Fossils DNA/embryo/tame | Knockout taming + imprint + cryopods for **original** beasts |
| Open Parties and Claims | Tribes, tribe ranks, alliance/war, claimed land |
| LSO thirst/temp/limbs | ASA heat/torpor/food as-is; add a **corruption/warp-tide** status (original) |
| Create factories + gothic blocks | Engram tree: primitive → chapter-forge → void-foundry |
| TaCZ original guns | ASA weapon BP + attachments; **no bolter names** |
| Epic Knights plate | Flak / carapace **analogues** with original silhouettes |
| Cataclysm bosses | Boss creatures / titans as map threats |
| Terralith + Alex’s Caves | Custom biomes / “death world” maps in DevKit |
| Blood moons (Enhanced Celestials) | Scheduled world event (red dusk, spawn spike) |
| Chapter as tribe name | Tribe cosmetics, banners, ranks (Sergeant, etc. — original titles) |

ASA official path: Unreal DevKit → CurseForge cloud cook → optional premium review. Wildcard **forbids unlicensed third-party IP** in mods. GW forbids unlicensed games using their setting. The portable product is **Rallous System**, not a 40k total conversion and not “Ark with Space Marines.”

---

## Top 10 mods (if you only remember ten)

1. Fossils and Archeology: Revival  
2. Legendary Survival Overhaul  
3. Epic Fight  
4. L_Ender’s Cataclysm  
5. Alex’s Caves  
6. TaCZ  
7. Create  
8. Open Parties and Claims  
9. Born in Chaos  
10. Simply Swords *(plus Magistu from CurseForge as #11)*

## Top 3 texture packs

1. **Grimdark Battlepack**  
2. **Grimdark Sky Pack**  
3. **Faithful 32x** (base)

Shader: Complementary Unbound.

## Closest existing modpacks (ideas, not installs)

RLCraft (fear) · DawnCraft (Epic Fight RPG) · Craft to Exile 2 (1.20.1 ARPG integration) · Hollowreach (RLCraft ideas on 1.20.1) · Titans of the Void (grim magic). None of them are this hybrid — that’s the point of this kit.
