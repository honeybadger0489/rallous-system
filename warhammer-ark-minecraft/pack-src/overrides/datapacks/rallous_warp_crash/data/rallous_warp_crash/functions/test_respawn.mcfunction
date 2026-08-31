# /function rallous_warp_crash:test_respawn — run death rules without dying.
function rallous_warp_crash:on_death
tellraw @s [{"text":"test_respawn: crater unless rallous.civ_bed is set.","color":"light_purple"}]
