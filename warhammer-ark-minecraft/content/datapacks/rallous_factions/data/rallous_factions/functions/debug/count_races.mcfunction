# Count rallous.camp markers by race. Fresh-world mix proof.
execute store result score $c_emp rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=1}]
execute store result score $c_vc rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=2}]
execute store result score $c_lm rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=3}]
execute store result score $c_bm rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=4}]
execute store result score $c_gs rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=5}]
execute store result score $c_dw rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=6}]
execute store result score $c_sk rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=7}]
execute store result score $c_kh rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=8}]
scoreboard players set $c_races rallous.gen 0
execute if score $c_emp rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_vc rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_lm rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_bm rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_gs rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_dw rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_sk rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_kh rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute store result score $c_lords rallous.gen if entity @e[tag=rallous.lord]
execute store result score $c_camps rallous.gen if entity @e[tag=rallous.camp]
execute store result score $c_temple rallous.gen if entity @e[tag=rallous.temple_beast]
execute store result score $c_herd rallous.gen if entity @e[tag=rallous.herd_beast]
tellraw @a [{"text":"[rallous.mix] camps=","color":"gold"},{"score":{"name":"$c_camps","objective":"rallous.gen"}},{"text":" lords=","color":"gold"},{"score":{"name":"$c_lords","objective":"rallous.gen"}},{"text":" races=","color":"gold"},{"score":{"name":"$c_races","objective":"rallous.gen"}},{"text":" emp=","color":"red"},{"score":{"name":"$c_emp","objective":"rallous.gen"}},{"text":" vc=","color":"dark_red"},{"score":{"name":"$c_vc","objective":"rallous.gen"}},{"text":" lm=","color":"aqua"},{"score":{"name":"$c_lm","objective":"rallous.gen"}},{"text":" bm=","color":"dark_green"},{"score":{"name":"$c_bm","objective":"rallous.gen"}},{"text":" gs=","color":"green"},{"score":{"name":"$c_gs","objective":"rallous.gen"}},{"text":" dw=","color":"gold"},{"score":{"name":"$c_dw","objective":"rallous.gen"}},{"text":" sk=","color":"light_purple"},{"score":{"name":"$c_sk","objective":"rallous.gen"}},{"text":" kh=","color":"dark_red"},{"score":{"name":"$c_kh","objective":"rallous.gen"}},{"text":" temple_beasts=","color":"aqua"},{"score":{"name":"$c_temple","objective":"rallous.gen"}},{"text":" herd_beasts=","color":"dark_green"},{"score":{"name":"$c_herd","objective":"rallous.gen"}}]
execute unless score $c_races rallous.gen matches 8 run say [rallous.mix] WARN unique races != 8
execute if score $c_races rallous.gen matches 8 run say [rallous.mix] OK eight races on this fresh field
execute store result score $pending rallous.gen if entity @e[tag=rallous.probe.pending]
tellraw @a [{"text":"[rallous.mix] pending_probes=","color":"gray"},{"score":{"name":"$pending","objective":"rallous.gen"}},{"text":" bite=","color":"red"},{"score":{"name":"$bite","objective":"rallous.gen"}},{"text":" raid=","color":"red"},{"score":{"name":"$raid_n","objective":"rallous.gen"}}]
