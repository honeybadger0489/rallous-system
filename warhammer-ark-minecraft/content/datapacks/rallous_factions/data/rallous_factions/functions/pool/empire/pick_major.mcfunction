# empire major pool (5)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 5
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #cult_of_sigmar rallous.used matches 1 run function rallous_factions:try/cult_of_sigmar
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #reikland rallous.used matches 1 run function rallous_factions:try/reikland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #the_golden_order rallous.used matches 1 run function rallous_factions:try/the_golden_order
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #the_huntsmarshals_expedition rallous.used matches 1 run function rallous_factions:try/the_huntsmarshals_expedition
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #wissenland_and_nuln rallous.used matches 1 run function rallous_factions:try/wissenland_and_nuln
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #reikland rallous.used matches 1 run function rallous_factions:try/reikland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #the_golden_order rallous.used matches 1 run function rallous_factions:try/the_golden_order
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #the_huntsmarshals_expedition rallous.used matches 1 run function rallous_factions:try/the_huntsmarshals_expedition
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #wissenland_and_nuln rallous.used matches 1 run function rallous_factions:try/wissenland_and_nuln
execute if score $done rallous.gen matches 0 unless score #cult_of_sigmar rallous.used matches 1 run function rallous_factions:try/cult_of_sigmar
