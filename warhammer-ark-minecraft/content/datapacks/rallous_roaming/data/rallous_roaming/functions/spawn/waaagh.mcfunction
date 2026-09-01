# Greenhost Waaagh — no capital. Pillagers / choppas / gobbos with lime skull banners.
scoreboard players set $event rallous.roam 1
function rallous_roaming:spawn/place_marker
execute at @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run function rallous_roaming:spawn/waaagh_mobs
execute at @e[type=minecraft:marker,tag=rallous.roam.spawner,limit=1] run function rallous_roaming:spawn/recruits_column
function rallous_roaming:announce/waaagh
function rallous_roaming:spawn/finish
