# FORKS — decisions after this goal

Parked forks in the road. **Do not implement these on the current successor-docs pass.** When a later goal picks one, move it out of this log (or mark Chosen) and leave a one-line why.

Seeded from locked honesty in PLAY / datapack READMEs / campaign research. Not a backlog to clear.

See also [`HANDOFF.md`](HANDOFF.md).

---

## Recruits has no found-banner API → Java bridge vs live with U screen

**Fact:** Villager Recruits 1.20.1-1.15.2 has **no** datapack or `/recruits admin` create. Admin can get/set/delete. Vanilla `/team add` becomes Team 1 / Team 2 and `getFactionByStringID` is null. Hire / Ally / Enemy / Found a Banner are GUIs. Research: [`content/RECRUITS-API.md`](content/RECRUITS-API.md), [`content/datapacks/rallous_recruits_bind/README.md`](content/datapacks/rallous_recruits_bind/README.md).

**v1 today:** `rallous_recruits_bind` writes scores, storage, book, and the crash-camp **display name**. PLAY.md + 0.3.10 ingest also expect `rallous-recruits-bridge` to call `FactionEvents.createTeam(false, …)` (same server path as U → Found a Banner) so chat / U say Reikland or Clan Mors.

**Fork later:**

| Path | Cost | Honest limit |
| --- | --- | --- |
| **A — Java bridge** | Keep / finish `mods/rallous-recruits-bridge`. One create path. Do not mixin a second create. | Hire / orders / Ally–Enemy still Recruits GUIs. |
| **B — Live with U** | Drop the jar. Player types the book name in Found a Banner. | Easy to get Team 2 if they skip U. Bind README already documents this. |

Do not start a **second** Java project for the same call.

---

## Fossils cannot per-race tame difficulty

**Fact:** Fossils and Archeology 9.3.4 has no per-faction tame tag. Only global `whipToTameDino` (we do not flip it). `race.taming_affinity` is JSON flavor: lizardmen `high`, beastmen `corrupt`, others `low`. `rallous_temple_herd` adds extra Tameable Beasts *food* tags (global — anyone can use them) and a Worse Hands book for other races. There is **no** hidden tame penalty.

**Fork later:** a tiny Forge/KubeJS tame multiplier keyed on `rallous.race` — or accept that Lizardmen “high” is voice + offerings, not a Fossils roll. Do not add another creature mod.

---

## Camps are pickets, not Total War cities

**Fact:** Compiled camps are war-host pickets: palisade, banners, campfires, site props, named lord, two soldiers. Caps 16 / 40. Beastmen / Waaagh / Khorne / some Skaven are roaming-style, not pretty capitals. Session night is named vanilla waves, not a Recruits field battle and not a TW city fight.

**Fork later:** thicken into walkable hubs (CTOV / Towns and Towers / authored structures) vs keep pickets and let the player’s own camp be the only “city.” CAMPAIGN.md already says do not model the whole Old World at TW scale.

---

## Custom faction HQ is hook-only

**Fact:** `rallous_crater_hq:mark` after `store_crater` writes storage + a forceloaded marker + oak fence + white banner at crater +2 X. That is the **player claim hook**, not a contact camp and not Recruits founding.

**Fork later:** recruit-into-player-faction DLC that *reads* `rallous_crater_hq:data` / `@e[tag=rallous.hq]`. Until then, do not grow the crater into a capital.

---

## No v1 ending vs later final act

**Fact:** v1 journal is **The Warp-Crash** (Crash / Paths / First Hour / The Winds / optional Host / Temple and Herd). Smoke is a checklist. There is no Act V siege, no New Game+, no “you won the Old World.”

**Vision (do not implement now):** [`CAMPAIGN.md`](CAMPAIGN.md) five acts + an epilogue that is **not** an ending. [`FACTIONS-AND-DIPLOMACY.md`](FACTIONS-AND-DIPLOMACY.md) optional late titles (oath-friend, puppet-crowned, howling convert).

**Fork later:** ship v1 as an open loop (crash → path → one night → levy) **or** add a later final act as a separate chapter pack. Do not gate the map.

---

## Crash site later 40k DLC

**Fact:** The crater is Fantasy Warp-crash wreckage. `rallous_crater_hq` is reserved as a **later-DLC** hook. IP policy: this pack is **not** 40k ([`IP-FANTASY.md`](IP-FANTASY.md)). No bolters, no Adeptus, no aquila in v1.

**Fork later:** a **separate** product/DLC that re-skins or extends the crash as a 40k landing — only if legal/licence review says go. Do not sneak 40k into this zip. Do not reuse Sons of the Empire / grim packs as Space Marines.

---

## MineColonies / Millénaire village growth

**Trigger:** user asked. Not in the 76-file v1 pin as a required colony sim.

**Research already on disk:**

- [`CAMPAIGN.md`](CAMPAIGN.md) — MineColonies = living town; Recruits = field army. Colony fall does not reset the campaign. Colony-win is one province verb.
- [`FACTION-MODS.md`](FACTION-MODS.md) — MineColonies 1.20.1 Forge + optional War 'N Taxes. Pick one as player capital or pay the performance cost.
- [`QUEST-AND-WORLD-MODS.md`](QUEST-AND-WORLD-MODS.md) — MineColonies optional; **Millenaire: not a 1.20.1 Forge spine. Skip.** A GitHub Millenaire rewrite exists; not a trusted pin.

**Fork later:** add MineColonies (and Structurize / BlockUI / …) for village growth **or** keep pickets + Recruits claims and ignore colony-win. Do not add Millénaire as the v1 spine.

---

## Second workspace: do not fork

**Fact:** Source of truth is this GitHub repo on `cursor/warhammer-ark-minecraft-d8d1` (PR #1). [`ORGANIZATION.md`](ORGANIZATION.md): a Desktop “real” folder and a second clone that diverges are lies.

**Rule:** another Cursor workspace / Cloud Agent / MDK tree may sit **beside** the clone (`mods/rallous-recruits-bridge/`, or an MDK outside git until `gradlew build` works). It must push **back to this repo and branch** (or a new `cursor/…-41fb` branch off it). Do **not** GitHub-fork `rallous-system`. Do not start a second Recruits-bridge Java project. Do not retitle a public pack “Warhammer.”

---

## Open

- Player zip is **0.3.13**. Dedicated-server smoke **passed on 0.3.12 and 0.3.13**. Client GUI boot / `wiki/TEST.md` is unverified. SHIP_READY: no.

<!-- Later goals add undecided forks here. Keep the seeds above stable. -->
