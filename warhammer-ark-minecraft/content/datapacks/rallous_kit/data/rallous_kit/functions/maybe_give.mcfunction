# Help-leaning (stance 1) or joined (5) get a levy kit. Daemon-suspicion / hostile: no free kit until a path.
scoreboard players set $kit_ok rallous.gen 0
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] if score @s rallous.fac.stance matches 1 run scoreboard players set $kit_ok rallous.gen 1
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] if score @s rallous.fac.stance matches 5 run scoreboard players set $kit_ok rallous.gen 1
execute if score $kit_ok rallous.gen matches 1 run tag @s remove rallous.kit.wary
execute if score $kit_ok rallous.gen matches 1 run function rallous_kit:give
execute if score $kit_ok rallous.gen matches 0 unless entity @s[tag=rallous.kit.wary] run tellraw @s {"text":"No guest-kit. These hosts are wary or hostile. Help or join first.","color":"yellow"}
execute if score $kit_ok rallous.gen matches 0 run tag @s add rallous.kit.wary
