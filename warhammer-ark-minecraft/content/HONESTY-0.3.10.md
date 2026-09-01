# HONESTY-0.3.10 — zip vs player docs

Audited `dist/rallous-warhammer-fantasy-0.3.10.zip` (24 825 254 bytes, 212 files, 2026-09-01 01:13) against `PLAY.md`, `wiki/Home.md`, `wiki/TEST.md`, `wiki/Recruits.md`, `wiki/Install.md`. Client GUI was not booted. Dedicated-server smoke on this zip: **Done** (`content/SERVER-SMOKE-0.3.10.md`).

This file is the ledger. Player-facing oversells were then cut in PLAY + wiki (see § Lies corrected).

---

## What is actually in the zip

| Check | Fact |
| --- | --- |
| Manifest | `0.3.10`, Minecraft **1.20.1**, Forge **47.4.10**, **76** CurseForge `files[]` |
| Rallous jars (14) | `rallous-old-world`, `rallous-recruits-bridge-1.0.0.jar`, `rallous_contact`, `rallous_crater_hq`, `rallous_diplomacy`, `rallous_factions`, **`rallous_grow`**, **`rallous_kit`**, `rallous_recruits_bind`, `rallous_roaming`, **`rallous_session`**, `rallous_temple_herd`, `rallous_warp_crash`, **`rallous_winds`** |
| Other override jar | `sonsoftheempire-1.1.9-forge-1.20.1.jar` |
| Folder datapacks | **none** (jars only) |
| Fabric Continuity `.jar` | **absent** |
| MineColonies | **absent** |
| First-join court | **not called**. `summon_lords` is a refuse tellraw. `ensure_court` / `place_court` are empty / no-op. `customnpcs/rallous_lords/*.json` are leftover letter text (`spawn: NOT first-join`). Old-world jar still *contains* unused `lords/karl`…`thorgrim` summon files. |
| `options.txt` pack order | Last enabled: **Rallous Continuity** (lang overlay). Also lists Faithful / Fresh Animations / Grimdark Battlepack / Grimdark Sky / Gothic RPG Font / Rallous Temple Herd. |
| Resource packs on disk | Faithful 32x zip, Fresh Animations zip, Grimdark Battlepack zip, **Rallous Continuity/** (lang only), **Rallous Temple Herd/** (lang only). Grimdark Sky / Gothic Font / Complementary Unbound are **CurseForge files**, not override zips. |
| Wiki in zip | Home, Install, TEST, Recruits, plus the rest of `overrides/wiki/` |
| Grow | 7×7 picket + up to **three** oak/cobble huts (east / west / south) + one nitwit “Outpost Settler”. Cap 3. Not a city. |
| Session | `/function rallous_session:start` / `:win`; vanilla pillagers/zombies named as race enemies; night auto-start once. |
| Kit | `rallous_kit:on_greet` race levy (SoTE State Trooper for Empire; vanilla stand-ins for the other seven). |
| Winds | Lectern letter + rare common ink. **No** filled spellbook functions. |
| Bridge | Java jar present. Calls Recruits `FactionEvents.createTeam(false, …)` after assign. **In-game U inspect was not clicked.** Fail tag is `rallous.rec.bridge_fail`. |

`modlist.html` inside the zip still titles itself **“Rallous Warhammer Fantasy 0.3.9”** while `manifest.json` is **0.3.10**. Stale chrome, not a second pack.

Zip `wiki/Install.md` still named **0.3.7** as the older pin and had **no** dedicated-server smoke line (repo wiki was ahead of the zip). Repo `wiki/Home.md` / `wiki/Install.md` already said smoke **passed on 0.3.10** before this audit.

---

## PLAY.md

| Claim | Verdict | Why |
| --- | --- | --- |
| Import **0.3.10** as a new profile; do not update 0.2.x–0.3.9 | **true** | Manifest + HANDOFF. |
| Java 17, ~8 GB, MC 1.20.1, Forge 47.4.10 | **true** | Manifest loaders. |
| Rallous Continuity on in `options.txt`, last, lang only, **not** Fabric Continuity | **true** | `options.txt` + pack is `assets/*/lang/en_us.json` only. No Continuity `.jar`. |
| If packs reset, Recruits still says Team 2 | **oversold** | Continuity remaps Recruit → Levy / Elector. **Team 2** is a Recruits *host name*. Lang off ≠ host name. Bridge or **U → Found a Banner** names the host. |
| Quest book **The Warp-Crash** (Crash → Paths → First Hour → The Winds → optional Host → Temple and Herd); Smoke side; no Reikland tutorial court | **true** | FTB chapters in zip. First-join does not call court. |
| Warp-crash crater; no Karl Franz war council | **true** | `rallous_warp_crash` + old-world first_join is welcome only. |
| Nearest camp: palisade, banners, campfires, site props, lord villager, two Recruits soldiers, stance | **true** (as authored) | Compiled `rallous_factions` pickets. These are **7×7** pads, not cities. |
| Second player crashes elsewhere | **true** (as authored) | Scatter functions in old-world + warp-crash. |
| Zip **includes** `rallous-recruits-bridge-1.0.0.jar`; founds/renames after assign; fallback **U** if bridge fails | **true** (jar) / **oversold** (certainty) | Jar is in the zip. Play-time founding is unclicked. PLAY already had the fallback — keep it. |
| Session night = named vanilla pillagers/zombies, not Recruits battle, not a Total War city fight | **true** | `rallous_session` wave files. |
| Camps are war-host pickets, not Total War cities; 16 / 40 / never 129 | **true** | Caps in `compile_factions.py`. |
| Client not booted in CI | **true** | |
| Authored list: crash, scatter, death, factions, diplomacy, session, bind, kit, grow, book, Continuity, force functions, sibling jars, court strip | **true** | All those jars are in `overrides/mods/`. |
| Grow is a “Millénaire loop” and the 7×7 “gains huts” | **oversold** | Credit loop is real (session / help / emeralds, cap 3). **Millénaire the mod is not in the zip.** Huts are 4×4 oak/cobble boxes + banners, not a Millénaire village. |
| Borrowed engines (Recruits, Iron’s, Fossils, Tameable Beasts, Epic Fight, Terralith, Towns and Towers, LSO, FTB, SoTE, Faithful, grim packs, Complementary) | **true** | Manifest + overrides. Towns and Towers is **other people’s** villages, not our camps. |
| We did not sculpt Total War models; bodies Steve/villager | **true** | |
| 76 CF fileIDs; Fabric Continuity out | **true** | |
| Smoke: chat names Reikland / Clan Mors, **never Team 2** | **oversold** | Bind tellraws the compiled name. Recruits **U** can still say Team 2 if the bridge misses. |
| Keys: `M` = Towns | **oversold** | `options.txt` binds `key.xaero_worldmap` to **M**. That is Xaero’s map, not a town UI. |
| Keys: `R` = Host Command until later | **true as intent** | Recruits default **R**. `options.txt` also binds Iron’s spell wheel to **R**. First-hour conflict is real; PLAY already says the wheel waits. |
| Winds: no crater spellbook; lectern letter; rare common ink; no filled book in barrel | **true** (as authored) | `rallous_winds` has no `/give` of a filled book. Iron’s own starter book is a separate risk (older QA). |
| `summon_lords` is a refuse line | **true** | |

---

## wiki/Home.md

| Claim | Verdict | Why |
| --- | --- | --- |
| Private pack; Warp-crash; no Karl Franz war council; named lord; friend-elsewhere | **true** | |
| **“Total War: Warhammer factions on the ground”** | **false / oversold** | Faction *names* come from the Total War / table list. Sites are **7×7 pickets**. No Altdorf, no campaign map, no TW models. |
| **“Ark survival (thirst, heat, tames)”** | **oversold** | LSO thirst/temp + Fossils / Tameable Beasts. Not Ark (no official tames, no metal tiers, no official heatstroke loop). |
| Eight races; camps are pickets, not city builders; one night = one village or one fight | **true** | |
| Mods are the engine; Steve/villager bodies; no TW models | **true** | |
| We authored crash, camps, stance, path diplomacy, session, roaming, Recruits bind + **banner-founding**, grow, quest book | **oversold** on founding | Bind is scores/book. Founding is the Java bridge **trying**. |
| 16 / 40 / never 129 | **true** | |
| Honest limits: palisade + lord + two soldiers, not Altdorf; session = named vanilla; Recruits GUIs; no starter spellbook; client not CI | **true** | |
| Dedicated-server smoke passed on 0.3.10 | **true** (repo) | Zip Home.md (01:12) omitted this line. |

---

## wiki/TEST.md

| Claim | Verdict | Why |
| --- | --- | --- |
| Crash bowl / no six lords / no Iron’s book / Warp-Crash book | **true** as the test | Court is not first-join. |
| Bannered camp; named lord; stance lines | **true** as the test | |
| Chat names a real faction, **Never Team 2** | **oversold** | Same as PLAY smoke. Test it; if Team 2, Found a Banner. |
| Session start / win / hostile banner take | **true** | Functions in the session jar. |
| **Camp growth (Millénaire)**; hut outside the 7×7; Elector / temple-city / hold / Under-Empire, not “town hall” | **oversold** (heading) / **true** (size) | Heading named a mod we do not ship. Placement *is* outside the pad. Voice lines say “lean-to” / “not Altdorf”. Tier 3 is a bigger shed + nitwit, not a hall. |
| Emerald spend ticks `rallous.grow` | **true** | `credit/trade` within 24 blocks. |
| **U** is Elector / Waaagh / Under-Empire, not Team 2 | **oversold** | Lang overlay + bridge. Either can miss. |
| No `/recruits hire`; **R** is Host Command | **true** | |
| LSO thirst / temp | **true** (mod in pin) | Feel-it is the test. |
| “This is Ark survival” | **oversold** | LSO + eat. Not Ark. |
| Tames: Fossils / Tameable Beasts; LM extras global; Worse Hands flavour | **true** | |
| `force_roaming` walks a named host at you | **true** as authored | Recruits `recruitPatrol tiny`, not a TW army. |
| Death crater / bed; friend scatter; Winds lectern | **true** as authored | |
| Continuity is lang, not Fabric; do not add Fabric Continuity | **true** | |

---

## wiki/Recruits.md

| Claim | Verdict | Why |
| --- | --- | --- |
| Recruits is the army engine; bind to the crash camp, not Team 2 | **true** as intent | |
| No chat create / hire / ally; GUIs only; `factionManager` has no create *subcommand* | **true** | |
| **“The crash-camp host is founded anyway.”** | **false** | Bridge **tries**. It can fail (`rallous.rec.bridge_fail`). Fallback is **U → Found a Banner**. PLAY already said this; Recruits.md did not. |
| Chat / **U** should already say Reikland or Clan Mors | **oversold** | Bind chat can. **U** only if create/rename stuck. |
| Table: bridge founds; fallback U; hire right-click; **R** orders; patrol is generic; do not `/team add` | **true** if read as “what works”, **oversold** if “bridge founds” is a guarantee | |
| Bind copies display name; datapack cannot write Recruits saves | **true** | |
| Bridge burns Team 1 / Team 2 and founds the compiled name | **true** as code intent | Unclicked in a client. |
| If still Team 2: Continuity, walk to camp, Found a Banner | **true** (steps 2–3) / **oversold** (step 1) | Continuity does not rename a host. |

---

## wiki/Install.md

| Claim | Verdict | Why |
| --- | --- | --- |
| Import 0.3.10 as a **new** profile | **true** | |
| Download URL on this branch | **true** | |
| Dedicated-server smoke passed on 0.3.10 | **true** (repo) | **Zip copy was stale** (older pin 0.3.7, no smoke). |
| Java 17; 8 GB; 1.20.1 / 47.4.10; cheats ON; private | **true** | |
| Rallous Continuity is lang, not Fabric Continuity; Fabric jar stays out | **true** | |
| `options.txt` already last | **true** | |
| Without Continuity, Recruits still says Team 2 / Recruit | **oversold** | **Recruit → Levy** is lang. **Team 2** is the host. |
| Grim sky, gothic font, Complementary Unbound expected | **true** | CF files + `optionsshaders.txt`. |

---

## Nearby wiki (not edited unless they oversold the same lie)

`wiki/Factions.md` already says “Not Total War cities” then labels Empire **Settled cities** / Lizardmen **Temple-cities** / Skaven **Hidden under-capitals**. Those words are race *fantasy*, not what `place/` builds. Left as flavour; Home was the player-facing lie.

`wiki/Villages.md` still says “does not ship MineColonies in the **0.3.9** zip” — stale version pin. Not in the requested edit set.

---

## Lies corrected (this change)

1. **Home:** “Total War: Warhammer factions on the ground” + “Ark survival” → eight **named 7×7 pickets** + LSO thirst/heat + Fossils/Tameable Beasts. Not TW cities. Not Ark.
2. **Home:** “Recruits bind + banner-founding” as a done fact → bind + a Java bridge that **tries** to found; **U** if it misses.
3. **Recruits:** “The crash-camp host is founded anyway” → **not guaranteed**. Bridge tries; fallback **U → Found a Banner**.
4. **Recruits / PLAY / TEST / Install:** Continuity or first-hour chat **guarantees** no Team 2 → Team 2 is a host-name miss. Lang overlay only changes Recruit / Elector words.
5. **PLAY / TEST:** “Millénaire loop” / “Camp growth (Millénaire)” → **7×7 picket, 1–3 huts**, Millénaire-*style credit*, not the Millénaire mod.
6. **PLAY keys:** `M` = “Towns” → **Xaero world map**.
7. **TEST:** “Never Team 2” / “U … not Team 2” as pass/fail facts → **check**; if Team 2, Found a Banner.
8. **TEST:** “This is Ark survival” → LSO thirst / temp / hunger.

No new zip. Docs only.
