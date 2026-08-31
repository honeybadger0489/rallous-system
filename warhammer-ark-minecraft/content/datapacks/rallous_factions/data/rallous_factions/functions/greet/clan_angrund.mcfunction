tellraw @a[distance=..48] [{"text": "<King of Karak Eight Peaks Belegar Ironhammer — Clan Angrund> ", "color": "gold", "bold": true}, {"text": "Wants his hold back. Help against Skarsnik and Queek or stay out of the underway. You stink of the Warp. Daemon? Prove you are not, or be slain.", "color": "dark_purple"}]
execute if score @s rallous.fac.stance matches 1 run give @p minecraft:iron_axe{display:{Name:'{"text":"Oath Axe","italic":false}'}} 1
execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {"text":"A melee weapon hits the dirt at your feet.","color":"gold"}
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {"text":"Prove yourself: last an hour in their fight or their village. Then the Paths book.","color":"yellow"}
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0
execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {"text":"Daemon-suspicion: they will not name you clean until you prove it.","color":"dark_purple"}
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/clan_angrund
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/clan_angrund
particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16
