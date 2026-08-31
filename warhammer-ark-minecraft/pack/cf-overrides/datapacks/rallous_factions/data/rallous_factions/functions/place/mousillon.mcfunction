# place Mousillon — Duke of Mousillon Maldred's Heir
execute if score #mousillon rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #mousillon rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:deepslate_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:black_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.mousillon"],CustomName:'{"text":"Duke of Mousillon Maldred’s Heir","color":"dark_red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Duke of Mousillon Maldred’s Heir","color":"dark_red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.mousillon"],VillagerData:{profession:"minecraft:cleric",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.mousillon,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 119
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.mousillon,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.mousillon,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.mousillon,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #mousillon rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_vampire_counts rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
