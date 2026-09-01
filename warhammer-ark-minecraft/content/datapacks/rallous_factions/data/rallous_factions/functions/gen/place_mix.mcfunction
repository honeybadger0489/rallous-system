# Ring mix: rotate the eight races. Skip biome prefer so dark woods are not four Beastmen.
# Nearby camp is a block, not a success — caller nudges. Increment rotation only when a camp lands.
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix_go
scoreboard players set $mix_only rallous.gen 0
