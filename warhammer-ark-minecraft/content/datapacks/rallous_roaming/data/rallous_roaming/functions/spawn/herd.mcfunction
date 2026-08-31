# Horned Woods herd — no capital. Bray-shaman, gors, ungor, one herd-beast.
scoreboard players set $event rallous.roam 2
function rallous_roaming:spawn/place_marker
execute at @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run function rallous_roaming:spawn/herd_mobs
function rallous_roaming:announce/herd
function rallous_roaming:spawn/finish
