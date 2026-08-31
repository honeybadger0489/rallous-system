advancement grant @s only rallous_temple_herd:lizardmen/warm_canopy
execute unless entity @s[tag=rallous.temple_primer] run function rallous_temple_herd:give_temple_primer
execute unless entity @s[tag=rallous.temple_primer] if entity @s[tag=rallous.old_world] run function rallous_temple_herd:give_lesser_bond
tag @s add rallous.temple_primer
