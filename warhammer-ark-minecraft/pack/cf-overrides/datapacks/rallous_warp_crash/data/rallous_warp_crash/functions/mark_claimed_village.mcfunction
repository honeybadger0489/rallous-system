# Faction/OPAC agent helper: mark this spot as a claimed village.
execute unless entity @e[tag=rallous.claimed_village,distance=..8,limit=1] run summon minecraft:marker ~ ~ ~ {Tags:["rallous.claimed_village"]}
