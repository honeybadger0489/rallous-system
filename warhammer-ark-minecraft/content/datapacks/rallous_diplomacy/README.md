# Rallous diplomacy
Minecraft **1.20.1** datapack (`pack_format` **15**). Consumes FTB first-contact scores; persists stance on **that** nearest camp.
Reads: `rallous.path` 1 help / 2 betray / 3 join / 4 leave. `rallous.race` 1–8 (empire…khorne).
Targets within 512: `rallous.camp` / `rallous_contact` first, else camp lords (`rallous.lord` / `rallous_lord` / `rallous.lord_stand`).
`/function rallous_diplomacy:apply_path` — dispatch from the player's path. Per-verb: `help` / `betray` / `join` / `leave`.
Call after `rallous_contact:path/*`, or run a verb alone. FTB only sets the score until the zip agent wires this.
**help** → `rallous.stance` 1 (ally) + tellraw + one vanilla gift (`rallous.gifted`). Mirrors `rallous.fac.stance` 1.
**betray** → stance 2 + `rallous.khorne_path` (player and marker) + golem `AngryAt`. Mirrors `rallous.fac.stance` 6 (war).
**join** → stance 3 + `rallous.civ_bed` 1 (eligible) + `rallous.claimed` 1. Mirrors `rallous.fac.stance` 5.
**leave** → stance 4 (neutral). Mirrors `rallous.fac.stance` 2. Marker also stores `rallous.path`.
Helpers: `util/bind` `util/write_marker` `util/finish` `marker/ally|hostile|joined|neutral` `gift/give` `gift/by_race`.
Load creates the objectives + team `rallous_ally`. No `#minecraft:tick`.
Smoke: stand near a `rallous.camp` or `rallous_contact` marker, then `/function rallous_diplomacy:help`.
Writes: `rallous.stance` `rallous.fac.stance` `rallous.khorne_path` `rallous.gifted` `rallous.civ_bed` `rallous.claimed` `rallous.diplo`.
No new mods. This folder only. Zip agent may ingest it (jar **or** world datapack, not both).
