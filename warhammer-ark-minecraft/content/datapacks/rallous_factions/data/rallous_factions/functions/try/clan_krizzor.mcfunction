# try clan-krizzor (minor)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ minecraft:plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:sunflower_plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:dripstone_caves run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:lush_caves run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:deep_dark run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_savanna run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #clan_krizzor rallous.used matches 1 run function rallous_factions:place/clan_krizzor
