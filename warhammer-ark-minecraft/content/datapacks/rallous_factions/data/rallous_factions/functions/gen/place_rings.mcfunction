# Mixed-race pickets on walkable rings. Not TW cities. Cap still 16.
# Inner ~96 (10 min walk). Outer ~220 (first hour). Cardinals only.
execute if score #placed rallous.gen < #cap rallous.const positioned ~96 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~-96 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~96 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~-96 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~220 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~-220 ~ ~ run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~220 run function rallous_factions:gen/ring_spot
execute if score #placed rallous.gen < #cap rallous.const positioned ~ ~ ~-220 run function rallous_factions:gen/ring_spot
