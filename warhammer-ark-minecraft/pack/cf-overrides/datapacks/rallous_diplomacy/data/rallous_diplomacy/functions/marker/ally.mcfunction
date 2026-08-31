# as player at player — persist ally on the bound marker.
scoreboard players operation #stance rallous.stance = #ally rallous.stance
execute as @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:util/write_marker
execute as @e[tag=rallous.diplo.target,limit=1] run tag @s add rallous.stance.ally
team join rallous_ally @s
execute as @e[type=minecraft:villager,distance=..48] run team join rallous_ally @s
execute as @e[type=minecraft:iron_golem,distance=..48] run team join rallous_ally @s
execute as @e[tag=rallous.diplo.target,limit=1] run team join rallous_ally @s
execute at @e[tag=rallous.diplo.target,limit=1] run particle minecraft:happy_villager ~ ~2 ~ 0.35 1 0.35 0 20
playsound minecraft:entity.villager.yes player @s ~ ~ ~ 1 1
