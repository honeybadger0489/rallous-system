# Unique pid + slot 0-11. Ring increments after the 12th player.
scoreboard players add #next rallous.pid 1
scoreboard players operation @s rallous.pid = #next rallous.pid

scoreboard players operation @s rallous.slot = #next rallous.slot
scoreboard players add #next rallous.slot 1
scoreboard players operation @s rallous.ring = @s rallous.slot
scoreboard players operation @s rallous.slot %= #12 rallous.const
scoreboard players operation @s rallous.ring /= #12 rallous.const
scoreboard players set @s rallous.retry 0
