# Temple and Herd — integrator pickup

Owned by the Lizardmen / Beastmen / Ark-creature glue agent. Do not rebuild the dist zip here. Do not rewrite PLAY.md.

## Copy

| Source | Into pack |
| --- | --- |
| `content/datapacks/rallous_temple_herd/` | world `datapacks/` or `overrides/datapacks/` |
| `content/resourcepacks/Rallous Temple Herd/` | `overrides/resourcepacks/` (enable in options) |
| `pack-src/resourcepacks/Rallous Temple Herd/` | same RP, path `integrate-overrides.py` already scans |
| `content/lang/en_us.json` | split into RP namespaces if you skip the folder RP |
| `content/ftbquests/chapters/temple_and_herd.snbt` | `config/ftbquests/quests/chapters/` |
| `pack-src/quests/chapters/temple_and_herd.snbt` | same chapter, path the zip script already scans |
| `content/ftbquests/chapter_groups.snippet.snbt` | merge group `0A030000` into `chapter_groups.snbt` |

## Mechanical vs cosmetic

**Mechanical**

- Worldgen structures `temple_marker` (jungle/warm tag) and `herdstone` (dark forest/taiga tag): platforms, banners, chests, armor stands.
- Tick: biome enter grants advancements + one-time primer books; proximity to tagged stands grants marker advancements.
- Tameable Beasts `*_tame_food` tags get extra vanilla foods (global, not per-player-race).
- Loot tables: temple cache vs uglier herdstone cache (Broken Collar lead).
- Advancements + FTB chapter tasks that read them.
- Place functions for cheats / quest commands.
- Soft hook: near `rallous.roam.herd` (roaming wars) also grants Horned Woods.
- Optional LowCodeFML `META-INF/mods.toml` so the zip agent can ship `rallous_temple_herd-1.0.0.jar`. Merge `#minecraft:load` / `#minecraft:tick` if you fold `data/` into the Old World jar — do not overwrite those tags.

**Cosmetic / framing (not a hidden tame buff)**

- Lang: Fossils vat/analyzer/scarab/whip/failuresaurus; TB gecko/quetzal/racoon names.
- Lore books (Temple-Beast Primer, Herdstone Rite, Worse Hands).
- Entity/item tags `temple_beasts` / `herd_beasts` / `broken_beasts` — Fossils does **not** read these for tame chance.
- Other races: Worse Hands book if `rallous.old_world` is already tagged. No damage/tame penalty.

**Cannot force**

- Per-faction Fossils tame difficulty. Config only has global `whipToTameDino` (left default / unset).
