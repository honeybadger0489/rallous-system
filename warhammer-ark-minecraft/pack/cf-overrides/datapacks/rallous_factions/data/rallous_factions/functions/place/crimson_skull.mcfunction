# place Crimson Skull — Skullmaster Crimson Skull (khorne war host)
execute if score #crimson_skull rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #crimson_skull rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:red_nether_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:magma_block
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:soul_campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:soul_campfire
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~ minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~ minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~ minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~ minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-3 minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~ ~2 ~-3 minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~-3 minecraft:wither_skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:nether_wart_block
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:blackstone
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.crimson_skull"],CustomName:'{"text":"Skullmaster Crimson Skull","color":"dark_red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Skullmaster Crimson Skull","color":"dark_red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.crimson_skull"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Bloodreaver","color":"dark_red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.crimson_skull"]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit_shieldman ~-2 ~ ~1 {CustomName:'{"text":"Blood Warrior","color":"dark_red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.crimson_skull"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.crimson_skull,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 80
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.crimson_skull,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 8
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.crimson_skull,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.crimson_skull,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #crimson_skull rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_khorne rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
