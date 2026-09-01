# Camp is tagged. Name it, book the Controls path, then ally/war from stance.
function rallous_recruits_bind:announce
function rallous_recruits_bind:give_book
# Stance on the camp marker: help/joined → ally scores; hostile/war → war scores.
execute if score @s rallous.rec.stance matches 1 run function rallous_recruits_bind:ally
execute if score @s rallous.rec.stance matches 5 run function rallous_recruits_bind:ally
execute if score @s rallous.rec.stance matches 3 run function rallous_recruits_bind:war
execute if score @s rallous.rec.stance matches 6 run function rallous_recruits_bind:war
execute if score @s rallous.rec.stance matches 2 run tellraw @s {"translate":"rallous_recruits_bind.tellraw.prove","fallback":"This camp is prove-yourself. Scores name their host. Recruits Ally waits for the U Diplomacy screen after you prove it.","color":"yellow"}
execute if score @s rallous.rec.stance matches 4 run tellraw @s {"translate":"rallous_recruits_bind.tellraw.daemon","fallback":"This camp is daemon-suspicion. Scores name their host. Recruits will not treat you as Ally until the U Diplomacy screen.","color":"dark_purple"}
