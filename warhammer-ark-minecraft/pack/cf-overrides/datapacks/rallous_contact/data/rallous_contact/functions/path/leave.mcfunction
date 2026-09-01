scoreboard players set @s rallous.path 4
scoreboard players set @s rallous.leave 1
advancement grant @s only rallous_contact:path/leave
tellraw @s {"text":"Path: align-and-leave. rallous.path=4","color":"gray"}
function rallous_diplomacy:apply_path
function rallous_factions:path/sync
