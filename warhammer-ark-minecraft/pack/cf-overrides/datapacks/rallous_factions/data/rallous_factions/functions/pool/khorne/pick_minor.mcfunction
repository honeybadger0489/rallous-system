# khorne minor pool (4)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 4
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #bloody_sword rallous.used matches 1 run function rallous_factions:try/bloody_sword
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #brazen_throne rallous.used matches 1 run function rallous_factions:try/brazen_throne
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #crimson_skull rallous.used matches 1 run function rallous_factions:try/crimson_skull
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #kharneths_sons rallous.used matches 1 run function rallous_factions:try/kharneths_sons
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #brazen_throne rallous.used matches 1 run function rallous_factions:try/brazen_throne
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #crimson_skull rallous.used matches 1 run function rallous_factions:try/crimson_skull
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #kharneths_sons rallous.used matches 1 run function rallous_factions:try/kharneths_sons
execute if score $done rallous.gen matches 0 unless score #bloody_sword rallous.used matches 1 run function rallous_factions:try/bloody_sword
