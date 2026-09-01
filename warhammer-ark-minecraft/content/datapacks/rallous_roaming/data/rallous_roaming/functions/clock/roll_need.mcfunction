# Next natural event at (max play ticks) + 24000..48000. 1.20.1: UUID modulo, not the 1.20.2 random command.
scoreboard players set $need rallous.roam.play 24000
execute store result score $rng rallous.roam run data get entity @p UUID[0]
execute if score $rng rallous.roam matches ..-1 run scoreboard players operation $rng rallous.roam *= $neg rallous.roam
scoreboard players operation $rng rallous.roam %= $24000 rallous.roam
scoreboard players operation $need rallous.roam.play += $rng rallous.roam
scoreboard players set $max rallous.roam.play 0
execute as @a run scoreboard players operation $max rallous.roam.play > @s rallous.roam.play
scoreboard players operation $need rallous.roam.play += $max rallous.roam.play
