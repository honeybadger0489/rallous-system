# Mixed-race pickets on walkable rings. Not TW cities. Cap still 16.
# Target inner ~120 / outer ~220. Forceload each 3x3 (72 chunks, under 256).
# Probes stay at the crash until spreadplayers finds land — never skip a race.
kill @e[type=minecraft:marker,tag=rallous.ring.origin]
kill @e[type=minecraft:marker,tag=rallous.probe.pending]
summon minecraft:marker ~ ~ ~ {Tags:["rallous.ring.origin"]}
execute store result score $origin_x rallous.gen run data get entity @s Pos[0]
execute store result score $origin_z rallous.gen run data get entity @s Pos[2]
execute positioned ~120 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~-120 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~120 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~-120 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~220 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~-220 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~220 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~-220 run forceload add ~-1 ~-1 ~1 ~1
scoreboard players set $ring_kind rallous.gen 0
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
scoreboard players set $ring_kind rallous.gen 1
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
execute as @e[type=minecraft:marker,tag=rallous.probe.pending] at @s run function rallous_factions:gen/ring_try
schedule function rallous_factions:debug/count_races 100t replace
