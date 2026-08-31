# Re-apply crater spawnpoint from the player's pid-matched marker.
tag @s add rallous.spawn_owner
execute as @e[type=minecraft:marker,tag=rallous.crater] if score @s rallous.pid = @a[tag=rallous.spawn_owner,limit=1] rallous.pid at @s run spawnpoint @a[tag=rallous.spawn_owner,limit=1] ~ ~ ~
tag @s remove rallous.spawn_owner
