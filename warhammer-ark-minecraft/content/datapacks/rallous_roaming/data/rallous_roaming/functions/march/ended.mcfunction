# Last host gone (killed or timed out).
tellraw @a {"text":"The roaming host scatters. The road is yours again — for now.","color":"gray","italic":true}
scoreboard players set $event rallous.roam 0
scoreboard players set $grief rallous.roam 0
