# FORCE: roll one of the three event IDs. Still skips play-time / crater gates.
# /function rallous_roaming:events/random
function rallous_roaming:clear
execute as @p at @s run function rallous_roaming:clock/pick
