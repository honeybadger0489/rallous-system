# Nearest compiled camp becomes this survivor's contact faction.
execute unless entity @e[tag=rallous.camp,distance=..400,limit=1] run function rallous_factions:gen/place_near
tag @e[tag=rallous_contact] remove rallous_contact
execute as @e[tag=rallous.camp,limit=1,sort=nearest] run tag @s add rallous_contact
execute as @e[tag=rallous.lord,limit=1,sort=nearest] run tag @s add rallous_contact
scoreboard players operation @s rallous.contact_id = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.id
scoreboard players operation @s rallous.race = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.race
scoreboard players set @s rallous.contact 1
tag @s add rallous.contacted
tag @s add rallous.fac.greeted
function rallous_factions:contact/greet
