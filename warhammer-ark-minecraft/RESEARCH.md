# Research notes — Rallous Frontier (Minecraft)

Accessed **2026-08-31**. Live sources: Modrinth API (`api.modrinth.com/v2`), CurseForge project pages + [CFWidget](https://api.cfwidget.com), official legal pages, project sites. Bright Data MCP search/scrape returned **HTTP 401** in this environment, so SERP/scrape tools were not used; Web search + direct APIs/pages filled in.

This is a survey for a **Warhammer-tone × Ark-survival** Minecraft prototype. Default recommendations live in [CURATED-PACK.md](CURATED-PACK.md). Version pins: [pack/mods.json](pack/mods.json) (generated 2026-08-31).

---

## Loader and version landscape

| Loader | 1.20.1 reality (2026) | Fit for this vision |
| --- | --- | --- |
| **Forge** | Still the densest pool of *content* mods (creatures, Epic Fight, Cataclysm, Fossils, Create 6, TaCZ, LSO). | **Recommended.** |
| **NeoForge** | Default on 1.21.1; some 1.20.1 jars are dual-loader. Hammercraft has a 1.21.1 NeoForge line. | Future port, not v0.1. |
| **Fabric / Quilt** | Best visual/QoL stack (Iris/Sodium native). Missing Epic Fight, Alex’s Mobs/Caves, Cataclysm, Ice and Fire. Fossils *does* ship Fabric. | Wrong ecosystem for this hybrid. |
| **Sinytra Connector** | Fabric-on-Forge bridge. Fragile for a first overhaul. | Avoid until the Forge pack is stable. |

**Why 1.20.1:** large-pack consensus through 2025–2026 (Craft to Exile 2, ATM9-era leftovers, Titan/Chaos overhauls, Hollowreach-style RLCraft rebuilds). 1.21.1 is healthier for *new* NeoForge work but still missing or beta-quality on several creature/combat pillars.

Sources:

- Craft to Exile 2, CurseForge — 1.20.1 Forge, updated 2025-11-06. https://www.curseforge.com/minecraft/modpacks/craft-to-exile-2 — accessed 2026-08-31
- DawnCraft, CurseForge — still **1.18.2** Forge (2.0.16_hf, 2025-11-20), not 1.20.1. https://www.curseforge.com/minecraft/modpacks/dawn-craft — accessed 2026-08-31
- RLCraft, CurseForge — still **1.12.2**. https://www.curseforge.com/minecraft/modpacks/rlcraft — accessed 2026-08-31
- Hollowreach (community 1.20.1 RLCraft rebuild) — Forge 47.4.10. https://www.modpackindex.com/modpack/158774/hollowreach — accessed 2026-08-31
- Epic Fight wiki — Forge/NeoForge only, not Fabric. https://www.minecraft-guides.com/mod/epic-fight/ — accessed 2026-08-31

Pinned **Forge 47.4.0** in pack metadata; 47.4.10 is equally fine.

---

## Warhammer / grimdark

### Direct 40k / Warhammer-branded (legal-risk overlay, not default)

| Project | Platform | 1.20.1 loader | Last seen | Notes |
| --- | --- | --- | --- | --- |
| **Hammercraft 40k** | CurseForge `wh40kmc-project` (id **964310**), Modrinth `hammercraft40k` | Forge | Modrinth **1.0.6** (2026-02-14); CF also lists 1.21.1 NeoForge | Full 40k factions/armor/weapons. License **All Rights Reserved** on CF; Modrinth copy tagged MIT (treat as GW-derived anyway). |
| **Tacz40k** | Modrinth `tacz40k` | Forge | 2.0.0 (2026-02-15) | Gunpack for TaCZ. GW firearms/names. |
| **Warhammer: Sons of the Empire** | Modrinth `warhammer-sons-of-the-empire` | Forge | 1.1.9 (2025-07-19) | ARR. Fantasy/empire branding. |
| **create: warhammer** | Modrinth `create-warhammer` | Forge | 1.0.0 (2025-01-17) | Create addon, ARR. |
| **Ultimate warhammer mod** | Modrinth `ultimate-warhammer-40k` | Forge | 1.0.0 (2025-08-20) | Tiny download count; ARR. |

Sources:

- Hammercraft 40k, CurseForge. https://www.curseforge.com/minecraft/mc-mods/wh40kmc-project — accessed 2026-08-31
- Hammercraft 40k, Modrinth. https://modrinth.com/mod/hammercraft40k — accessed 2026-08-31
- Tacz40k, Modrinth. https://modrinth.com/mod/tacz40k — accessed 2026-08-31
- MC百科 Hammercraft. https://www.mcmod.cn/class/14110.html — accessed 2026-08-31

**Age of Sigmar:** no healthy, complete AoS conversion showed up on Modrinth 1.20.1 search. Fantasy-Warhammer tone is better served by **Epic Knights (Magistu)**, **Simply Swords**, **Born in Chaos**, **Cataclysm**, **When Dungeons Arise**, **Malum**.

### Original grimdark (use these)

| Project | Slug | 1.20.1 pin (2026-08-31) | Why it fits |
| --- | --- | --- | --- |
| L_Ender's Cataclysm | `l_enders-cataclysm` / CF `lendercataclysm` **551586** | **3.31** (2026-06-14) | Titan-scale bosses as Carnifex / greater-daemon *analogues*. |
| Born in Chaos | `borninchaos` / CF `born-in-chaos` **686437** | **1.7.5** (2026-04-12) | Night-raid hostiles, grim structures. |
| Epic Fight | `epic-fight` / CF `epic-fight-mod` **405076** | **20.14.17** (2026-05-06) | Weight, stamina, stance — “chapter sergeants,” not click-spam. |
| Simply Swords | `simply-swords` **659887** | **1.70.2** (2026-08-27) | Relic weapons, runic powers. Original art. |
| Epic Knights (Magistu) | CF only `epic-knights-armor-and-weapons` **509041** | CF file 10.11 (2026-03-14) | Gothic plate, polearms, bannered horse armour. **Not on Modrinth.** |
| Malum | `malum` | **1.20.1-1.6.7** (2025-06-13) | Spirit harvest / forbidden metal. Warp-adjacent without GW names. |
| Enhanced Celestials | `enhanced-celestials` | **5.0.3.3** | Blood moons as “warp tide.” |
| When Dungeons Arise | `when-dungeons-arise` | **2.1.58** | Cathedral-scale ruins. |
| Iron’s Spells | `irons-spells-n-spellbooks` | **3.16.3** (2026-08-18) | Optional psyker kit. Skip if you want guns+melee only. |
| TaCZ | `timeless-and-classics-zero` / CF **1028108** | **1.1.8-hotfix** (2026-05-25) | Gun *framework*. Custom original gunpacks later; **not** Tacz40k. |

Sources:

- Cataclysm, CurseForge. https://www.curseforge.com/minecraft/mc-mods/lendercataclysm — accessed 2026-08-31
- Epic Knights, CurseForge. https://www.curseforge.com/minecraft/mc-mods/epic-knights-armor-and-weapons — accessed 2026-08-31
- TaCZ, CurseForge. https://www.curseforge.com/minecraft/mc-mods/timeless-and-classics-zero — accessed 2026-08-31
- Better Combat × Epic Fight Compat (only if you insist on both). https://www.modpackindex.com/mod/170142/better-combat-epic-fight-compat — accessed 2026-08-31

Create + Chipped + Architect’s Palette + Macaw’s + Supplementaries cover **gothic-industrial** bases without a 40k furniture pack.

---

## Ark-like: creatures, taming, survival

### Dinosaur / prehistoric

| Project | Status | 1.20.1 | Taming? | Verdict |
| --- | --- | --- | --- | --- |
| **Fossils and Archeology: Revival** | Alive. CF id **223908**, Modrinth `fossils-and-archeology-revival` | **9.3.4.0** Forge *and* Fabric (2026-06-08) | DNA → embryo → creature; ride/tame loop | **Default pick.** Closest “Ark on Minecraft.” |
| **Jurassic Revived** | JurassiCraft successor after JC went private | **0.215.0** Forge (2026-06-06); NeoForge 1.21.1 | Park/DNA, GeckoLib | Alternate instance, not mixed with Fossils. |
| **Jurassic Reborn** | Separate park mod, ARR | **1.3.44** (2026-03-31) | Park loop | Don’t stack. |
| **Prehistoric Fauna** | Superlord, CF **311600** | **2.3.3** (2025-03-14) | Ecosystem dimensions; **not** classic taming | Expedition pack, not default. |
| **JurassiCraft (classic)** | Downloads disappeared / private | — | — | **Abandoned.** Use Jurassic Revived if you want that fantasy. |
| **Prehistoric Dinosaurs** | Modrinth `prehistoric-dinosaurs` | Fabric-only on 1.20.1 | — | Wrong loader. |
| **Ice and Fire: Dragons** | CF **264231**, Modrinth `ice-and-fire-dragons` | **2.1.13-1.20.1-beta-5** (2024-08-15) | Dragon taming | **Stale beta.** Optional later. Citadel required. |

Sources:

- Fossils 9.3.4.0, CurseForge. https://www.curseforge.com/minecraft/mc-mods/fossils — accessed 2026-08-31
- Jurassic Revived site. https://jurassicrevived.com/ — accessed 2026-08-31
- Jurassic Revived GitHub. https://github.com/classic-mods-revived/Jurassic-Revived — accessed 2026-08-31
- Prehistoric Fauna wiki (limited taming). https://prehistoric-fauna-mod.fandom.com/wiki/Mobs — accessed 2026-08-31
- Ice and Fire files. https://www.curseforge.com/minecraft/mc-mods/ice-and-fire-dragons — accessed 2026-08-31

### Other fauna / taming

| Project | Pin | Notes |
| --- | --- | --- |
| Alex’s Mobs | **1.22.9** (2024-09-06) | 80+ purposeful mobs. Citadel. Still the 1.20.1 standard despite last update 2024. |
| Alex’s Caves | **2.0.2** (2024-10-26) | Magnetic/toxic/primordial caves — “xenos biome” without 40k names. |
| Tameable Beasts | **7.1.3** (2026-01-02) | Extra tames/mounts. Tune config so Fossils dinos stay special. |
| Salvation & Sacrifice | GitHub Forge 1.20.1 | Universal taming/riding framework for pack authors. Not in default mrpack (manual). https://github.com/Ku00115/Salvation-and-Sacrifice-Forge |

### Survival needs (Ark “you will die of heat and thirst”)

| Project | Pin | Use? |
| --- | --- | --- |
| **Legendary Survival Overhaul** | **2.4.7** (2026-08-09) | **Default.** Temp + thirst + body health. Integrates Serene Seasons, Farmer’s Delight, Cataclysm, Born in Chaos, Ice and Fire. |
| Serene Seasons | **9.1.0.3** (2026-06-14) | Seasons → LSO climate. |
| Farmer’s Delight | **1.20.1-1.3.4** (2026-08-29) | Cooking / tribe kitchen. |
| Tough As Nails | 9.2.0.171 | **Do not stack with LSO.** |
| Cold Sweat | 2.4.2 | Temp-only; **do not stack with LSO.** |
| Thirst Was Taken | 1.4.0 | **Do not stack with LSO.** |
| Spice of Life: Apple Pie Edition | 2.3.1 | Diet diversity. Optional later. Classic SOL Carrot is not current on Modrinth 1.20.1. |
| Hardcore Torches | 1.20.1-x | Primitive lighting. Optional. |
| **Primitive Survival (Minecraft)** | — | **Does not exist** as a maintained MC mod. The well-known *Primitive Survival* is a **Vintage Story** mod. https://mods.vintagestory.at/primitivesurvival — accessed 2026-08-31 |

LSO integration list (Ice and Fire, Cataclysm, Born in Chaos, Farmer’s Delight, Serene Seasons, Create, …): https://github.com/sfiomn/LegendarySurvivalOverhaul — accessed 2026-08-31

### Tribes / claims

| Project | Pin | Notes |
| --- | --- | --- |
| **Open Parties and Claims** | **0.30.3** (2026-08-20) | Default tribe analogue. |
| FTB Teams / Chunks | — | Not on Modrinth under the old slugs (CurseForge / FTB App). Use if you also want FTB Quests. |
| MineColonies | 0 Forge files on Modrinth for 1.20.1 in this pull | NPC colony sim — later, via CurseForge, if you want “chapter keep” NPCs. |

---

## Texture / resource packs and shaders

| Pack | Slug | 1.20.1 pin | Role |
| --- | --- | --- | --- |
| Grimdark Sky | `grimdark-sky` (CF `grimdark-sky`) | **v1.1** | Chaos moon, exoplanets. Needs custom sky (Oculus/OptiFine). |
| Grimdark Battlepack | `battlepack` | **v2.7** | Armor/weapon variants; CIT for anvil names. |
| Grimdark Pirate / Samurai / Viking | `pirate`, `samurai`, `viking` | 1.4 / 2.7 / … | Subsets of Battlepack. Don’t need all if Battlepack is in. |
| Faithful 32x | `faithful-32x` | **1.20.1-june-2026** | Base 32x. |
| Fresh Animations | `fresh-animations` | **1.10.4** | Needs ETF + EMF. |
| Gothic RPG Font | `gothic-rpg-font` | **1.0.0** | Tiny UI flavour. |
| Thalyrus II | `thalyrus2` | **0.5a** | Full medieval overhaul — **alternative** to Faithful, not a stack. |
| Dramatic Skys | `dramatic-skys` | **1.5.3.36.5** | Conflicts with Grimdark Sky. |
| Complementary Unbound | `complementary-unbound` | **r5.8.1** (2026-05-21) | Default shader (darker). |
| Complementary Reimagined | `complementary-reimagined` | **r5.8.1** | Brighter twin. |
| BSL | `bsl-shaders` | **10.1.3** | Alternate look. |

Forge shader stack: **Embeddium 0.3.31** + **Oculus 1.8.0** (Iris/OptiFine loaders on Complementary). Official Complementary site lists r5.8.1 for Java 1.8.9–1.21.x. https://complementaryshaders.com/ — accessed 2026-08-31

Grimdark Sky, Modrinth. https://modrinth.com/resourcepack/grimdark-sky — accessed 2026-08-31  
Kal’s Grimdark Sky, CurseForge. https://www.curseforge.com/minecraft/texture-packs/grimdark-sky — accessed 2026-08-31

**Mythic** (32x dark-fantasy, third-party texture index) was **not** on Modrinth under `mythic` — skip unless you fetch from the author’s official page later.

---

## Existing modpacks closest to the vision

None are “Warhammer × Ark.” Steal **structure**, not files.

| Pack | Version | Steal this | Leave this |
| --- | --- | --- | --- |
| **RLCraft** | 1.12.2 Forge | Fear, thirst/temp, dragons as apex, “the world is unfair” | Ancient version; don’t copy configs blindly. |
| **Hollowreach** | 1.20.1 Forge 47.4.10 | How to rebuild RLCraft *ideas* on 1.20.1 | It’s a full pack; don’t merge jars. |
| **DawnCraft** | 1.18.2 | Epic Fight + quests + reputation + boss roster | Stuck on 1.18.2. |
| **Craft to Exile 2** | 1.20.1 Forge (1.1.3, 2025-11-06) | ARPG loot, datapack integration, Mine and Slash | Diablo, not dinosaurs. |
| **Titans of the Void: Ascension** | 1.20.1 Forge ~350 mods | Iron’s Spellbooks + Malum + Voidscape as “warp” | Wizard power fantasy can drown survival. |
| **Dark Chaos Ascension** | 1.20.1 Forge 47.4.10, ~179 mods | First Aid + Reskillable + dragons | Overlap with LSO if combined. |
| **Better Minecraft / Valhelsia / ATM9 / Vault Hunters** | 1.20.x kitchen sinks | Kitchen-sink *quality* (performance mods, quests) | Too cheerful / too expert-tech / too vault-raid. Ideas only. |

Sources: CurseForge pack pages cited above; Titans of the Void — https://www.modpackindex.com/modpack/157516/titans-of-the-void-ascension — accessed 2026-08-31

---

## Abandoned / incompatible / legal-risk (do not put in v0.1)

| Item | Why |
| --- | --- |
| JurassiCraft (classic) | Private / vanished downloads. |
| Ice and Fire 1.20.1 | Still **beta**, last meaningful file 2024. |
| Primitive Survival (MC) | Not a Minecraft mod (Vintage Story). |
| RLCraft / DawnCraft as a base | Wrong MC version. |
| Fabric-first creature packs | Missing Epic Fight, Alex’s, Cataclysm. |
| Hammercraft, Tacz40k, Sons of the Empire, create-warhammer, Ultimate 40k | **Games Workshop: “must not create computer games or apps based on our characters and settings”** without a licence. |
| Mixing Fossils + Jurassic Revived + Reborn + Prehistoric Fauna | Spawn/DNA/entity pile-up. |
| LSO + TAN + Cold Sweat + Thirst Was Taken | Duplicate vitals. |
| Epic Fight + Better Combat | Needs an extra compat mod; skip for v0.1. |
| Terralith + BOP + Oh The Biomes We’ve Gone | Biome soup. |
| TaCZ + Vic’s Point Blank | Scope/zoom bugs reported. https://github.com/MCModderAnchor/TACZ/issues/442 — accessed 2026-08-31 |
| Legacy Flywheel + Create 6 | Create 6.0.8 bundles rendering; extra Flywheel jars fight it. |
| OptiFine + Oculus | Pick Oculus. |
| Third-party dump sites (9Minecraft, etc.) | Use Modrinth/CurseForge only. |

---

## Open-source / GitHub landmarks

- Jurassic Revived — https://github.com/classic-mods-revived/Jurassic-Revived  
- TaCZ — https://github.com/MCModderAnchor/TACZ  
- Legendary Survival Overhaul — https://github.com/sfiomn/LegendarySurvivalOverhaul  
- Salvation & Sacrifice (universal tame/ride) — https://github.com/Ku00115/Salvation-and-Sacrifice-Forge  

GitHub MCP was unavailable in this run; `gh search` returned empty (auth/scope). URLs above come from project pages.

---

## What Minecraft modding can actually do (capability map)

Useful for “can we even prototype this in MC?”

| Fantasy | Minecraft lever |
| --- | --- |
| Chapter / tribe | Open Parties and Claims (later: custom datapack ranks) |
| Tame apex fauna | Fossils revival + Tameable Beasts + (later) Salvation framework |
| Death-world climate | LSO + Serene Seasons + Alex’s Caves biomes |
| Gothic hive-city | Create + Chipped + Dungeons Arise + Terralith peaks |
| Bolter-feel guns | TaCZ gunpacks (original models) |
| Power armour gait | Epic Fight + heavy Epic Knights sets |
| Warp corruption | Malum / blood moons / Born in Chaos night spawns (custom status later) |
| Engram-like unlocks | FTB Quests / datapacks / Create sequenced recipes (not in v0.1) |
| Dedicated server tribes | Same Forge pack minus client visual mods |

Custom Java mods (Rallous species, knockout taming, corruption meter) are a **later** step. This pack is the mood board you can boot tonight.

Machine-readable pins and hashes: [pack/resolved.json](pack/resolved.json).
