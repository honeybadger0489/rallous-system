tag @s add rallous.path_actor
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.path_actor,limit=1] rallous.contact_id run function rallous_factions:path/help_camp
execute unless entity @e[tag=rallous.camp,limit=1] run tellraw @s {"text":"Path noted: help. Meet a named lord and that faction will remember.","color":"gray"}
tag @s remove rallous.path_actor
