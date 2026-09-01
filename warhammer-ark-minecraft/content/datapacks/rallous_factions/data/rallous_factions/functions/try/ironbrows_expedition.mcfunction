# try ironbrows-expedition (major)
scoreboard players set $biome_ok rallous.gen 0
execute if biome ~ ~ ~ #minecraft:is_jungle run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_savanna run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $biome_ok rallous.gen 1
execute if biome ~ ~ ~ minecraft:desert run scoreboard players set $biome_ok rallous.gen 1
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1
execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 unless score #ironbrows_expedition rallous.used matches 1 run function rallous_factions:place/ironbrows_expedition
