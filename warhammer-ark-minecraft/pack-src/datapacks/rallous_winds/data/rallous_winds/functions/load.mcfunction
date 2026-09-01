# rallous_winds — lectern path to Iron's ink/scroll. No starter spellbook.
scoreboard objectives add rallous.winds dummy
scoreboard objectives add rallous.magic dummy
scoreboard objectives add rallous.kislev dummy
scoreboard objectives add rallous.fac.race dummy
execute unless score #clock rallous.winds = #clock rallous.winds run scoreboard players set #clock rallous.winds 0
