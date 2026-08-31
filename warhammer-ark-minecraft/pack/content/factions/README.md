# Faction spawn data (V1)

Load every `races/<id>.json`, then every `factions/<race>/<slug>.json`. Do not hardcode names.

**Worldgen mix:** pick from majors *and* minors of a race. When every `tier: major` of that race already has a placed instance, further rolls for that race are **minor-only**.

**Capitals:** if `race.settlement == roaming` **or** `faction.site == roaming`, skip a capital hub — camp/herdstone/brass-host only. Settled factions get a capital on `biome_tags`.

**Attitude:** start from `starting_attitude` / `starting_standing`, then apply `race.warp_stranger_stance` (`help_with_blade` | `prove_yourself` | `hostile` | `daemon_suspicion`). The lord `offer` (`help` | `recruit` | `tribute` | `war` | `prove`) is the first-meet verb.

**Taming:** `race.taming_affinity` — lizardmen `high`, beastmen `corrupt`, others `low`. Colors and `banner` are dye/pattern ids, not meshes. Titles/names come from race pools when the lord template is dead.
