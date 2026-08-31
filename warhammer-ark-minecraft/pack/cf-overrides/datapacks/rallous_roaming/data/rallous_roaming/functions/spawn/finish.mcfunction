# Shared post-spawn: same team (Recruits-unfriendly hostiles do not krump each other), short lock, drop the marker.
team join rallous_roam @e[tag=rallous.roam.host]
scoreboard players set @e[tag=rallous.roam.host] rallous.roam.life 0
scoreboard players set $grief rallous.roam 0
scoreboard players set $cooldown rallous.roam 2
scoreboard players set $pulse rallous.roam.life 0
kill @e[type=minecraft:marker,tag=rallous.roam.spawner]
