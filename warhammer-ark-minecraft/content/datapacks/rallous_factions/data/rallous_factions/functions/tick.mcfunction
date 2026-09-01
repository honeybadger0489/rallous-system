# First-days mix, then explore placements, then path stance sync.
scoreboard players add #clock rallous.gen 1
execute if score #booted rallous.gen matches 1 if score #placed rallous.gen < #cap rallous.const if score #clock rallous.gen matches 40 run function rallous_factions:gen/tick_place
execute if score #clock rallous.gen matches 40 run scoreboard players set #clock rallous.gen 0
execute if score #placed rallous.gen >= #cap rallous.const if score #placed rallous.gen < #xcap rallous.const as @a[tag=rallous.warp_landed] at @s unless entity @e[tag=rallous.camp,distance=..180,limit=1] run function rallous_factions:gen/explore
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_diplomacy:apply_path
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_factions:path/sync
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s if entity @e[tag=rallous.camp,distance=..18,limit=1] run function rallous_factions:contact/assign
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s as @e[tag=rallous.camp,limit=1,sort=nearest,distance=..80] at @s run particle minecraft:campfire_signal_smoke ~ ~3 ~ 0.15 0.8 0.15 0.01 3
execute as @a[scores={rallous.burn=1..},tag=rallous.fac.greeted,tag=!rallous.burned] at @s if entity @e[tag=rallous.camp,distance=..14,limit=1] run function rallous_factions:path/burn_welcome
execute as @a[scores={rallous.burn=1..}] unless entity @e[tag=rallous.camp,distance=..14,limit=1] run scoreboard players set @s rallous.burn 0
execute as @a[tag=rallous.fac.greeted,tag=!rallous.burned] at @s at @e[tag=rallous.camp,distance=..14,limit=1,sort=nearest] if block ~1 ~1 ~ minecraft:fire run function rallous_factions:path/burn_welcome
