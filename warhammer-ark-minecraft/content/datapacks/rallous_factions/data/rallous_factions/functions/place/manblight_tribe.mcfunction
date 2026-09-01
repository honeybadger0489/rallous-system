# place Manblight Tribe — Bray-Shaman Slugtongue's Kin (herd war host)
execute if score #manblight_tribe rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #manblight_tribe rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:rooted_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:soul_campfire
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-3 minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:brown_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:brown_banner
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-2 minecraft:dark_oak_log
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-2 minecraft:dark_oak_log
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~3 minecraft:wither_skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:bone_block
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:hay_block
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.manblight_tribe"],CustomName:'{"text":"Bray-Shaman Slugtongue’s Kin","color":"dark_green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Bray-Shaman Slugtongue’s Kin","color":"dark_green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.manblight_tribe"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:stone_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Gor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.manblight_tribe"]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit_shieldman ~-2 ~ ~1 {CustomName:'{"text":"Bestigor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.manblight_tribe"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.manblight_tribe,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.manblight_tribe,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.manblight_tribe,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.manblight_tribe,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #manblight_tribe rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_beastmen rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
