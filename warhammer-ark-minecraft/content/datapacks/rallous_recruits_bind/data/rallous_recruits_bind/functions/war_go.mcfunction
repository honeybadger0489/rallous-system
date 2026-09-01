# Camp is tagged. Scores only — Recruits Enemy is the U Diplomacy GUI.
scoreboard players set @s rallous.rec.rel 2
data modify storage rallous_recruits_bind:contact rel set value 2
tag @s add rallous.rec.war
tag @s remove rallous.rec.ally
tag @e[tag=rallous.rec.camp,limit=1] add rallous.rec.war
tag @e[tag=rallous.rec.camp,limit=1] remove rallous.rec.ally
execute as @e[type=#rallous_recruits_bind:levy,distance=..64] run tag @s add rallous.rec.war
tellraw @s [{"text":"Scores mark ","color":"red"},{"nbt":"name","storage":"rallous_recruits_bind:contact","color":"white"},{"text":" Enemy (war). Recruits will not take this as a declaration.","color":"red"}]
tellraw @s {"translate":"rallous_recruits_bind.tellraw.war_gui","fallback":"Open this GUI to make Recruits Enemy: Options → Controls → Hosts of the Old World → Open Elector / Waaagh / Under-Empire Screen (default U) → Diplomacy → Enemy. Found a Banner first, named as the crash-camp host.","color":"gold"}
# Recruits admin (op 2) only works after TWO Recruits banners already exist:
# /recruits admin diplomacyManager setRelations <A> <B> Enemy
