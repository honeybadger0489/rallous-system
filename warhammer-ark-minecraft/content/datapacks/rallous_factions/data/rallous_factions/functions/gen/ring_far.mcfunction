# 1 if the probe left the crater (spreadplayers found a ring cell).
execute store result score $px rallous.gen run data get entity @s Pos[0]
execute store result score $pz rallous.gen run data get entity @s Pos[2]
scoreboard players operation $dx rallous.gen = $px rallous.gen
scoreboard players operation $dx rallous.gen -= $origin_x rallous.gen
execute if score $dx rallous.gen matches ..-1 run scoreboard players operation $dx rallous.gen *= #-1 rallous.const
scoreboard players operation $dz rallous.gen = $pz rallous.gen
scoreboard players operation $dz rallous.gen -= $origin_z rallous.gen
execute if score $dz rallous.gen matches ..-1 run scoreboard players operation $dz rallous.gen *= #-1 rallous.const
scoreboard players set $far rallous.gen 0
execute if score $dx rallous.gen matches 40.. run scoreboard players set $far rallous.gen 1
execute if score $dz rallous.gen matches 40.. run scoreboard players set $far rallous.gen 1
