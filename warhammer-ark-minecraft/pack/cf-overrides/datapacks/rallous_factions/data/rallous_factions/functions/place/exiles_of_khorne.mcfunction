# place Exiles of Khorne — The Exiled Skarbrand the Exiled
execute if score #exiles_of_khorne rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #exiles_of_khorne rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:red_nether_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:magma_block
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:soul_campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:nether_brick_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.exiles_of_khorne"],CustomName:'{"text":"The Exiled Skarbrand the Exiled","color":"dark_red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"The Exiled Skarbrand the Exiled","color":"dark_red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.exiles_of_khorne"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:savanna"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.exiles_of_khorne,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 81
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.exiles_of_khorne,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 8
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.exiles_of_khorne,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.exiles_of_khorne,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #exiles_of_khorne rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_khorne rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
