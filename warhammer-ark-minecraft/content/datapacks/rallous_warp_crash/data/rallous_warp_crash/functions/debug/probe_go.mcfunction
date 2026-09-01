# Spread this probe onto its slot, then settle if the 900 reject is clear.
function rallous_warp_crash:scatter_coords
execute at @s run function rallous_warp_crash:debug/probe_settle
