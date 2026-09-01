# Hook for session:win after rallous.session 1. Tick is a backup.
# Call as the winning player: /function rallous_grow:on_session
# Idempotent: grow_sess 1 skips a second credit.
execute unless score @s rallous.grow_sess matches 1 run function rallous_grow:credit/session
