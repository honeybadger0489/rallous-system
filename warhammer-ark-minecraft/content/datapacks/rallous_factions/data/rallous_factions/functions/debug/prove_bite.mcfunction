# Hostile camp must spawn raid entities. Help-leaning must not.
say [rallous.bite] start
scoreboard players set $bite rallous.gen 0
kill @e[tag=rallous.bite.dummy]
kill @e[tag=rallous.help.dummy]
kill @e[tag=rallous.raid]
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/skaven/pick
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/khorne/pick
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/beastmen/pick
scoreboard players set $mix_only rallous.gen 0
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1,sort=nearest] at @s run summon minecraft:villager ~1 ~ ~ {Tags:["rallous.bite.dummy"],CustomName:'{"text":"Bite Dummy","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b}
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1,sort=nearest] at @s run function rallous_factions:stance/bite
execute store result score $raid_n rallous.gen if entity @e[tag=rallous.raid]
execute if score $bite rallous.gen matches 1.. if score $raid_n rallous.gen matches 1.. run say [rallous.bite] OK hostile raid spawned
execute unless score $raid_n rallous.gen matches 1.. run say [rallous.bite] FAIL no raid entities
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1] positioned ~-28 ~ ~ run function rallous_factions:pool/empire/pick
scoreboard players set $mix_only rallous.gen 0
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] at @s run summon minecraft:villager ~1 ~ ~ {Tags:["rallous.help.dummy"],CustomName:'{"text":"Help Dummy","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b}
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] if entity @s[tag=rallous.bitten] run say [rallous.bite] FAIL help camp bitten
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] unless entity @s[tag=rallous.bitten] run say [rallous.bite] OK help camp did not bite
execute as @e[tag=rallous.help.dummy,limit=1] at @s if entity @e[type=minecraft:pillager,tag=rallous.host.levy,distance=..8,limit=1] run say [rallous.bite] FAIL help levy is a pillager
execute as @e[tag=rallous.help.dummy,limit=1] at @s unless entity @e[type=minecraft:pillager,tag=rallous.host.levy,distance=..8,limit=1] run say [rallous.bite] OK help dummy not facing camp pillagers
