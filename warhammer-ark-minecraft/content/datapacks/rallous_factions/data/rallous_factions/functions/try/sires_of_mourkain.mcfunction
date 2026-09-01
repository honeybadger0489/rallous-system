# try sires-of-mourkain (minor)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_badlands run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_savanna run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:desert run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #sires_of_mourkain rallous.used matches 1 run function rallous_factions:place/sires_of_mourkain
