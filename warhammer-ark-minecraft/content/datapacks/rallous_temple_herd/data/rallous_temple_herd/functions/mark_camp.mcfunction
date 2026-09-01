# Compact presence next to a 7x7 picket. Not the 13x13 plaza (that would overwrite the camp).
# Fossils tame stays global — this is site flavour only.
execute if score @s rallous.fac.race matches 3 unless entity @e[tag=rallous.temple_marker,distance=..16,limit=1] run function rallous_temple_herd:mark_camp_temple
execute if score @s rallous.fac.race matches 4 unless entity @e[tag=rallous.herdstone,distance=..16,limit=1] run function rallous_temple_herd:mark_camp_herd
