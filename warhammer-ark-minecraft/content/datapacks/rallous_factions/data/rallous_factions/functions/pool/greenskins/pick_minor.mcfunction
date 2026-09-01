# greenskins minor pool (27)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 27
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #arachnos rallous.used matches 1 run function rallous_factions:try/arachnos
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #black_venom rallous.used matches 1 run function rallous_factions:try/black_venom
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #bloody_spearz rallous.used matches 1 run function rallous_factions:try/bloody_spearz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #blue_vipers rallous.used matches 1 run function rallous_factions:try/blue_vipers
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #broken_chainz rallous.used matches 1 run function rallous_factions:try/broken_chainz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #broken_nose rallous.used matches 1 run function rallous_factions:try/broken_nose
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #cluster_eye_tribe rallous.used matches 1 run function rallous_factions:try/cluster_eye_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..7 unless score #creeping_death rallous.used matches 1 run function rallous_factions:try/creeping_death
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..8 unless score #crooked_moon_mutinous_gits rallous.used matches 1 run function rallous_factions:try/crooked_moon_mutinous_gits
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..9 unless score #da_cage_breakaz rallous.used matches 1 run function rallous_factions:try/da_cage_breakaz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..10 unless score #dark_land_orcs rallous.used matches 1 run function rallous_factions:try/dark_land_orcs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..11 unless score #dimmed_sunz rallous.used matches 1 run function rallous_factions:try/dimmed_sunz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..12 unless score #drippin_fangs rallous.used matches 1 run function rallous_factions:try/drippin_fangs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..13 unless score #leaf_cutterz_tribe rallous.used matches 1 run function rallous_factions:try/leaf_cutterz_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..14 unless score #moon_howlerz rallous.used matches 1 run function rallous_factions:try/moon_howlerz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..15 unless score #red_cloud rallous.used matches 1 run function rallous_factions:try/red_cloud
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..16 unless score #red_eye rallous.used matches 1 run function rallous_factions:try/red_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..17 unless score #red_fangs rallous.used matches 1 run function rallous_factions:try/red_fangs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..18 unless score #scabby_eye rallous.used matches 1 run function rallous_factions:try/scabby_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..19 unless score #skull_crag rallous.used matches 1 run function rallous_factions:try/skull_crag
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..20 unless score #skull_takerz rallous.used matches 1 run function rallous_factions:try/skull_takerz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..21 unless score #skullsmasherz rallous.used matches 1 run function rallous_factions:try/skullsmasherz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..22 unless score #slaves_of_zharr rallous.used matches 1 run function rallous_factions:try/slaves_of_zharr
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..23 unless score #teef_snatchaz rallous.used matches 1 run function rallous_factions:try/teef_snatchaz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..24 unless score #the_black_pit_tribe rallous.used matches 1 run function rallous_factions:try/the_black_pit_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..25 unless score #top_knotz rallous.used matches 1 run function rallous_factions:try/top_knotz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..26 unless score #tusked_sunz rallous.used matches 1 run function rallous_factions:try/tusked_sunz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #black_venom rallous.used matches 1 run function rallous_factions:try/black_venom
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #bloody_spearz rallous.used matches 1 run function rallous_factions:try/bloody_spearz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #blue_vipers rallous.used matches 1 run function rallous_factions:try/blue_vipers
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #broken_chainz rallous.used matches 1 run function rallous_factions:try/broken_chainz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #broken_nose rallous.used matches 1 run function rallous_factions:try/broken_nose
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #cluster_eye_tribe rallous.used matches 1 run function rallous_factions:try/cluster_eye_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 7.. unless score #creeping_death rallous.used matches 1 run function rallous_factions:try/creeping_death
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 8.. unless score #crooked_moon_mutinous_gits rallous.used matches 1 run function rallous_factions:try/crooked_moon_mutinous_gits
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 9.. unless score #da_cage_breakaz rallous.used matches 1 run function rallous_factions:try/da_cage_breakaz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 10.. unless score #dark_land_orcs rallous.used matches 1 run function rallous_factions:try/dark_land_orcs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 11.. unless score #dimmed_sunz rallous.used matches 1 run function rallous_factions:try/dimmed_sunz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 12.. unless score #drippin_fangs rallous.used matches 1 run function rallous_factions:try/drippin_fangs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 13.. unless score #leaf_cutterz_tribe rallous.used matches 1 run function rallous_factions:try/leaf_cutterz_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 14.. unless score #moon_howlerz rallous.used matches 1 run function rallous_factions:try/moon_howlerz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 15.. unless score #red_cloud rallous.used matches 1 run function rallous_factions:try/red_cloud
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 16.. unless score #red_eye rallous.used matches 1 run function rallous_factions:try/red_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 17.. unless score #red_fangs rallous.used matches 1 run function rallous_factions:try/red_fangs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 18.. unless score #scabby_eye rallous.used matches 1 run function rallous_factions:try/scabby_eye
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 19.. unless score #skull_crag rallous.used matches 1 run function rallous_factions:try/skull_crag
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 20.. unless score #skull_takerz rallous.used matches 1 run function rallous_factions:try/skull_takerz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 21.. unless score #skullsmasherz rallous.used matches 1 run function rallous_factions:try/skullsmasherz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 22.. unless score #slaves_of_zharr rallous.used matches 1 run function rallous_factions:try/slaves_of_zharr
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 23.. unless score #teef_snatchaz rallous.used matches 1 run function rallous_factions:try/teef_snatchaz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 24.. unless score #the_black_pit_tribe rallous.used matches 1 run function rallous_factions:try/the_black_pit_tribe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 25.. unless score #top_knotz rallous.used matches 1 run function rallous_factions:try/top_knotz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 26.. unless score #tusked_sunz rallous.used matches 1 run function rallous_factions:try/tusked_sunz
execute if score $done rallous.gen matches 0 unless score #arachnos rallous.used matches 1 run function rallous_factions:try/arachnos
