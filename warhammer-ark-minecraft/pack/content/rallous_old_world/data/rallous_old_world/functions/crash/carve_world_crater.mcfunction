# Bowl under the first survivor. Sets world spawn + their spawnpoint.
fill ~-6 ~-1 ~-6 ~6 ~5 ~6 air
fill ~-6 ~-4 ~-6 ~6 ~-3 ~6 blackstone
fill ~-4 ~-3 ~-4 ~4 ~-3 ~4 magma_block
fill ~-5 ~-2 ~-5 ~5 ~-2 ~5 polished_blackstone
fill ~-3 ~-2 ~-3 ~3 ~-2 ~3 crying_obsidian
setblock ~ ~-2 ~ crying_obsidian
setblock ~1 ~-2 ~ amethyst_block
setblock ~-1 ~-2 ~ budding_amethyst
setblock ~ ~-2 ~1 obsidian
setblock ~ ~-2 ~-1 crying_obsidian
fill ~-7 ~-1 ~-7 ~7 ~-1 ~7 blackstone
fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 air
setblock ~-3 ~-2 ~2 warped_nylium
setblock ~-3 ~-1 ~2 warped_fungus
setblock ~3 ~-2 ~3 crimson_nylium
setblock ~2 ~-1 ~2 campfire
setblock ~-2 ~-1 ~-2 lantern
setblock ~4 ~-1 ~-1 chest{Items:[{Slot:0b,id:"minecraft:bread",Count:8b},{Slot:1b,id:"minecraft:torch",Count:16b},{Slot:2b,id:"minecraft:leather",Count:4b},{Slot:3b,id:"minecraft:stone_sword",Count:1b},{Slot:4b,id:"minecraft:leather_chestplate",Count:1b},{Slot:5b,id:"minecraft:leather_boots",Count:1b}]}
summon marker ~ ~-1 ~ {Tags:["rallous.world_crater","rallous.crater","rallous.crash.crater","rallous.crash.origin"],CustomName:'{"text":"Warp Crater"}'}
forceload add ~-2 ~-2 ~2 ~2
setworldspawn ~ ~-1 ~
spawnpoint @s ~ ~-1 ~
gamerule spawnRadius 0
tp @s ~ ~-1 ~
tellraw @s {"text":"You hit the Old World. This crater is home until you sleep in a bed.","color":"dark_purple"}
