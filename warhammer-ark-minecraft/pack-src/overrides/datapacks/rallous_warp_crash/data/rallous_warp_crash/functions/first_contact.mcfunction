# Quest-agent hook. /function rallous_warp_crash:first_contact
execute unless entity @e[tag=rallous_contact,distance=..512,limit=1] at @s run function rallous_warp_crash:place_camp
tag @s add rallous.contacted
scoreboard players set @s rallous.contact 1
data modify storage rallous_warp_crash:data last_contact.UUID set from entity @s UUID
execute store result storage rallous_warp_crash:data last_contact.x int 1 run data get entity @e[tag=rallous_contact,limit=1,sort=nearest] Pos[0]
execute store result storage rallous_warp_crash:data last_contact.y int 1 run data get entity @e[tag=rallous_contact,limit=1,sort=nearest] Pos[1]
execute store result storage rallous_warp_crash:data last_contact.z int 1 run data get entity @e[tag=rallous_contact,limit=1,sort=nearest] Pos[2]
advancement grant @s only rallous_warp_crash:first_contact
tellraw @s [{"text":"A banner on the ridge. Someone already holds this land.","color":"dark_purple"}]
execute at @e[tag=rallous_contact,limit=1,sort=nearest] run particle minecraft:witch ~ ~2 ~ 0.25 1 0.25 0 24
