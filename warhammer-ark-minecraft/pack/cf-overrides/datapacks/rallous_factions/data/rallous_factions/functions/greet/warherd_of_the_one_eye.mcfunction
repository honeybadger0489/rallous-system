tellraw @a[distance=..48] [{"text": "<Beastlord Khazrak the One-Eye — Warherd of the One-Eye> ", "color": "dark_green", "bold": true}, {"text": "Hunts Todbringer. A stranger is a scalp or a rival. No camp-capital. This host does not treat crash-meat as a guest.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:stone_axe{display:{Name:'{"text":"Herd Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/warherd_of_the_one_eye
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/warherd_of_the_one_eye
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
