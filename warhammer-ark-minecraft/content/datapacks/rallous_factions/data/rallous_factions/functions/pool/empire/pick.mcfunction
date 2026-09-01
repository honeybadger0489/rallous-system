# Mix majors+minors until every major of this race is placed.
execute unless score $mix_only rallous.gen matches 1 run scoreboard players set $need_biome rallous.gen 1
execute if score $mix_only rallous.gen matches 1 run scoreboard players set $need_biome rallous.gen 0
execute store result score $rng rallous.rng run data get entity @s UUID[0]
function rallous_factions:abs_rng
scoreboard players operation $mix rallous.rng = $rng rallous.rng
scoreboard players operation $mix rallous.rng %= #2 rallous.const
execute if score #left_maj_empire rallous.gen matches 1.. if score $mix rallous.rng matches 0 run function rallous_factions:pool/empire/pick_major
execute if score #left_maj_empire rallous.gen matches 1.. if score $mix rallous.rng matches 1 run function rallous_factions:pool/empire/pick_minor
execute if score #left_maj_empire rallous.gen matches 0 run function rallous_factions:pool/empire/pick_minor
scoreboard players set $need_biome rallous.gen 0
execute if score $done rallous.gen matches 0 if score #left_maj_empire rallous.gen matches 1.. run function rallous_factions:pool/empire/pick_major
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/empire/pick_minor
execute if score $done rallous.gen matches 0 if score #left_maj_empire rallous.gen matches 1.. run function rallous_factions:pool/empire/pick_major
