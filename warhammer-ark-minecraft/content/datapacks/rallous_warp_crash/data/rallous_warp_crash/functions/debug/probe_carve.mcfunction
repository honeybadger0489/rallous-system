# Mini crater + marker. Not a full player land (no greet / kit / rings).
forceload add ~ ~
fill ~-2 ~-1 ~-2 ~2 ~1 ~2 minecraft:air
fill ~-2 ~-2 ~-2 ~2 ~-2 ~2 minecraft:blackstone
setblock ~ ~-2 ~ minecraft:crying_obsidian
setblock ~ ~-1 ~ minecraft:campfire
summon minecraft:marker ~ ~ ~ {Tags:["rallous.crater","rallous.crash.crater","rallous.slot_probe_crater"]}
scoreboard players operation @e[type=minecraft:marker,tag=rallous.slot_probe_crater,limit=1,sort=nearest] rallous.slot = @s rallous.slot
scoreboard players operation @e[type=minecraft:marker,tag=rallous.slot_probe_crater,limit=1,sort=nearest] rallous.pid = @s rallous.slot
tag @s add rallous.slot_landed
tp @s ~ ~ ~
