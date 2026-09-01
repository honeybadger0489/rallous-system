tellraw @a[distance=..48] [{"text": "<Gorebull Redhorn — Redhorn Tribe> ", "color": "dark_green", "bold": true}, {"text": "Prey. The herd of Redhorn Tribe does not share this camp. Run, or be eaten.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:stone_axe{display:{Name:'{"text":"Herd Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A herd-axe in the dirt. Gore with them, or be cattle.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last the horns. The herd has not kept you yet.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "Warp-stink. Rival or meat — they have not picked.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "Prey. The herd is already moving to eat.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:stance/bite
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:stance/bite
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
