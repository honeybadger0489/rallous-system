tellraw @a[distance=..48] [{"text": "<Doombull Stone-Horn — Stone-Horn Tribe> ", "color": "dark_green", "bold": true}, {"text": "Prey. The herd of Stone-Horn Tribe does not share this camp. Run, or be eaten.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:stone_axe{display:{Name:'{"text":"Herd Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A blade is thrown at your feet. Take it.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Last this night among them. Then they will speak of a path.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"They smell the Warp on you. Steel or the pyre — they have not decided.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/stone_horn_tribe
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/stone_horn_tribe
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
