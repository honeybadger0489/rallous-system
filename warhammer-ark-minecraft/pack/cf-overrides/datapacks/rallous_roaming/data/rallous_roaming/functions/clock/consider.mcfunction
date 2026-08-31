# As a player who has waited long enough. Natural spawn only if crash-safe and the 25% roll hits.
function rallous_roaming:safety/check
execute if score $safe rallous.roam matches 1 if predicate rallous_roaming:chance_25 run function rallous_roaming:clock/pick
