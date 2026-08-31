# place Caravan of Blue Roses — The Red Duke The Red Duke
execute if score #caravan_of_blue_roses rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #caravan_of_blue_roses rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:black_banner
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.caravan_of_blue_roses"],CustomName:'{"text":"The Red Duke The Red Duke","color":"dark_red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"The Red Duke The Red Duke","color":"dark_red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.caravan_of_blue_roses"],VillagerData:{profession:"minecraft:cleric",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.caravan_of_blue_roses,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 116
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.caravan_of_blue_roses,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.caravan_of_blue_roses,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.caravan_of_blue_roses,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #caravan_of_blue_roses rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_vampire_counts rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
