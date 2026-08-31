# place The Ancestral Throng — The White Dwarf Grombrindal
execute if score #the_ancestral_throng rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #the_ancestral_throng rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.the_ancestral_throng"],CustomName:'{"text":"The White Dwarf Grombrindal","color":"gold","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"The White Dwarf Grombrindal","color":"gold","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.the_ancestral_throng"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_ancestral_throng,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 27
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_ancestral_throng,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 6
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_ancestral_throng,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.the_ancestral_throng,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #the_ancestral_throng rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_dwarfs rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
