# /function rallous_diplomacy:leave — walk away; nearest camp goes neutral.
scoreboard players set @s rallous.path 4
scoreboard players set @s rallous.leave 1
tag @s add rallous.diplo.actor
function rallous_diplomacy:util/bind
tellraw @s {"text":"You walk on. The banner stays neither friend nor foe.","color":"gray"}
execute if entity @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:marker/neutral
execute unless entity @e[tag=rallous.diplo.target,limit=1] run tellraw @s {"text":"No camp marker in 512 blocks. Path recorded on you; stance waits for a banner.","color":"dark_gray"}
function rallous_diplomacy:util/finish
