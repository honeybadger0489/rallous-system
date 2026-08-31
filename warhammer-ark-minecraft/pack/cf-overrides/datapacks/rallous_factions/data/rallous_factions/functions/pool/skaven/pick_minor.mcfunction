# skaven minor pool (13)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 13
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #clan_carrion rallous.used matches 1 run function rallous_factions:try/clan_carrion
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #clan_gnaw rallous.used matches 1 run function rallous_factions:try/clan_gnaw
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #clan_gritus rallous.used matches 1 run function rallous_factions:try/clan_gritus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #clan_kreepus rallous.used matches 1 run function rallous_factions:try/clan_kreepus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #clan_krizzor rallous.used matches 1 run function rallous_factions:try/clan_krizzor
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #clan_mange rallous.used matches 1 run function rallous_factions:try/clan_mange
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #clan_morbidus rallous.used matches 1 run function rallous_factions:try/clan_morbidus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #clan_mordkin rallous.used matches 1 run function rallous_factions:try/clan_mordkin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..8 unless score #clan_septik rallous.used matches 1 run function rallous_factions:try/clan_septik
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..9 unless score #clan_skrat rallous.used matches 1 run function rallous_factions:try/clan_skrat
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..10 unless score #clan_spittel rallous.used matches 1 run function rallous_factions:try/clan_spittel
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..11 unless score #clan_treecherik rallous.used matches 1 run function rallous_factions:try/clan_treecherik
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..12 unless score #clan_verms rallous.used matches 1 run function rallous_factions:try/clan_verms
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #clan_gnaw rallous.used matches 1 run function rallous_factions:try/clan_gnaw
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #clan_gritus rallous.used matches 1 run function rallous_factions:try/clan_gritus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #clan_kreepus rallous.used matches 1 run function rallous_factions:try/clan_kreepus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #clan_krizzor rallous.used matches 1 run function rallous_factions:try/clan_krizzor
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #clan_mange rallous.used matches 1 run function rallous_factions:try/clan_mange
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #clan_morbidus rallous.used matches 1 run function rallous_factions:try/clan_morbidus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #clan_mordkin rallous.used matches 1 run function rallous_factions:try/clan_mordkin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 8.. unless score #clan_septik rallous.used matches 1 run function rallous_factions:try/clan_septik
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 9.. unless score #clan_skrat rallous.used matches 1 run function rallous_factions:try/clan_skrat
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 10.. unless score #clan_spittel rallous.used matches 1 run function rallous_factions:try/clan_spittel
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 11.. unless score #clan_treecherik rallous.used matches 1 run function rallous_factions:try/clan_treecherik
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 12.. unless score #clan_verms rallous.used matches 1 run function rallous_factions:try/clan_verms
execute if score $done rallous.gen matches 0 unless score #clan_carrion rallous.used matches 1 run function rallous_factions:try/clan_carrion
