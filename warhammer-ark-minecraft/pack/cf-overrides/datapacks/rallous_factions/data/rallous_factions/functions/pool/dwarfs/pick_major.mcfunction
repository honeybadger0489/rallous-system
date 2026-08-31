# dwarfs major pool (6)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 6
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #clan_angrund rallous.used matches 1 run function rallous_factions:try/clan_angrund
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #ironbrows_expedition rallous.used matches 1 run function rallous_factions:try/ironbrows_expedition
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #karak_kadrin rallous.used matches 1 run function rallous_factions:try/karak_kadrin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #karaz_a_karak rallous.used matches 1 run function rallous_factions:try/karaz_a_karak
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #masters_of_innovation rallous.used matches 1 run function rallous_factions:try/masters_of_innovation
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #the_ancestral_throng rallous.used matches 1 run function rallous_factions:try/the_ancestral_throng
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #ironbrows_expedition rallous.used matches 1 run function rallous_factions:try/ironbrows_expedition
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #karak_kadrin rallous.used matches 1 run function rallous_factions:try/karak_kadrin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #karaz_a_karak rallous.used matches 1 run function rallous_factions:try/karaz_a_karak
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #masters_of_innovation rallous.used matches 1 run function rallous_factions:try/masters_of_innovation
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #the_ancestral_throng rallous.used matches 1 run function rallous_factions:try/the_ancestral_throng
execute if score $done rallous.gen matches 0 unless score #clan_angrund rallous.used matches 1 run function rallous_factions:try/clan_angrund
