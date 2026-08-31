# Walk the host toward the warband. Stay on the surface. Do not enter player melee range via teleport.
execute if entity @p[distance=5..80] facing entity @p feet run tp @s ^ ^ ^0.42
execute if entity @p[distance=80..] facing entity @p feet run tp @s ^ ^ ^0.7
data modify entity @s WanderTarget.X set from entity @p Pos[0]
data modify entity @s WanderTarget.Y set from entity @p Pos[1]
data modify entity @s WanderTarget.Z set from entity @p Pos[2]
execute at @s unless block ~ ~ ~ #minecraft:replaceable run tp @s ~ ~1 ~
execute at @s if block ~ ~-1 ~ #minecraft:replaceable if block ~ ~-2 ~ #minecraft:replaceable run tp @s ~ ~-1 ~
execute at @s if entity @p[distance=8..] run particle minecraft:cloud ~ ~0.2 ~ 0.2 0.05 0.2 0.01 1
