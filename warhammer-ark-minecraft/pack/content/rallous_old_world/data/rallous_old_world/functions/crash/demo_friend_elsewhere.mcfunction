# Solo smoke: pretend you are the second player.
tag @s remove rallous.anchor
function rallous_old_world:crash/scatter_friend
tellraw @s {"text":"Solo demo: you were scattered. /function rallous_old_world:crash/return_crater  goes back to the first crater.","color":"yellow"}
