# Recruits missing or command failed. Help camps must not murder. Hostile camps still bite.
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:host/levy_fallback_hostile
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:host/levy_fallback_hostile
execute unless score @s rallous.fac.stance matches 3 unless score @s rallous.fac.stance matches 6 run function rallous_factions:host/levy_fallback_guard
