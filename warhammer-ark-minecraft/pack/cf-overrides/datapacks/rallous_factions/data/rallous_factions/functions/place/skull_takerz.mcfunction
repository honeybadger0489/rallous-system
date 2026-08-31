# place Skull-takerz — Savage Orc Warboss Skull-taka
execute if score #skull_takerz rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #skull_takerz rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.skull_takerz"],CustomName:'{"text":"Savage Orc Warboss Skull-taka","color":"green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Savage Orc Warboss Skull-taka","color":"green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.skull_takerz"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skull_takerz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 68
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skull_takerz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 5
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skull_takerz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.skull_takerz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #skull_takerz rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_greenskins rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
