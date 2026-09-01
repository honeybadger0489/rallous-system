# Hostile — the camp raid is the session. Adopt rallous.raid, else spawn at the picket.
scoreboard players set @s rallous.session_kind 3
tag @e[tag=rallous.session.site] remove rallous.session.site
execute as @e[tag=rallous.session.camp,limit=1] run tag @s add rallous.session.site
execute as @e[tag=rallous.raid,distance=..64] run tag @s add rallous.session.foe
execute as @e[tag=rallous.session.camp,limit=1] at @s as @e[tag=rallous.raid,distance=..64] run tag @s add rallous.session.foe
execute unless entity @e[tag=rallous.session.foe,limit=1] as @e[tag=rallous.session.camp,limit=1] at @s run function rallous_session:wave/by_race
