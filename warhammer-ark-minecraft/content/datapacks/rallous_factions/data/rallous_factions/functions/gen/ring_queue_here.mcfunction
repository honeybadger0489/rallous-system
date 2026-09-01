summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe.pending","rallous.probe.ring","rallous.probe.new"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] at @s run forceload add ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run scoreboard players set @s rallous.tries 0
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run tag @s remove rallous.probe.new
execute as @e[type=minecraft:marker,tag=rallous.probe.pending,limit=1,sort=nearest] at @s if loaded ~ ~ ~ run function rallous_factions:gen/ring_try
