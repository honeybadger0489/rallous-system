# Defend — short enemy wave at a tagged village, else the camp.
scoreboard players set @s rallous.session_kind 1
function rallous_session:pick_site
execute as @e[tag=rallous.session.site,limit=1] at @s run function rallous_session:wave/by_race
