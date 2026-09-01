# As the camp marker, at the camp. Place any tiers the grow score has earned.
execute if score @s rallous.grow matches 1.. unless score @s rallous.grow_tier matches 1.. run function rallous_grow:tier/1
execute if score @s rallous.grow matches 2.. unless score @s rallous.grow_tier matches 2.. run function rallous_grow:tier/2
execute if score @s rallous.grow matches 3.. unless score @s rallous.grow_tier matches 3.. run function rallous_grow:tier/3
