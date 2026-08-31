# Caller has crater scores. Write {owner, pos}, then plant at those coords.

data modify storage rallous_crater_hq:data owner set from entity @s UUID
data modify storage rallous_crater_hq:data pos set value {x:0,y:0,z:0}
execute store result storage rallous_crater_hq:data pos.x int 1 run scoreboard players get @s rallous.crater_x
execute store result storage rallous_crater_hq:data pos.y int 1 run scoreboard players get @s rallous.crater_y
execute store result storage rallous_crater_hq:data pos.z int 1 run scoreboard players get @s rallous.crater_z

kill @e[type=minecraft:marker,tag=rallous.hq.probe]
summon minecraft:marker ~ ~ ~ {Tags:["rallous.hq.probe"]}
execute store result entity @e[type=minecraft:marker,tag=rallous.hq.probe,limit=1] Pos[0] double 1 run scoreboard players get @s rallous.crater_x
execute store result entity @e[type=minecraft:marker,tag=rallous.hq.probe,limit=1] Pos[1] double 1 run scoreboard players get @s rallous.crater_y
execute store result entity @e[type=minecraft:marker,tag=rallous.hq.probe,limit=1] Pos[2] double 1 run scoreboard players get @s rallous.crater_z

tag @s add rallous.hq.marking
execute as @e[type=minecraft:marker,tag=rallous.hq.probe,limit=1] at @s run function rallous_crater_hq:place
tag @s remove rallous.hq.marking
