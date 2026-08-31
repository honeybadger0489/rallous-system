# Runs as probe at crater scores. forceload so the HQ marker stays findable.
forceload add ~ ~
execute unless entity @e[type=minecraft:marker,tag=rallous.hq,distance=..8,limit=1] run function rallous_crater_hq:plant
kill @s
