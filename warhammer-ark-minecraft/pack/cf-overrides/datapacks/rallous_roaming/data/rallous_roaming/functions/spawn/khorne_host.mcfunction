# Blood Host — no capital. Skull-tithe wither skeletons, bloodreavers, red banners.
scoreboard players set $event rallous.roam 3
function rallous_roaming:spawn/place_marker
execute at @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run function rallous_roaming:spawn/khorne_mobs
execute at @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run function rallous_roaming:spawn/recruits_column
function rallous_roaming:announce/khorne_host
function rallous_roaming:spawn/finish
