# 3x3 mossy plaza + lime banner + named stand, east of the 7x7 picket.
fill ~5 ~-1 ~-1 ~7 ~-1 ~1 minecraft:mossy_stone_bricks
setblock ~6 ~-1 ~ minecraft:chiseled_stone_bricks
setblock ~6 ~ ~ minecraft:sea_lantern
setblock ~6 ~1 ~ minecraft:lime_banner
summon minecraft:armor_stand ~6 ~1 ~ {CustomName:'{"text":"Temple-Spawn","color":"aqua"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,Tags:["rallous.temple_marker"],ArmorItems:[{},{},{},{id:"minecraft:lime_banner",Count:1b}]}
