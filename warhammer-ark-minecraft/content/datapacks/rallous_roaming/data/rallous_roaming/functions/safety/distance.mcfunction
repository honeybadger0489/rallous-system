# Chunk-safe crater test: (px-ox)^2 + (pz-oz)^2 >= 128^2 (16384). Run as the considering player.
execute store result score $px rallous.roam run data get entity @s Pos[0]
execute store result score $pz rallous.roam run data get entity @s Pos[2]
scoreboard players operation $dx rallous.roam = $px rallous.roam
scoreboard players operation $dx rallous.roam -= $ox rallous.roam
scoreboard players operation $dz rallous.roam = $pz rallous.roam
scoreboard players operation $dz rallous.roam -= $oz rallous.roam
scoreboard players operation $dx rallous.roam *= $dx rallous.roam
scoreboard players operation $dz rallous.roam *= $dz rallous.roam
scoreboard players operation $d2 rallous.roam = $dx rallous.roam
scoreboard players operation $d2 rallous.roam += $dz rallous.roam
execute if score $d2 rallous.roam >= $16384 rallous.roam run scoreboard players set $safe rallous.roam 1
