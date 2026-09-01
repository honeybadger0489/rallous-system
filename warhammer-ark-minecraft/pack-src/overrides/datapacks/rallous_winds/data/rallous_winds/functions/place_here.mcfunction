# Cheats: plant a path lectern at your feet. Uses nearest camp race if any.
scoreboard players set $school rallous.winds 0
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest,distance=..48] run scoreboard players operation $tmp rallous.winds = @s rallous.fac.race
execute if score $tmp rallous.winds matches 1 run scoreboard players set $school rallous.winds 1
execute if score $tmp rallous.winds matches 3 run scoreboard players set $school rallous.winds 1
execute if score $tmp rallous.winds matches 2 run scoreboard players set $school rallous.winds 3
execute if score $tmp rallous.winds matches 4 run scoreboard players set $school rallous.winds 4
execute if score $tmp rallous.winds matches 8 run scoreboard players set $school rallous.winds 4
execute align xyz positioned ~0.5 ~ ~0.5 run function rallous_winds:set_lectern
tellraw @s {"text":"A Winds lectern. The letter points to Iron's ink. No spellbook.","color":"gray"}
