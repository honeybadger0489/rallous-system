# Guaranteed contact camp just off the crater. Mix-rotate — do not biome-stack.
summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.near"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 20 36 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_mix
kill @e[type=minecraft:marker,tag=rallous.probe]
