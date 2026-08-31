# /function rallous_diplomacy:apply_path
# as player at player. Consumes rallous.path 1/2/3/4 set by FTB / rallous_contact.
execute unless score @s rallous.path matches 1..4 run tellraw @s {"text":"No path set. Finish a Paths quest or run rallous_diplomacy:help|betray|join|leave.","color":"gray"}
execute if score @s rallous.path matches 1 run function rallous_diplomacy:help
execute if score @s rallous.path matches 2 run function rallous_diplomacy:betray
execute if score @s rallous.path matches 3 run function rallous_diplomacy:join
execute if score @s rallous.path matches 4 run function rallous_diplomacy:leave
