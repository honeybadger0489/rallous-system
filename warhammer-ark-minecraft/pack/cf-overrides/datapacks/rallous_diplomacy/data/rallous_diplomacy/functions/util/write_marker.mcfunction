# as the target marker. #stance / #path / #race already set.
# rallous.stance 1 ally / 2 hostile / 3 joined / 4 neutral
# Mirror rallous.fac.stance for compiled camps: 1 help / 5 join / 6 war / 2 prove
scoreboard players operation @s rallous.stance = #stance rallous.stance
scoreboard players operation @s rallous.path = #path rallous.path
execute unless score @s rallous.race matches 1..8 run scoreboard players operation @s rallous.race = #race rallous.race
execute if score #stance rallous.stance matches 1 run scoreboard players set @s rallous.fac.stance 1
execute if score #stance rallous.stance matches 2 run scoreboard players set @s rallous.fac.stance 6
execute if score #stance rallous.stance matches 3 run scoreboard players set @s rallous.fac.stance 5
execute if score #stance rallous.stance matches 4 run scoreboard players set @s rallous.fac.stance 2
tag @s remove rallous.stance.ally
tag @s remove rallous.stance.hostile
tag @s remove rallous.stance.joined
tag @s remove rallous.stance.neutral
