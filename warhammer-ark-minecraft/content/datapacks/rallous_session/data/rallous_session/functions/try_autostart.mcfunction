# Night + contact (or a camp at your feet). Silent if already live / done.
scoreboard players set #skip rallous.session 0
execute if entity @s[tag=rallous.session.live] run scoreboard players set #skip rallous.session 1
execute if entity @s[tag=rallous.session.done] run scoreboard players set #skip rallous.session 1
execute unless score #skip rallous.session matches 1 run tag @s add rallous.session.actor
execute unless score #skip rallous.session matches 1 run function rallous_session:bind
execute unless score #skip rallous.session matches 1 if entity @e[tag=rallous.session.camp,distance=..16,limit=1] run function rallous_session:start_go
tag @s remove rallous.session.actor
scoreboard players set #skip rallous.session 0
