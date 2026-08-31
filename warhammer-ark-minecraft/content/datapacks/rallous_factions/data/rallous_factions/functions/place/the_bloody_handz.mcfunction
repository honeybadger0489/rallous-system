# place The Bloody Handz — Great Shaman Wurrzag da Great Green Prophet
execute if score #the_bloody_handz rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #the_bloody_handz rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:packed_mud
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:green_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.the_bloody_handz"],CustomName:'{"text":"Great Shaman Wurrzag da Great Green Prophet","color":"green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Great Shaman Wurrzag da Great Green Prophet","color":"green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.the_bloody_handz"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_bloody_handz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 73
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_bloody_handz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 5
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_bloody_handz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_bloody_handz,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #the_bloody_handz rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_greenskins rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
