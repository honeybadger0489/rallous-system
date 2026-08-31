function rallous_warp_crash:build_crater
execute at @s run function rallous_warp_crash:place_relic
execute at @s run function rallous_warp_crash:store_crater
execute at @s run spawnpoint @s ~ ~ ~
execute at @s run function rallous_warp_crash:contact_hook
tag @s add rallous.warp_landed
tag @s add rallous.anchor
scoreboard players set @s rallous.has_crater 1
scoreboard players set @s rallous.civ_bed 0
scoreboard players operation @s rallous.wc_seen = @s rallous.wc_deaths
advancement grant @s only rallous_warp_crash:landed
function rallous_contact:crash/awake
title @s times 10 70 20
title @s title {"text":"Warp-Crash","color":"dark_purple","bold":true}
title @s subtitle {"text":"You fell. The wound still smokes.","color":"gray"}
tellraw @s [{"text":"This crater is your spawn until you sleep in a claimed village.","color":"light_purple"}]
