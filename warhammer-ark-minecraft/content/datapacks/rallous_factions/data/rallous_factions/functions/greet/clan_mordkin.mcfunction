tellraw @a[distance=..48] [{"text": "<Warlord Mordkin — Clan Mordkin> ", "color": "light_purple", "bold": true}, {"text": "Man-thing reeks of Warp. Intruder-meat. Clan Mordkin does not greet. Live the knives, or die-die.", "color": "red"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"Warp-shiv","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A warp-shiv, yes-yes. Fight-fight, or be meat.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Prove-prove you are not a spy. Last the night under the Clan.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "Daemon-spy, they hiss. Paths exist. Trust does not.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "Knives in the dark. The Clan does not greet man-things.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:stance/bite
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:stance/bite
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
