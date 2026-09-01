summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.far"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 140 380 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_mix
kill @e[type=minecraft:marker,tag=rallous.probe]
