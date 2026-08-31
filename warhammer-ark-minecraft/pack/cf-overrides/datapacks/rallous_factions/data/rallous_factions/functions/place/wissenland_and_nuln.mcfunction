# place Wissenland & Nuln — Elector Countess of Wissenland Elspeth von Draken
execute if score #wissenland_and_nuln rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #wissenland_and_nuln rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:packed_mud
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:red_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.wissenland_and_nuln"],CustomName:'{"text":"Elector Countess of Wissenland Elspeth von Draken","color":"red","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Elector Countess of Wissenland Elspeth von Draken","color":"red","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.wissenland_and_nuln"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:plains"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wissenland_and_nuln,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 42
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wissenland_and_nuln,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 1
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wissenland_and_nuln,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 1
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.wissenland_and_nuln,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #wissenland_and_nuln rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_empire rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
