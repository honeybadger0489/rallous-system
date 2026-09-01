# place Middenland — Elector Count of Middenland Boris Todbringer (settled war host)
execute if score #middenland rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #middenland rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:packed_mud
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-3 minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:lantern
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~-2 minecraft:barrel
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:hay_block
execute if score $skip rallous.gen matches 0 run setblock ~ ~2 ~-3 minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~2 minecraft:crafting_table
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.middenland"],CustomName:'{"text":"Elector Count of Middenland Boris Todbringer","color":"red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Elector Count of Middenland Boris Todbringer","color":"red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.middenland"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:plains"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit_shieldman ~2 ~ ~1 {CustomName:'{"text":"State Troop","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.middenland"]}
execute if score $skip rallous.gen matches 0 run summon recruits:bowman ~-2 ~ ~1 {CustomName:'{"text":"Handgunner","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.middenland"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.middenland,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 33
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.middenland,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 1
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.middenland,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 1
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.middenland,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #middenland rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_empire rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
