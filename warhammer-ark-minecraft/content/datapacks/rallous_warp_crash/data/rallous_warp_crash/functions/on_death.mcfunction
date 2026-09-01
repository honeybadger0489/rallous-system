# Same person. Never scatter a new crater. 1.20.1 — no /return.
scoreboard players operation @s rallous.wc_seen = @s rallous.wc_deaths
execute unless score @s rallous.civ_bed matches 1.. run function rallous_warp_crash:goto_crater
execute unless score @s rallous.civ_bed matches 1.. run function rallous_warp_crash:keep_crater_spawn
tellraw @s {"text":"No village bed. The Warp hauled you back to the crater.","color":"dark_purple"}
