summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp_probe"]}
execute as @e[type=minecraft:marker,tag=rallous.camp_probe,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 72 140 false @s
execute as @e[type=minecraft:marker,tag=rallous.camp_probe,limit=1,sort=nearest] at @s run function rallous_warp_crash:build_camp
