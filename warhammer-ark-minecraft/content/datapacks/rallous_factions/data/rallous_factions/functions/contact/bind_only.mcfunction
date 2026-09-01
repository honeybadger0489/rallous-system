# Crash bind: scores + Recruits name. Do not greet — the lord is off the bowl.
scoreboard players set @s rallous.joined 1
execute unless entity @e[tag=rallous.camp,distance=..400,limit=1] run function rallous_factions:gen/place_near
tag @e[tag=rallous_contact] remove rallous_contact
execute as @e[tag=rallous.camp,limit=1,sort=nearest] run tag @s add rallous_contact
execute as @e[tag=rallous.lord,limit=1,sort=nearest] run tag @s add rallous_contact
scoreboard players operation @s rallous.contact_id = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.id
scoreboard players operation @s rallous.race = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.race
scoreboard players set @s rallous.contact 1
function rallous_recruits_bind:on_contact
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:contact/beacon
tellraw @s {"text":"Banner-smoke on the horizon. Walk to it. A named lord will speak when you reach the picket — not a mute village.","color":"gold"}
