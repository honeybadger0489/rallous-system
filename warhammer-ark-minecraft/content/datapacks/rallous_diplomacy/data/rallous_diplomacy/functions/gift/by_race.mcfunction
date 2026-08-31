# as the helping player. Vanilla only. Race 1–8 from rallous_contact.
execute unless score @s rallous.race matches 1..8 run give @s minecraft:bread 8
execute if score @s rallous.race matches 1 run give @s minecraft:bread 8
execute if score @s rallous.race matches 1 run give @s minecraft:iron_ingot 2
execute if score @s rallous.race matches 2 run give @s minecraft:bone 8
execute if score @s rallous.race matches 2 run give @s minecraft:redstone 4
execute if score @s rallous.race matches 3 run give @s minecraft:tropical_fish 8
execute if score @s rallous.race matches 3 run give @s minecraft:gold_nugget 8
execute if score @s rallous.race matches 4 run give @s minecraft:leather 6
execute if score @s rallous.race matches 4 run give @s minecraft:bone 6
execute if score @s rallous.race matches 5 run give @s minecraft:rotten_flesh 8
execute if score @s rallous.race matches 5 run give @s minecraft:iron_nugget 8
execute if score @s rallous.race matches 6 run give @s minecraft:iron_ingot 4
execute if score @s rallous.race matches 6 run give @s minecraft:coal 8
execute if score @s rallous.race matches 7 run give @s minecraft:gunpowder 4
execute if score @s rallous.race matches 7 run give @s minecraft:string 8
execute if score @s rallous.race matches 8 run give @s minecraft:iron_axe 1
execute if score @s rallous.race matches 8 run give @s minecraft:cooked_beef 4
tellraw @s {"text":"A gift from the camp.","color":"gold"}
