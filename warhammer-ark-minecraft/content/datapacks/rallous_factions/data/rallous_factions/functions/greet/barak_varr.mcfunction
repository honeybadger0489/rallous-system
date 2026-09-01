tellraw @a[distance=..48] [{"text": "<King of Barak Varr Byrrnoth Grundadrakk — Barak Varr> ", "color": "gold", "bold": true}, {"text": "No oath is sworn. Barak Varr is wary. You stink of the Warp. Kill until the Book names you clean — or entered.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Oath Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "An oath-axe is offered. Hold the gate, or be a grudge.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last this night in the hold. Then the Book is marked.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "The hold is wary. Warp-stink is a grudge until you kill it clean.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "The hold is shut. Survive the raid, or be a thief.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/barak_varr
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/barak_varr
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
