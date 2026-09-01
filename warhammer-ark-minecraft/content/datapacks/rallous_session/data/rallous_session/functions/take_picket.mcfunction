# /function rallous_session:take_picket — hostile complete by claiming the banner.
tag @s add rallous.session.actor
function rallous_session:bind
scoreboard players set #took rallous.session 0
execute if entity @s[tag=rallous.session.live] if score @s rallous.session_kind matches 3 run scoreboard players set #took rallous.session 1
execute if score #took rallous.session matches 1 run function rallous_session:win
execute if entity @s[tag=rallous.session.live] unless score @s rallous.session_kind matches 3 run tellraw @s {"text":"This night is a defence. Hold the fight. Do not steal their banner.","color":"gray"}
execute unless score #took rallous.session matches 1 unless entity @s[tag=rallous.session.live] if entity @e[tag=rallous.session.camp,distance=..8,limit=1] run function rallous_session:win
execute unless score #took rallous.session matches 1 unless entity @s[tag=rallous.session.live] unless entity @e[tag=rallous.session.camp,distance=..8,limit=1] run tellraw @s {"text":"Stand on the camp banner, then take the picket.","color":"gray"}
tag @s remove rallous.session.actor
scoreboard players set #took rallous.session 0
