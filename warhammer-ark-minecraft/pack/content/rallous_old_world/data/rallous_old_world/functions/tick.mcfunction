# Court never. Spawn is rallous_warp_crash. Primer after that pack lands (or 5s fallback).
scoreboard players add @a[tag=!rallous.old_world] rallous.joined 1
execute as @a[tag=!rallous.old_world,tag=rallous.warp_landed] at @s run function rallous_old_world:first_join
execute as @a[tag=!rallous.old_world,tag=!rallous.warp_landed,scores={rallous.joined=100..}] at @s run function rallous_old_world:first_join
