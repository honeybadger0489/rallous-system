# /recruits spawn recruitPatrol tiny = recruit + shieldman + bowman + patrol_leader.
# Command uses getEntity().getOnPos() — must run as an entity at the column.
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.host.recsrc"],Invisible:1b,Marker:1b,NoGravity:1b,Small:1b,Invulnerable:1b,DisabledSlots:4144959}
execute as @e[type=minecraft:armor_stand,tag=rallous.host.recsrc,limit=1] at @s run recruits spawn recruitPatrol tiny
kill @e[type=minecraft:armor_stand,tag=rallous.host.recsrc]
scoreboard players set $levy rallous.gen 0
execute if entity @e[type=#rallous_factions:levy,distance=..16,tag=!rallous.soldier,tag=!rallous.roam] run scoreboard players set $levy rallous.gen 1
execute if score $levy rallous.gen matches 1 run function rallous_factions:host/levy_tag
execute if score $levy rallous.gen matches 0 run function rallous_factions:host/levy_fallback
tag @s add rallous.host.levied
