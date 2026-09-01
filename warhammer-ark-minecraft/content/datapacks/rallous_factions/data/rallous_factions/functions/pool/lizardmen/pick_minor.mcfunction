# lizardmen minor pool (7)
execute store result score $rng rallous.rng run data get entity @s UUID[1]
function rallous_factions:abs_rng
scoreboard players set #n rallous.const 7
scoreboard players operation $rng rallous.rng %= #n rallous.const
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..0 unless score #sentinels_of_xeti rallous.used matches 1 run function rallous_factions:try/sentinels_of_xeti
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..1 unless score #southern_sentinels rallous.used matches 1 run function rallous_factions:try/southern_sentinels
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..2 unless score #tepoks_spawn rallous.used matches 1 run function rallous_factions:try/tepoks_spawn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..3 unless score #tlaxtlan rallous.used matches 1 run function rallous_factions:try/tlaxtlan
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..4 unless score #wardens_of_the_living_pools rallous.used matches 1 run function rallous_factions:try/wardens_of_the_living_pools
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..5 unless score #xlanhuapec rallous.used matches 1 run function rallous_factions:try/xlanhuapec
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..6 unless score #zlatlan rallous.used matches 1 run function rallous_factions:try/zlatlan
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 1.. unless score #southern_sentinels rallous.used matches 1 run function rallous_factions:try/southern_sentinels
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 2.. unless score #tepoks_spawn rallous.used matches 1 run function rallous_factions:try/tepoks_spawn
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 3.. unless score #tlaxtlan rallous.used matches 1 run function rallous_factions:try/tlaxtlan
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 4.. unless score #wardens_of_the_living_pools rallous.used matches 1 run function rallous_factions:try/wardens_of_the_living_pools
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 5.. unless score #xlanhuapec rallous.used matches 1 run function rallous_factions:try/xlanhuapec
execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches 6.. unless score #zlatlan rallous.used matches 1 run function rallous_factions:try/zlatlan
execute if score $done rallous.gen matches 0 unless score #sentinels_of_xeti rallous.used matches 1 run function rallous_factions:try/sentinels_of_xeti
