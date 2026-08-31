execute as @a at @s if biome ~ ~ ~ #rallous_temple_herd:temple_jungles run function rallous_temple_herd:enter_temple_biome
execute as @a at @s if biome ~ ~ ~ #rallous_temple_herd:horned_woods run function rallous_temple_herd:enter_herd_biome
execute as @a at @s if entity @e[type=minecraft:armor_stand,tag=rallous.temple_marker,distance=..8] run advancement grant @s only rallous_temple_herd:lizardmen/temple_marker
execute as @a at @s if entity @e[type=minecraft:armor_stand,tag=rallous.herdstone,distance=..8] run advancement grant @s only rallous_temple_herd:beastmen/herdstone
execute as @a at @s if entity @e[tag=rallous.roam.herd,distance=..16] run advancement grant @s only rallous_temple_herd:beastmen/horned_woods
