# rallous_warp_crash (MC 1.20.1, pack_format 15)
Warp-crash spawn/respawn. Up to 12 players scatter to far slots, then a sculk/obsidian crater.
Crater stored on scores rallous.crater_x/y/z + pid and storage rallous_warp_crash:data craters.
Death returns to that crater unless rallous.civ_bed is set. Same player; no second crash.
Sleep in a claimed village (villager / rallous.claimed_village / rallous.claimed) sets civ_bed.
Faction hook: armor stand tag rallous_contact. Quests call first_contact.
## /function tests
/function rallous_warp_crash:first_join
/function rallous_warp_crash:first_contact
/function rallous_warp_crash:goto_crater
/function rallous_warp_crash:claim_civ_bed
/function rallous_warp_crash:test_crater
/function rallous_warp_crash:test_camp
/function rallous_warp_crash:test_respawn
/function rallous_warp_crash:keep_crater_spawn
