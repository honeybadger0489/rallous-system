# Carve / contact once. rallous.warp_landed is the lock (set at the start of land_go_do).
execute unless entity @s[tag=rallous.warp_landed] run function rallous_warp_crash:land_go_do
