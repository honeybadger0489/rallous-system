tellraw @a[distance=..48] [{"text": "<Exalted Hero of Khorne Son of Kharneth — Kharneth's Sons> ", "color": "dark_red", "bold": true}, {"text": "You are the offering. The Blood Host of Kharneth's Sons does not treat Warp-spawn as guests. Survive, or die on this picket.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Blood Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A blood-axe. Spill with the pack, or be the offering.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Skulls or cowardice. Last this fight.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "Bleed until they name you, or be the skull.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "You are the offering. The Blood Host is already on you.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:stance/bite
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:stance/bite
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
