# /function rallous_roaming:debug/status
execute store result score $day rallous.roam run time query day
execute store result score $hosts rallous.roam run execute if entity @e[tag=rallous.roam.host]
tellraw @a [{"text":"rallous_roaming status","color":"gold","bold":true}]
tellraw @a [{"text":"  play ticks (nearest): ","color":"gray"},{"score":{"name":"@p","objective":"rallous.roam.play"},"color":"white"},{"text":"  need: ","color":"gray"},{"score":{"name":"$need","objective":"rallous.roam.play"},"color":"white"}]
tellraw @a [{"text":"  day: ","color":"gray"},{"score":{"name":"$day","objective":"rallous.roam"},"color":"white"},{"text":"  safe: ","color":"gray"},{"score":{"name":"$safe","objective":"rallous.roam"},"color":"white"},{"text":"  origin set: ","color":"gray"},{"score":{"name":"$origin","objective":"rallous.roam"},"color":"white"}]
tellraw @a [{"text":"  event 1=waaagh 2=herd 3=khorne: ","color":"gray"},{"score":{"name":"$event","objective":"rallous.roam"},"color":"white"},{"text":"  hosts: ","color":"gray"},{"score":{"name":"$hosts","objective":"rallous.roam"},"color":"white"}]
tellraw @a [{"text":"  cooldown clocks: ","color":"gray"},{"score":{"name":"$cooldown","objective":"rallous.roam"},"color":"white"},{"text":"  grief used: ","color":"gray"},{"score":{"name":"$grief","objective":"rallous.roam"},"color":"white"}]
tellraw @a {"text":"  force: /function rallous_roaming:events/waaagh | events/herd | events/khorne_host","color":"yellow"}
