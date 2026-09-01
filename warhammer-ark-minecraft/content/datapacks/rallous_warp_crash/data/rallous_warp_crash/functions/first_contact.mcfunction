# Quest-agent hook. Named lord from compiled tables, not a mute camp.
# Greet only at the picket. Bind scores from the crater so Recruits can found the name.
execute if entity @e[tag=rallous.camp,distance=..18,limit=1] run function rallous_factions:contact/assign
execute unless entity @e[tag=rallous.camp,distance=..18,limit=1] run function rallous_factions:contact/bind_only
function rallous_kit:on_greet
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
data modify storage rallous_warp_crash:data last_contact.UUID set from entity @s UUID
execute store result storage rallous_warp_crash:data last_contact.x int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[0]
execute store result storage rallous_warp_crash:data last_contact.y int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[1]
execute store result storage rallous_warp_crash:data last_contact.z int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[2]
advancement grant @s only rallous_warp_crash:first_contact
