# Herdstone pit. 13x13 dirt ring, 5x5 soul hollow, 5-high stone, skull banners, named stands, caches.
kill @e[type=minecraft:armor_stand,tag=rallous.herdstone,distance=..12]
fill ~-6 ~-1 ~-6 ~6 ~6 ~6 minecraft:air
fill ~-6 ~-1 ~-6 ~6 ~-1 ~6 minecraft:cobbled_deepslate
fill ~-6 ~-1 ~-6 ~6 ~-1 ~-6 minecraft:mossy_cobblestone
fill ~-6 ~-1 ~6 ~6 ~-1 ~6 minecraft:mossy_cobblestone
fill ~-6 ~-1 ~-6 ~-6 ~-1 ~6 minecraft:mossy_cobblestone
fill ~6 ~-1 ~-6 ~6 ~-1 ~6 minecraft:mossy_cobblestone
fill ~-6 ~ ~-6 ~6 ~ ~6 minecraft:coarse_dirt
fill ~-6 ~ ~-6 ~6 ~ ~-6 minecraft:dark_oak_planks
fill ~-6 ~ ~6 ~6 ~ ~6 minecraft:dark_oak_planks
fill ~-6 ~ ~-6 ~-6 ~ ~6 minecraft:dark_oak_planks
fill ~6 ~ ~-6 ~6 ~ ~6 minecraft:dark_oak_planks
fill ~-2 ~-1 ~-2 ~2 ~ ~2 minecraft:air
fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:soul_soil
setblock ~-2 ~-1 ~-2 minecraft:bone_block
setblock ~2 ~-1 ~-2 minecraft:bone_block
setblock ~-2 ~-1 ~2 minecraft:bone_block
setblock ~2 ~-1 ~2 minecraft:bone_block
fill ~-1 ~-1 ~-1 ~1 ~3 ~1 minecraft:cobbled_deepslate
fill ~ ~-1 ~ ~ ~4 ~ minecraft:cracked_stone_bricks
setblock ~ ~2 ~ minecraft:bone_block
setblock ~ ~4 ~ minecraft:dark_oak_log
setblock ~ ~5 ~ minecraft:wither_skeleton_skull
setblock ~-1 ~3 ~ minecraft:skeleton_skull
setblock ~1 ~3 ~ minecraft:skeleton_skull
setblock ~ ~3 ~-1 minecraft:skeleton_skull
setblock ~ ~3 ~1 minecraft:wither_skeleton_skull
setblock ~ ~ ~3 minecraft:soul_campfire
setblock ~ ~1 ~-6 minecraft:red_banner
setblock ~ ~1 ~6 minecraft:black_banner
setblock ~-6 ~1 ~ minecraft:black_banner
setblock ~6 ~1 ~ minecraft:red_banner
setblock ~-6 ~1 ~-6 minecraft:dark_oak_fence
setblock ~-6 ~2 ~-6 minecraft:dark_oak_fence
setblock ~-6 ~3 ~-6 minecraft:skeleton_skull
setblock ~6 ~1 ~-6 minecraft:dark_oak_fence
setblock ~6 ~2 ~-6 minecraft:dark_oak_fence
setblock ~6 ~3 ~-6 minecraft:wither_skeleton_skull
setblock ~-6 ~1 ~6 minecraft:dark_oak_fence
setblock ~-6 ~2 ~6 minecraft:dark_oak_fence
setblock ~-6 ~3 ~6 minecraft:wither_skeleton_skull
setblock ~6 ~1 ~6 minecraft:dark_oak_fence
setblock ~6 ~2 ~6 minecraft:dark_oak_fence
setblock ~6 ~3 ~6 minecraft:skeleton_skull
setblock ~-4 ~1 ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/herdstone_cache"}
setblock ~4 ~1 ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/herdstone_cache"}
setblock ~ ~1 ~-4 minecraft:hay_block
setblock ~2 ~1 ~4 minecraft:red_wool
setblock ~-2 ~1 ~4 minecraft:bone_block
summon minecraft:armor_stand ~ ~1 ~3 {CustomName:'{"text":"Herdstone","color":"dark_red"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,ShowArms:1b,Tags:["rallous.herdstone"],ArmorItems:[{},{},{},{id:"minecraft:wither_skeleton_skull",Count:1b}]}
summon minecraft:armor_stand ~-3 ~1 ~ {CustomName:'{"text":"Broken-Beast Post","color":"red"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,ShowArms:1b,Tags:["rallous.herdstone","rallous.herd_post"],ArmorItems:[{},{},{},{id:"minecraft:skeleton_skull",Count:1b}]}
advancement grant @s only rallous_temple_herd:beastmen/herdstone
