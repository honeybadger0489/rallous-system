tellraw @a[distance=..48] [{"text": "<Elector Count of Middenland Boris Todbringer — Middenland> ", "color": "red", "bold": true}, {"text": "Ulrican hunter of beasts. Prove you kill horned things, not that you tame them. Warp-born, take a blade. Hold the line and we will name you useful.", "color": "white"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"State Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/middenland
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/middenland
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
