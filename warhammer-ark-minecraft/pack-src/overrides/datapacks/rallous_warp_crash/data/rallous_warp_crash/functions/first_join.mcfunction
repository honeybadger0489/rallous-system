# First join only. 1.20.1 — no /return.
execute unless entity @s[tag=rallous.warp_landed] if dimension minecraft:overworld run function rallous_warp_crash:assign_ids
execute unless entity @s[tag=rallous.warp_landed] if dimension minecraft:overworld run function rallous_warp_crash:scatter
