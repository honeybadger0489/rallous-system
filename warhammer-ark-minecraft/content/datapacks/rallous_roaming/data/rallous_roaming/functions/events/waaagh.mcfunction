# FORCE: Greenhost Waaagh. Smoke-test / 1-hour QA. Skips play-time and crater gates.
# /function rallous_roaming:events/waaagh
function rallous_roaming:clear
execute as @p at @s run function rallous_roaming:spawn/waaagh
