# Pulse: strip crash magic once, plant lecterns on new camps.
scoreboard players add #clock rallous.winds 1
execute if score #clock rallous.winds matches 20.. run function rallous_winds:pulse
execute if score #clock rallous.winds matches 20.. run scoreboard players set #clock rallous.winds 0
