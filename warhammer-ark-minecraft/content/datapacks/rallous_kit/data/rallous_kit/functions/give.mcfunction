# Dispatch the tier-1 kit for rallous.race 1–8, then mark kitted.
execute if score @s rallous.race matches 1 run function rallous_kit:give/empire
execute if score @s rallous.race matches 2 run function rallous_kit:give/vampire
execute if score @s rallous.race matches 3 run function rallous_kit:give/lizard
execute if score @s rallous.race matches 4 run function rallous_kit:give/beast
execute if score @s rallous.race matches 5 run function rallous_kit:give/greenskin
execute if score @s rallous.race matches 6 run function rallous_kit:give/dwarf
execute if score @s rallous.race matches 7 run function rallous_kit:give/skaven
execute if score @s rallous.race matches 8 run function rallous_kit:give/khorne
scoreboard players set @s rallous.kitted 1
tellraw @s {"text":"They throw you a levy's kit — leather, iron, and a day's bread. Nothing more.","color":"gold"}
