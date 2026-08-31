# try wissenland-and-nuln (major)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ minecraft:plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:sunflower_plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:river run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:frozen_river run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_hills run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_forest run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_gravelly_hills run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_savanna run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #wissenland_and_nuln rallous.used matches 1 run function rallous_factions:place/wissenland_and_nuln
