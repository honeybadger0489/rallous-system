# vampire_counts minor pool (9)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 9
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #jiangshi_rebels rallous.used matches 1 run function rallous_factions:try/jiangshi_rebels
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #lahmian_sisterhood rallous.used matches 1 run function rallous_factions:try/lahmian_sisterhood
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #mousillon rallous.used matches 1 run function rallous_factions:try/mousillon
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #necrarch_brotherhood rallous.used matches 1 run function rallous_factions:try/necrarch_brotherhood
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #sires_of_mourkain rallous.used matches 1 run function rallous_factions:try/sires_of_mourkain
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #strygos_empire rallous.used matches 1 run function rallous_factions:try/strygos_empire
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #templehof rallous.used matches 1 run function rallous_factions:try/templehof
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #the_court_of_night rallous.used matches 1 run function rallous_factions:try/the_court_of_night
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..8 unless score #the_silver_host rallous.used matches 1 run function rallous_factions:try/the_silver_host
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #lahmian_sisterhood rallous.used matches 1 run function rallous_factions:try/lahmian_sisterhood
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #mousillon rallous.used matches 1 run function rallous_factions:try/mousillon
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #necrarch_brotherhood rallous.used matches 1 run function rallous_factions:try/necrarch_brotherhood
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #sires_of_mourkain rallous.used matches 1 run function rallous_factions:try/sires_of_mourkain
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #strygos_empire rallous.used matches 1 run function rallous_factions:try/strygos_empire
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #templehof rallous.used matches 1 run function rallous_factions:try/templehof
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #the_court_of_night rallous.used matches 1 run function rallous_factions:try/the_court_of_night
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 8.. unless score #the_silver_host rallous.used matches 1 run function rallous_factions:try/the_silver_host
execute if score $done rallous.gen matches 0 unless score #jiangshi_rebels rallous.used matches 1 run function rallous_factions:try/jiangshi_rebels
