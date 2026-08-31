# Setblock bowl + Warp-taint. Not a ship. Sculk / obsidian / crying / amethyst.
fill ~-6 ~ ~-6 ~6 ~5 ~6 minecraft:air
fill ~-5 ~-1 ~-5 ~5 ~ ~5 minecraft:air
fill ~-4 ~-2 ~-4 ~4 ~-1 ~4 minecraft:air
fill ~-3 ~-3 ~-3 ~3 ~-2 ~3 minecraft:air
fill ~-2 ~-4 ~-2 ~2 ~-3 ~2 minecraft:air
fill ~-1 ~-5 ~-1 ~1 ~-4 ~1 minecraft:air

fill ~-1 ~-6 ~-1 ~1 ~-6 ~1 minecraft:obsidian
setblock ~ ~-6 ~ minecraft:crying_obsidian

fill ~-3 ~-5 ~-3 ~3 ~-5 ~3 minecraft:sculk
fill ~-1 ~-5 ~-1 ~1 ~-5 ~1 minecraft:obsidian
setblock ~ ~-5 ~ minecraft:crying_obsidian
setblock ~1 ~-5 ~1 minecraft:amethyst_block
setblock ~-1 ~-5 ~-1 minecraft:amethyst_block

fill ~-4 ~-4 ~-4 ~4 ~-4 ~4 minecraft:sculk
setblock ~ ~-4 ~ minecraft:sculk
setblock ~2 ~-4 ~ minecraft:crying_obsidian
setblock ~-2 ~-4 ~ minecraft:obsidian
setblock ~ ~-4 ~2 minecraft:amethyst_block
setblock ~ ~-4 ~-2 minecraft:crying_obsidian

fill ~-5 ~-3 ~-5 ~5 ~-3 ~5 minecraft:blackstone
fill ~-3 ~-3 ~-3 ~3 ~-3 ~3 minecraft:air
setblock ~-5 ~-3 ~ minecraft:sculk
setblock ~5 ~-3 ~ minecraft:sculk
setblock ~ ~-3 ~-5 minecraft:crying_obsidian
setblock ~ ~-3 ~5 minecraft:obsidian
setblock ~4 ~-3 ~4 minecraft:amethyst_block
setblock ~-4 ~-3 ~-4 minecraft:amethyst_block

fill ~-6 ~-2 ~-6 ~6 ~-2 ~6 minecraft:deepslate
fill ~-4 ~-2 ~-4 ~4 ~-2 ~4 minecraft:air
setblock ~-6 ~-2 ~2 minecraft:sculk
setblock ~6 ~-2 ~-2 minecraft:sculk
setblock ~2 ~-2 ~-6 minecraft:crying_obsidian
setblock ~-2 ~-2 ~6 minecraft:obsidian
setblock ~5 ~-2 ~5 minecraft:budding_amethyst
setblock ~-5 ~-2 ~-5 minecraft:crying_obsidian

fill ~-7 ~-1 ~-7 ~7 ~-1 ~7 minecraft:cobbled_deepslate
fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:air
setblock ~-7 ~-1 ~ minecraft:sculk
setblock ~7 ~-1 ~ minecraft:obsidian
setblock ~ ~-1 ~-7 minecraft:crying_obsidian
setblock ~ ~-1 ~7 minecraft:amethyst_block
setblock ~3 ~-1 ~-5 minecraft:amethyst_cluster[facing=up]
setblock ~-4 ~-1 ~4 minecraft:amethyst_cluster[facing=up]
setblock ~5 ~-1 ~2 minecraft:sculk_vein[down=true]
setblock ~-3 ~-1 ~-6 minecraft:sculk_vein[down=true]

# Stand on the inner sculk plate, not inside the chest.
tp @s ~ ~-3 ~
