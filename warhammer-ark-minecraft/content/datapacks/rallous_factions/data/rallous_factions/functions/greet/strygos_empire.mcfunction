tellraw @a[distance=..48] [{"text": "<Ghoul King Gashnag — Strygos Empire> ", "color": "dark_red", "bold": true}, {"text": "Crash-meat. Last the night among the dead of Strygos Empire. Then we may name you guest.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"Night Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A blade is thrown at your feet. Take it.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Last this night among them. Then they will speak of a path.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"They smell the Warp on you. Steel or the pyre — they have not decided.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/strygos_empire
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/strygos_empire
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
