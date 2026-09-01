# beastmen minor pool (8)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 8
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #blooded_axe_tribe rallous.used matches 1 run function rallous_factions:try/blooded_axe_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #jagged_horn_tribe rallous.used matches 1 run function rallous_factions:try/jagged_horn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #manblight_tribe rallous.used matches 1 run function rallous_factions:try/manblight_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #redhorn_tribe rallous.used matches 1 run function rallous_factions:try/redhorn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #ripper_horn_tribe rallous.used matches 1 run function rallous_factions:try/ripper_horn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #shadowgor_warherd rallous.used matches 1 run function rallous_factions:try/shadowgor_warherd
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #skrinderkin_warherd rallous.used matches 1 run function rallous_factions:try/skrinderkin_warherd
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #stone_horn_tribe rallous.used matches 1 run function rallous_factions:try/stone_horn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #jagged_horn_tribe rallous.used matches 1 run function rallous_factions:try/jagged_horn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #manblight_tribe rallous.used matches 1 run function rallous_factions:try/manblight_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #redhorn_tribe rallous.used matches 1 run function rallous_factions:try/redhorn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #ripper_horn_tribe rallous.used matches 1 run function rallous_factions:try/ripper_horn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #shadowgor_warherd rallous.used matches 1 run function rallous_factions:try/shadowgor_warherd
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #skrinderkin_warherd rallous.used matches 1 run function rallous_factions:try/skrinderkin_warherd
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #stone_horn_tribe rallous.used matches 1 run function rallous_factions:try/stone_horn_tribe
execute if score $done rallous.gen matches 0 unless score #blooded_axe_tribe rallous.used matches 1 run function rallous_factions:try/blooded_axe_tribe
