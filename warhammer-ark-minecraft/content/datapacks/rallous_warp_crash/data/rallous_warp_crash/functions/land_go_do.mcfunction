# Mark landed first so a second land_go in this tick cannot carve or assign again.
tag @s add rallous.warp_landed
scoreboard players set @s rallous.joined 1
function rallous_warp_crash:build_crater
execute at @s run function rallous_warp_crash:place_relic
execute at @s run function rallous_warp_crash:store_crater
execute at @s run spawnpoint @s ~ ~ ~
execute at @s run function rallous_warp_crash:contact_hook
tag @s add rallous.anchor
scoreboard players set @s rallous.has_crater 1
scoreboard players set @s rallous.civ_bed 0
scoreboard players operation @s rallous.wc_seen = @s rallous.wc_deaths
advancement grant @s only rallous_warp_crash:landed
function rallous_contact:crash/awake
title @s times 10 80 20
title @s title {"text":"Cast from the Warp","color":"dark_purple","bold":true}
title @s subtitle {"text":"A host is near. They may take you in — or take your head.","color":"gray"}
tellraw @s [{"text":"You crashed. The crater is yours until you sleep at a claimed camp or after join. Wilderness beds do not stick. Banner-smoke is a host — walk to it. The lord speaks at the picket.","color":"light_purple"}]
