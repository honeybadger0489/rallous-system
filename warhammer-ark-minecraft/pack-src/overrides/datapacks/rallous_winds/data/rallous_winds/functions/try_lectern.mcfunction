execute positioned ~1 ~ ~-1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~-1 ~ ~1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~2 ~ ~-1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~0 ~ ~2 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~1 ~ ~-1 run function rallous_winds:set_lectern
