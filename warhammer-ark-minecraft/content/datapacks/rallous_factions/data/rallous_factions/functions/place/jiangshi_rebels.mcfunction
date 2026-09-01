# place Jiangshi Rebels — Jiangshi Lord Prince Jiang (settled war host)
execute if score #jiangshi_rebels rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #jiangshi_rebels rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:deepslate_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:soul_campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:campfire
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
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:black_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:black_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:soul_lantern
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~-2 minecraft:barrel
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:hay_block
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~3 minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~-1 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~-1 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.jiangshi_rebels"],CustomName:'{"text":"Jiangshi Lord Prince Jiang","color":"dark_red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Jiangshi Lord Prince Jiang","color":"dark_red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.jiangshi_rebels"],VillagerData:{profession:"minecraft:cleric",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}],ArmorItems:[{id:"minecraft:leather_boots",Count:1b,tag:{display:{color:1908001}}},{id:"minecraft:leather_leggings",Count:1b,tag:{display:{color:1908001}}},{id:"minecraft:leather_chestplate",Count:1b,tag:{display:{color:1908001}}},{id:"minecraft:leather_helmet",Count:1b,tag:{display:{color:1908001}}}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Grave Guard","color":"dark_red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.jiangshi_rebels"]}
execute if score $skip rallous.gen matches 0 run summon recruits:bowman ~-2 ~ ~1 {CustomName:'{"text":"Sylvanian Levy","color":"dark_red"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.jiangshi_rebels"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 117
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.jiangshi_rebels,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute if score $skip rallous.gen matches 0 run scoreboard players set #jiangshi_rebels rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_vampire_counts rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
