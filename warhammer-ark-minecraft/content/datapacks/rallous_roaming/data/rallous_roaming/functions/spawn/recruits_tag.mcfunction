# Fold the just-spawned Recruits patrol into this column.
execute as @e[type=#rallous_roaming:levy,distance=..16,tag=!rallous.roam] run function rallous_roaming:spawn/recruits_tag_one
