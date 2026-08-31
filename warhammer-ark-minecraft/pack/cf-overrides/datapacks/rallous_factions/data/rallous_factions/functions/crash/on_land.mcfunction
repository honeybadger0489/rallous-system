# Warp-crash: living camp from the tables, not a mute villager.
function rallous_factions:gen/boot
execute unless entity @e[tag=rallous.camp,distance=..220,limit=1] run function rallous_factions:gen/place_near
execute unless entity @e[tag=rallous.camp,distance=..260,limit=1] run function rallous_factions:gen/place_one
function rallous_factions:contact/assign
