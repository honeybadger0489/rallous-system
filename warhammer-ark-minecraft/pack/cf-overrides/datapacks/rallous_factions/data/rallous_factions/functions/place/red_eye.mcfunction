# place Red Eye — Night Goblin Warboss Red Eye
execute if score #red_eye rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #red_eye rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:packed_mud
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.red_eye"],CustomName:'{"text":"Night Goblin Warboss Red Eye","color":"green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Night Goblin Warboss Red Eye","color":"green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.red_eye"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.red_eye,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 64
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.red_eye,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 5
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.red_eye,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.red_eye,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #red_eye rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_greenskins rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
