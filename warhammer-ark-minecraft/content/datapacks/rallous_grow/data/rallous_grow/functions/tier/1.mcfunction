# First house + banner outside the 7x7 pad.
scoreboard players set @s rallous.grow_tier 1
execute unless score @s rallous.fac.tier matches 1.. run scoreboard players set @s rallous.fac.tier 1
scoreboard players set #slot rallous.grow 1
function rallous_grow:hut/by_race
function rallous_grow:voice/tier1
