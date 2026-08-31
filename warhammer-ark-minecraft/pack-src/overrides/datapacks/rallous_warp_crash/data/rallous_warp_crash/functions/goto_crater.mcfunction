tag @s add rallous.goto
execute as @e[type=minecraft:marker,tag=rallous.crater] if score @s rallous.pid = @a[tag=rallous.goto,limit=1] rallous.pid at @s run tp @a[tag=rallous.goto,limit=1] ~ ~ ~
tag @s remove rallous.goto
