execute unless entity @e[tag=rallous.lord,limit=1] run tellraw @a {"text":"The war council takes the field.","color":"gold"}
execute unless entity @e[tag=rallous.lord,limit=1] run function rallous_old_world:place_court
execute unless entity @e[tag=rallous.lord.karl,limit=1] run function rallous_old_world:lords/karl
execute unless entity @e[tag=rallous.lord.grimgor,limit=1] run function rallous_old_world:lords/grimgor
execute unless entity @e[tag=rallous.lord.mannfred,limit=1] run function rallous_old_world:lords/mannfred
execute unless entity @e[tag=rallous.lord.thorgrim,limit=1] run function rallous_old_world:lords/thorgrim
execute unless entity @e[tag=rallous.lord.katarin,limit=1] run function rallous_old_world:lords/katarin
execute unless entity @e[tag=rallous.lord.archaon,limit=1] run function rallous_old_world:lords/archaon
