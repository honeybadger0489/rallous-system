# QA 0.3.5 — read-only

Walked `content/datapacks/` and `dist/rallous-warhammer-fantasy-0.3.5.zip` (1008 entries, 2026-09-01 00:05). Did not rewrite packs, jars, or the zip. In-flight compile / Recruits bridge work was left untouched.

Runtime on the label: **Minecraft 1.20.1 + Forge 47.4.10 + Java 17**. Client is not booted in this QA.

---

## Top 5 risks for the player’s first boot

1. **Wrong JVM / loader (Java 21 or Fabric).**  
   The 0.3.5 manifest is `forge-47.4.10` / `1.20.1`. PLAY.md and `BEFORE-YOU-BEGIN.md` lock **Java 17**. Java 21 is the usual “newer” default and is documented as a break for this FG line. A Fabric profile (or dropping in a Fabric-only Continuity jar) will not load these LowCodeFML / JavaFML mods. First symptom: CurseForge import “works,” then FML dies before the title screen. Send `crash-*-fml.txt`.

2. **`#minecraft:tick` / `#minecraft:load` fire twice from the jars alone.**  
   `rallous-old-world-1.0.0.jar` already lists `rallous_warp_crash:tick`, `rallous_temple_herd:tick`, and `rallous_roaming:tick`. Those sibling jars also register the same functions. Same pattern on load (`old_world` + `contact` + `warp_crash` all pull `rallous_old_world:load` / `rallous_warp_crash:load`). First join can increment `rallous.join_wait` twice per tick and call `rallous_warp_crash:first_join` twice before `rallous.warp_landed` sticks — two scatters, two bowls, two contact assigns. The zip also ships the same packs as `overrides/datapacks/` *and* LowCodeFML jars. `rallous_session` README says jar **or** world datapack, not both. CurseForge does not auto-enable instance-root `datapacks/`, but copying them into a world (or a global-datapack mod) triples the tick.

3. **Iron’s starter book can survive the crash.**  
   Authored chests have no spellbook (old-world wreckage: bread / torch / leather / stone sword / leather armor; warp-crash relic chest: one echo shard). `rallous_old_world:crash/strip_starter_magic` exists, but `welcome` only runs it when `tag=!rallous.warp_landed`. The happy path lands `rallous_warp_crash` first (~2s), then welcome skips the strip. There is **no** `irons_spellbooks` toml in the zip. Iron’s 3.16.3 is a CurseForge file (not an override). If that jar still grants a default book, the Winds chapter (“no starter spellbook”) is a lie on minute one.

4. **Continuity-the-mod vs Rallous Continuity.**  
   The Fabric connected-textures **mod jar is not in the zip** (correct). What *is* in the zip is the lang-only resource pack `overrides/resourcepacks/Rallous Continuity`. `options.txt` already enables it. Searching CurseForge for “Continuity” and adding the Fabric mod is the boot-killer this pack was built to avoid. Leaving the **pack** off does not crash; Recruits just says Team 2 / Recruit.

5. **Recruits is still not a faction on first join.**  
   `rallous_recruits_bind:on_contact` is wired from `rallous_factions:contact/assign`. It copies the camp name, scores, and a book. Recruits 1.15.x still has no datapack API that founds a banner or sets Ally / Enemy. First boot looks like “I crashed next to Karl Franz / Mundvard and U still says Team 2” until the player Found-a-Banner by hand. That is the authored limit, not a missing function ref — but it is the first-hour “the pack is broken” report.

---

## Function refs

| Tree | Indexed `.mcfunction` | `function ns:path` refs | Missing |
| --- | ---: | ---: | --- |
| `content/datapacks` (9 packs) | 705 | all resolve against content + `pack/content` + `pack/cf-overrides/datapacks` | **0** |
| 0.3.5 zip `overrides/datapacks` | 705 | 1061 | **0** (within those 9 namespaces) |
| `content/DATAPACK-VALIDATE.txt` (2026-09-01 00:00:30Z) | — | 1164 | **0** (12 pack roots, pack_format 15) |

Cross-pack calls from `content/datapacks` that resolve:

- `rallous_warp_crash` → `rallous_factions:crash/on_land`, `contact/assign`, `debug/force_contact`; `rallous_contact:crash/awake`; `rallous_crater_hq:mark`
- `rallous_factions` → `rallous_diplomacy:apply_path`; `rallous_recruits_bind:on_contact` / `ally` / `war`
- `rallous_contact` → `rallous_diplomacy:apply_path`; `rallous_factions:path/sync`

Zip folder datapacks do **not** contain `rallous_old_world`. Load/tick tags still name `rallous_old_world:load` / `:tick`. Those IDs live in `overrides/mods/rallous-old-world-1.0.0.jar` (34 functions). If that jar is deleted, those tags become missing refs.

---

## Missing hooks (kit / winds)

**OK as specified — kit / winds are not called yet.**

- No `rallous_kit` namespace in `content/datapacks` or the 0.3.5 zip.
- No `function …:kit` / `…:winds` from authored mcfunctions.
- FTB `winds.snbt` is quest copy + optional `/function rallous_contact:magic/discover|colleges|…` (those files exist; they grant advancements / tellraw, they do not give a book).

Wired on first land (not missing): `contact_hook` → `rallous_factions:crash/on_land`; `store_crater` → `rallous_crater_hq:mark`; `land_go` → `rallous_contact:crash/awake`; `contact/assign` → `rallous_recruits_bind:on_contact`; session night auto-start from `rallous_session:tick`.

---

## Court (0.2.2 six-lord Reikland)

**First-join court is stripped. Leftover summon files are still in the old-world jar.**

| ID | In 0.3.5 old-world jar | Called on first join? |
| --- | --- | --- |
| `summon_lords` | refuse tellraw only | no |
| `ensure_court` | empty comment | no |
| `place_court` | no-op comment | no |
| `first_join` / `welcome` | primer + optional strip; no lord summons | yes (after warp land, or 5s fallback) |
| `lords/karl` … `lords/thorgrim` | **still `summon villager` + armor stand** (Karl + Ghal Maraz kit, etc.) | **no** caller in any `.mcfunction` |
| `crash/first_crash` → `carve_world_crater` | second blackstone / magma bowl + wreckage chest | **no** caller (orphan) |

`the_court_of_night` is a Vampire Counts **minor camp** (Mundvard, id 126): `try` / `place` / `greet` / `raid` / `contact/dispatch` all present in content and zip. That is not the Reikland tutorial court.

A Reikland **camp** can still name Karl Franz. That is the living-map picket, not the six-lord war council. Smoke check remains: no six named lords in the crater.

`overrides/customnpcs/rallous_lords/*.json` are marked leftover letter text, not first-join spawn.

---

## Continuity-the-mod jar

**Absent from 0.3.5.** Override jars are the ten `rallous_*` / `rallous-old-world` LowCodeFML jars plus `sonsoftheempire-1.1.9-forge-1.20.1.jar`. Manifest `files` (76) have no Continuity project. Overlay is `overrides/resourcepacks/Rallous Continuity/` (lang for Recruits / OPAC / Vassal / contact / bind). Do not add the Fabric connected-textures mod.

---

## Starter spellbooks

| Path | Spellbook? |
| --- | --- |
| Zip wreckage chest (`carve_world_crater`) | no |
| Zip / content `place_relic` chest | no (echo shard) |
| Authored `give @` in greet | race blades / axes, not Iron’s books |
| `strip_starter_magic` | clears Iron’s books / staves / scroll — **skipped if already `rallous.warp_landed`** |
| Iron’s jar | CF pin `irons_spellbooks-1.20.1-3.16.3.jar` — no pack toml override |

See risk 3.

---

## Java 21 / Fabric

| Check | 0.3.5 |
| --- | --- |
| Manifest loader | `forge-47.4.10` only |
| Java on PLAY.md | **17** |
| Java 21 | forbidden in `TOOLING.md` / `BEFORE-YOU-BEGIN.md` (1.20.5+ / 1.21 line) |
| Fabric loader | not in the zip |
| Dual-loader filenames | `Towns-and-Towers-1.12-Fabric+Forge.jar` (Forge-capable); ETF is the **Forge** jar despite a Fabric CF slug |
| LowCodeFML | `loaderVersion="[47,)"` — Forge 47, not Fabric / NeoForge 21 |

---

## Zip vs `content/datapacks` (informational)

Same nine authored packs in the zip folder tree. `rallous_old_world` is jar-only. Grimdark Sky, Gothic RPG Font, and Complementary Unbound are CurseForge `files` (not loose overrides); `options.txt` still names `file/Grimdark-Sky-v1-1-15.zip` and `file/Gothic RPG Font.zip` — they appear after a real CF import, not after unzipping `overrides/` alone.

Tree PLAY.md (post-0.3.5 commits) describes palisade + two Recruits soldiers. The 0.3.5 zip PLAY.md still says banner + lord picket. That is zip-vs-tree drift, not a broken function.

---

## What this QA did not change

No datapack, jar, manifest, or zip edits. Dual-tick tags, Iron’s config, and leftover `lords/*.mcfunction` are report-only so they do not collide with in-flight compile / bridge.
