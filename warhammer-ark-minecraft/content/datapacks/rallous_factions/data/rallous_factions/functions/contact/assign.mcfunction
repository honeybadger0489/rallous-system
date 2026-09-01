# Once per survivor. A second land/tick path cannot greet or kit again.
execute unless entity @s[tag=rallous.contacted] run function rallous_factions:contact/assign_go
