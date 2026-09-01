# First join only. 1.20.1 — no /return.
# rallous.joined=1 claims this join so a second tick path cannot scatter again.
execute unless entity @s[tag=rallous.warp_landed] unless score @s rallous.joined matches 1.. if dimension minecraft:overworld run function rallous_warp_crash:first_join_go
