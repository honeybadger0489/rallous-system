tellraw @s {"text":"Forcing a Waaagh, a Beastmen herd, and a Khorne pack.","color":"red"}
# Sibling jar (rallous_roaming) if present; local proxies always fire.
function rallous_roaming:clear
execute as @s at @s run function rallous_roaming:spawn/waaagh
execute as @s at @s positioned ~18 ~ ~ run function rallous_roaming:spawn/herd
execute as @s at @s positioned ~-18 ~ ~ run function rallous_roaming:spawn/khorne_host
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/waaagh
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/herd
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/khorne
