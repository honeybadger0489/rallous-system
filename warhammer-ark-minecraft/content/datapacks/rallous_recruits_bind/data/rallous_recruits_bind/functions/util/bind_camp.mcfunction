# as player at player — nearest compiled camp is the Recruits host, never a generic Team 2.
tag @e[tag=rallous.rec.camp] remove rallous.rec.camp
execute as @e[tag=rallous.camp,distance=..512,limit=1,sort=nearest] run tag @s add rallous.rec.camp
execute unless entity @e[tag=rallous.rec.camp,limit=1] as @e[tag=rallous_contact,distance=..512,limit=1,sort=nearest] run tag @s add rallous.rec.camp
execute if entity @e[tag=rallous.rec.camp,limit=1] run scoreboard players operation @s rallous.contact_id = @e[tag=rallous.rec.camp,limit=1] rallous.fac.id
execute if entity @e[tag=rallous.rec.camp,limit=1] run scoreboard players operation @s rallous.rec.id = @e[tag=rallous.rec.camp,limit=1] rallous.fac.id
execute if entity @e[tag=rallous.rec.camp,limit=1] run scoreboard players operation @s rallous.rec.race = @e[tag=rallous.rec.camp,limit=1] rallous.fac.race
execute if entity @e[tag=rallous.rec.camp,limit=1] run scoreboard players operation @s rallous.rec.stance = @e[tag=rallous.rec.camp,limit=1] rallous.fac.stance
execute if entity @e[tag=rallous.rec.camp,limit=1] run scoreboard players set @s rallous.contact 1
tag @s add rallous.rec.bound
execute as @e[type=#rallous_recruits_bind:levy,distance=..64] run tag @s add rallous.rec.host
function rallous_recruits_bind:name/set
