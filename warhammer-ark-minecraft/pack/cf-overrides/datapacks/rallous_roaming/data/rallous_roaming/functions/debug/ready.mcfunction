# Make the *scheduled* path eligible without waiting 20–40 min. Advances one day (clears crater lock).
# Force-test still does not need this: /function rallous_roaming:events/waaagh
scoreboard players set @a rallous.roam.play 48000
scoreboard players set $need rallous.roam.play 1
scoreboard players set $cooldown rallous.roam 0
time add 24000
function rallous_roaming:safety/ensure_origin
function rallous_roaming:safety/check
tellraw @a [{"text":"Roaming clock is eligible. Next minute it may roll a host (25%). Or force: ","color":"yellow"},{"text":"/function rallous_roaming:events/waaagh","color":"white"}]
