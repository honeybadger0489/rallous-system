# Advancement reward. Claimed village only — wilderness beds do not stick.
execute if entity @e[type=minecraft:villager,distance=..64,limit=1] run function rallous_warp_crash:claim_civ_bed
execute if entity @e[tag=rallous.claimed_village,distance=..80,limit=1] run function rallous_warp_crash:claim_civ_bed
execute if score @s rallous.claimed matches 1.. run function rallous_warp_crash:claim_civ_bed
advancement revoke @s only rallous_warp_crash:slept_in_bed
