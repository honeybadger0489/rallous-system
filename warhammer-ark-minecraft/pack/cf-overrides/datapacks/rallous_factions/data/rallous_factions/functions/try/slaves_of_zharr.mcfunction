# try slaves-of-zharr (minor)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_badlands run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:badlands run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:eroded_badlands run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:desert run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #slaves_of_zharr rallous.used matches 1 run function rallous_factions:place/slaves_of_zharr
