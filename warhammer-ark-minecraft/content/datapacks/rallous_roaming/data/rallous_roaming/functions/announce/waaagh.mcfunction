# Greenhost voice. No capital — the Waaagh *is* the road.
title @a times 10 70 20
title @a title {"text":"WAAAGH!","color":"green","bold":true}
title @a subtitle {"text":"Da Greenhost is on da move","color":"dark_green"}
tellraw @a [{"text":"[Greenhost] ","color":"green","bold":true},{"text":"WAAAGH! Get stuck in, ya gits! Smash da umies! No camp, no boss tent — just da Waaagh on da road.","color":"dark_green"}]
execute at @a run playsound minecraft:event.raid.horn hostile @a ~ ~ ~ 0.85 0.75
execute at @a run playsound minecraft:item.goat_horn.sound.1 ambient @a ~ ~ ~ 0.7 0.85
