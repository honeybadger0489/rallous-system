# Extra smoke so the picket is visible from the crater rim.
execute unless block ~2 ~ ~-2 minecraft:campfire unless block ~2 ~ ~-2 minecraft:soul_campfire run setblock ~2 ~ ~-2 minecraft:campfire
execute unless block ~-2 ~ ~2 minecraft:campfire unless block ~-2 ~ ~2 minecraft:soul_campfire run setblock ~-2 ~ ~2 minecraft:campfire
particle minecraft:campfire_signal_smoke ~ ~4 ~ 0.2 1.2 0.2 0.02 12
