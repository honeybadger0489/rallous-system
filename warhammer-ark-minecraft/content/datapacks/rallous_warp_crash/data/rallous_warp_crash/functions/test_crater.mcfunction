# /function rallous_warp_crash:test_crater — bowl + relic + store here (no scatter).
execute unless score @s rallous.pid matches 1.. run function rallous_warp_crash:assign_ids
function rallous_warp_crash:build_crater
execute at @s run function rallous_warp_crash:place_relic
execute at @s run function rallous_warp_crash:store_crater
execute at @s run spawnpoint @s ~ ~ ~
tag @s add rallous.warp_landed
scoreboard players set @s rallous.has_crater 1
scoreboard players operation @s rallous.wc_seen = @s rallous.wc_deaths
tellraw @s [{"text":"test_crater: wound cut at your feet.","color":"dark_purple"}]
