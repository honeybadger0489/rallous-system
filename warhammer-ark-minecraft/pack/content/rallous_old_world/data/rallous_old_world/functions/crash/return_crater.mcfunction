execute if entity @e[type=marker,tag=rallous.world_crater,limit=1] run tp @s @e[type=marker,tag=rallous.world_crater,limit=1]
execute unless entity @e[type=marker,tag=rallous.world_crater,limit=1] run tellraw @s {"text":"No world crater marker. Die without a bed, or rejoin a new world.","color":"red"}
