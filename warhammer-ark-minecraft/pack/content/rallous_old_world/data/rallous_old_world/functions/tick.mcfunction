# Court never. Spawn is rallous_warp_crash. Primer after that pack lands.
# Do not increment rallous.joined while warp_crash owns the join (join_wait 1+).
# That score is the lock so land_go / assign / kit cannot run twice.
execute as @a[tag=!rallous.old_world,tag=rallous.warp_landed] at @s run function rallous_old_world:first_join
execute as @a[tag=!rallous.old_world,tag=!rallous.warp_landed] unless score @s rallous.join_wait matches 1.. unless score @s rallous.joined matches 1.. run scoreboard players add @s rallous.joined 1
execute as @a[tag=!rallous.old_world,tag=!rallous.warp_landed,scores={rallous.joined=100..}] unless score @s rallous.join_wait matches 1.. at @s run function rallous_old_world:first_join
