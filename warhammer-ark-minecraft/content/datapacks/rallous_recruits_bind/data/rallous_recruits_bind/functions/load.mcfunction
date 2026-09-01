# Recruits bind scores. Recruits configs / later addons can read these.
# rallous.rec.id = compiled camp rallous.fac.id (1..129)
# rallous.rec.race = rallous.fac.race (1 empire .. 8 khorne)
# rallous.fac.stance on the camp: 1 help / 2 prove / 3 hostile / 4 daemon / 5 joined / 6 war
# rallous.rec.stance mirrors that camp
# rallous.rec.rel 0 unbound / 1 ally (help or joined) / 2 war (hostile or betray-war)
# rallous.rec.book 1 after the Controls book is given
# storage rallous_recruits_bind:contact {id,name,slug,lord,race,stance,rel}
scoreboard objectives add rallous.rec.id dummy
scoreboard objectives add rallous.rec.race dummy
scoreboard objectives add rallous.rec.stance dummy
scoreboard objectives add rallous.rec.rel dummy
scoreboard objectives add rallous.rec.book dummy
scoreboard objectives add rallous.contact_id dummy
scoreboard objectives add rallous.fac.id dummy
scoreboard objectives add rallous.fac.race dummy
scoreboard objectives add rallous.fac.stance dummy
scoreboard objectives add rallous.contact dummy
scoreboard objectives add rallous.rec.tries dummy
scoreboard players set #ally rallous.rec.rel 1
scoreboard players set #war rallous.rec.rel 2
