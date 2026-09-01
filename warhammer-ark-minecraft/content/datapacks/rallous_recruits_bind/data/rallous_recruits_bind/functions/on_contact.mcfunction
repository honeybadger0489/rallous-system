# After rallous_factions:contact/assign. Bind Recruits to THAT compiled camp.
# Recruits 1.15.x: no create/name/hire/ally command that founds a banner from a datapack.
function rallous_recruits_bind:util/bind_camp
execute unless entity @e[tag=rallous.rec.camp,limit=1] run tellraw @s {"text":"No compiled camp in 512. Recruits stay unbound — still not Team 2.","color":"dark_gray"}
execute if entity @e[tag=rallous.rec.camp,limit=1] run function rallous_recruits_bind:on_contact_go
