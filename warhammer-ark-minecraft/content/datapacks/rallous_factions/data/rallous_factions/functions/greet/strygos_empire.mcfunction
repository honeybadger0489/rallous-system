tellraw @a[distance=..48] [{"text": "<Ghoul King Gashnag — Strygos Empire> ", "color": "dark_red", "bold": true}, {"text": "Daemon-stink on living breath. The graves of Strygos Empire do not trust Warp-born. Name a path, or hang with the suspected.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"Night Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A night-blade is laid on a grave. Serve, or be levied.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last the night among the dead. Guest-right is not given yet.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "They name you daemon-suspect. The graves watch. Paths still open — at a cost.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "The grave-levy comes for crash-meat.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/strygos_empire
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/strygos_empire
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
