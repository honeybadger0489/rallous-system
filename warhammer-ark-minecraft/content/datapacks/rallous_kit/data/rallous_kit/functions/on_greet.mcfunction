# Hook for warp-crash / factions after first-contact greet.
# Call as the greeted player:  /function rallous_kit:on_greet
# Also runs from #minecraft:tick when rallous.greeted=1 and rallous.kitted is unset.
# Waits until rallous.race is 1–8. Idempotent once rallous.kitted is 1.
scoreboard players set @s rallous.greeted 1
# Hook for warp-crash / factions after first-contact greet.
# Call as the greeted player:  /function rallous_kit:on_greet
# Also runs from #minecraft:tick when rallous.greeted=1 and rallous.kitted is unset.
# Waits until rallous.race is 1–8. Idempotent once rallous.kitted is 1.
# Hostile / daemon-suspicion camps do not hand a free kit until a path.
scoreboard players set @s rallous.greeted 1
execute unless score @s rallous.kitted matches 1.. if entity @s[tag=rallous.warp_landed] if score @s rallous.race matches 1..8 run function rallous_kit:maybe_give
execute unless score @s rallous.kitted matches 1.. unless entity @s[tag=rallous.warp_landed] if score @s rallous.joined matches 1.. if score @s rallous.race matches 1..8 run function rallous_kit:maybe_give
execute unless score @s rallous.kitted matches 1.. unless entity @s[tag=rallous.warp_landed] unless score @s rallous.joined matches 1.. if score @s rallous.race matches 1..8 run function rallous_kit:maybe_give
