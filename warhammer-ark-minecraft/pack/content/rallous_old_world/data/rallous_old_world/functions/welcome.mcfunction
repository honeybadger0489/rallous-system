tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
title @s times 20 80 20
title @s title {"text":"The Old World","color":"gold","bold":true}
title @s subtitle {"text":"Reikland · Border Princes · Sylvania · Worlds Edge · Kislev · Chaos Wastes","color":"gray"}
tellraw @s [{"text":"A war council waits near you. Trade with a lord for a letter. Quest book: ","color":"gold"},{"text":"`","color":"white"},{"text":" (grave). Re-summon: ","color":"gold"},{"text":"/function rallous_old_world:summon_lords","color":"yellow"}]
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
