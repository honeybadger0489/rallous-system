# One night won. Help/defend (session_kind 1) is worth a second mark.
tag @s add rallous.grow.actor
tag @e[type=minecraft:marker,tag=rallous.camp,distance=..64,limit=1,sort=nearest] add rallous.grow.camp
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run scoreboard players add @s rallous.grow 1
execute if score @s rallous.session_kind matches 1 as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run function rallous_grow:credit/help
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] if score @s rallous.grow > #cap rallous.grow run scoreboard players operation @s rallous.grow = #cap rallous.grow
scoreboard players operation @s rallous.grow = @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] rallous.grow
scoreboard players set @s rallous.grow_sess 1
execute as @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] at @s run function rallous_grow:try_apply
execute if entity @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run tellraw @s [{"text":"The picket remembers you. Growth ","color":"gold"},{"score":{"name":"@s","objective":"rallous.grow"},"color":"white","bold":true},{"text":"/3.","color":"gold"}]
execute unless entity @e[type=minecraft:marker,tag=rallous.grow.camp,limit=1] run tellraw @s {"text":"No camp in range to grow. Stand by a rallous.camp banner.","color":"gray"}
tag @e[tag=rallous.grow.camp] remove rallous.grow.camp
tag @s remove rallous.grow.actor
