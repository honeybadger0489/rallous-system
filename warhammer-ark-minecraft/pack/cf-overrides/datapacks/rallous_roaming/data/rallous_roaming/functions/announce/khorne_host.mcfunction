# Blood Host voice. No treaty. Only the skull-tithe.
title @a times 10 70 20
title @a title {"text":"BLOOD FOR THE BLOOD GOD","color":"dark_red","bold":true}
title @a subtitle {"text":"The Blood Host marches","color":"red"}
tellraw @a [{"text":"[Blood Host] ","color":"red","bold":true},{"text":"No treaty. No camp. Skulls and blood. Pay the tithe or be the tithe.","color":"dark_red"}]
execute at @a run playsound minecraft:entity.wither_skeleton.ambient hostile @a ~ ~ ~ 1 0.6
execute at @a run playsound minecraft:item.goat_horn.sound.7 ambient @a ~ ~ ~ 0.75 0.55
execute at @a run playsound minecraft:entity.blaze.ambient hostile @a ~ ~ ~ 0.4 0.5
