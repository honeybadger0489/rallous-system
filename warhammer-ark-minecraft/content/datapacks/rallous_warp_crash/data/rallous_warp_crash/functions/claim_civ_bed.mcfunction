# Chosen civilization bed. Later deaths use this bed, not a new crash.
scoreboard players set @s rallous.civ_bed 1
tag @s add rallous.civ_bed
tellraw @s [{"text":"This village holds your sleep. Death will not drag you back to the crater.","color":"gold"}]
