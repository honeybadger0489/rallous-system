# greenskins major pool (6)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 6
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #bonerattlaz rallous.used matches 1 run function rallous_factions:try/bonerattlaz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #broken_axe rallous.used matches 1 run function rallous_factions:try/broken_axe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #crooked_moon rallous.used matches 1 run function rallous_factions:try/crooked_moon
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #grimgors_ardboyz rallous.used matches 1 run function rallous_factions:try/grimgors_ardboyz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #ironclaw_orcs rallous.used matches 1 run function rallous_factions:try/ironclaw_orcs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #the_bloody_handz rallous.used matches 1 run function rallous_factions:try/the_bloody_handz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #broken_axe rallous.used matches 1 run function rallous_factions:try/broken_axe
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #crooked_moon rallous.used matches 1 run function rallous_factions:try/crooked_moon
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #grimgors_ardboyz rallous.used matches 1 run function rallous_factions:try/grimgors_ardboyz
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #ironclaw_orcs rallous.used matches 1 run function rallous_factions:try/ironclaw_orcs
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #the_bloody_handz rallous.used matches 1 run function rallous_factions:try/the_bloody_handz
execute if score $done rallous.gen matches 0 unless score #bonerattlaz rallous.used matches 1 run function rallous_factions:try/bonerattlaz
