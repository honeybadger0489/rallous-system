# as the target marker. #stance / #path / #race already set.
scoreboard players operation @s rallous.stance = #stance rallous.stance
scoreboard players operation @s rallous.path = #path rallous.path
execute unless score @s rallous.race matches 1..8 run scoreboard players operation @s rallous.race = #race rallous.race
tag @s remove rallous.stance.ally
tag @s remove rallous.stance.hostile
tag @s remove rallous.stance.joined
tag @s remove rallous.stance.neutral
