# 12 unique crash slots. Armor stands as fake players (no Carpet).
# Call: execute positioned <x> <y> <z> run function rallous_warp_crash:debug/prove_slots
# Does not claim SHIP_READY. Does not full-land (no greet/kit).
say [rallous.slots] start 12-slot proof
kill @e[tag=rallous.slot_probe]
kill @e[tag=rallous.slot_probe_crater]
scoreboard players set $pile rallous.slot 0
scoreboard players set $slots rallous.slot 0
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n0"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n0,limit=1] rallous.slot 0
scoreboard players set @e[tag=rallous.slot_n0,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n0,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n0,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n1"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n1,limit=1] rallous.slot 1
scoreboard players set @e[tag=rallous.slot_n1,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n1,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n1,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n2"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n2,limit=1] rallous.slot 2
scoreboard players set @e[tag=rallous.slot_n2,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n2,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n2,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n3"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n3,limit=1] rallous.slot 3
scoreboard players set @e[tag=rallous.slot_n3,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n3,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n3,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n4"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n4,limit=1] rallous.slot 4
scoreboard players set @e[tag=rallous.slot_n4,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n4,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n4,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n5"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n5,limit=1] rallous.slot 5
scoreboard players set @e[tag=rallous.slot_n5,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n5,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n5,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n6"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n6,limit=1] rallous.slot 6
scoreboard players set @e[tag=rallous.slot_n6,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n6,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n6,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n7"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n7,limit=1] rallous.slot 7
scoreboard players set @e[tag=rallous.slot_n7,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n7,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n7,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n8"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n8,limit=1] rallous.slot 8
scoreboard players set @e[tag=rallous.slot_n8,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n8,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n8,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n9"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n9,limit=1] rallous.slot 9
scoreboard players set @e[tag=rallous.slot_n9,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n9,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n9,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n10"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n10,limit=1] rallous.slot 10
scoreboard players set @e[tag=rallous.slot_n10,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n10,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n10,limit=1] at @s run function rallous_warp_crash:debug/probe_go
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.slot_probe","rallous.slot_n11"],Invisible:1b,NoGravity:1b,Invulnerable:1b,Small:1b}
scoreboard players set @e[tag=rallous.slot_n11,limit=1] rallous.slot 11
scoreboard players set @e[tag=rallous.slot_n11,limit=1] rallous.ring 0
scoreboard players set @e[tag=rallous.slot_n11,limit=1] rallous.retry 0
execute as @e[tag=rallous.slot_n11,limit=1] at @s run function rallous_warp_crash:debug/probe_go
execute store result score $slots rallous.slot if entity @e[tag=rallous.slot_probe_crater]
scoreboard players set $pile rallous.slot 0
execute as @e[tag=rallous.slot_probe_crater] at @s if entity @e[tag=rallous.slot_probe_crater,distance=0.1..900] run scoreboard players add $pile rallous.slot 1
tellraw @a [{"text":"[rallous.slots] craters=","color":"gold"},{"score":{"name":"$slots","objective":"rallous.slot"}},{"text":" pile(<900)=","color":"gold"},{"score":{"name":"$pile","objective":"rallous.slot"}}]
execute unless score $slots rallous.slot matches 12 run say [rallous.slots] FAIL crater count != 12
execute if score $pile rallous.slot matches 1.. run say [rallous.slots] FAIL two landings share a crater (<900)
execute if score $slots rallous.slot matches 12 if score $pile rallous.slot matches 0 run say [rallous.slots] OK 12 distinct slots
say [rallous.slots] done
