execute as @a[tag=rallous.warp_landed,tag=!rallous.winds.stripped] run function rallous_winds:strip
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds] at @s run function rallous_winds:place
