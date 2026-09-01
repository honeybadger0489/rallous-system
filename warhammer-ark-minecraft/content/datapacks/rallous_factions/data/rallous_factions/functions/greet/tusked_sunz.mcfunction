tellraw @a[distance=..48] [{"text": "<Savage Orc Warboss Tusked Sun — Tusked Sunz> ", "color": "green", "bold": true}, {"text": "Prove yer a proper scrap. Last the night wiv Tusked Sunz. Then da boss might keep ya.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Choppa","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A blade is thrown at your feet. Take it.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Last this night among them. Then they will speak of a path.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"They smell the Warp on you. Steel or the pyre — they have not decided.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/tusked_sunz
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/tusked_sunz
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
