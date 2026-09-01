# Last chance: land anywhere in a first-hour walk of the crater. Then stop the probe.
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run spreadplayers ~ ~ 28 80 false @s
execute at @s if entity @e[tag=rallous.camp,distance=..28,limit=1] run tp @s ~40 ~ ~-20
execute at @s unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix
function rallous_factions:gen/ring_done
