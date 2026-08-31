# place Clan Moulder — Master Moulder Throt the Unclean
execute if score #clan_moulder rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #clan_moulder rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:deepslate
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:purple_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:cobweb
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.clan_moulder"],CustomName:'{"text":"Master Moulder Throt the Unclean","color":"light_purple","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Master Moulder Throt the Unclean","color":"light_purple","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.clan_moulder"],VillagerData:{profession:"minecraft:toolsmith",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_moulder,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 107
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_moulder,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 7
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_moulder,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_moulder,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #clan_moulder rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_skaven rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
