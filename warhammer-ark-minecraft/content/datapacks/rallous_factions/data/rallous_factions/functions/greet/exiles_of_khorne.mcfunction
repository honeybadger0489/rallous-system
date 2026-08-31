tellraw @a[distance=..48] [{"text": "<The Exiled Skarbrand the Exiled — Exiles of Khorne> ", "color": "dark_red", "bold": true}, {"text": "No treaties. Skulls or flight. Camp moves when the killing thins. This host does not treat crash-meat as a guest.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Blood Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/exiles_of_khorne
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/exiles_of_khorne
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
