tellraw @a[distance=..48] [{"text": "<Elector Count of Hochland Aldebrand Ludenhof — Hochland> ", "color": "red", "bold": true}, {"text": "The Warp spat you onto Hochland soil. Take a blade. Fight with us — hold this road, or be meat for the next banner.", "color": "white"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"State Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A State Blade is thrown at your feet. Fight with this host.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last this night among the State Troops. Then they will speak of a path.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "Witch-hunters have not decided. Steel or the pyre.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "The palisade closes. This is a fight, not a greeting.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/hochland
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/hochland
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
