scoreboard players set @s rallous.fac.stance 6
tellraw @a[distance=..48] {"text":"This faction names you oath-breaker. Their stance is war.","color":"red"}
execute at @s run function rallous_factions:contact/raid_generic
execute as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:war
