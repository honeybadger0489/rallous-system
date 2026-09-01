tag @s add rallous.roam
tag @s add rallous.roam.host
execute if score $event rallous.roam matches 1 run tag @s add rallous.roam.waaagh
execute if score $event rallous.roam matches 2 run tag @s add rallous.roam.herd
execute if score $event rallous.roam matches 3 run tag @s add rallous.roam.khorne
data modify entity @s PersistenceRequired set value 1b
data modify entity @s CustomNameVisible set value 1b
execute if score $event rallous.roam matches 1 run data modify entity @s CustomName set value '{"text":"Waaagh Boy","color":"green"}'
execute if score $event rallous.roam matches 2 run data modify entity @s CustomName set value '{"text":"Gor","color":"#8B5A2B"}'
execute if score $event rallous.roam matches 3 run data modify entity @s CustomName set value '{"text":"Bloodreaver","color":"dark_red"}'
