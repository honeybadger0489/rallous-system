tellraw @a[distance=..48] [{"text": "<The Red Duke The Red Duke — Caravan of Blue Roses> ", "color": "dark_red", "bold": true}, {"text": "Blood Dragon errant. Recruit if you ride to war; he does not keep a peasant court. Prove yourself. Until then you are a Warp-stranger, not a guest.", "color": "yellow"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_sword{display:{Name:'{"text":"Night Blade","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/caravan_of_blue_roses
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/caravan_of_blue_roses
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
