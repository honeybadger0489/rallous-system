# Small Recruits patrol at this camp. Same command as roaming. Not an armor-stand host.
execute if entity @s[tag=rallous.host.levied] run scoreboard players set $noop rallous.gen 1
execute unless entity @s[tag=rallous.host.levied] run function rallous_factions:host/levy_go
