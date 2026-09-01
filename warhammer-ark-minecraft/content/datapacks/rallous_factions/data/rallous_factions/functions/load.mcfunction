# Compiled faction scoreboards. Do not wipe placed camps on /reload.
scoreboard objectives add rallous.gen dummy
scoreboard objectives add rallous.rng dummy
scoreboard objectives add rallous.used dummy
scoreboard objectives add rallous.fac.id dummy
scoreboard objectives add rallous.fac.race dummy
scoreboard objectives add rallous.fac.stance dummy
scoreboard objectives add rallous.fac.tier dummy
scoreboard objectives add rallous.contact dummy
scoreboard objectives add rallous.contact_id dummy
scoreboard objectives add rallous.path dummy
scoreboard objectives add rallous.path_seen dummy
scoreboard objectives add rallous.help dummy
scoreboard objectives add rallous.betray dummy
scoreboard objectives add rallous.join dummy
scoreboard objectives add rallous.leave dummy
scoreboard objectives add rallous.proved dummy
scoreboard objectives add rallous.race dummy
scoreboard objectives add rallous.const dummy
scoreboard objectives add rallous.burn minecraft.used:minecraft.flint_and_steel
scoreboard objectives add rallous.khorne dummy
scoreboard objectives add rallous.chaos dummy
scoreboard objectives add rallous.tries dummy
scoreboard players set #-1 rallous.const -1
scoreboard players set #2 rallous.const 2
scoreboard players set #cap rallous.const 16
scoreboard players set #xcap rallous.const 40
execute unless score #placed rallous.gen = #placed rallous.gen run scoreboard players set #placed rallous.gen 0
execute unless score #booted rallous.gen = #booted rallous.gen run scoreboard players set #booted rallous.gen 0
execute unless score #clock rallous.gen = #clock rallous.gen run scoreboard players set #clock rallous.gen 0
execute unless score #next_race rallous.gen = #next_race rallous.gen run scoreboard players set #next_race rallous.gen 0
execute unless score $mix_only rallous.gen = $mix_only rallous.gen run scoreboard players set $mix_only rallous.gen 0
scoreboard players set #n_maj_beastmen rallous.const 4
scoreboard players set #n_min_beastmen rallous.const 8
execute unless score #left_maj_beastmen rallous.gen = #left_maj_beastmen rallous.gen run scoreboard players set #left_maj_beastmen rallous.gen 4
execute unless score #left_min_beastmen rallous.gen = #left_min_beastmen rallous.gen run scoreboard players set #left_min_beastmen rallous.gen 8
scoreboard players set #n_maj_dwarfs rallous.const 6
scoreboard players set #n_min_dwarfs rallous.const 10
execute unless score #left_maj_dwarfs rallous.gen = #left_maj_dwarfs rallous.gen run scoreboard players set #left_maj_dwarfs rallous.gen 6
execute unless score #left_min_dwarfs rallous.gen = #left_min_dwarfs rallous.gen run scoreboard players set #left_min_dwarfs rallous.gen 10
scoreboard players set #n_maj_empire rallous.const 5
scoreboard players set #n_min_empire rallous.const 9
execute unless score #left_maj_empire rallous.gen = #left_maj_empire rallous.gen run scoreboard players set #left_maj_empire rallous.gen 5
execute unless score #left_min_empire rallous.gen = #left_min_empire rallous.gen run scoreboard players set #left_min_empire rallous.gen 9
scoreboard players set #n_maj_greenskins rallous.const 6
scoreboard players set #n_min_greenskins rallous.const 27
execute unless score #left_maj_greenskins rallous.gen = #left_maj_greenskins rallous.gen run scoreboard players set #left_maj_greenskins rallous.gen 6
execute unless score #left_min_greenskins rallous.gen = #left_min_greenskins rallous.gen run scoreboard players set #left_min_greenskins rallous.gen 27
scoreboard players set #n_maj_khorne rallous.const 3
scoreboard players set #n_min_khorne rallous.const 4
execute unless score #left_maj_khorne rallous.gen = #left_maj_khorne rallous.gen run scoreboard players set #left_maj_khorne rallous.gen 3
execute unless score #left_min_khorne rallous.gen = #left_min_khorne rallous.gen run scoreboard players set #left_min_khorne rallous.gen 4
scoreboard players set #n_maj_lizardmen rallous.const 7
scoreboard players set #n_min_lizardmen rallous.const 7
execute unless score #left_maj_lizardmen rallous.gen = #left_maj_lizardmen rallous.gen run scoreboard players set #left_maj_lizardmen rallous.gen 7
execute unless score #left_min_lizardmen rallous.gen = #left_min_lizardmen rallous.gen run scoreboard players set #left_min_lizardmen rallous.gen 7
scoreboard players set #n_maj_skaven rallous.const 6
scoreboard players set #n_min_skaven rallous.const 13
execute unless score #left_maj_skaven rallous.gen = #left_maj_skaven rallous.gen run scoreboard players set #left_maj_skaven rallous.gen 6
execute unless score #left_min_skaven rallous.gen = #left_min_skaven rallous.gen run scoreboard players set #left_min_skaven rallous.gen 13
scoreboard players set #n_maj_vampire_counts rallous.const 5
scoreboard players set #n_min_vampire_counts rallous.const 9
execute unless score #left_maj_vampire_counts rallous.gen = #left_maj_vampire_counts rallous.gen run scoreboard players set #left_maj_vampire_counts rallous.gen 5
execute unless score #left_min_vampire_counts rallous.gen = #left_min_vampire_counts rallous.gen run scoreboard players set #left_min_vampire_counts rallous.gen 9
