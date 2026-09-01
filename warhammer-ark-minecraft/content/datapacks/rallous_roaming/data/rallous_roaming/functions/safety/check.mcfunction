# Natural events stay off until the player left the crater (128 blocks) OR day count >= 1.
# Force-test functions never call this.
# Run as the considering player.
scoreboard players set $safe rallous.roam 0
execute store result score $day rallous.roam run time query day
execute if score $day rallous.roam matches 1.. run scoreboard players set $safe rallous.roam 1

# This survivor's own wound (rallous_warp_crash).
execute if score $safe rallous.roam matches 0 if score @s rallous.crater_x = @s rallous.crater_x run scoreboard players operation $ox rallous.roam = @s rallous.crater_x
execute if score $safe rallous.roam matches 0 if score @s rallous.crater_z = @s rallous.crater_z run scoreboard players operation $oz rallous.roam = @s rallous.crater_z

execute if score $safe rallous.roam matches 0 if score $origin rallous.roam matches 1 run function rallous_roaming:safety/distance
execute if score $safe rallous.roam matches 0 as @e[tag=rallous.crater,limit=1,sort=nearest] at @s unless entity @a[tag=rallous.roam.ready,distance=..128] run scoreboard players set $safe rallous.roam 1
execute if score $safe rallous.roam matches 0 as @e[tag=rallous.crash.crater,limit=1] at @s unless entity @a[tag=rallous.roam.ready,distance=..128] run scoreboard players set $safe rallous.roam 1
execute if score $safe rallous.roam matches 0 as @e[tag=rallous.crash.origin,limit=1] at @s unless entity @a[tag=rallous.roam.ready,distance=..128] run scoreboard players set $safe rallous.roam 1
execute if score $safe rallous.roam matches 0 as @e[tag=rallous.roam.origin,limit=1] at @s unless entity @a[tag=rallous.roam.ready,distance=..128] run scoreboard players set $safe rallous.roam 1
