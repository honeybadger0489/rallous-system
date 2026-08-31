# lizardmen major pool (7)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 7
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #cult_of_sotek rallous.used matches 1 run function rallous_factions:try/cult_of_sotek
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #ghosts_of_pahuax rallous.used matches 1 run function rallous_factions:try/ghosts_of_pahuax
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #hexoatl rallous.used matches 1 run function rallous_factions:try/hexoatl
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #itza rallous.used matches 1 run function rallous_factions:try/itza
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #last_defenders rallous.used matches 1 run function rallous_factions:try/last_defenders
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #spirit_of_the_jungle rallous.used matches 1 run function rallous_factions:try/spirit_of_the_jungle
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #tlaqua rallous.used matches 1 run function rallous_factions:try/tlaqua
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #ghosts_of_pahuax rallous.used matches 1 run function rallous_factions:try/ghosts_of_pahuax
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #hexoatl rallous.used matches 1 run function rallous_factions:try/hexoatl
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #itza rallous.used matches 1 run function rallous_factions:try/itza
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #last_defenders rallous.used matches 1 run function rallous_factions:try/last_defenders
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #spirit_of_the_jungle rallous.used matches 1 run function rallous_factions:try/spirit_of_the_jungle
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #tlaqua rallous.used matches 1 run function rallous_factions:try/tlaqua
execute if score $done rallous.gen matches 0 unless score #cult_of_sotek rallous.used matches 1 run function rallous_factions:try/cult_of_sotek
