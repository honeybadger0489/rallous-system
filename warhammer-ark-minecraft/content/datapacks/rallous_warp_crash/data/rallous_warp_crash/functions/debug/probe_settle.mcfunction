execute if score @s rallous.retry matches 8.. run function rallous_warp_crash:debug/probe_carve
execute unless score @s rallous.retry matches 8.. if entity @e[type=minecraft:marker,tag=rallous.slot_probe_crater,distance=..900] run function rallous_warp_crash:debug/probe_bump
execute unless score @s rallous.retry matches 8.. unless entity @e[type=minecraft:marker,tag=rallous.slot_probe_crater,distance=..900] run function rallous_warp_crash:debug/probe_carve
