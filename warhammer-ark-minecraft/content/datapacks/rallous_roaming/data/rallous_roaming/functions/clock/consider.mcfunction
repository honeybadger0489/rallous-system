# As a player who has waited long enough.
# First natural host after the 20–40 min wait is guaranteed. Later rolls stay 25%.
function rallous_roaming:safety/check
execute if score $safe rallous.roam matches 1 unless score $fired rallous.roam matches 1.. run function rallous_roaming:clock/pick
execute if score $safe rallous.roam matches 1 if score $fired rallous.roam matches 1.. if predicate rallous_roaming:chance_25 run function rallous_roaming:clock/pick
