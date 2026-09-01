# Chunk is loaded. Hunt land. If ocean, fall inward. Do not skip the race.
execute if score #placed rallous.gen >= #cap rallous.const run function rallous_factions:gen/ring_done
execute if score #placed rallous.gen < #cap rallous.const run function rallous_factions:gen/ring_try_go
