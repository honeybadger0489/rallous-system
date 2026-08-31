# Nudge the host toward the nearest player. Reset the 10-tick pulse.
scoreboard players set $pulse rallous.roam.life 0
execute as @e[tag=rallous.roam.leader,limit=1] at @s run tp @s ~ ~ ~ facing entity @p
execute as @e[tag=rallous.roam.host] at @s unless entity @p[distance=..8] run tp @s ^ ^ ^0.35
