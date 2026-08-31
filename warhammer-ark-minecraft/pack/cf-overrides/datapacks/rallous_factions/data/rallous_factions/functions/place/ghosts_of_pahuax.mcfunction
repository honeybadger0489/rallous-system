# place Ghosts of Pahuax — The Hidden Oxyotl
execute if score #ghosts_of_pahuax rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #ghosts_of_pahuax rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:mossy_stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:lime_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.ghosts_of_pahuax"],CustomName:'{"text":"The Hidden Oxyotl","color":"aqua","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"The Hidden Oxyotl","color":"aqua","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.ghosts_of_pahuax"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:jungle"},HandItems:[{id:"minecraft:stone_sword",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.ghosts_of_pahuax,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 84
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.ghosts_of_pahuax,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.ghosts_of_pahuax,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.ghosts_of_pahuax,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #ghosts_of_pahuax rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_lizardmen rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
