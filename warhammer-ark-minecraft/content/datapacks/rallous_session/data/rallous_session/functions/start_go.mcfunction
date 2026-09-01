# actor tagged. Camp tagged. Restart kills a leftover wave.
execute if score #restart rallous.session matches 1 run kill @e[tag=rallous.session.foe]
scoreboard players set @s rallous.session 0
scoreboard players set @s rallous.session_on 1
scoreboard players set @s rallous.session_age 0
scoreboard players set @s rallous.session_hold 0
tag @s add rallous.session.live
tag @s remove rallous.session.done
scoreboard players operation @s rallous.session_race = @e[tag=rallous.session.camp,limit=1] rallous.fac.race
execute unless score @s rallous.session_race matches 1..8 run scoreboard players operation @s rallous.session_race = @s rallous.race
execute unless score @s rallous.session_race matches 1..8 run scoreboard players set @s rallous.session_race 1
scoreboard players operation #race rallous.session_race = @s rallous.session_race
scoreboard players operation #stance rallous.session_kind = @e[tag=rallous.session.camp,limit=1] rallous.fac.stance
execute if score #stance rallous.session_kind matches 1 run function rallous_session:begin_help
execute if score #stance rallous.session_kind matches 5 run function rallous_session:begin_help
execute if score #stance rallous.session_kind matches 2 run function rallous_session:begin_prove
execute if score #stance rallous.session_kind matches 4 run function rallous_session:begin_prove
execute if score #stance rallous.session_kind matches 3 run function rallous_session:begin_hostile
execute if score #stance rallous.session_kind matches 6 run function rallous_session:begin_hostile
execute unless score #stance rallous.session_kind matches 1..6 run function rallous_session:begin_prove
execute as @e[tag=rallous.session.camp,limit=1] at @s run function rallous_session:voice/start
