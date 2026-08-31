# /function rallous_diplomacy:help — ally the nearest camp.
scoreboard players set @s rallous.path 1
scoreboard players set @s rallous.help 1
tag @s add rallous.diplo.actor
function rallous_diplomacy:util/bind
tellraw @s {"text":"The nearest banner takes your help. Ally.","color":"gold"}
execute if entity @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:marker/ally
execute if entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous.diplo.target,limit=1] unless score @s rallous.gifted matches 1.. run function rallous_diplomacy:gift/give
execute unless entity @e[tag=rallous.diplo.target,limit=1] run tellraw @s {"text":"No camp marker in 512 blocks. Path recorded on you; stance waits for a banner.","color":"dark_gray"}
function rallous_diplomacy:util/finish
