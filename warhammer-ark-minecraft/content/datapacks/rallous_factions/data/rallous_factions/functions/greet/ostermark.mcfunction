tellraw @a[distance=..48] [{"text": "<Elector Count of Ostermark Wolfram Hertwig — Ostermark> ", "color": "red", "bold": true}, {"text": "The Warp spat you onto Ostermark soil. Take a blade. Hold the line — or walk on and be meat for the next banner.", "color": "white"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"State Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A blade is thrown at your feet. Take it.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Last this night among them. Then they will speak of a path.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"They smell the Warp on you. Steel or the pyre — they have not decided.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/ostermark
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/ostermark
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
