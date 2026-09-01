# Summon at origin (loaded). Inner vs outer radius. spreadplayers hunts land.
summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe.pending","rallous.probe.ring","rallous.probe.new"]}
execute if score $ring_kind rallous.gen matches 0 run tag @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] add rallous.probe.inner
execute if score $ring_kind rallous.gen matches 1 run tag @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] add rallous.probe.outer
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run scoreboard players set @s rallous.tries 0
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run tag @s remove rallous.probe.new
