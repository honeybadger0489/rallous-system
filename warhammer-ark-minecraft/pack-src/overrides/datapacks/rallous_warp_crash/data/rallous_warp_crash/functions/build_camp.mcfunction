# Bannered picket — faction-contact hook, not a crash ship.
fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:packed_mud
setblock ~ ~ ~ minecraft:campfire
setblock ~1 ~ ~ minecraft:oak_fence
setblock ~1 ~1 ~ minecraft:lantern
setblock ~-1 ~ ~ minecraft:oak_fence
setblock ~-1 ~1 ~ minecraft:purple_banner
setblock ~ ~ ~1 minecraft:white_banner
execute unless entity @e[tag=rallous_contact,distance=..6,limit=1] run summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous_contact"],Invisible:1b,Marker:1b,NoGravity:1b,Invulnerable:1b,Small:1b,CustomName:'{"text":"Faction Contact","color":"gold"}',CustomNameVisible:1b}
kill @s
