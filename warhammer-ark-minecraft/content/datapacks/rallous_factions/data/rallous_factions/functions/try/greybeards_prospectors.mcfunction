# try greybeards-prospectors (minor)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_jungle run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:dripstone_caves run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:lush_caves run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:deep_dark run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #greybeards_prospectors rallous.used matches 1 run function rallous_factions:place/greybeards_prospectors
