scoreboard players add @s rallous.tries 1
execute if entity @s[tag=rallous.probe.inner] run spreadplayers ~ ~ 80 140 false @s
execute if entity @s[tag=rallous.probe.outer] run spreadplayers ~ ~ 150 230 false @s
function rallous_factions:gen/ring_far
execute if score $far rallous.gen matches 0 run scoreboard players set $wet rallous.gen 1
execute if score $far rallous.gen matches 1 run function rallous_factions:gen/ring_wet
execute if score $wet rallous.gen matches 1 if entity @s[tag=rallous.probe.outer] run spreadplayers ~ ~ 80 140 false @s
function rallous_factions:gen/ring_far
execute if score $far rallous.gen matches 0 if entity @s[tag=rallous.probe.outer] run function rallous_factions:gen/ring_inward
function rallous_factions:gen/ring_wet
execute if score $wet rallous.gen matches 1 run function rallous_factions:gen/ring_inward
execute at @s if entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/ring_nudge
scoreboard players set $done rallous.gen 0
function rallous_factions:gen/ring_wet
function rallous_factions:gen/ring_far
execute if score $wet rallous.gen matches 0 if score $far rallous.gen matches 1 at @s unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix
execute if score $done rallous.gen matches 1 run function rallous_factions:gen/ring_done
execute if score $done rallous.gen matches 0 if score @s rallous.tries matches 6.. run function rallous_factions:gen/ring_last
