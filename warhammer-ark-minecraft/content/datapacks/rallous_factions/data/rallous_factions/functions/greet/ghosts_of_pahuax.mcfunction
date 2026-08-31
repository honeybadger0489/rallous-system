tellraw @a[distance=..48] [{"text": "<The Hidden Oxyotl — Ghosts of Pahuax> ", "color": "aqua", "bold": true}, {"text": "Chaos-hunter from the lost city. Daemon-suspicion is doctrine; prove you are not bait. You stink of the Warp. Daemon? Prove you are not, or be slain.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:stone_sword{display:{Name:'{"text":"Temple Macuahuitl","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/ghosts_of_pahuax
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/ghosts_of_pahuax
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
