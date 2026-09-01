# Legacy single-spot entry. Queue one pending probe at this offset, then try if loaded.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const run function rallous_factions:gen/ring_queue_here
