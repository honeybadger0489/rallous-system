# Tag a nearby village/pillager site, or plant a bannered camp. 1.20.1 — no /return.
execute unless entity @e[tag=rallous_contact,distance=..256,limit=1] if entity @e[type=minecraft:villager,distance=..192,limit=1] at @e[type=minecraft:villager,distance=..192,limit=1,sort=nearest] run function rallous_warp_crash:tag_existing_contact
execute unless entity @e[tag=rallous_contact,distance=..256,limit=1] if entity @e[type=minecraft:pillager,distance=..192,limit=1] at @e[type=minecraft:pillager,distance=..192,limit=1,sort=nearest] run function rallous_warp_crash:tag_existing_contact
execute unless entity @e[tag=rallous_contact,distance=..256,limit=1] if entity @e[type=minecraft:iron_golem,distance=..192,limit=1] at @e[type=minecraft:iron_golem,distance=..192,limit=1,sort=nearest] run function rallous_warp_crash:tag_existing_contact
execute unless entity @e[tag=rallous_contact,distance=..256,limit=1] run function rallous_warp_crash:place_camp
