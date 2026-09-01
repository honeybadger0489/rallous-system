# Lizardmen / Beastmen Ark glue. Fossils IDs vary by jar; vanilla proxies always spawn.
tellraw @s {"text":"Jungle-side Lizardmen proxies and forest Beastmen. Fossils dinos spawn if that mod loaded this entity.","color":"aqua"}
summon turtle ~3 ~ ~ {CustomName:'{"text":"Skink","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
summon turtle ~4 ~ ~1 {CustomName:'{"text":"Skink","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
summon goat ~-3 ~ ~2 {CustomName:'{"text":"Ungor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.beastmen"]}
summon ravager ~-5 ~ ~ {CustomName:'{"text":"Cygor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.beastmen"]}
summon fossil:triceratops ~6 ~ ~ {CustomName:'{"text":"Stegadon","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
