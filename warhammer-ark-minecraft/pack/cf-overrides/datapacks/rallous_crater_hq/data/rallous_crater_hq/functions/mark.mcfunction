# Crash pack calls this as the landed player after crater scores exist.
# 1.20.1 — no /return. Missing rallous.crater_x/y/z → no-op.
execute if score @s rallous.crater_x = @s rallous.crater_x if score @s rallous.crater_y = @s rallous.crater_y if score @s rallous.crater_z = @s rallous.crater_z run function rallous_crater_hq:mark_go
