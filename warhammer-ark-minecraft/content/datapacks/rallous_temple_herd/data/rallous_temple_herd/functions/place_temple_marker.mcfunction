# Temple-Spawn courtyard. 13x13 mossy plaza, 5x5 spawning-pool pit, lime banners, named stands, caches.
kill @e[type=minecraft:armor_stand,tag=rallous.temple_marker,distance=..12]
fill ~-6 ~-1 ~-6 ~6 ~5 ~6 minecraft:air
fill ~-6 ~-1 ~-6 ~6 ~-1 ~6 minecraft:mossy_cobblestone
fill ~-6 ~ ~-6 ~6 ~ ~6 minecraft:mossy_stone_bricks
setblock ~-6 ~-1 ~-6 minecraft:jungle_planks
setblock ~6 ~-1 ~-6 minecraft:jungle_planks
setblock ~-6 ~-1 ~6 minecraft:jungle_planks
setblock ~6 ~-1 ~6 minecraft:jungle_planks
setblock ~-6 ~ ~-6 minecraft:jungle_planks
setblock ~6 ~ ~-6 minecraft:jungle_planks
setblock ~-6 ~ ~6 minecraft:jungle_planks
setblock ~6 ~ ~6 minecraft:jungle_planks
fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:prismarine
setblock ~ ~-1 ~ minecraft:gold_block
setblock ~-1 ~-1 ~ minecraft:sea_lantern
setblock ~1 ~-1 ~ minecraft:sea_lantern
setblock ~ ~-1 ~-1 minecraft:sea_lantern
setblock ~ ~-1 ~1 minecraft:sea_lantern
fill ~-2 ~ ~-2 ~2 ~ ~2 minecraft:water
setblock ~-6 ~1 ~-6 minecraft:jungle_fence
setblock ~-6 ~2 ~-6 minecraft:jungle_fence
setblock ~-6 ~3 ~-6 minecraft:lime_banner
setblock ~6 ~1 ~-6 minecraft:jungle_fence
setblock ~6 ~2 ~-6 minecraft:jungle_fence
setblock ~6 ~3 ~-6 minecraft:lime_banner
setblock ~-6 ~1 ~6 minecraft:jungle_fence
setblock ~-6 ~2 ~6 minecraft:jungle_fence
setblock ~-6 ~3 ~6 minecraft:lime_banner
setblock ~6 ~1 ~6 minecraft:jungle_fence
setblock ~6 ~2 ~6 minecraft:jungle_fence
setblock ~6 ~3 ~6 minecraft:lime_banner
setblock ~ ~1 ~-6 minecraft:lime_banner
setblock ~ ~1 ~6 minecraft:lime_banner
setblock ~-6 ~1 ~ minecraft:lime_banner
setblock ~6 ~1 ~ minecraft:lime_banner
setblock ~4 ~1 ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/temple_cache"}
setblock ~-4 ~1 ~ minecraft:chest{LootTable:"rallous_temple_herd:chests/temple_cache"}
setblock ~ ~1 ~4 minecraft:chest{LootTable:"rallous_temple_herd:chests/temple_cache"}
setblock ~ ~1 ~-4 minecraft:gold_block
setblock ~ ~2 ~-4 minecraft:sea_lantern
setblock ~-5 ~1 ~-5 minecraft:jungle_leaves[persistent=true]
setblock ~5 ~1 ~-5 minecraft:jungle_leaves[persistent=true]
setblock ~-5 ~1 ~5 minecraft:jungle_leaves[persistent=true]
setblock ~5 ~1 ~5 minecraft:jungle_leaves[persistent=true]
setblock ~ ~1 ~-3 minecraft:mossy_stone_brick_stairs[facing=south]
setblock ~ ~1 ~3 minecraft:mossy_stone_brick_stairs[facing=north]
setblock ~-3 ~1 ~ minecraft:mossy_stone_brick_stairs[facing=east]
setblock ~3 ~1 ~ minecraft:mossy_stone_brick_stairs[facing=west]
summon minecraft:armor_stand ~ ~1 ~-3 {CustomName:'{"text":"Temple-Spawn Marker","color":"dark_green"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,ShowArms:1b,Tags:["rallous.temple_marker"],ArmorItems:[{},{},{},{id:"minecraft:lime_banner",Count:1b}]}
summon minecraft:armor_stand ~4 ~1 ~-2 {CustomName:'{"text":"Spawning Pool","color":"aqua"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,ShowArms:1b,Tags:["rallous.temple_marker","rallous.temple_pit"],ArmorItems:[{},{},{},{id:"minecraft:heart_of_the_sea",Count:1b}]}
advancement grant @s only rallous_temple_herd:lizardmen/temple_marker
