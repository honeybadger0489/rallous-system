# Emeralds leaving the pack near a camp, or a villager trade, credit once per tick.
execute store result score @s rallous.em_now run clear @s minecraft:emerald 0
execute unless score @s rallous.em_init matches 1 run scoreboard players operation @s rallous.em_prev = @s rallous.em_now
execute unless score @s rallous.em_init matches 1 run scoreboard players set @s rallous.em_init 1
execute if score @s rallous.em_now < @s rallous.em_prev if entity @e[type=minecraft:marker,tag=rallous.camp,distance=..24,limit=1] run function rallous_grow:credit/trade
execute unless score @s rallous.em_now < @s rallous.em_prev if score @s rallous.traded matches 1.. if entity @e[type=minecraft:marker,tag=rallous.camp,distance=..24,limit=1] run function rallous_grow:credit/trade
scoreboard players set @s rallous.traded 0
scoreboard players operation @s rallous.em_prev = @s rallous.em_now
