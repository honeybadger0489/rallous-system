scoreboard players set @s rallous.path 2
scoreboard players set @s rallous.betray 1
advancement grant @s only rallous_contact:path/betray
tellraw @s {"text":"Path: betray. rallous.path=2","color":"gray"}
function rallous_diplomacy:apply_path
function rallous_factions:path/sync
