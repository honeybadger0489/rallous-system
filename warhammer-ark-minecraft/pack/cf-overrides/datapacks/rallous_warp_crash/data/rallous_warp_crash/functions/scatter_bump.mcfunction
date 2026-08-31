scoreboard players add @s rallous.retry 1
execute if score @s rallous.retry matches 8.. run function rallous_warp_crash:land
execute unless score @s rallous.retry matches 8.. run scoreboard players add @s rallous.slot 1
execute unless score @s rallous.retry matches 8.. if score @s rallous.slot matches 12.. run scoreboard players add @s rallous.ring 1
execute unless score @s rallous.retry matches 8.. if score @s rallous.slot matches 12.. run scoreboard players set @s rallous.slot 0
execute unless score @s rallous.retry matches 8.. run function rallous_warp_crash:scatter
