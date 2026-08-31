# rallous_warp_crash load — scoreboards + storage. Do not wipe stored craters.
scoreboard objectives add rallous.pid dummy
scoreboard objectives add rallous.slot dummy
scoreboard objectives add rallous.ring dummy
scoreboard objectives add rallous.crater_x dummy
scoreboard objectives add rallous.crater_y dummy
scoreboard objectives add rallous.crater_z dummy
scoreboard objectives add rallous.has_crater dummy
scoreboard objectives add rallous.civ_bed dummy
scoreboard objectives add rallous.wc_deaths deathCount
scoreboard objectives add rallous.wc_seen dummy
scoreboard objectives add rallous.join_wait dummy
scoreboard objectives add rallous.contact dummy
scoreboard objectives add rallous.claimed dummy
scoreboard objectives add rallous.retry dummy
scoreboard objectives add rallous.const dummy

scoreboard players set #12 rallous.const 12
execute unless score #next rallous.pid = #next rallous.pid run scoreboard players set #next rallous.pid 0
execute unless score #next rallous.slot = #next rallous.slot run scoreboard players set #next rallous.slot 0
execute unless data storage rallous_warp_crash:data craters run data modify storage rallous_warp_crash:data craters set value []
