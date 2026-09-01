# Drop the 8 ring 3x3 forceloads after probes finish. Stay under the 256 cap.
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~120 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~-120 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~120 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~-120 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~220 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~-220 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~220 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~-220 run forceload remove ~-1 ~-1 ~1 ~1
tag @e[type=minecraft:marker,tag=rallous.ring.origin] add rallous.ring.unloaded
