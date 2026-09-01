tag @s add rallous.bitten
scoreboard players add $bite rallous.gen 1
tellraw @a[distance=..48] {"text":"The host lowers spears. Warp-born is meat.","color":"red"}
execute if score @s rallous.fac.race matches 7 run function rallous_factions:stance/bite_skaven
execute if score @s rallous.fac.race matches 4 run function rallous_factions:stance/bite_beastmen
execute if score @s rallous.fac.race matches 8 run function rallous_factions:stance/bite_khorne
execute unless score @s rallous.fac.race matches 4 unless score @s rallous.fac.race matches 7 unless score @s rallous.fac.race matches 8 run function rallous_factions:stance/bite_generic
execute as @e[tag=rallous.raid,distance=..16] run data modify entity @s AngryAt set from entity @p UUID
execute as @e[tag=rallous.raid,distance=..16] run data merge entity @s {AngerTime:2000}
execute store result score $raid_n rallous.gen if entity @e[tag=rallous.raid,distance=..24]
