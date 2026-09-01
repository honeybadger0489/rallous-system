execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 1 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 2 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 3 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 4 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 5 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 6 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 7 run function rallous_factions:pool/khorne/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/khorne/pick
execute if score $done rallous.gen matches 1 run scoreboard players add #next_race rallous.gen 1
execute if score #next_race rallous.gen matches 8.. run scoreboard players set #next_race rallous.gen 0
