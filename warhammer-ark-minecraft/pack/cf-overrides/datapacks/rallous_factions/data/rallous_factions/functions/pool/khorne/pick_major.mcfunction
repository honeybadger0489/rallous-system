# khorne major pool (3)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 3
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #blooded_wanderers rallous.used matches 1 run function rallous_factions:try/blooded_wanderers
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #challengers_of_khorne rallous.used matches 1 run function rallous_factions:try/challengers_of_khorne
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #exiles_of_khorne rallous.used matches 1 run function rallous_factions:try/exiles_of_khorne
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #challengers_of_khorne rallous.used matches 1 run function rallous_factions:try/challengers_of_khorne
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #exiles_of_khorne rallous.used matches 1 run function rallous_factions:try/exiles_of_khorne
execute if score $done rallous.gen matches 0 unless score #blooded_wanderers rallous.used matches 1 run function rallous_factions:try/blooded_wanderers
