# Play-time counter (20 ticks = 1s). 20 min = 24000, 40 min = 48000.
scoreboard players add @a rallous.roam.play 1

# March pulse every 10 ticks while a host is on the field.
execute if entity @e[tag=rallous.roam.host,limit=1] run scoreboard players add $pulse rallous.roam.life 1
execute if entity @e[tag=rallous.roam.host,limit=1] if score $pulse rallous.roam.life matches 10.. run function rallous_roaming:march/pulse
execute unless entity @e[tag=rallous.roam.host,limit=1] if score $event rallous.roam matches 1.. run function rallous_roaming:march/ended
