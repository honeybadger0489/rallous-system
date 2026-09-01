# Despawn the current roaming host so a force spawn is clean.
kill @e[tag=rallous.roam.host]
kill @e[type=minecraft:marker,tag=rallous.roam.spawner]
scoreboard players set $pulse rallous.roam.life 0
scoreboard players set $cooldown rallous.roam 0
