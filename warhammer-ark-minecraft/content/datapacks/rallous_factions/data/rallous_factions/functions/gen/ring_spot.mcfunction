# Surface one mixed camp at this ring offset.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const run summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.ring"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.ring,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 8 28 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.ring,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_one
kill @e[type=minecraft:marker,tag=rallous.probe.ring]
