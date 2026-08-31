# place Karak Norn — King of Karak Norn Brokk Ironpick
execute if score #karak_norn rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #karak_norn rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-2 ~-1 ~-2 ~2 ~-1 ~2 minecraft:stone_bricks
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:cobblestone
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~2 ~ ~ minecraft:oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~2 ~1 ~ minecraft:yellow_banner
execute if score $skip rallous.gen matches 0 run setblock ~-2 ~ ~ minecraft:lantern
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.karak_norn"],CustomName:'{"text":"King of Karak Norn Brokk Ironpick","color":"gold","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"King of Karak Norn Brokk Ironpick","color":"gold","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.karak_norn"],VillagerData:{profession:"minecraft:weaponsmith",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karak_norn,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 22
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karak_norn,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 6
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karak_norn,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.karak_norn,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 2
execute if score $skip rallous.gen matches 0 run scoreboard players set #karak_norn rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_dwarfs rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
