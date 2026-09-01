# place Wardens of the Living Pools — Skink Chief Huatl Pool-Guard (temple war host)
execute if score #wardens_of_the_living_pools rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #wardens_of_the_living_pools rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:mossy_stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:chiseled_stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:sea_lantern
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~ minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~ minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~ minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~ minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-3 minecraft:jungle_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:lime_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:lime_banner
execute if score $skip rallous.gen matches 0 run setblock ~ ~2 ~-3 minecraft:lime_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:lantern
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~-1 ~-2 minecraft:gold_block
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:moss_carpet
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~-1 minecraft:moss_carpet
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~1 minecraft:vine
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.wardens_of_the_living_pools"],CustomName:'{"text":"Skink Chief Huatl Pool-Guard","color":"aqua","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Skink Chief Huatl Pool-Guard","color":"aqua","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.wardens_of_the_living_pools"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:jungle"},HandItems:[{id:"minecraft:stone_sword",Count:1b},{}],ArmorItems:[{id:"minecraft:leather_boots",Count:1b,tag:{display:{color:8439583}}},{id:"minecraft:leather_leggings",Count:1b,tag:{display:{color:8439583}}},{id:"minecraft:leather_chestplate",Count:1b,tag:{display:{color:8439583}}},{id:"minecraft:turtle_helmet",Count:1b}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Temple Guard","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.wardens_of_the_living_pools"]}
execute if score $skip rallous.gen matches 0 run summon recruits:scout ~-2 ~ ~1 {CustomName:'{"text":"Skink Scout","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.wardens_of_the_living_pools"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 94
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wardens_of_the_living_pools,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute if score $skip rallous.gen matches 0 run scoreboard players set #wardens_of_the_living_pools rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_lizardmen rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
