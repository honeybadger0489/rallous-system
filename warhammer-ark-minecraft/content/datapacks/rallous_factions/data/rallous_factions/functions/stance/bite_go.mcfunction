execute if entity @s[tag=rallous.bitten] run scoreboard players set $noop rallous.gen 1
execute unless entity @s[tag=rallous.bitten] run function rallous_factions:stance/bite_fire
