# FULL-REVIEW — player zip 0.3.11

Audited `dist/rallous-warhammer-fantasy-0.3.11.zip` (24 819 594 bytes, 212 files, 2026-09-01 01:34) against the locked-goal list, conversation extras, `PLAY.md`, `wiki/`, `HANDOFF.md`, `FORKS.md`, `PURPOSE.md`, `content/HONESTY-0.3.10.md`, and `content/SERVER-SMOKE-0.3.10.md` / `0.3.9`.

**Zip under review:** newest `dist/rallous-warhammer-fantasy-0.3.*.zip` = **0.3.11** (newer than 0.3.10).

**What this is not:** a client GUI boot, a two-hour `wiki/TEST.md` play, or a dedicated-server smoke of **this** zip. 0.3.10 dedicated smoke passed. **0.3.11 is unsmoked.** Client TEST was **not run**.

**Verdict grades:** `IN ZIP` = authored payload is in the player zip (as functions/jars/config). `IN REPO ONLY` = on `cursor/warhammer-ark-minecraft-d8d1`, not in the zip. `MISSING` = neither zip nor a usable branch copy. `OVERSOLD` = zip has a thinner thing than the player-facing sentence.

Client-unverified items can still be `IN ZIP` as authored. That does **not** make them play-proven.

---

## Locked goals

| # | Item | Grade | Evidence |
| --- | --- | --- | --- |
| 1 | CurseForge zip 1.20.1 Forge Java 17 | **IN ZIP** | `manifest.json` version `0.3.11`, `minecraft.version` **1.20.1**, loader `forge-47.4.10`, **76** `files[]`. PLAY / Install require Java **17**. Java itself is not inside the zip (runtime). |
| 2 | Warp-crash crater, persist, death crater or claimed bed | **IN ZIP** (copy **OVERSOLD** on “any bed” and wreckage loot) | `rallous_warp_crash` jar: blackstone / crying-obsidian bowl (`build_crater`), `store_crater` (scores + marker + storage + forceload), `on_death` → `goto_crater` unless `rallous.civ_bed`. Join-path sets civ_bed. **Wilderness beds do not stick** (`keep_crater_spawn` while `civ_bed=0`; `on_sleep` only claims if a villager / claimed village is near). PLAY/TEST “Place a bed. Sleep. Die. Respawn at the bed” oversells that. Primary wreckage is `place_relic` (**echo shard**, not bread/leather/stone). Bread/leather/stone lives on the **old-world fallback** carve, which first-join does not use. |
| 3 | Up to 12 players scatter different craters | **IN ZIP** | `assign_ids` unique pid + slot `0–11`; `scatter` 12 ring-0 `spreadplayers` + ring-1 if more than 12. `after_scatter` rejects another landed player within 900. Demo: `rallous_old_world:crash/demo_friend_elsewhere`. **12-player live test not run.** |
| 4 | First contact reacting faction (help / hostile / prove / daemon-suspicion) | **IN ZIP** | Compiled greet functions (e.g. Reikland help-blade, Hexoatl daemon-suspicion, Grimgor prove). Stance 1 gift / 2 prove / 3+6 raid / 4 daemon line. Race JSON `warp_stranger_stance`. **Chat not heard in a client.** |
| 5 | Help/betray/join/leave changes THAT camp | **IN ZIP** | FTB Paths → `rallous_contact:path/*` → `rallous_diplomacy:apply_path` binds **nearest** camp (512). `rallous_factions:path/sync` applies to the camp whose `rallous.fac.id` = player `rallous.contact_id`. Not global race. **Quest click not exercised.** |
| 6 | Magic not in hotbar; findable path | **IN ZIP** | `rallous_winds` pulse strips Iron’s books once after `warp_landed`. Lectern letters + rare `common_ink`. No filled-spellbook give. Relic chest is not a book. Iron’s **own** starter book is still a residual risk (HONESTY). **Hotbar not seen in a client.** |
| 7 | No v1 ending | **IN ZIP** | FTB groups: The Warp-Crash, Side Paths, Smoke, Temple and Herd. No Act V / NG+ / “you won.” `data.snbt` `progression_mode: flexible`. |
| 8 | Optional army UI; body on the field | **IN ZIP** | Host chapter `group: Side Paths`, quests `optional: true`. Recruits is the body (hire / **R** orders). Steve/villager + SoTE kits. No TW models. |
| 9 | V1 races only as full citizens: Empire, VC, Lizardmen, Beastmen, Greenskins, Dwarfs, Skaven, Khorne | **IN ZIP** (leftover **Kislev/court chrome**) | Eight race JSON + eight faction folders only. `compiled_index` those eight. **Not** High Elves / Bretonnia / Cathay / Chaos undivided as races. Leftover: old-world advancements `kislev` / `reikland` / unused `lords/*.mcfunction`; CustomNPC letters (`katarin`, `karl`, `spawn: NOT first-join`). Kislev ice is a **Winds letter**, not a citizen race. |
| 10 | Faction gen: major/minor pools, mix, majors exhausted → minors only, lords from templates | **IN ZIP** | Jar `compiled_index.json`: 129 / 42 major / 87 minor; caps 16 / 40. Pool pick templates mix then minor-only. Lords from JSON templates (greet names Karl Franz *as Reikland contact*, not a six-lord court). Source JSON also copied under `overrides/content/factions/` (vanilla cannot read it; runtime is the jar). |
| 11 | Mid-game Waaagh / herd / Khorne | **IN ZIP** | `rallous_roaming` clock 60s; natural spawn gated day ≥ 1 **or** 128 from crater; 25% roll. Force: `rallous_old_world:force_roaming`. Recruits `recruitPatrol tiny`, not a TW army. |
| 12 | Crater HQ hook (not full custom faction) | **IN ZIP** | `store_crater` → `rallous_crater_hq:mark` → oak fence + white banner + `rallous.hq` marker. Hook only. |
| 13 | LM/BM Ark framing (honest if tame is global) | **IN ZIP** | `rallous_temple_herd` + wiki/Beasts.md: LM extras **global**, Fossils no per-faction tame, Worse Hands flavour, no hidden penalty. Not Ark. |
| 14 | No Karl Franz six-lord court on first join | **IN ZIP** | `summon_lords` refuse tellraw. `ensure_court` empty. first_join does not call court. Unused `lords/karl`… still **inside** the old-world jar. |
| 15 | No Fabric Continuity jar, no guns/40k | **IN ZIP** | No Continuity `.jar`, no TaCZ / 40k / bolter / MineColonies in zip or `files[]`. Catalog `mods.json` still lists TaCZ / 40k as **not default**. |
| 16 | Grimdark packs + Unbound in options | **IN ZIP** | `options.txt` enables Faithful, Fresh Animations, Grimdark Battlepack (bundled zip), Grimdark Sky, Gothic RPG Font, Rallous Temple Herd, **Rallous Continuity last**. `optionsshaders.txt` `shaderPack=ComplementaryUnbound_r5.8.1.zip`. Sky / font / Unbound are **CF downloads**, not override zips. Battlepack is bundled. |
| 17 | PLAY.md + wiki + TEST.md | **IN ZIP** | `overrides/PLAY.md` + `overrides/wiki/` (Home, Install, TEST, Recruits, Factions, Diplomacy, Magic, Beasts, Villages, Crash-and-death, Roaming, Commands, README, `_sidebar`). |
| 18 | Recruits bridge `createTeam` in the zip jar | **IN ZIP** | `overrides/mods/rallous-recruits-bridge-1.0.0.jar` (12 754 B, 01:29). `javap` HostFounder: `FactionEvents.createTeam:(Z LServerPlayer; LServerLevel; String; String; String; ItemStack; ChatFormatting; B)V`. Fail tag `rallous.rec.bridge_fail`. Recruits optional. **U-screen never clicked.** |
| 19 | Session fight + camp grow | **IN ZIP** | `rallous_session:start` / `:win`; named vanilla waves. `win` → `rallous_grow:on_session`. Grow: 1–3 oak/cobble huts **outside** the 7×7. Not MineColonies, not the Millénaire mod. |
| 20 | Greet kits | **IN ZIP** | `rallous_kit:on_greet` from assign / first_contact. Race 1–8; Empire SoTE State Trooper + vanilla fallback; `rallous.kitted` once. |
| 21 | Join guards / no double scatter | **IN ZIP** | `rallous.joined` / `rallous.warp_landed` / `rallous.contacted` / `rallous.kitted`. first_join refuses if already joined. Death never re-scatters. land_go_do sets landed **before** carve. |
| 22 | Server smoke evidence vs client unverified | **IN REPO ONLY** (0.3.10 smoke) / **MISSING** (0.3.11 smoke) / client **unverified** | Repo: `content/SERVER-SMOKE-0.3.10.md` — dedicated **Done (1.918s)**, 0 `ModLoadingException`, 0 `Failed to load function`, on the **0.3.10** jars. Zip wiki honestly says **0.3.11 is unsmoked**. Client TEST.md checkboxes are all empty. Smoke logs are **not** in the player zip (correct). |

---

## Conversation extras

| Extra | Grade | Evidence |
| --- | --- | --- |
| Millénaire-style growth (huts, not MineColonies in default zip) | **IN ZIP** | `rallous_grow` 4×4 oak/cobble boxes + banners, cap 3. MineColonies absent. PLAY says Millénaire-*style credit*, not the mod. |
| Wiki for friends | **IN ZIP** | Full `overrides/wiki/` set. PLAY links Home + TEST. |
| HANDOFF / PURPOSE / FORKS for next agent | **IN REPO ONLY** | Root `HANDOFF.md`, `PURPOSE.md`, `FORKS.md`. Not in the player zip (correct — agent docs). |
| Honest copy (not “TW cities”) | **IN ZIP** with leftover **OVERSOLD** | Home/PLAY/TEST honesty cuts shipped. Still: `wiki/Factions.md` “never Team 2”; table “Settled cities / Temple-cities”; `wiki/Villages.md` still says **0.3.9** zip; PLAY smoke “bread / leather / stone” vs echo-shard relic. |
| First-hour Old World voice | **IN ZIP** | 0.3.11 `land_go_do` director tellraw: *“You crashed. The crater is yours until you sleep under a village roof…”* + title **Cast from the Warp**. Greet lines are compiled lord voice. Not branch-only. |

---

## What is actually in the zip (inventory)

| Kind | Fact |
| --- | --- |
| Manifest | `0.3.11`, MC 1.20.1, Forge 47.4.10, 76 CF files |
| Rallous jars (14) | `rallous-old-world`, `rallous-recruits-bridge`, `rallous_contact`, `rallous_crater_hq`, `rallous_diplomacy`, `rallous_factions`, `rallous_grow`, `rallous_kit`, `rallous_recruits_bind`, `rallous_roaming`, `rallous_session`, `rallous_temple_herd`, `rallous_warp_crash`, `rallous_winds` |
| Other override jar | `sonsoftheempire-1.1.9-forge-1.20.1.jar` |
| Folder datapacks | **none** (jars only — no double `#minecraft:tick`) |
| Fabric Continuity / MineColonies / TaCZ / 40k | **absent** |
| Recruits/Fossils leftover IDs (0.3.11) | levy tag `recruits:patrol_leader`; loyal_beast `fossil:egg_item_triceratops` |
| Smoke reports / HONESTY / HANDOFF | **not in zip** |

---

## 0.3.12 ingest (on branch / stale in zip — do not rebuild unless asked)

No critical missing jar that can be copied in 10 minutes. The 0.3.11 zip already has the rebuilt bridge and the 14 Rallous jars.

If a later goal rebuilds **0.3.12**, ingest these **docs/copy** fixes (same files on branch today — fix then `integrate-overrides.py --version 0.3.12`):

1. `wiki/Villages.md` + `pack/cf-overrides/wiki/Villages.md` — replace “0.3.9 zip” with **0.3.12** (or “this zip”).
2. `wiki/Factions.md` — drop “never Team 2” as a fact; say bind chat names the camp, **U** may still say Team 2 (same honesty as Recruits.md).
3. `PLAY.md` + `wiki/TEST.md` — wreckage: primary chest is the **Warp-tainted relic** (echo shard). Bread/leather/stone is the old-world **fallback** carve, not `rallous_warp_crash:place_relic`. Death: **claimed village / join civ-bed**, not any wilderness bed.
4. `content/mods/rallous-recruits-bridge-1.0.0.jar` is **stale** (11 563 B vs zip 12 754 B). Integrator picks newest mtime, so 0.3.11 is fine; copy `mods/rallous-recruits-bridge/build/libs/rallous-recruits-bridge-1.0.0.jar` over `content/mods/` so a future search cannot prefer the old file by accident.
5. Do **not** ingest HANDOFF / PURPOSE / FORKS / HONESTY / SERVER-SMOKE into the player zip.
6. After ingest: dedicated-server smoke **this** zip (0.3.10 evidence does not cover 0.3.11/0.3.12). Then a human runs `wiki/TEST.md` on a client.

---

## Why this is not ship-ready

Locked goals **1–21** are present in the zip as authored datapack/Java/config. That is not the same as play-proven.

Goal **22** fails the “IN ZIP” bar: 0.3.11 has **no** dedicated-server smoke; 0.3.10 smoke lives in the **repo**; client TEST was **not run**.

User rule: if client play is unverified, do not ship.

SHIP_READY: no
WHY: client TEST not run
