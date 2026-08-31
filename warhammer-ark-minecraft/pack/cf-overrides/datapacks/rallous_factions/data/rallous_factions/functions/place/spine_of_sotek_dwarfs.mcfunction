# place Spine of Sotek Dwarfs — Thane Sotek-Spine
execute if score #spine_of_sotek_dwarfs rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #spine_of_sotek_dwarfs rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.spine_of_sotek_dwarfs"],CustomName:'{"text":"Thane Sotek-Spine","color":"gold","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Thane Sotek-Spine","color":"gold","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.spine_of_sotek_dwarfs"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.spine_of_sotek_dwarfs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 26
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.spine_of_sotek_dwarfs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 6
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.spine_of_sotek_dwarfs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.spine_of_sotek_dwarfs,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #spine_of_sotek_dwarfs rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_dwarfs rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
