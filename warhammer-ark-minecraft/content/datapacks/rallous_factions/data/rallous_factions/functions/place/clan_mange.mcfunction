# place Clan Mange — Chieftain Mange (under-empire war host)
execute if score #clan_mange rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #clan_mange rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:deepslate
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:deepslate_tiles
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~-2 minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~ ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~1 ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~ ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~1 ~ minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~-3 minecraft:cobblestone_wall
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:purple_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:purple_banner
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~-1 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~-1 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~1 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:cobweb
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~-2 minecraft:cauldron
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:iron_bars
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~2 minecraft:iron_bars
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.clan_mange"],CustomName:'{"text":"Chieftain Mange","color":"light_purple","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"Chieftain Mange","color":"light_purple","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.clan_mange"],VillagerData:{profession:"minecraft:toolsmith",level:3,type:"minecraft:swamp"},HandItems:[{id:"minecraft:iron_sword",Count:1b},{}],ArmorItems:[{id:"minecraft:leather_boots",Count:1b,tag:{display:{color:4863784}}},{id:"minecraft:leather_leggings",Count:1b,tag:{display:{color:4863784}}},{id:"minecraft:leather_chestplate",Count:1b,tag:{display:{color:4863784}}},{id:"minecraft:leather_helmet",Count:1b,tag:{display:{color:4863784}}}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit ~2 ~ ~1 {CustomName:'{"text":"Clanrat","color":"light_purple"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.clan_mange"]}
execute if score $skip rallous.gen matches 0 run summon recruits:scout ~-2 ~ ~1 {CustomName:'{"text":"Night Runner","color":"light_purple"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.clan_mange"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 103
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 7
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.clan_mange,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute if score $skip rallous.gen matches 0 run scoreboard players set #clan_mange rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_skaven rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
