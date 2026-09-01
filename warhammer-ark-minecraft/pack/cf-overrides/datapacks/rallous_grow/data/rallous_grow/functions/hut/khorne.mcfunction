# Bloodbound shrine — nether brick / blackstone / red banners.
execute if score #slot rallous.grow matches 1 run fill ~5 ~-1 ~-1 ~8 ~-1 ~2 minecraft:blackstone
execute if score #slot rallous.grow matches 1 run fill ~5 ~ ~-1 ~8 ~2 ~2 minecraft:nether_bricks
execute if score #slot rallous.grow matches 1 run fill ~6 ~ ~0 ~7 ~1 ~1 minecraft:air
execute if score #slot rallous.grow matches 1 run setblock ~5 ~ ~0 minecraft:air
execute if score #slot rallous.grow matches 1 run setblock ~5 ~1 ~0 minecraft:air
execute if score #slot rallous.grow matches 1 run fill ~5 ~3 ~-1 ~8 ~3 ~2 minecraft:nether_brick_slab
execute if score #slot rallous.grow matches 1 run setblock ~7 ~ ~1 minecraft:barrel
execute if score #slot rallous.grow matches 1 run setblock ~6 ~2 ~-1 minecraft:soul_lantern
execute if score #slot rallous.grow matches 1 run setblock ~8 ~4 ~0 minecraft:red_banner
execute if score #slot rallous.grow matches 2 run fill ~-8 ~-1 ~-1 ~-5 ~-1 ~2 minecraft:blackstone
execute if score #slot rallous.grow matches 2 run fill ~-8 ~ ~-1 ~-5 ~2 ~2 minecraft:nether_bricks
execute if score #slot rallous.grow matches 2 run fill ~-7 ~ ~0 ~-6 ~1 ~1 minecraft:air
execute if score #slot rallous.grow matches 2 run setblock ~-5 ~ ~0 minecraft:air
execute if score #slot rallous.grow matches 2 run setblock ~-5 ~1 ~0 minecraft:air
execute if score #slot rallous.grow matches 2 run fill ~-8 ~3 ~-1 ~-5 ~3 ~2 minecraft:nether_brick_slab
execute if score #slot rallous.grow matches 2 run setblock ~-7 ~ ~1 minecraft:barrel
execute if score #slot rallous.grow matches 2 run setblock ~-8 ~4 ~0 minecraft:red_banner
execute if score #slot rallous.grow matches 3 run fill ~-2 ~-1 ~5 ~3 ~-1 ~8 minecraft:blackstone
execute if score #slot rallous.grow matches 3 run fill ~-2 ~ ~5 ~3 ~2 ~8 minecraft:nether_bricks
execute if score #slot rallous.grow matches 3 run fill ~-1 ~ ~6 ~2 ~1 ~7 minecraft:air
execute if score #slot rallous.grow matches 3 run setblock ~0 ~ ~5 minecraft:air
execute if score #slot rallous.grow matches 3 run setblock ~0 ~1 ~5 minecraft:air
execute if score #slot rallous.grow matches 3 run fill ~-2 ~3 ~5 ~3 ~3 ~8 minecraft:nether_brick_slab
execute if score #slot rallous.grow matches 3 run setblock ~2 ~ ~7 minecraft:soul_campfire
execute if score #slot rallous.grow matches 3 run setblock ~-2 ~4 ~6 minecraft:red_banner
execute if score #slot rallous.grow matches 3 run setblock ~3 ~4 ~6 minecraft:red_banner
execute if score #slot rallous.grow matches 3 run setblock ~3 ~2 ~8 minecraft:skeleton_skull
