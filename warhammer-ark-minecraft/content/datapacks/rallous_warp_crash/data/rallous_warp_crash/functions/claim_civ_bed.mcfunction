# Chosen civilization bed. Later deaths use this bed, not a new crash.
scoreboard players set @s rallous.civ_bed 1
tag @s add rallous.civ_bed
tellraw @s [{"text":"This village holds your bed. Death will not return you to the crater.","color":"gold"}]
