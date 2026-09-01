# vampire_counts major pool (5)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 5
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #caravan_of_blue_roses rallous.used matches 1 run function rallous_factions:try/caravan_of_blue_roses
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #sylvania rallous.used matches 1 run function rallous_factions:try/sylvania
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #the_barrow_legion rallous.used matches 1 run function rallous_factions:try/the_barrow_legion
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #the_drakenhof_conclave rallous.used matches 1 run function rallous_factions:try/the_drakenhof_conclave
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #vampire_counts rallous.used matches 1 run function rallous_factions:try/vampire_counts
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #sylvania rallous.used matches 1 run function rallous_factions:try/sylvania
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #the_barrow_legion rallous.used matches 1 run function rallous_factions:try/the_barrow_legion
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #the_drakenhof_conclave rallous.used matches 1 run function rallous_factions:try/the_drakenhof_conclave
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #vampire_counts rallous.used matches 1 run function rallous_factions:try/vampire_counts
execute if score $done rallous.gen matches 0 unless score #caravan_of_blue_roses rallous.used matches 1 run function rallous_factions:try/caravan_of_blue_roses
