# as player at player — pick THAT nearest contact / camp lord (512).
tag @e[tag=rallous.diplo.target] remove rallous.diplo.target
tag @e[tag=rallous_contact] add rallous.diplo.camp
tag @e[tag=rallous.lord] add rallous.diplo.camp
tag @e[tag=rallous_lord] add rallous.diplo.camp
tag @e[tag=rallous.lord_stand] add rallous.diplo.camp
tag @e[tag=rallous.camp_lord] add rallous.diplo.camp
execute as @e[tag=rallous.diplo.camp,distance=..512,limit=1,sort=nearest] run tag @s add rallous.diplo.target
scoreboard players operation #path rallous.path = @s rallous.path
scoreboard players operation #race rallous.race = @s rallous.race
scoreboard players set @s rallous.diplo 1
