# First-days mix, then explore placements, then path stance sync.
scoreboard players add #clock rallous.gen 1
execute if score #booted rallous.gen matches 1 if score #placed rallous.gen < #cap rallous.const if score #clock rallous.gen matches 40 run function rallous_factions:gen/tick_place
execute if score #clock rallous.gen matches 40 run scoreboard players set #clock rallous.gen 0
execute if score #placed rallous.gen >= #cap rallous.const if score #placed rallous.gen < #xcap rallous.const as @a[tag=rallous.warp_landed] at @s unless entity @e[tag=rallous.camp,distance=..180,limit=1] run function rallous_factions:gen/explore
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_factions:path/sync
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s if entity @e[tag=rallous.camp,distance=..14,limit=1] run function rallous_factions:contact/assign
