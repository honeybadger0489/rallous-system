tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
scoreboard players set @s rallous.crashed 1
scoreboard players set @s rallous.deaths 0
execute if entity @s[tag=!rallous.warp_landed] run function rallous_old_world:crash/strip_starter_magic
# Spawn/respawn is rallous_warp_crash. Do not carve a second crater or restore the court.
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
