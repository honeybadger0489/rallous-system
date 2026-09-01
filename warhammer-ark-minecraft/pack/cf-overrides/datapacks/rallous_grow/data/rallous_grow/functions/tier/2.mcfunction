# Second house opposite the first.
scoreboard players set @s rallous.grow_tier 2
execute unless score @s rallous.fac.tier matches 2.. run scoreboard players set @s rallous.fac.tier 2
scoreboard players set #slot rallous.grow 2
function rallous_grow:hut/by_race
function rallous_grow:voice/tier2
