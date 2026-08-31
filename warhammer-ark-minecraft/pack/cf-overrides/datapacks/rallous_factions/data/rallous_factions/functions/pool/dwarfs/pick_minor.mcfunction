# dwarfs minor pool (10)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 10
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #barak_varr rallous.used matches 1 run function rallous_factions:try/barak_varr
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #clan_helhein rallous.used matches 1 run function rallous_factions:try/clan_helhein
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #greybeards_prospectors rallous.used matches 1 run function rallous_factions:try/greybeards_prospectors
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #karak_azorn rallous.used matches 1 run function rallous_factions:try/karak_azorn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #karak_azul rallous.used matches 1 run function rallous_factions:try/karak_azul
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #karak_hirn rallous.used matches 1 run function rallous_factions:try/karak_hirn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #karak_norn rallous.used matches 1 run function rallous_factions:try/karak_norn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #karak_ziflin rallous.used matches 1 run function rallous_factions:try/karak_ziflin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..8 unless score #spine_of_sotek_dwarfs rallous.used matches 1 run function rallous_factions:try/spine_of_sotek_dwarfs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..9 unless score #zhufbar rallous.used matches 1 run function rallous_factions:try/zhufbar
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #clan_helhein rallous.used matches 1 run function rallous_factions:try/clan_helhein
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #greybeards_prospectors rallous.used matches 1 run function rallous_factions:try/greybeards_prospectors
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #karak_azorn rallous.used matches 1 run function rallous_factions:try/karak_azorn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #karak_azul rallous.used matches 1 run function rallous_factions:try/karak_azul
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #karak_hirn rallous.used matches 1 run function rallous_factions:try/karak_hirn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #karak_norn rallous.used matches 1 run function rallous_factions:try/karak_norn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #karak_ziflin rallous.used matches 1 run function rallous_factions:try/karak_ziflin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 8.. unless score #spine_of_sotek_dwarfs rallous.used matches 1 run function rallous_factions:try/spine_of_sotek_dwarfs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 9.. unless score #zhufbar rallous.used matches 1 run function rallous_factions:try/zhufbar
execute if score $done rallous.gen matches 0 unless score #barak_varr rallous.used matches 1 run function rallous_factions:try/barak_varr
