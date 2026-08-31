# Rallous diplomacy
Minecraft **1.20.1** datapack (`pack_format` **15**). Consumes FTB first-contact scores; persists stance on **that** nearest camp.
Reads: `rallous.path` 1 help / 2 betray / 3 join / 4 leave. `rallous.race` 1–8 (empire…khorne).
Targets within 512: `rallous_contact`, or camp lords (`rallous.lord` / `rallous_lord` / `rallous.lord_stand` / `rallous.camp_lord`).
`/function rallous_diplomacy:apply_path` — dispatch from the player's path. Per-verb: `help` / `betray` / `join` / `leave`.
Call after `rallous_contact:path/*`, or run a verb alone. FTB only sets the score until the zip agent wires this.
**help** → marker `rallous.stance` 1 (ally) + tellraw + one vanilla gift (`rallous.gifted` on the marker).
**betray** → stance 2 (hostile) + `rallous.khorne_path` (player and marker) + nearby iron-golem `AngryAt`.
**join** → stance 3 + `rallous.civ_bed` 1 (eligible) + `rallous.claimed` 1 so crater beds no longer lock.
**leave** → stance 4 (neutral). Marker also stores `rallous.path`; copies `rallous.race` only if the marker has none.
Helpers: `util/bind` `util/write_marker` `util/finish` `marker/ally|hostile|joined|neutral` `gift/give` `gift/by_race`.
Load creates the objectives + team `rallous_ally`. No `#minecraft:tick`.
Smoke: stand near a `rallous_contact` marker, then `/function rallous_diplomacy:help`.
No new mods. Source of truth: this folder. Zip agent may ingest it (jar **or** world datapack, not both).
