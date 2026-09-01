execute as @e[type=#rallous_factions:levy,distance=..16,tag=!rallous.soldier,tag=!rallous.roam] run tag @s add rallous.soldier
execute as @e[type=#rallous_factions:levy,distance=..16,tag=rallous.soldier] run tag @s add rallous.host.levy
execute as @e[type=#rallous_factions:levy,distance=..16,tag=rallous.soldier] run data merge entity @s {PersistenceRequired:1b}
