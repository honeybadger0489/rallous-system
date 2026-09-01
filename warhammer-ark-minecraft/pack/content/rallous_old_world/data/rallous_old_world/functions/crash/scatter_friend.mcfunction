tag @s add rallous.friend
tellraw @s {"text":"Your friend crashed elsewhere. The warp dropped you far from their crater.","color":"light_purple"}
spreadplayers ~ ~ 800 1800 false @s
execute at @s align xyz positioned ~0.5 ~ ~0.5 run function rallous_old_world:crash/carve_friend_crater
