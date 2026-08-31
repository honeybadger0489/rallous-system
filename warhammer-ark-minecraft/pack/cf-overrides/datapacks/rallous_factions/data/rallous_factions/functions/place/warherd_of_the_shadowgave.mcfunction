# place Warherd of the Shadowgave — The Shadowgave Morghur
execute if score #warherd_of_the_shadowgave rallous.used matches 1 run scoreboard players set $skip rallous.gen 1
execute unless score #warherd_of_the_shadowgave rallous.used matches 1 run scoreboard players set $skip rallous.gen 0
execute if score $skip rallous.gen matches 0 run fill ~-1 ~-1 ~-1 ~1 ~-1 ~1 minecraft:coarse_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~-1 ~ minecraft:rooted_dirt
execute if score $skip rallous.gen matches 0 run setblock ~ ~ ~ minecraft:campfire
execute if score $skip rallous.gen matches 0 run setblock ~1 ~ ~ minecraft:dark_oak_fence
execute if score $skip rallous.gen matches 0 run setblock ~1 ~1 ~ minecraft:brown_banner
execute if score $skip rallous.gen matches 0 run setblock ~-1 ~ ~ minecraft:skeleton_skull
execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ {Tags:["rallous.camp","rallous.fac.warherd_of_the_shadowgave"],CustomName:'{"text":"The Shadowgave Morghur","color":"dark_green","bold":true}'}
execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ {CustomName:'{"text":"The Shadowgave Morghur","color":"dark_green","bold":true}',CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,Tags:["rallous.lord","rallous.fac.warherd_of_the_shadowgave"],VillagerData:{profession:"minecraft:nitwit",level:3,type:"minecraft:taiga"},HandItems:[{id:"minecraft:stone_axe",Count:1b},{}]}
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.warherd_of_the_shadowgave,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id 12
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.warherd_of_the_shadowgave,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race 4
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.warherd_of_the_shadowgave,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance 3
execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.warherd_of_the_shadowgave,limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier 1
execute if score $skip rallous.gen matches 0 run scoreboard players set #warherd_of_the_shadowgave rallous.used 1
execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_beastmen rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1
execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1
