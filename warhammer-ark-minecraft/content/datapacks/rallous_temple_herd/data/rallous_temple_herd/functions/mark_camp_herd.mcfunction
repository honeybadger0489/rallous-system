# Skull post + named stand, east of the 7x7 picket. Not the 13x13 herdstone pit.
fill ~5 ~-1 ~-1 ~7 ~-1 ~1 minecraft:coarse_dirt
setblock ~6 ~ ~ minecraft:cobbled_deepslate
setblock ~6 ~1 ~ minecraft:cobbled_deepslate
setblock ~6 ~2 ~ minecraft:wither_skeleton_skull
summon minecraft:armor_stand ~6 ~1 ~ {CustomName:'{"text":"Herdstone","color":"dark_red"}',CustomNameVisible:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,Tags:["rallous.herdstone"],ArmorItems:[{},{},{},{id:"minecraft:wither_skeleton_skull",Count:1b}]}
