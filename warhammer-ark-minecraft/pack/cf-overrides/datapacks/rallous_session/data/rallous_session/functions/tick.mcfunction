# Live night: age, clear-win, hostile picket hold. Night + contact auto-starts once.
scoreboard players add @a[tag=rallous.session.live] rallous.session_age 1
execute store result score #tod rallous.session run time query daytime
execute if score #tod rallous.session matches 13000..23000 as @a[tag=!rallous.session.live,tag=!rallous.session.done] at @s if score @s rallous.contact matches 1 run function rallous_session:try_autostart
execute if score #tod rallous.session matches 13000..23000 as @a[tag=!rallous.session.live,tag=!rallous.session.done] at @s unless score @s rallous.contact matches 1 if entity @e[tag=rallous.camp,distance=..16,limit=1] run function rallous_session:try_autostart
execute as @a[tag=rallous.session.live,scores={rallous.session_age=40..}] at @s unless entity @e[tag=rallous.session.foe,distance=..128] run function rallous_session:win
execute as @a[tag=rallous.session.live,scores={rallous.session_kind=3}] at @s if entity @e[tag=rallous.session.camp,distance=..4,limit=1] run scoreboard players add @s rallous.session_hold 1
execute as @a[tag=rallous.session.live,scores={rallous.session_kind=3}] at @s unless entity @e[tag=rallous.session.camp,distance=..4,limit=1] run scoreboard players set @s rallous.session_hold 0
execute as @a[tag=rallous.session.live,scores={rallous.session_kind=3,rallous.session_hold=60..}] run function rallous_session:win
