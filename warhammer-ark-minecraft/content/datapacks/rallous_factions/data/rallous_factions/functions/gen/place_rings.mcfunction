# Mixed-race pickets on walkable rings. Not TW cities. Cap still 16.
# Inner ~120 (clears the contact camp). Outer ~220 (first hour). Cardinals only.
execute if score #placed rallous.gen < #cap rallous.const positioned ~120 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~-120 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~120 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~-120 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~220 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~-220 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~220 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~-220 run function rallous_factions:gen/ring_spot
