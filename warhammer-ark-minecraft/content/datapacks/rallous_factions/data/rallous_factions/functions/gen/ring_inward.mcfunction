# Halfway toward crash origin, then land-hunt a closer ring.
execute store result score $px rallous.gen run data get entity @s Pos[0]
execute store result score $pz rallous.gen run data get entity @s Pos[2]
scoreboard players operation $px rallous.gen += $origin_x rallous.gen
scoreboard players operation $pz rallous.gen += $origin_z rallous.gen
scoreboard players operation $px rallous.gen /= #2 rallous.const
scoreboard players operation $pz rallous.gen /= #2 rallous.const
execute store result entity @s Pos[0] double 1 run scoreboard players get $px rallous.gen
execute store result entity @s Pos[2] double 1 run scoreboard players get $pz rallous.gen
data modify entity @s Pos[1] set value 80.0d
execute at @s run forceload add ~-1 ~-1 ~1 ~1
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run spreadplayers ~ ~ 36 90 false @s
