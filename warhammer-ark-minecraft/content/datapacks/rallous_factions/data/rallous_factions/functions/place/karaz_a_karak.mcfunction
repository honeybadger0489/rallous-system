# place Karaz-a-Karak — High King of the Karaz Ankor Thorgrim Grudgebearer (hold war host)
execute if score #karaz_a_karak rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #karaz_a_karak rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 minecraft:stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
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
execute if score $skip rallous.gen matches 0 run setblock ~3 ~2 ~ minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run setblock ~-3 ~2 ~ minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~2 minecraft:lantern
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~-2 minecraft:anvil
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~2 minecraft:smithing_table
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~3 minecraft:iron_bars
execute if score $skip rallous.gen matches 0 run setblock ~ ~1 ~3 minecraft:iron_bars
execute if score $skip rallous.gen matches 0 run setblock ~ ~2 ~-3 minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.karaz_a_karak"],CustomName:'{"text":"High King of the Karaz Ankor Thorgrim Grudgebearer","color":"gold","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"High King of the Karaz Ankor Thorgrim Grudgebearer","color":"gold","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.karaz_a_karak"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}],ArmorItems:[{id:"minecraft:chainmail_boots",Count:1b},{id:"minecraft:chainmail_leggings",Count:1b},{id:"minecraft:chainmail_chestplate",Count:1b},{id:"minecraft:chainmail_helmet",Count:1b}]}
execute if score $skip rallous.gen matches 0 run summon recruits:recruit_shieldman ~2 ~ ~1 {CustomName:'{"text":"Dwarf Warrior","color":"gold"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.karaz_a_karak"]}
execute if score $skip rallous.gen matches 0 run summon recruits:crossbowman ~-2 ~ ~1 {CustomName:'{"text":"Quarreller","color":"gold"}',CustomNameVisible:1b,PersistenceRequired:1b,CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.karaz_a_karak"]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 24
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 6
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karaz_a_karak,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute if score $skip rallous.gen matches 0 run scoreboard players set #karaz_a_karak rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_dwarfs rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
