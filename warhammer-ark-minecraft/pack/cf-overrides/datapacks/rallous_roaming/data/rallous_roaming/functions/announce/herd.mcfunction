# Horned Woods voice. No town. Only the hung skull-banner.
title @a times 10 70 20
title @a title {"text":"The Herd","color":"gold","bold":true}
title @a subtitle {"text":"Hooves in the trees. No town.","color":"#8B5A2B"}
tellraw @a [{"text":"[Horned Woods] ","color":"gold","bold":true},{"text":"The herdstone howls. The herd walks. There is no capital. Only the hung skull-banner and the dark between the trunks.","color":"yellow"}]
execute at @a run playsound minecraft:entity.ravager.roar hostile @a ~ ~ ~ 0.8 0.7
execute at @a run playsound minecraft:item.goat_horn.sound.5 ambient @a ~ ~ ~ 0.65 0.7
