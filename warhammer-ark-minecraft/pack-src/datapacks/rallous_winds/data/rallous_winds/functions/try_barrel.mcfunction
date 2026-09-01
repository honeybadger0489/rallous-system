execute if block ~-2 ~ ~-2 minecraft:barrel positioned ~-2 ~ ~-2 run function rallous_winds:fill_barrel
execute unless block ~-2 ~ ~-2 minecraft:barrel positioned ~-1 ~ ~-2 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:put_barrel
execute unless block ~-2 ~ ~-2 minecraft:barrel unless block ~-1 ~ ~-2 minecraft:barrel positioned ~1 ~ ~1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:put_barrel
