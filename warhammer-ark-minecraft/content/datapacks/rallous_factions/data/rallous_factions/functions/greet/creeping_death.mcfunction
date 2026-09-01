tellraw @a[distance=..48] [{"text": "<Forest Goblin Warboss Creeping Death — Creeping Death> ", "color": "green", "bold": true}, {"text": "You fell outta the sky onto Creeping Death. Take a choppa. Fight wiv us — da scrap starts now, or get krumped.", "color": "white"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Choppa","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] [{"text": "A choppa lands at your boots. Fight wiv da boyz. Dis is a scrap, not a speech.", "color": "gold"}]
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] [{"text": "Last da night. If you still stand, da boss might keep ya.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] [{"text": "You smell wrong. Fight till they say you ain't a daemon.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 3 run tellraw @a[distance=..48] [{"text": "Dis scrap is already on. Live it or nick da banner and die.", "color": "red"}]
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/creeping_death
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/creeping_death
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
