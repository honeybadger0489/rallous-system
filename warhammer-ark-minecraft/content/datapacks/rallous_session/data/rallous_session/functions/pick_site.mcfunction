# Village if a villager or bell is near the camp or the actor; else the camp picket.
tag @e[tag=rallous.session.site] remove rallous.session.site
tag @e[tag=rallous.session.village] remove rallous.session.village
execute as @e[tag=rallous.session.camp,limit=1] at @s if entity @e[type=minecraft:villager,distance=..80,limit=1] run tag @e[type=minecraft:villager,distance=..80,limit=1,sort=nearest] add rallous.session.village
execute as @e[tag=rallous.session.camp,limit=1] at @s if entity @e[type=minecraft:villager,distance=..80,limit=1] run tag @e[type=minecraft:villager,distance=..80,limit=1,sort=nearest] add rallous.session.site
execute unless entity @e[tag=rallous.session.site,limit=1] if entity @e[type=minecraft:villager,distance=..48,limit=1] run tag @e[type=minecraft:villager,distance=..48,limit=1,sort=nearest] add rallous.session.village
execute unless entity @e[tag=rallous.session.site,limit=1] if entity @e[type=minecraft:villager,distance=..48,limit=1] run tag @e[type=minecraft:villager,distance=..48,limit=1,sort=nearest] add rallous.session.site
execute as @e[type=minecraft:villager,tag=rallous.session.village] run tag @s add rallous.session.site
execute unless entity @e[tag=rallous.session.site,limit=1] as @e[tag=rallous.session.camp,limit=1] run tag @s add rallous.session.site
