# Once after crash. Clears a default Iron's book if the jar still handed one out.
# Does not run again, so later ink/scroll finds stay.
function rallous_old_world:crash/strip_starter_magic
tag @s add rallous.winds.stripped
