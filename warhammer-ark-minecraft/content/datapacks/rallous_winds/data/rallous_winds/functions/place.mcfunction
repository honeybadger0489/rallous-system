# As a rallous.camp marker. One lectern + barrel loot. No spellbook.
tag @s add rallous.winds
scoreboard players set $school rallous.winds 0
execute if score @s rallous.fac.race matches 1 run scoreboard players set $school rallous.winds 1
execute if score @s rallous.fac.race matches 3 run scoreboard players set $school rallous.winds 1
execute if score @s rallous.fac.race matches 2 run scoreboard players set $school rallous.winds 3
execute if score @s rallous.fac.race matches 4 run scoreboard players set $school rallous.winds 4
execute if score @s rallous.fac.race matches 8 run scoreboard players set $school rallous.winds 4
execute if entity @s[tag=rallous.fac.nordland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.ostland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.hochland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.middenland] run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_plains run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_taiga run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_beach run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:ice_spikes run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:frozen_peaks run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_slopes run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:frozen_river run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:jagged_peaks run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.lahmian_sisterhood] run scoreboard players set $school rallous.winds 4
function rallous_winds:try_lectern
function rallous_winds:try_barrel
