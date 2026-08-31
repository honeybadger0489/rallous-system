# /function rallous_diplomacy:join — join the camp; civ_bed eligible.
scoreboard players set @s rallous.path 3
scoreboard players set @s rallous.join 1
scoreboard players set @s rallous.civ_bed 1
scoreboard players set @s rallous.claimed 1
tag @s add rallous.civ_bed
tag @s add rallous.diplo.actor
function rallous_diplomacy:util/bind
tellraw @s {"text":"You swore into this camp. A civilization bed will hold. The crater will not.","color":"gold"}
execute if entity @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:marker/joined
execute unless entity @e[tag=rallous.diplo.target,limit=1] run tellraw @s {"text":"No camp marker in 512 blocks. civ_bed is still eligible on you.","color":"dark_gray"}
function rallous_diplomacy:util/finish
