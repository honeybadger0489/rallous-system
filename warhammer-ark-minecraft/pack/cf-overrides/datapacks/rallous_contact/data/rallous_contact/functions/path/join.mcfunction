scoreboard players set @s rallous.path 3
scoreboard players set @s rallous.join 1
advancement grant @s only rallous_contact:path/join
tellraw @s {"text":"Path: join. rallous.path=3","color":"gray"}
function rallous_diplomacy:apply_path
function rallous_factions:path/sync
