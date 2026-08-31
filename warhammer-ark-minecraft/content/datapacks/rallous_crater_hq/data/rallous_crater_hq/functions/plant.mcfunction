# Fence + white banner + durable marker. Owner UUID for later player-faction recruit.
setblock ~2 ~ ~ minecraft:oak_fence
setblock ~2 ~1 ~ minecraft:white_banner

summon minecraft:marker ~2 ~1 ~ {Tags:["rallous.hq","rallous.crater_hq","rallous.hq_new"],CustomName:'{"text":"Crater HQ"}'}
data modify entity @e[type=minecraft:marker,tag=rallous.hq_new,limit=1,sort=nearest] data.Owner set from entity @a[tag=rallous.hq.marking,limit=1] UUID
data modify entity @e[type=minecraft:marker,tag=rallous.hq_new,limit=1,sort=nearest] data.pos set from storage rallous_crater_hq:data pos
execute if score @a[tag=rallous.hq.marking,limit=1] rallous.pid = @a[tag=rallous.hq.marking,limit=1] rallous.pid run scoreboard players operation @e[type=minecraft:marker,tag=rallous.hq_new,limit=1,sort=nearest] rallous.pid = @a[tag=rallous.hq.marking,limit=1] rallous.pid
tag @e[type=minecraft:marker,tag=rallous.hq_new] remove rallous.hq_new
