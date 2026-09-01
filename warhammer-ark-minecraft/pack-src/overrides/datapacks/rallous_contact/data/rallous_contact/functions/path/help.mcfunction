scoreboard players set @s rallous.path 1
scoreboard players set @s rallous.help 1
advancement grant @s only rallous_contact:path/help
tellraw @s {"text":"Path: help. rallous.path=1","color":"gray"}
function rallous_diplomacy:apply_path
function rallous_factions:path/sync
