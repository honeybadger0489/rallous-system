scoreboard players set $done rallous.gen 0
execute if entity @e[tag=rallous.camp,distance=..48,limit=1] run scoreboard players set $done rallous.gen 1
scoreboard players set $pref rallous.gen -1
execute if biome ~ ~ ~ #minecraft:is_jungle run scoreboard players set $pref rallous.gen 3
execute if biome ~ ~ ~ minecraft:mangrove_swamp run scoreboard players set $pref rallous.gen 3
execute if biome ~ ~ ~ minecraft:dark_forest run scoreboard players set $pref rallous.gen 4
execute if biome ~ ~ ~ #minecraft:is_forest run scoreboard players set $pref rallous.gen 4
execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $pref rallous.gen 6
execute if biome ~ ~ ~ minecraft:swamp run scoreboard players set $pref rallous.gen 2
execute if biome ~ ~ ~ #minecraft:is_badlands run scoreboard players set $pref rallous.gen 5
execute if biome ~ ~ ~ #minecraft:is_savanna run scoreboard players set $pref rallous.gen 5
execute if biome ~ ~ ~ minecraft:plains run scoreboard players set $pref rallous.gen 1
execute if biome ~ ~ ~ minecraft:sunflower_plains run scoreboard players set $pref rallous.gen 1
execute if biome ~ ~ ~ minecraft:meadow run scoreboard players set $pref rallous.gen 1
execute if biome ~ ~ ~ minecraft:dripstone_caves run scoreboard players set $pref rallous.gen 7
execute if biome ~ ~ ~ minecraft:lush_caves run scoreboard players set $pref rallous.gen 7
execute if biome ~ ~ ~ minecraft:desert run scoreboard players set $pref rallous.gen 8
execute if biome ~ ~ ~ minecraft:snowy_plains run scoreboard players set $pref rallous.gen 8
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 1 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 2 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 3 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 4 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 5 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 6 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 7 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 8 run function rallous_factions:pool/khorne/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 1 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 2 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 3 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 4 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 5 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 6 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 7 run function rallous_factions:pool/khorne/pick
scoreboard players add #next_race rallous.gen 1
execute if score #next_race rallous.gen matches 8.. run scoreboard players set #next_race rallous.gen 0
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/khorne/pick
