# Prove — same short wave. Voice differs.
scoreboard players set @s rallous.session_kind 2
function rallous_session:pick_site
execute as @e[tag=rallous.session.site,limit=1] at @s run function rallous_session:wave/by_race
