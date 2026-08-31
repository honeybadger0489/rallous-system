# try marienburg (minor)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_beach run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:river run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:frozen_river run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:sunflower_plains run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_ocean run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:swamp run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:mangrove_swamp run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #marienburg rallous.used matches 1 run function rallous_factions:place/marienburg
