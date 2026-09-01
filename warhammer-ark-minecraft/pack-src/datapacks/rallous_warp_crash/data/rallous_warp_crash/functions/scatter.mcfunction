# Surface-spread onto this player's far slot. spreadDistance keeps a local gap.
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 0 run spreadplayers 3200 0 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 1 run spreadplayers 2771 1600 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 2 run spreadplayers 1600 2771 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 3 run spreadplayers 0 3200 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 4 run spreadplayers -1600 2771 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 5 run spreadplayers -2771 1600 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 6 run spreadplayers -3200 0 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 7 run spreadplayers -2771 -1600 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 8 run spreadplayers -1600 -2771 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 9 run spreadplayers 0 -3200 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 10 run spreadplayers 1600 -2771 160 480 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 11 run spreadplayers 2771 -1600 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 0 run spreadplayers 5200 0 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 1 run spreadplayers 4503 2600 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 2 run spreadplayers 2600 4503 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 3 run spreadplayers 0 5200 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 4 run spreadplayers -2600 4503 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 5 run spreadplayers -4503 2600 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 6 run spreadplayers -5200 0 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 7 run spreadplayers -4503 -2600 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 8 run spreadplayers -2600 -4503 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 9 run spreadplayers 0 -5200 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 10 run spreadplayers 2600 -4503 160 480 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 11 run spreadplayers 4503 -2600 160 480 false @s
execute at @s run function rallous_warp_crash:after_scatter
