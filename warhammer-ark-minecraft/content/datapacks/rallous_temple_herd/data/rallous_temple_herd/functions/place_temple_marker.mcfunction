# Visible Temple-Spawn marker. Cheats / quest reward.
fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:mossy_cobblestone
fill ~-3 ~-1 ~-3 ~3 ~-1 ~-3 minecraft:mossy_stone_bricks
fill ~-3 ~-1 ~3 ~3 ~-1 ~3 minecraft:mossy_stone_bricks
setblock ~ ~-1 ~ minecraft:chiseled_stone_bricks
setblock ~ ~ ~ minecraft:sea_lantern
setblock ~ ~ ~-3 minecraft:lime_banner
setblock ~ ~ ~3 minecraft:lime_banner
setblock ~-3 ~ ~ minecraft:lime_banner
setblock ~3 ~ ~ minecraft:lime_banner
setblock ~2 ~ ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/temple_cache"}
setblock ~-2 ~-1 ~ minecraft:gold_block
summon minecraft:armor_stand ~ ~1 ~ {CustomName:'{"text":"Temple-Spawn Marker","color":"dark_green"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,Tags:["rallous.temple_marker"],ArmorItems:[{},{},{},{id:"minecraft:lime_banner",Count:1b}]}
advancement grant @s only rallous_temple_herd:lizardmen/temple_marker
