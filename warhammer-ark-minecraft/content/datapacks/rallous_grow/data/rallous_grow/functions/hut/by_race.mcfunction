# #slot rallous.grow is 1 (east hut), 2 (west hut), or 3 (south hall).
scoreboard players operation #race rallous.grow = @s rallous.fac.race
execute unless score #race rallous.grow matches 1..8 run scoreboard players operation #race rallous.grow = @p[distance=..48] rallous.race
execute unless score #race rallous.grow matches 1..8 run scoreboard players set #race rallous.grow 1
execute if score #race rallous.grow matches 1 run function rallous_grow:hut/empire
execute if score #race rallous.grow matches 2 run function rallous_grow:hut/vampire
execute if score #race rallous.grow matches 3 run function rallous_grow:hut/lizard
execute if score #race rallous.grow matches 4 run function rallous_grow:hut/beast
execute if score #race rallous.grow matches 5 run function rallous_grow:hut/greenskin
execute if score #race rallous.grow matches 6 run function rallous_grow:hut/dwarf
execute if score #race rallous.grow matches 7 run function rallous_grow:hut/skaven
execute if score #race rallous.grow matches 8 run function rallous_grow:hut/khorne
