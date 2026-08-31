# One limited scar. Fire only on grass, and only if the player is 16+ blocks away.
fill ~-1 ~ ~-1 ~1 ~2 ~1 air replace #minecraft:leaves
fill ~-1 ~ ~-1 ~1 ~ ~1 air replace #minecraft:crops
fill ~-1 ~ ~-1 ~1 ~ ~1 air replace minecraft:wheat
fill ~-1 ~ ~-1 ~1 ~1 ~1 air replace minecraft:grass
fill ~-1 ~ ~-1 ~1 ~1 ~1 air replace minecraft:tall_grass
execute if entity @p[distance=16..] if block ~ ~-1 ~ minecraft:grass_block if block ~ ~ ~ minecraft:air run setblock ~ ~ ~ minecraft:fire keep
scoreboard players add $grief rallous.roam 1
