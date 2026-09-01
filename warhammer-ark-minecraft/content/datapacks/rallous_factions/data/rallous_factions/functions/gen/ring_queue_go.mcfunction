# Kept for zip asserts. Probes no longer teleport into unloaded cells.
execute store result score $tx rallous.gen run data get entity @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] Pos[0]
execute store result score $tz rallous.gen run data get entity @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] Pos[2]
scoreboard players operation $tx rallous.gen += $ring_dx rallous.gen
scoreboard players operation $tz rallous.gen += $ring_dz rallous.gen
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run forceload add ~-1 ~-1 ~1 ~1
