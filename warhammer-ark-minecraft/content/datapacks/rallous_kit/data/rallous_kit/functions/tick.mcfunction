# Once: if greeted and not yet kitted, issue the race kit.
# Warp/factions should call rallous_kit:on_greet; this is the backup.
execute as @a[tag=rallous.fac.greeted] unless score @s rallous.greeted matches 1.. run scoreboard players set @s rallous.greeted 1
execute as @a[tag=rallous.contacted] unless score @s rallous.greeted matches 1.. run scoreboard players set @s rallous.greeted 1
execute as @a if score @s rallous.contact matches 1.. unless score @s rallous.greeted matches 1.. run scoreboard players set @s rallous.greeted 1
execute as @a[tag=rallous.warp_landed] if score @s rallous.greeted matches 1.. unless score @s rallous.kitted matches 1.. if score @s rallous.race matches 1..8 run function rallous_kit:on_greet
execute as @a[tag=!rallous.warp_landed] if score @s rallous.joined matches 1.. if score @s rallous.greeted matches 1.. unless score @s rallous.kitted matches 1.. if score @s rallous.race matches 1..8 run function rallous_kit:on_greet
