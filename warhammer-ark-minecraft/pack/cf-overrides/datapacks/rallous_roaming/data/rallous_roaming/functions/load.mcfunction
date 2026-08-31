# Rallous roaming wars — scoreboards + clock. No chat on /reload.
# 1.20.1 / pack_format 15. schedule replace so /reload does not stack clocks.

scoreboard objectives add rallous.roam dummy
scoreboard objectives add rallous.roam.play dummy
scoreboard objectives add rallous.roam.life dummy

scoreboard players set $neg rallous.roam -1
scoreboard players set $3 rallous.roam 3
scoreboard players set $24000 rallous.roam 24000
scoreboard players set $16384 rallous.roam 16384

team add rallous_roam
team modify rallous_roam friendlyFire false
team modify rallous_roam seeFriendlyInvisibles true
team modify rallous_roam nametagVisibility always
team modify rallous_roam color dark_red

# First natural check in 60s. replace = one pending clock after reload.
schedule function rallous_roaming:clock 1200t replace
