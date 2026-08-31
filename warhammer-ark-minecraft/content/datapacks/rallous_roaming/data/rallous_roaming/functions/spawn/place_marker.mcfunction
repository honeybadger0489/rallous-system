# Surface a spawn point 28–56 blocks from the player. 1.20.1 spreadplayers.
kill @e[type=minecraft:marker,tag=rallous.roam.spawner]
summon minecraft:marker ~ ~ ~ {Tags:["rallous.roam.spawner"]}
spreadplayers ~ ~ 28 56 false @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1]
