# Emerald hire / villager trade at the nearest camp. Caps at 3.
tag @s add rallous.grow.actor
tag @e[type=minecraft:marker,tag=rallous.camp,distance=..24,limit=1,sort=nearest] add rallous.grow.camp
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run scoreboard players add @s rallous.grow 1
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] if score @s rallous.grow > #cap rallous.grow run scoreboard players operation @s rallous.grow = #cap rallous.grow
scoreboard players operation @s rallous.grow = @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] rallous.grow
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] at @s run function rallous_grow:try_apply
execute if entity @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run tellraw @s [{"text":"Tribute taken. The outpost grows ","color":"gold"},{"score":{"name":"@s","objective":"rallous.grow"},"color":"white","bold":true},{"text":"/3.","color":"gold"}]
tag @e[tag=rallous.grow.camp] remove rallous.grow.camp
tag @s remove rallous.grow.actor
