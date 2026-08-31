# as player at player — persist hostile + Khorne lean on the bound marker.
scoreboard players operation #stance rallous.stance = #hostile rallous.stance
execute as @e[tag=rallous.diplo.target,limit=1] run function rallous_diplomacy:util/write_marker
execute as @e[tag=rallous.diplo.target,limit=1] run tag @s add rallous.stance.hostile
scoreboard players operation @e[tag=rallous.diplo.target,limit=1] rallous.khorne_path = @s rallous.khorne_path
team leave @s
execute as @e[type=minecraft:iron_golem,distance=..48] run data modify entity @s AngryAt set from entity @a[tag=rallous.diplo.actor,limit=1] UUID
execute at @e[tag=rallous.diplo.target,limit=1] run particle minecraft:flame ~ ~2 ~ 0.35 1 0.35 0.01 24
playsound minecraft:entity.villager.no player @s ~ ~ ~ 1 0.8
