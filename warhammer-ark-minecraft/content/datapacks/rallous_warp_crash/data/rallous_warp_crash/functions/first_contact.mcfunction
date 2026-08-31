# Quest-agent hook. Named lord from compiled tables, not a mute camp.
function rallous_factions:contact/assign
data modify storage rallous_warp_crash:data last_contact.UUID set from entity @s UUID
execute store result storage rallous_warp_crash:data last_contact.x int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[0]
execute store result storage rallous_warp_crash:data last_contact.y int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[1]
execute store result storage rallous_warp_crash:data last_contact.z int 1 run data get entity @e[tag=rallous.camp,limit=1,sort=nearest] Pos[2]
advancement grant @s only rallous_warp_crash:first_contact
