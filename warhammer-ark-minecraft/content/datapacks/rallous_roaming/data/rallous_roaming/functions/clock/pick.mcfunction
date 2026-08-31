# Pick waaagh / herd / khorne_host from UUID % 3. Then roll the next 20–40 min window.
execute store result score $rng rallous.roam run data get entity @s UUID[3]
execute if score $rng rallous.roam matches ..-1 run scoreboard players operation $rng rallous.roam *= $neg rallous.roam
scoreboard players operation $rng rallous.roam %= $3 rallous.roam
execute if score $rng rallous.roam matches 0 run function rallous_roaming:spawn/waaagh
execute if score $rng rallous.roam matches 1 run function rallous_roaming:spawn/herd
execute if score $rng rallous.roam matches 2 run function rallous_roaming:spawn/khorne_host
function rallous_roaming:clock/roll_need
