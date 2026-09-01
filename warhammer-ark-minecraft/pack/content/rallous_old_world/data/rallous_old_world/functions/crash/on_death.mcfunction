# Vanilla already sent you to bed or to the spawnpoint we set (your crater).
tellraw @s {"text":"If you had no claimed village / join civ-bed, the warp hauled you back to your crater. Wilderness beds do not stick.","color":"dark_purple"}
scoreboard players set @s rallous.deaths 0
