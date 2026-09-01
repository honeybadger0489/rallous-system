# Race 1 — Empire plate. SoTE 1.1.9 State Trooper (confirmed in jar + recruits.toml).
give @s sonsoftheempire:swordsman_armor_helmet 1
give @s sonsoftheempire:swordsman_armor_chestplate 1
give @s sonsoftheempire:swordsman_armor_leggings 1
give @s sonsoftheempire:swordsman_armor_boots 1
give @s sonsoftheempire:altdorfbanner 1
execute unless data entity @s Inventory[{id:"sonsoftheempire:swordsman_armor_helmet"}] run give @s minecraft:iron_helmet 1
execute unless data entity @s Inventory[{id:"sonsoftheempire:swordsman_armor_chestplate"}] run give @s minecraft:iron_chestplate 1
execute unless data entity @s Inventory[{id:"sonsoftheempire:swordsman_armor_leggings"}] run give @s minecraft:iron_leggings 1
execute unless data entity @s Inventory[{id:"sonsoftheempire:swordsman_armor_boots"}] run give @s minecraft:iron_boots 1
execute unless data entity @s Inventory[{id:"sonsoftheempire:altdorfbanner"}] run give @s minecraft:yellow_banner 1
give @s minecraft:iron_sword 1
give @s minecraft:shield 1
give @s minecraft:bread 8
