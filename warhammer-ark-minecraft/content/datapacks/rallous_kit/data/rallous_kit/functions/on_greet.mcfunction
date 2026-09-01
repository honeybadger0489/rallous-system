# Hook for warp-crash / factions after first-contact greet.
# Call as the greeted player:  /function rallous_kit:on_greet
# Also runs from #minecraft:tick when rallous.greeted=1 and rallous.kitted is unset.
# Waits until rallous.race is 1–8. Idempotent once rallous.kitted is 1.
scoreboard players set @s rallous.greeted 1
execute unless score @s rallous.kitted matches 1.. if score @s rallous.race matches 1..8 run function rallous_kit:give
