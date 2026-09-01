# Function driver: crash / on_land / greet / rings / levy / paths / roaming / death.
# Run at a surface. No CurseForge GPU. Does not claim SHIP_READY.
say [rallous.proof] start field driver
function rallous_factions:gen/boot
execute unless entity @e[tag=rallous.camp,distance=..48,limit=1] run function rallous_factions:gen/place_near
function rallous_factions:gen/place_rings
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute store result score $proof_camps rallous.gen if entity @e[tag=rallous.camp]
execute store result score $proof_lords rallous.gen if entity @e[tag=rallous.lord]
execute store result score $proof_soldiers rallous.gen if entity @e[tag=rallous.soldier]
execute store result score $proof_levy rallous.gen if entity @e[tag=rallous.host.levy]
scoreboard players operation $proof_placed rallous.gen = #placed rallous.gen
function rallous_factions:debug/count_races
function rallous_factions:debug/prove_bite
function rallous_factions:contact/assign
function rallous_factions:path/offer
function rallous_contact:path/help
function rallous_factions:path/burn_welcome
function rallous_roaming:events/waaagh
function rallous_warp_crash:on_death
function rallous_warp_crash:debug/prove_slots
tellraw @a [{"text":"[rallous.proof] camps=","color":"gold"},{"score":{"name":"$proof_camps","objective":"rallous.gen"}},{"text":" lords=","color":"gold"},{"score":{"name":"$proof_lords","objective":"rallous.gen"}},{"text":" soldiers=","color":"gold"},{"score":{"name":"$proof_soldiers","objective":"rallous.gen"}},{"text":" levy=","color":"gold"},{"score":{"name":"$proof_levy","objective":"rallous.gen"}},{"text":" placed=","color":"gold"},{"score":{"name":"$proof_placed","objective":"rallous.gen"}}]
execute unless score $proof_camps rallous.gen matches 2.. run say [rallous.proof] FAIL camps < 2
execute unless score $proof_lords rallous.gen matches 1.. run say [rallous.proof] FAIL no named lord
execute unless score $proof_soldiers rallous.gen matches 1.. run say [rallous.proof] FAIL no soldiers
execute if score $proof_camps rallous.gen matches 2.. if score $proof_lords rallous.gen matches 1.. if score $proof_soldiers rallous.gen matches 1.. run say [rallous.proof] OK field has lord + host + mixed camps
say [rallous.proof] done
