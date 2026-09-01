# Villages — Millénaire analogue (live, 2026-09-01)

What can actually ship in **this** 1.20.1 Forge Warhammer pack without forty new mods. Bright Data SERP returned HTTP 401 in this environment; pins below are from Modrinth API, CurseForge `/api/v1/mods/{id}/files`, GitHub `ldtteam/minecolonies` releases, and `pack/curseforge-resolved.json`.

## Verdict

**Ship `rallous_grow`.** The 7×7 crash camp grows when you help, win `rallous.session`, or spend emeralds. One well-known colony sim (MineColonies) **does** have 1.20.1 Forge fileIDs, but it is a five-jar overlay that fights Recruits as a second capital. Catalog entries are pinned for a later opt-in. They are **not** in the 0.3.6 default zip.

## Live research

| Mod | 1.20.1 Forge? | In this pack tonight? | Millénaire job |
| --- | --- | --- | --- |
| **MineColonies** | **Yes, CurseForge only.** Modrinth project `sSr0QEGx` is stale (1.18.2, updated 2023-07-19, **0** Forge 1.20.1 versions). CF project **245506**. Release `minecolonies-1.20.1-1.1.1276.jar` **fileID 8615315** (2026-08-10). Latest snapshot `1.1.1280` **fileID 8775822** (2026-08-31). GitHub tag `v1.20.1-1.1.1280-snapshot`. ~74MB. | Catalog only (`include_in_default: false`). | True growing colony. Needs **Structurize 298744 / fileID 8610456** (1.0.818), **BlockUI 522992 / fileID 7541343** (1.0.193), **Domum Ornamentum 527361 / fileID 7585567** (1.0.296), **MultiPiston 303278 / fileID 5204918** (1.2.43-RELEASE). TownTalk showed on some file cards; GitHub 1280 required-deps list does **not** include it. |
| **Millénaire ports** | Official site: **1.12 Forge** and **1.21.1 NeoForge** (`millenaire.org`). GitHub rewrite (WangMioG / JasonCian) targets Forge 1.20.1 but is **not** a Modrinth/CF pack pin. | **Do not add.** | The fantasy we want. Not shippable as a jar tonight. |
| **Villager Recruits** | Yes. Modrinth `2zXpVxK4` = `recruits-1.20.1-1.15.2.jar` (2026-06-29). CF **523860 / fileID 8339846**. | **Already in 0.3.6.** Claims, banners, hire, siege. | Army + province claim. Not village *growth*. |
| **Guard Villagers** | Yes. Modrinth `zCzBkn3R` = `guardvillagers-1.20.1-1.6.19.jar` (2026-08-23). CF **360203 / fileID 8719057**. | **Already in 0.3.6.** | Occupied Towns-and-Towers villages fight. No build-as-you-help. |
| **Towns and Towers** | Yes. Modrinth `7ZwnSrVW` = `Towns-and-Towers-1.12-Fabric+Forge.jar` (2023-12-03). Already in `pack/mods.json`. | **Already in the pin.** | Architecture. Static structures. |

## Why MineColonies is catalog-only

Recruits is already the Elector / Waaagh / Under-Empire banner layer. `FACTION-MODS.md` and `QUEST-AND-WORLD-MODS.md` say do not run MineColonies + Recruits as dual player capitals without a performance pass. Enabling MC also pulls four LDT libraries. That is five mods, not forty — still too heavy for the cheap loop, and it would fight the 0.3.6 zip rebuild.

If a later integrate opts them in, frame the colony as an **Elector outpost / temple-city / hold / Under-Empire warren**, not a town hall. `rallous_grow` already uses those words on the 7×7 camp.

## How a player grows a place in one night

Datapack: `content/datapacks/rallous_grow/` (`rallous_grow`).

1. Land at a crash-camp picket (`rallous.camp`, 7×7 pad + banners + lord).
2. Do the **help** night (`rallous_session`). `rallous.session` **1** adds **+1** to that camp’s `rallous.grow`; help/defend (`session_kind` **1**) adds a second mark.
3. **Trade or spend emeralds** within 24 blocks (levy hire or villager trade). Each spend/trade **+1**.
4. At grow **1** a race hut and banner appear east of the pad. At **2** a second hut west. At **3** a south hall, extra banners, one settler.

Cap **3**. Empire reads Elector outpost; lizards temple-city; dwarfs hold; skaven Under-Empire; greenskins Waaagh; vampires von Carstein hamlet; beastmen herd; Khorne Bloodbound shrine.

FTB: task on `rallous.grow` **3**. Cheats: `/function rallous_grow:on_session` or set the nearest camp’s `rallous.grow` to 3.

## Citations (accessed 2026-09-01)

- MineColonies CurseForge files API / project 245506 — fileIDs 8615315 (1.1.1276), 8775822 (1.1.1280-snapshot)
- MineColonies GitHub release `v1.20.1-1.1.1280-snapshot` required deps
- Modrinth API: `minecolonies` (no 1.20.1 Forge), `villager-recruits` 1.15.2, `guard-villagers` 1.6.19, `towns-and-towers` 1.12
- https://www.millenaire.org/ — 1.12 + 1.21.1 only
- Pack pin: `pack/curseforge-resolved.json` Recruits 8339846, Guard Villagers 8719057
