# Rallous kit

Minecraft **1.20.1** datapack (`pack_format` **15**). After first-contact greet, issues a **tier-1** levy kit for `rallous.race` 1–8.

No new mods. This folder only. Zip agent may ingest it (jar **or** world datapack, not both). Do not edit `compile_factions.py`, the dist zip, or `PLAY.md` from here.

## Hook

Wired from `rallous_factions:contact/assign` and `rallous_warp_crash:first_contact` **as the greeted player** after the lord voice:

```
/function rallous_kit:on_greet
```

Sets `rallous.greeted` **1**. If `rallous.race` is 1–8 and `rallous.kitted` is not set, gives the race kit and sets `rallous.kitted` **1**. Safe to call twice.

A `#minecraft:tick` backup also runs `on_greet` once when `rallous.greeted` is set and `rallous.kitted` is not. Existing greet signals (`rallous.fac.greeted`, `rallous.contacted`, `rallous.contact` 1+) are mirrored onto `rallous.greeted` so the kit still fires if the hook is not wired yet.

Cheats: `/scoreboard players set @s rallous.race 1` then `/function rallous_kit:on_greet`.

## Item IDs per race

Sons of the Empire **1.1.9** jar (`sonsoftheempire-1.1.9-forge-1.20.1.jar`) was searched. That mod is Empire / Bretonnia / Kislev / Dwarf / High Elf kits only — no Vampire Counts, Lizardmen, Beastmen, Greenskin, Skaven, or Khorne items. Epic Knights was not on disk; no unconfirmed `magistuarmory:` ids.

If a SoTE `/give` fails (mod missing or id wrong), the next line gives a vanilla stand-in so the kit still works.

| Race | Score | Primary ids | Fallback if SoTE missing |
| --- | --- | --- | --- |
| Empire plate | 1 | `sonsoftheempire:swordsman_armor_helmet` `swordsman_armor_chestplate` `swordsman_armor_leggings` `swordsman_armor_boots` `altdorfbanner`; `minecraft:iron_sword` `shield` `bread` | `minecraft:iron_helmet` `iron_chestplate` `iron_leggings` `iron_boots` `yellow_banner` |
| VC ragged | 2 | `sonsoftheempire:witchhunter_armor_helmet` (Mannfred stand-in from prior docs); black leather (`color:1908001`); `minecraft:red_banner` `iron_sword` `bone` `bread` | `minecraft:leather_helmet` same dye |
| LM scute/leather + banner | 3 | `minecraft:turtle_helmet` lime leather (`color:8439583`) `lime_banner` `scute` `stone_sword` `tropical_fish` | vanilla only (no SoTE LM set) |
| Beastmen leather/skull | 4 | brown leather (`color:8602624`) `minecraft:skeleton_skull` `brown_banner` `stone_axe` `goat_horn` `bread` | vanilla only |
| Greenskin cheap iron | 5 | `minecraft:iron_helmet` `iron_chestplate` `iron_sword` `lime_banner` `rotten_flesh` `bread` | vanilla only |
| Dwarf chain | 6 | `minecraft:chainmail_helmet` `chainmail_chestplate` `chainmail_leggings` `chainmail_boots` `gray_banner` `iron_axe` `bread` `coal` | vanilla only (SoTE thane/hammerer/ironbreaker are above levy) |
| Skaven leather | 7 | dirty-brown leather (`color:4863784`) `minecraft:brown_banner` `iron_sword` `string` `bread` | vanilla only |
| Khorne red/nether | 8 | red leather (`color:11546150`) `minecraft:red_banner` `iron_axe` `nether_brick` `magma_cream` `cooked_beef` | vanilla only |

Confirmed in the 1.1.9 jar / `en_us.json` / prior JEI-style names: `sonsoftheempire:swordsman_armor_*` (State Trooper), `altdorfbanner`, `witchhunter_armor_helmet`, `empireknight_armor_*`, `thane_armor_*`, `hammerer_armor_*`, `grailknight_armor_*`, `armoredkossar_armor_*`, `altdorfswordsman_armor_*`. Levy uses the State Trooper set, not knight / thane / emperor.

## Files

`on_greet` `give` `give/empire|vampire|lizard|beast|greenskin|dwarf|skaven|khorne` `load` `tick`

Writes: `rallous.greeted` `rallous.kitted`. Reads: `rallous.race` `rallous.contact`.
