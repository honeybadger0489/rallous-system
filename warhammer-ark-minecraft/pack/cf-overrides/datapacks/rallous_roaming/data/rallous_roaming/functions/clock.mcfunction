# Natural roam ticker. Re-arms itself every 60s (1200 ticks).
# Does nothing if a host is already marching.
schedule function rallous_roaming:clock 1200t replace
function rallous_roaming:safety/ensure_origin
execute unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_roaming:clock/idle
