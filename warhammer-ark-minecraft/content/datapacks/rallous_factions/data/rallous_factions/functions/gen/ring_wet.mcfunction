scoreboard players set $wet rallous.gen 0
execute at @s if biome ~ ~ ~ #minecraft:is_ocean run scoreboard players set $wet rallous.gen 1
execute at @s if biome ~ ~ ~ #minecraft:is_river run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~ ~ minecraft:water run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:water run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:air run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:cave_air run scoreboard players set $wet rallous.gen 1
