# beastmen major pool (4)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 4
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #harbinger_of_disaster rallous.used matches 1 run function rallous_factions:try/harbinger_of_disaster
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #slaughterhorn_tribe rallous.used matches 1 run function rallous_factions:try/slaughterhorn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #warherd_of_the_one_eye rallous.used matches 1 run function rallous_factions:try/warherd_of_the_one_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #warherd_of_the_shadowgave rallous.used matches 1 run function rallous_factions:try/warherd_of_the_shadowgave
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #slaughterhorn_tribe rallous.used matches 1 run function rallous_factions:try/slaughterhorn_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #warherd_of_the_one_eye rallous.used matches 1 run function rallous_factions:try/warherd_of_the_one_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #warherd_of_the_shadowgave rallous.used matches 1 run function rallous_factions:try/warherd_of_the_shadowgave
execute if score $done rallous.gen matches 0 unless score #harbinger_of_disaster rallous.used matches 1 run function rallous_factions:try/harbinger_of_disaster
