scoreboard players set @s rallous.fac.stance 5
tellraw @a[distance=..48] {"text":"This faction takes your colour. You are of the host now.","color":"gold"}
give @p minecraft:white_banner{display:{Name:'{"text":"Taken Colour","italic":false}'}} 1
execute as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
