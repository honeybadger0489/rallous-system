# as the target marker — one vanilla gift, then lock rallous.gifted.
execute as @a[tag=rallous.diplo.actor,limit=1] run function rallous_diplomacy:gift/by_race
scoreboard players set @s rallous.gifted 1
