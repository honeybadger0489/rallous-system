# First-hour verbs at the picket. Lead-in is race-skeptical. Four paths stay reachable.
give @s minecraft:flint_and_steel{display:{Name:'{"text":"Burn their welcome","italic":false}',Lore:['{"text":"Use this at the picket. Khorne hears.","color":"dark_red"}']}} 1
give @s minecraft:bread{display:{Name:'{"text":"Share food","italic":false}'}} 4
execute if score @s rallous.race matches 1 run function rallous_factions:path/offer_empire
execute if score @s rallous.race matches 2 run function rallous_factions:path/offer_vampire_counts
execute if score @s rallous.race matches 3 run function rallous_factions:path/offer_lizardmen
execute if score @s rallous.race matches 4 run function rallous_factions:path/offer_beastmen
execute if score @s rallous.race matches 5 run function rallous_factions:path/offer_greenskins
execute if score @s rallous.race matches 6 run function rallous_factions:path/offer_dwarfs
execute if score @s rallous.race matches 7 run function rallous_factions:path/offer_skaven
execute if score @s rallous.race matches 8 run function rallous_factions:path/offer_khorne
execute unless score @s rallous.race matches 1..8 run function rallous_factions:path/offer_empire
