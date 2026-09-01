tag @s add rallous.burned
scoreboard players set @s rallous.burn 0
scoreboard players set @s rallous.path 2
scoreboard players set @s rallous.betray 1
scoreboard players add @s rallous.khorne 1
scoreboard players add @s rallous.chaos 1
function rallous_contact:race/khorne
function rallous_contact:path/betray
tellraw @s {"text":"You burned their welcome. Blood is a path. This camp names you oath-breaker. Khorne hears.","color":"dark_red","bold":true}
execute as @e[tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:contact/raid_generic
execute as @e[tag=rallous.camp,limit=1,sort=nearest] at @s run particle minecraft:lava ~ ~1 ~ 0.6 0.4 0.6 0.02 20
