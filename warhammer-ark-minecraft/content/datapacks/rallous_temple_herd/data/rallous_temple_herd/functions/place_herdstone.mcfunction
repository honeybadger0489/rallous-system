# Visible herdstone. Cheats / quest reward.
fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:mossy_cobblestone
fill ~-3 ~-1 ~-3 ~3 ~-1 ~-3 minecraft:cobbled_deepslate
fill ~-3 ~-1 ~3 ~3 ~-1 ~3 minecraft:dark_oak_planks
setblock ~ ~-1 ~ minecraft:cracked_stone_bricks
setblock ~ ~ ~ minecraft:soul_campfire
setblock ~ ~ ~-3 minecraft:red_banner
setblock ~ ~ ~3 minecraft:black_banner
setblock ~-3 ~ ~ minecraft:black_banner
setblock ~3 ~ ~ minecraft:red_banner
setblock ~1 ~ ~ minecraft:dark_oak_fence
setblock ~1 ~1 ~ minecraft:skeleton_skull
setblock ~-1 ~ ~ minecraft:dark_oak_fence
setblock ~-1 ~1 ~ minecraft:wither_skeleton_skull
setblock ~-2 ~ ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/herdstone_cache"}
summon minecraft:armor_stand ~ ~1 ~1 {CustomName:'{"text":"Herdstone","color":"dark_red"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,Tags:["rallous.herdstone"],ArmorItems:[{},{},{},{id:"minecraft:wither_skeleton_skull",Count:1b}]}
advancement grant @s only rallous_temple_herd:beastmen/herdstone
