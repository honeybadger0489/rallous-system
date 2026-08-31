# Crater origin. Prefers warp-crash markers/scores so a new wound is not a Waaagh spawn.
# Stored as $ox/$oz so the check still works after the origin chunk unloads.

execute if entity @e[tag=rallous.crater,limit=1] run tag @e[tag=rallous.crater,limit=1,sort=nearest] add rallous.roam.origin
execute unless entity @e[tag=rallous.roam.origin,limit=1] if entity @e[tag=rallous.crash.crater,limit=1] run tag @e[tag=rallous.crash.crater,limit=1] add rallous.roam.origin
execute unless entity @e[tag=rallous.roam.origin,limit=1] if entity @e[tag=rallous.crash.origin,limit=1] run tag @e[tag=rallous.crash.origin,limit=1] add rallous.roam.origin

execute as @e[tag=rallous.roam.origin,limit=1] store result score $ox rallous.roam run data get entity @s Pos[0]
execute as @e[tag=rallous.roam.origin,limit=1] store result score $oz rallous.roam run data get entity @s Pos[2]
execute if entity @e[tag=rallous.roam.origin,limit=1] run scoreboard players set $origin rallous.roam 1

# Crash agent: per-player rallous.crater_x / rallous.crater_z (first online player as world default).
execute as @p if score @s rallous.crater_x = @s rallous.crater_x run scoreboard players operation $ox rallous.roam = @s rallous.crater_x
execute as @p if score @s rallous.crater_z = @s rallous.crater_z run scoreboard players operation $oz rallous.roam = @s rallous.crater_z
execute as @p if score @s rallous.crater_x = @s rallous.crater_x run scoreboard players set $origin rallous.roam 1

# Optional published fake-player coords.
execute if score $x rallous.crash.pos = $x rallous.crash.pos run scoreboard players operation $ox rallous.roam = $x rallous.crash.pos
execute if score $z rallous.crash.pos = $z rallous.crash.pos run scoreboard players operation $oz rallous.roam = $z rallous.crash.pos
execute if score $x rallous.crash.pos = $x rallous.crash.pos run scoreboard players set $origin rallous.roam 1

# Fallback: first online player (crash crater is at first boots).
execute unless score $origin rallous.roam matches 1 as @p store result score $ox rallous.roam run data get entity @s Pos[0]
execute unless score $origin rallous.roam matches 1 as @p store result score $oz rallous.roam run data get entity @s Pos[2]
execute unless score $origin rallous.roam matches 1 if entity @p run scoreboard players set $origin rallous.roam 1
execute unless entity @e[tag=rallous.roam.origin,limit=1] if score $origin rallous.roam matches 1 at @p run summon minecraft:marker ~ ~ ~ {Tags:["rallous.roam.origin"],CustomName:'{"text":"Roaming origin"}'}
