# Mid-session host at the player's camp gate — not a distant unloaded roll.
kill @e[type=minecraft:marker,tag=rallous.roam.spawner]
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run summon minecraft:marker ~ ~ ~8 {Tags:["rallous.roam.spawner"]}
execute unless entity @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run summon minecraft:marker ~ ~ ~ {Tags:["rallous.roam.spawner"]}
execute as @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] at @s run forceload add ~ ~
execute as @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] at @s run spreadplayers ~ ~ 12 28 false @s
