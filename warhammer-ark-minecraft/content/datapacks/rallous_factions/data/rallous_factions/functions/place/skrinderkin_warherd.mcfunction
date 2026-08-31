# place Skrinderkin Warherd — Wargor Skrinderkin
execute if score #skrinderkin_warherd rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #skrinderkin_warherd rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:rooted_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:brown_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.skrinderkin_warherd"],CustomName:'{"text":"Wargor Skrinderkin","color":"dark_green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Wargor Skrinderkin","color":"dark_green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.skrinderkin_warherd"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:stone_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skrinderkin_warherd,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 8
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skrinderkin_warherd,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skrinderkin_warherd,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skrinderkin_warherd,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #skrinderkin_warherd rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_beastmen rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
