# as player at player — persist joined; civ_bed already set on the player.
scoreboard players operation #stance rallous.stance = #joined rallous.stance
execute as @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:util/write_marker
execute as @e[tag=rallous.diplo.target,limit=1] run tag @s add rallous.stance.joined
team join rallous_ally @s
execute as @e[type=minecraft:villager,distance=..48] run team join rallous_ally @s
execute as @e[type=minecraft:iron_golem,distance=..48] run team join rallous_ally @s
execute as @e[tag=rallous.diplo.target,limit=1] run team join rallous_ally @s
execute at @e[tag=rallous.diplo.target,limit=1] run particle minecraft:end_rod ~ ~2 ~ 0.25 1 0.25 0.01 16
playsound minecraft:block.bell.use player @s ~ ~ ~ 0.7 1
