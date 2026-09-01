scoreboard players operation @s rallous.path_seen = @s rallous.path
execute if score @s rallous.path matches 1 run function rallous_factions:path/help
execute if score @s rallous.path matches 2 run function rallous_factions:path/betray
execute if score @s rallous.path matches 3 run function rallous_factions:path/join
execute if score @s rallous.path matches 4 run function rallous_factions:path/leave
