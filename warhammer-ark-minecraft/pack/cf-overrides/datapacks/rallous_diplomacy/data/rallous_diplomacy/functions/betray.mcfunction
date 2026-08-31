# /function rallous_diplomacy:betray — hostile + Khorne lean.
scoreboard players set @s rallous.path 2
scoreboard players set @s rallous.betray 1
scoreboard players add @s rallous.khorne_path 1
tag @s add rallous.diplo.actor
function rallous_diplomacy:util/bind
tellraw @s {"text":"You turned on the camp. They will remember. Blood is a path.","color":"dark_red"}
execute if entity @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:marker/hostile
execute unless entity @e[tag=rallous.diplo.target,limit=1] run tellraw @s {"text":"No camp marker in 512 blocks. Path and khorne_path recorded on you.","color":"dark_gray"}
function rallous_diplomacy:util/finish
