# Slot centers on a 12-gon. Ring 0 radius 4200 so after spread (80/200)
# adjacent landings stay >900 apart. Ring 1 radius 6800.
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 0 run spreadplayers 4200 0 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 1 run spreadplayers 3637 2100 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 2 run spreadplayers 2100 3637 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 3 run spreadplayers 0 4200 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 4 run spreadplayers -2100 3637 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 5 run spreadplayers -3637 2100 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 6 run spreadplayers -4200 0 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 7 run spreadplayers -3637 -2100 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 8 run spreadplayers -2100 -3637 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 9 run spreadplayers 0 -4200 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 10 run spreadplayers 2100 -3637 80 200 false @s
execute if score @s rallous.ring matches 0 if score @s rallous.slot matches 11 run spreadplayers 3637 -2100 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 0 run spreadplayers 6800 0 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 1 run spreadplayers 5890 3400 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 2 run spreadplayers 3400 5890 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 3 run spreadplayers 0 6800 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 4 run spreadplayers -3400 5890 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 5 run spreadplayers -5890 3400 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 6 run spreadplayers -6800 0 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 7 run spreadplayers -5890 -3400 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 8 run spreadplayers -3400 -5890 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 9 run spreadplayers 0 -6800 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 10 run spreadplayers 3400 -5890 80 200 false @s
execute if score @s rallous.ring matches 1.. if score @s rallous.slot matches 11 run spreadplayers 5890 -3400 80 200 false @s
