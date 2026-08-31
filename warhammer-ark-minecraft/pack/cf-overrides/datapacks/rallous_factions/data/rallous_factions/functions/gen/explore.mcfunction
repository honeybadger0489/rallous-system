# Player walked off the first ring. Place from the remaining pool.
execute if score #placed rallous.gen >= #xcap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #xcap rallous.const run function rallous_factions:gen/place_far
