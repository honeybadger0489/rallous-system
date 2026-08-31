# rallous_diplomacy — stance on camp markers. No chat on /reload.
# rallous.stance on the marker: 1 ally / 2 hostile / 3 joined / 4 neutral
# rallous.khorne_path: betray lean (player + that marker)
scoreboard objectives add rallous.path dummy
scoreboard objectives add rallous.race dummy
scoreboard objectives add rallous.help dummy
scoreboard objectives add rallous.betray dummy
scoreboard objectives add rallous.join dummy
scoreboard objectives add rallous.leave dummy
scoreboard objectives add rallous.stance dummy
scoreboard objectives add rallous.khorne_path dummy
scoreboard objectives add rallous.gifted dummy
scoreboard objectives add rallous.civ_bed dummy
scoreboard objectives add rallous.claimed dummy
scoreboard objectives add rallous.diplo dummy

scoreboard players set #ally rallous.stance 1
scoreboard players set #hostile rallous.stance 2
scoreboard players set #joined rallous.stance 3
scoreboard players set #neutral rallous.stance 4

team add rallous_ally
team modify rallous_ally friendlyFire false
team modify rallous_ally seeFriendlyInvisibles true
team modify rallous_ally nametagVisibility always
team modify rallous_ally color gold
