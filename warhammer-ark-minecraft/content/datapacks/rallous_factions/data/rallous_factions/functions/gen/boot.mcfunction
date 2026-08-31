# Start the first-days mix once. Contact camp is placed separately.
execute if score #booted rallous.gen matches 1 run scoreboard players set $noop rallous.gen 1
execute unless score #booted rallous.gen matches 1 run scoreboard players set #booted rallous.gen 1
