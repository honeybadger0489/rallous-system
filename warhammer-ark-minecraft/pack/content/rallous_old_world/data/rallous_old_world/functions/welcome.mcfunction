tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
scoreboard players set @s rallous.crashed 1
scoreboard players set @s rallous.deaths 0
function rallous_old_world:crash/strip_starter_magic
# Sibling warp-crash already scattered and carved if tag rallous.warp_landed.
execute unless entity @s[tag=rallous.warp_landed] unless entity @e[type=marker,tag=rallous.world_crater,limit=1] run function rallous_old_world:crash/first_crash
execute unless entity @s[tag=rallous.warp_landed] if entity @s[tag=!rallous.anchor] if entity @e[type=marker,tag=rallous.world_crater,limit=1] run function rallous_old_world:crash/scatter_friend
title @s times 20 80 20
title @s title {"text":"Warp-crash","color":"dark_purple","bold":true}
title @s subtitle {"text":"The court is gone. You hit the Old World.","color":"gray"}
tellraw @s [{"text":"No war council. Friends land elsewhere. Quest book: ","color":"light_purple"},{"text":"`","color":"white"},{"text":"  Force roaming: ","color":"light_purple"},{"text":"/function rallous_old_world:force_roaming","color":"yellow"}]
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
