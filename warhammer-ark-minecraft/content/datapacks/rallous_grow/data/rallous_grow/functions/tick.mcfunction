# Session win, emerald spend / villager trade near a camp, then apply missing tiers.
execute as @a if score @s rallous.session matches 1 unless score @s rallous.grow_sess matches 1 at @s if entity @e[type=minecraft:marker,tag=rallous.camp,distance=..64,limit=1] run function rallous_grow:credit/session
execute as @a at @s run function rallous_grow:tick_trade
execute as @a at @s as @e[type=minecraft:marker,tag=rallous.camp,distance=..64] at @s run function rallous_grow:try_apply
