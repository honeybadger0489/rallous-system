tellraw @a[distance=..48] [{"text": "<Mage-Priest of the Mists Uaxti — Xlanhuapec> ", "color": "aqua", "bold": true}, {"text": "The Old Ones smell the Great Enemy on you. Xlanhuapec is wary. An omen must clear the Warp — or the temple will.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:stone_sword{display:{Name:'{"text":"Temple Macuahuitl","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A temple weapon is offered. Stand the plaque, or be judged.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last this night at the temple. The plaque has not named you.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "The temple is wary. Warp-stink is the Great Enemy until an omen — or a verb — clears you.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "The temple is shut. Survive the judgement.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/xlanhuapec
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/xlanhuapec
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
