# One step friendlier. Prove first so hostile does not skip to help in one tick.
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @s rallous.fac.stance 1
execute if score @s rallous.fac.stance matches 3 run scoreboard players set @s rallous.fac.stance 2
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @s rallous.fac.stance 2
execute if score @s rallous.fac.stance matches 6 run scoreboard players set @s rallous.fac.stance 3
tellraw @a[distance=..48] {"text":"This faction watched you help. Their stance toward you shifted.","color":"green"}
execute if score @s rallous.fac.stance matches 1 as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
execute if score @s rallous.fac.stance matches 5 as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
