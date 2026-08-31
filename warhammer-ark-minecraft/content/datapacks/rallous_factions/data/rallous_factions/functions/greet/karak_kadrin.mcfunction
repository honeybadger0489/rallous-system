tellraw @a[distance=..48] [{"text": "<Slayer King Ungrim Ironfist — Karak Kadrin> ", "color": "gold", "bold": true}, {"text": "Wants a worthy doom. Recruit if you hunt the same monster. You stink of the Warp. Daemon? Prove you are not, or be slain.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Oath Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/karak_kadrin
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/karak_kadrin
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
