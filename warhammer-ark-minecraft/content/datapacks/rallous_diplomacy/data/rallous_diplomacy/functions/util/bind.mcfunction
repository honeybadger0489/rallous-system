# as player at player — THAT nearest camp marker (prefer score-holder), else a lord.
tag @e[tag=rallous.diplo.target] remove rallous.diplo.target
execute as @e[tag=rallous.camp,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
execute unless entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous_contact,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
execute unless entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous.lord,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
execute unless entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous_lord,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
execute unless entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous.lord_stand,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
execute unless entity @e[tag=rallous.diplo.target,limit=1] as @e[tag=rallous.camp_lord,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
scoreboard players operation #path rallous.path = @s rallous.path
scoreboard players operation #race rallous.race = @s rallous.race
scoreboard players set @s rallous.diplo 1
