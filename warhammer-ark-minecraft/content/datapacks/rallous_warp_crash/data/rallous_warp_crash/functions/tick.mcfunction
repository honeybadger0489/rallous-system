# New arrivals wait briefly so chunks exist, then crash once.
execute as @a[tag=!rallous.warp_landed] unless score @s rallous.joined matches 1.. if dimension minecraft:overworld run scoreboard players add @s rallous.join_wait 1
execute as @a[tag=!rallous.warp_landed,scores={rallous.join_wait=40..}] unless score @s rallous.joined matches 1.. at @s if dimension minecraft:overworld run function rallous_warp_crash:first_join

# Death: same person, same crater, unless they chose a civilization bed.
execute as @a[scores={rallous.has_crater=1}] if score @s rallous.wc_deaths > @s rallous.wc_seen run function rallous_warp_crash:on_death

# Wilderness beds must not steal crater spawn until civ_bed is set.
execute as @a[scores={rallous.has_crater=1,rallous.civ_bed=0}] run function rallous_warp_crash:keep_crater_spawn
