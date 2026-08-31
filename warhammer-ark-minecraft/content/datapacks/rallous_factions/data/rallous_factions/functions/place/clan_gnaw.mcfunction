# place Clan Gnaw — Chieftain Gnaw
execute if score #clan_gnaw rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #clan_gnaw rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:deepslate
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:purple_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:cobweb
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.clan_gnaw"],CustomName:'{"text":"Chieftain Gnaw","color":"light_purple","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Chieftain Gnaw","color":"light_purple","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.clan_gnaw"],VillagerData:{profession:"minecraft:toolsmith",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_gnaw,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 99
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_gnaw,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 7
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_gnaw,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_gnaw,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #clan_gnaw rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_skaven rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
