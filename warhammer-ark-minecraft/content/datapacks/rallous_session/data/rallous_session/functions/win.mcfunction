# /function rallous_session:win — night done. FTB reads rallous.session = 1.
tag @s add rallous.session.actor
execute unless entity @e[tag=rallous.session.camp,limit=1] run function rallous_session:bind
scoreboard players operation #race rallous.session_race = @s rallous.session_race
execute unless score #race rallous.session_race matches 1..8 run scoreboard players operation #race rallous.session_race = @s rallous.race
scoreboard players set @s rallous.session 1
scoreboard players set @s rallous.session_on 0
scoreboard players set @s rallous.proved 1
execute if score @s rallous.session_kind matches 1 run scoreboard players set @s rallous.crash 2
execute unless score @s rallous.session_kind matches 1 run scoreboard players set @s rallous.crash 3
execute if entity @s[tag=!rallous.session.done] as @e[tag=rallous.session.camp,limit=1] at @s run function rallous_session:voice/win
execute if entity @s[tag=!rallous.session.done] unless entity @e[tag=rallous.session.camp,limit=1] run tellraw @s {"text":"The night is done. One village or one fight. That is enough.","color":"gold"}
execute if entity @s[tag=rallous.session.done] run tellraw @s {"text":"This night is already marked won.","color":"gray"}
tag @s remove rallous.session.live
tag @s add rallous.session.done
scoreboard players set @s rallous.session_hold 0
kill @e[tag=rallous.session.foe]
execute if score @s rallous.session_kind matches 1 run advancement grant @s only rallous_contact:crash/village
execute unless score @s rallous.session_kind matches 1 run advancement grant @s only rallous_contact:crash/fight
advancement grant @s only rallous_contact:crash/proved
tag @s remove rallous.session.actor
