# Recruits command missing, NPE, or no levy in range. Two extra named vanilla.
execute if score $event rallous.roam matches 1 run function rallous_roaming:spawn/fallback_waaagh
execute if score $event rallous.roam matches 2 run function rallous_roaming:spawn/fallback_herd
execute if score $event rallous.roam matches 3 run function rallous_roaming:spawn/fallback_khorne
