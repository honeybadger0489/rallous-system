# Between hosts: decay the short lock, roll the 20–40 min need, then consider one player.
execute if score $cooldown rallous.roam matches 1.. run scoreboard players remove $cooldown rallous.roam 1
execute unless score $need rallous.roam.play matches 1.. run function rallous_roaming:clock/roll_need
execute unless score $cooldown rallous.roam matches 1.. if score $need rallous.roam.play matches 1.. as @a if score @s rallous.roam.play >= $need rallous.roam.play run tag @s add rallous.roam.ready
execute unless score $cooldown rallous.roam matches 1.. as @a[tag=rallous.roam.ready,limit=1] at @s run function rallous_roaming:clock/consider
tag @a remove rallous.roam.ready
