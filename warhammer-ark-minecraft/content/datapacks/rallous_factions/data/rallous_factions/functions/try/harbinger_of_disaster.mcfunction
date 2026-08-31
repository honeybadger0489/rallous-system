# try harbinger-of-disaster (major)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_hills run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_forest run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_gravelly_hills run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:windswept_savanna run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:dark_forest run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_badlands run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #harbinger_of_disaster rallous.used matches 1 run function rallous_factions:place/harbinger_of_disaster
