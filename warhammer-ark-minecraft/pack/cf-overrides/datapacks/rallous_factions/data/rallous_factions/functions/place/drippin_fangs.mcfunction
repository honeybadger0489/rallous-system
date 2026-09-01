# place Drippin Fangs — Savage Orc Warboss Drippin Fangs (waaagh war host)
execute if score #drippin_fangs rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #drippin_fangs rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:coarse_dirt
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
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~ ~2 ~-3 minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:hay_block
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~-2 minecraft:mossy_cobblestone
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.drippin_fangs"],CustomName:'{"text":"Savage Orc Warboss Drippin Fangs","color":"green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Savage Orc Warboss Drippin Fangs","color":"green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.drippin_fangs"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Orc Boy","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.drippin_fangs"]}
execute if score $skip rallous.gen matches 0 run summon recruits:bowman ~-2 ~ ~1 {CustomName:'{"text":"Arrer Boy","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.drippin_fangs"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.drippin_fangs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 58
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.drippin_fangs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 5
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.drippin_fangs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.drippin_fangs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #drippin_fangs rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_greenskins rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
