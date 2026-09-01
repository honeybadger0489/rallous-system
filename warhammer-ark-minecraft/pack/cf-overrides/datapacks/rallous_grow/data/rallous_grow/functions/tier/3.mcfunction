# Hall, extra banners, one settler. This is an outpost, not a town hall.
scoreboard players set @s rallous.grow_tier 3
execute unless score @s rallous.fac.tier matches 3.. run scoreboard players set @s rallous.fac.tier 3
scoreboard players set #slot rallous.grow 3
function rallous_grow:hut/by_race
execute unless entity @e[tag=rallous.grow.settler,distance=..16,limit=1] run summon minecraft:villager ~1.2 ~ ~6 {CustomName:'{"text":"Outpost Settler","color":"gold"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.grow.settler"],VillagerData:{profession:"minecraft:nitwit",level:1,type:"minecraft:plains"}}
function rallous_grow:voice/tier3
