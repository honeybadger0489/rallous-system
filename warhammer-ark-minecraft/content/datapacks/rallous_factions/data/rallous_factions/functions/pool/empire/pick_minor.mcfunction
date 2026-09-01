# empire minor pool (9)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 9
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #averland rallous.used matches 1 run function rallous_factions:try/averland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #hochland rallous.used matches 1 run function rallous_factions:try/hochland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #marienburg rallous.used matches 1 run function rallous_factions:try/marienburg
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #middenland rallous.used matches 1 run function rallous_factions:try/middenland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #nordland rallous.used matches 1 run function rallous_factions:try/nordland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #ostermark rallous.used matches 1 run function rallous_factions:try/ostermark
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #ostland rallous.used matches 1 run function rallous_factions:try/ostland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #stirland rallous.used matches 1 run function rallous_factions:try/stirland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..8 unless score #talabecland rallous.used matches 1 run function rallous_factions:try/talabecland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #hochland rallous.used matches 1 run function rallous_factions:try/hochland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #marienburg rallous.used matches 1 run function rallous_factions:try/marienburg
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #middenland rallous.used matches 1 run function rallous_factions:try/middenland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #nordland rallous.used matches 1 run function rallous_factions:try/nordland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #ostermark rallous.used matches 1 run function rallous_factions:try/ostermark
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #ostland rallous.used matches 1 run function rallous_factions:try/ostland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #stirland rallous.used matches 1 run function rallous_factions:try/stirland
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 8.. unless score #talabecland rallous.used matches 1 run function rallous_factions:try/talabecland
execute if score $done rallous.gen matches 0 unless score #averland rallous.used matches 1 run function rallous_factions:try/averland
