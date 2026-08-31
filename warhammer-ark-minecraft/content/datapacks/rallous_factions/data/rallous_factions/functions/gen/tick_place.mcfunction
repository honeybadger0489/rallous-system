# One more camp around the first crater / a landed player.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const as @a[tag=rallous.warp_landed,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_far
