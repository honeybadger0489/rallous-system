# /function rallous_session:start — after contact, one village or one fight.
scoreboard players set #restart rallous.session 1
tag @s add rallous.session.actor
function rallous_session:bind
execute if entity @e[tag=rallous.session.camp,limit=1] run function rallous_session:start_go
execute unless entity @e[tag=rallous.session.camp,limit=1] run tellraw @s {"text":"No bannered camp answers you. Walk until you find a host. Then the night can begin.","color":"gray"}
tag @s remove rallous.session.actor
scoreboard players set #restart rallous.session 0
