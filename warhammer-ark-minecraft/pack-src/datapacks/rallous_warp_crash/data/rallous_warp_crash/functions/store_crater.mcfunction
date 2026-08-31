# Scoreboard + data storage + per-player marker. forceload so death can find it.
execute store result score @s rallous.crater_x run data get entity @s Pos[0]
execute store result score @s rallous.crater_y run data get entity @s Pos[1]
execute store result score @s rallous.crater_z run data get entity @s Pos[2]
forceload add ~ ~

summon minecraft:marker ~ ~ ~ {Tags:["rallous.crater","rallous.crater_new"]}
scoreboard players operation @e[type=minecraft:marker,tag=rallous.crater_new,limit=1,sort=nearest] rallous.pid = @s rallous.pid
data modify entity @e[type=minecraft:marker,tag=rallous.crater_new,limit=1,sort=nearest] data.Owner set from entity @s UUID
tag @e[type=minecraft:marker,tag=rallous.crater_new] remove rallous.crater_new

data modify storage rallous_warp_crash:data craters append value {UUID:[I;0,0,0,0],pid:0,slot:0,x:0,y:0,z:0}
data modify storage rallous_warp_crash:data craters[-1].UUID set from entity @s UUID
execute store result storage rallous_warp_crash:data craters[-1].pid int 1 run scoreboard players get @s rallous.pid
execute store result storage rallous_warp_crash:data craters[-1].slot int 1 run scoreboard players get @s rallous.slot
execute store result storage rallous_warp_crash:data craters[-1].x int 1 run scoreboard players get @s rallous.crater_x
execute store result storage rallous_warp_crash:data craters[-1].y int 1 run scoreboard players get @s rallous.crater_y
execute store result storage rallous_warp_crash:data craters[-1].z int 1 run scoreboard players get @s rallous.crater_z
