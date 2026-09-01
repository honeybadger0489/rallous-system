# Camp is tagged. Scores only — Recruits Ally is the U Diplomacy GUI.
scoreboard players set @s rallous.rec.rel 1
data modify storage rallous_recruits_bind:contact rel set value 1
tag @s add rallous.rec.ally
tag @s remove rallous.rec.war
tag @e[tag=rallous.rec.camp,limit=1] add rallous.rec.ally
tag @e[tag=rallous.rec.camp,limit=1] remove rallous.rec.war
execute as @e[type=#rallous_recruits_bind:levy,distance=..64] run tag @s add rallous.rec.ally
tellraw @s [{"text":"Scores mark ","color":"green"},{"nbt":"name","storage":"rallous_recruits_bind:contact","color":"white"},{"text":" Ally (help). Recruits will not take this as a treaty.","color":"green"}]
tellraw @s {"translate":"rallous_recruits_bind.tellraw.ally_gui","fallback":"Open this GUI to make Recruits Ally: Options → Controls → Hosts of the Old World → Open Elector / Waaagh / Under-Empire Screen (default U) → Diplomacy → Ally. Found a Banner first, named as the crash-camp host.","color":"aqua"}
# Recruits admin (op 2) only works after TWO Recruits banners already exist:
# /recruits admin diplomacyManager setRelations <A> <B> Ally
