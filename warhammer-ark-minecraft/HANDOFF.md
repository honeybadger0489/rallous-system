# HANDOFF — successor agent

Read this instead of the chat. Player file is still [`PLAY.md`](PLAY.md). Do not clobber vision docs (`CAMPAIGN.md`, `FACTIONS-AND-DIPLOMACY.md`, `IP-FANTASY.md`).

**This task:** successor docs only. Do **not** rebuild or commit a new zip unless a later goal asks.

---

## Purpose

Private **Minecraft 1.20.1 + Forge 47.4.10** CurseForge import pack: a **Warp-crash** into a grimdark-fantasy Old World (Warhammer Fantasy / Total War: Warhammer tone-ref + Ark survival). You wake in a crater. A **named lord from a real table faction** is the nearest camp. Paths (help / betray / join / align-and-leave) change **that** camp. Recruits is the levy. Fossils + Tameable Beasts are the beasts. There is no Reikland tutorial court.

Public name is **Rallous**. Internal working title still says Warhammer. See [`IP-FANTASY.md`](IP-FANTASY.md) and [`PURPOSE.md`](PURPOSE.md).

---

## Locked fantasy (do not reopen)

| Lock | Meaning |
| --- | --- |
| Runtime | Java **17**, MC **1.20.1**, Forge **47.4.10**. Not NeoForge. Not 1.21. |
| First join | Warp-crash crater (blackstone / crying obsidian). Per-player spawn. Friend-elsewhere scatter. |
| Contact | Nearest compiled camp: palisade, banners, named lord from JSON, two Recruits soldiers, stance line. |
| Paths | `rallous.path` 1 help / 2 betray / 3 join / 4 leave. Stance shifts **that** contact faction only. |
| Session | One night = one village **or** one fight (`rallous_session`). Vanilla pillagers/zombies **named** as that race’s enemies. |
| Quest book | **The Warp-Crash** — Crash → Paths → First Hour → The Winds → optional Host → Temple and Herd. Smoke is a side checklist. |
| Bodies | Steve-like / villager. We did not sculpt Total War models. |
| Libraries | **76** CurseForge fileIDs from the 0.2.1 pin. `build-cf-pack.py` owns fileIDs — do not race it. |
| Continuity | **Rallous Continuity** = lang overlay (Elector / Waaagh / Under-Empire / von Carstein / Dawi / herd / temple-city / Bloodbound). **Not** the Fabric Continuity connected-textures mod. |
| Private | Do not upload the pack. Do not monetize GW identity. |

---

## v1 races

Source: `content/factions/races/*.json`. Numbers in `scripts/compile_factions.py` `RACE_NUM`:

| # | id | Settlement | Default stranger stance | Taming affinity |
| --- | --- | --- | --- | --- |
| 1 | `empire` | settled | `help_with_blade` | low |
| 2 | `vampire_counts` | settled | (JSON) | low |
| 3 | `lizardmen` | settled | `daemon_suspicion` | **high** |
| 4 | `beastmen` | roaming | (JSON) | **corrupt** |
| 5 | `greenskins` | roaming | (JSON) | low |
| 6 | `dwarfs` | settled (holds) | (JSON) | low |
| 7 | `skaven` | mixed / under-empire | (JSON) | low |
| 8 | `khorne` | roaming | (JSON) | low |

Faction files live under `content/factions/factions/<race>/<slug>.json`. About **129** compiled camps. First-days cap **16**; walking farther can place up to **40**. Never all 129 at once. After every `tier: major` of a race is placed, that race rolls **minor-only**.

Do not add High Elves, Kislev, Bretonnia, Cathay, or Chaos undivided as v1 races.

---

## Branch and PR

| | |
| --- | --- |
| Repo | `honeybadger0489/rallous-system` |
| Branch | `cursor/warhammer-ark-minecraft-d8d1` |
| PR | **#1** (DRAFT) — https://github.com/honeybadger0489/rallous-system/pull/1 |
| Base | `main` |

Work here. Do not open a second GitHub fork. A sibling Java tree (`mods/rallous-recruits-bridge/` or an MDK outside git) is allowed; a second clone that diverges is not. See [`FORKS.md`](FORKS.md) § Second workspace.

---

## Current zip version

**PLAY.md + `pack/curseforge/manifest.json` + `dist/`:** **0.3.6**

File: `warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.6.zip`

Raw: https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.6.zip

Older archives (0.2.0–0.3.5) stay in `dist/` for history. **Import 0.3.6 as a new CurseForge profile.** Do not update 0.2.1 / 0.2.2 / 0.3.0–0.3.5.

0.3.6 payload: compiled thicker camps, `rallous_session`, `rallous_recruits_bind`, **`rallous-recruits-bridge-1.0.0.jar`**, `options.txt` pack order with **Rallous Continuity** last, 76 CF files, no Fabric Continuity jar, no first-join court. If the bridge fails on boot: `crash-*-fml.txt` and fall back to U → Found a Banner.

---

## Datapack / jar map

Sibling folders under `content/datapacks/` compile or copy into `pack/cf-overrides/datapacks/` **and** LowCodeFML jars under `pack/cf-overrides/mods/`. Enable **folder or jar, not both**.

| Pack | Role | Hook |
| --- | --- | --- |
| `rallous_warp_crash` | Crater, world spawn, wreckage chest + journal, per-player spawnpoint, death→crater unless bed | After `store_crater` calls `rallous_crater_hq:mark`. `contact_hook` → `rallous_factions:crash/on_land`. |
| `rallous_old_world` | Fallback + `/function rallous_old_world:force_roaming` / `lm_bm/summon` / crash demos | Lives in `pack/content/rallous_old_world/` (jar `rallous-old-world-1.0.0.jar`). `summon_lords` is a **refuse** line — does not rebuild the 0.2.2 court. |
| `rallous_factions` | **Compiled** camps, lords, contact assign, path sync | **Do not edit mcfunctions.** Source is `content/factions/`. |
| `rallous_diplomacy` | `apply_path` from FTB help/betray/join/leave | Called by `rallous_contact:path/*` and a factions tick. |
| `rallous_contact` | First-contact path scores / FTB rewards | Path verbs call diplomacy then factions sync. |
| `rallous_session` | `/function rallous_session:start` / `:win` — one village or one fight | Needs `rallous.contact` or a nearby `rallous.camp`. |
| `rallous_recruits_bind` | Copies crash-camp **display name** onto scores / storage / book | Hooked from `rallous_factions:contact/assign`. **Does not found a RecruitsFaction.** |
| `rallous-recruits-bridge` | Java Forge jar. Calls Recruits `FactionEvents.createTeam` so U / chat say **Reikland** / **Clan Mors**, not Team 2 | Source: `mods/rallous-recruits-bridge/`. API notes: [`content/RECRUITS-API.md`](content/RECRUITS-API.md). In the 0.3.6 zip. |
| `rallous_kit` | Tier-1 levy kit after first-contact greet (`rallous_kit:on_greet`) | Race 1–8. Sets `rallous.kitted`. Folder or jar, not both. Do not edit `compile_factions.py` from here. |
| `rallous_crater_hq` | Oak fence + white banner + storage at crater | **Hook only.** Not faction gameplay. Later DLC. |
| `rallous_roaming` | Scheduled Waaagh / herd / Khorne host (no capital) | Crash-gate until day ≥ 1 or 128+ from crater. |
| `rallous_temple_herd` | Fossils / Tameable Beasts flavor (temple / herdstone) | Cannot per-race Fossils tame difficulty. |

**Resource pack:** `content/resourcepacks/Rallous Continuity/` (and pack-src / overrides copies). Lang only. `options.txt` must list it so players do not forget.

**FTB:** Warp-Crash book in overrides (`config/ftbquests/`). Chapters match PLAY.md.

---

## `compile_factions.py`

`scripts/compile_factions.py` — vanilla cannot read `content/factions/*.json` at runtime.

1. Load every `races/<id>.json`, then every `factions/<race>/<slug>.json`.
2. Write `content/datapacks/rallous_factions/` (pools, `place/<slug>`, crash contact, path-stance hooks, `compiled_index.json`).
3. Rules: mix majors + minors while a race still has unplaced majors; then minor-only. Lords from templates. First-contact stance = `race.warp_stranger_stance`. Camps are **war-host pickets** (`camp_sites.py` / `assert_camps_thick`).
4. Caps: `FIRST_CAP = 16`, `EXPLORE_CAP = 40`.

Called automatically by `integrate-overrides.py`. To compile only:

```bash
python3 warhammer-ark-minecraft/scripts/compile_factions.py
```

---

## What MUST not return

| Ban | Why |
| --- | --- |
| **Karl Franz court / six-lord first-join** | 0.2.2 `summon_lords` / `ensure_court` / `place_court` on `first_join`. Zip assert fails if those strings reappear. `/function rallous_old_world:summon_lords` is a refuse line. |
| **Fabric Continuity** (connected textures) | Fabric-leaning; kept **out** so the instance boots. Do not add a Continuity `.jar`. **Rallous Continuity** lang pack is the replacement. |
| **Guns / 40k** | No TaCZ rewards, no bolters, no Adeptus, no aquila, no “grim darkness of the far future.” Crash crater is **not** a 40k landing — that is a later DLC fork. Epic Fight + Iron’s (gated, no starter spellbook). |

Also refuse: mute village tagged “Faction Contact”; Team 1 / Team 2 as the intended host name; vanilla `/team add` as a Recruits host (Recruits intercepts this and you get Team 2).

---

## How to rebuild the zip (when asked)

Do **not** run this for docs-only work.

From `warhammer-ark-minecraft/`:

```bash
python3 scripts/compile_factions.py
python3 scripts/integrate-overrides.py --version 0.3.6
```

`integrate-overrides.py` (default `--version 0.3.6`):

1. `compile_factions()`
2. Ingest siblings: `content/factions/`, `content/datapacks/`, `content/resourcepacks/`, `pack-src/` datapacks / resourcepacks / quests / config, `options.txt` pack order, optional `rallous-recruits-bridge*.jar`
3. `apply_warp_crash()` unless `--skip-author`
4. Restore sibling FTB, `strip_court_hooks()`, rebuild LowCodeFML jars
5. Copy `PLAY.md` into overrides
6. `pack-zip.py --version …` → `dist/rallous-warhammer-fantasy-0.3.6.zip`
7. Assert: 76 CF files, Forge-only loaders, no court on join, no Continuity jar, camps / session / bind / diplomacy / crater HQ present

Does **not** resolve CurseForge fileIDs. Full pin refresh is `scripts/build-cf-pack.py` (dependency agent owns that). Zip-only from existing overrides: `python3 scripts/pack-zip.py --version 0.3.6`.

Client is **not** booted in CI. Smoke is [`PLAY.md`](PLAY.md) “One-hour smoke.” Crashes: `crash-*-fml.txt`.

---

## Read next

| File | When |
| --- | --- |
| [`PURPOSE.md`](PURPOSE.md) | Why / fantasy / success test (one page) |
| [`FORKS.md`](FORKS.md) | Decisions parked **after** this goal |
| [`PLAY.md`](PLAY.md) | Player import + smoke |
| [`content/RECRUITS-API.md`](content/RECRUITS-API.md) | Recruits `FactionEvents.createTeam` |
| [`scripts/README.md`](scripts/README.md) | Script index |
| [`content/factions/README.md`](content/factions/README.md) | JSON compile rules |
