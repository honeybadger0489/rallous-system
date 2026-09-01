# as player — contact camp by id, else nearest banner / lord.
tag @e[tag=rallous.session.camp] remove rallous.session.camp
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.session.actor,limit=1] rallous.contact_id run tag @s add rallous.session.camp
execute unless entity @e[tag=rallous.session.camp,limit=1] as @e[tag=rallous.camp,distance=..400,limit=1,sort=nearest] run tag @s add rallous.session.camp
execute unless entity @e[tag=rallous.session.camp,limit=1] as @e[tag=rallous_contact,distance=..400,limit=1,sort=nearest] run tag @s add rallous.session.camp
execute unless entity @e[tag=rallous.session.camp,limit=1] as @e[tag=rallous.lord,distance=..400,limit=1,sort=nearest] run tag @s add rallous.session.camp
execute unless entity @e[tag=rallous.session.camp,limit=1] as @e[tag=rallous.camp,limit=1,sort=nearest] run tag @s add rallous.session.camp
