# as player at player — persist neutral on the bound marker.
scoreboard players operation #stance rallous.stance = #neutral rallous.stance
execute as @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:util/write_marker
execute as @e[tag=rallous.diplo.target,limit=1] run tag @s add rallous.stance.neutral
team leave @s
execute at @e[tag=rallous.diplo.target,limit=1] run particle minecraft:cloud ~ ~2 ~ 0.35 0.6 0.35 0.01 12
playsound minecraft:entity.villager.ambient player @s ~ ~ ~ 1 1
