# Hostile / betray-war stance. Mechanical: scores + storage + levy tags. Recruits Enemy is still the U Diplomacy GUI.
function rallous_recruits_bind:util/bind_camp
execute unless entity @e[tag=rallous.rec.camp,limit=1] run tellraw @s {"text":"No compiled camp in 512. War scores wait for a banner.","color":"dark_gray"}
execute if entity @e[tag=rallous.rec.camp,limit=1] run function rallous_recruits_bind:war_go
