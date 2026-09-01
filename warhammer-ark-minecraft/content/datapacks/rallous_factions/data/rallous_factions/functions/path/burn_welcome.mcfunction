# Khorne if you burn welcome. Reachable at the picket, not a wiki sentence.
execute if entity @s[tag=rallous.burned] run scoreboard players set @s rallous.burn 0
execute unless entity @s[tag=rallous.burned] run function rallous_factions:path/burn_welcome_go
