# Recruits 1.20.1-1.15.x (talhanation PatrolSpawnCommand):
#   /recruits spawn recruitPatrol tiny|small|medium|large|huge|caravan
#   /recruits spawn pillagerPatrol tiny|small|medium|large
# tiny = recruit + shieldman + bowman + commander. Command uses
# getEntity().getOnPos() — must run as an entity at the column, not the player.
# Command always returns 0, so success is "levy appeared", not store success.
# Vanilla named mobs in *_mobs stay up. Extra vanilla only if this fails.

summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.roam.recsrc"],Invisible:1b,Marker:1b,NoGravity:1b,Small:1b,Invulnerable:1b,DisabledSlots:4144959}
execute as @e[type=minecraft:armor_stand,tag=rallous.roam.recsrc,limit=1] at @s run recruits spawn recruitPatrol tiny
kill @e[type=minecraft:armor_stand,tag=rallous.roam.recsrc]

scoreboard players set $rec rallous.roam 0
execute if entity @e[type=#rallous_roaming:levy,distance=..16,tag=!rallous.roam] run scoreboard players set $rec rallous.roam 1
execute if score $rec rallous.roam matches 1 run function rallous_roaming:spawn/recruits_tag
execute if score $rec rallous.roam matches 0 run function rallous_roaming:spawn/recruits_fallback
