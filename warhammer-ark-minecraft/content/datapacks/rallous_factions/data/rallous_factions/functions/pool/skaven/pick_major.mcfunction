# skaven major pool (6)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 6
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #clan_eshin rallous.used matches 1 run function rallous_factions:try/clan_eshin
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #clan_mors rallous.used matches 1 run function rallous_factions:try/clan_mors
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #clan_moulder rallous.used matches 1 run function rallous_factions:try/clan_moulder
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #clan_pestilens rallous.used matches 1 run function rallous_factions:try/clan_pestilens
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #clan_rictus rallous.used matches 1 run function rallous_factions:try/clan_rictus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #clan_skryre rallous.used matches 1 run function rallous_factions:try/clan_skryre
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #clan_mors rallous.used matches 1 run function rallous_factions:try/clan_mors
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #clan_moulder rallous.used matches 1 run function rallous_factions:try/clan_moulder
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #clan_pestilens rallous.used matches 1 run function rallous_factions:try/clan_pestilens
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #clan_rictus rallous.used matches 1 run function rallous_factions:try/clan_rictus
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #clan_skryre rallous.used matches 1 run function rallous_factions:try/clan_skryre
execute if score $done rallous.gen matches 0 unless score #clan_eshin rallous.used matches 1 run function rallous_factions:try/clan_eshin
