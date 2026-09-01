# Organization — repo, knowledge, scale

This GitHub repository is the **source of truth**. Discord, screenshots, and a second “real” folder on the Desktop are lies that diverge in a week.

Locked constraints (also in `.cursor/rules/rallous-modding.mdc`): original **Rallous** names, **no Games Workshop / Wildcard IP**, Minecraft **1.20.1 Forge**, first ship = [FIRST-MOD.md](FIRST-MOD.md).

---

## 1. What this repo is

| Layer | Role |
| --- | --- |
| Root `README.md` | Points at this folder. Playable HTML title lives at repo root; do not mix it with the Forge MDK. |
| `warhammer-ark-minecraft/` | Prototype kit: vision, pack *metadata*, lessons, future tiny mods. |
| `pack/` | packwiz + mrpack **pins**. Launchers download jars. **Do not commit jars.** |
| GitHub issues / PRs | Decisions that need a second brain. |

If it is not in git, it did not happen.

---

## 2. Suggested tree

Current files stay where they are. **Add**, do not reshuffle vision docs into a new hierarchy this week.

```text
rallous-system/
  README.md
  .cursor/rules/rallous-modding.mdc    # invariants for agents
  warhammer-ark-minecraft/
    README.md                          # TOC for this kit
    CAMPAIGN.md                        # vision — do not clobber
    FACTIONS-AND-DIPLOMACY.md          # vision — do not clobber
    FACTION-MODS.md                    # research overlay
    CURATED-PACK.md / RESEARCH.md / …
    pack/                              # already exists
    lessons/                           # journal (you write)
      TEMPLATE.md
      000-why-not-the-whole-game.md
    docs/                              # ADRs + specs that are not “vision”
      adr/
        README.md                      # how to write an ADR
    mods/
      rallous-allegiance/              # FUTURE Forge project (gitignore build/, run/)
    downloads/                         # gitignored jars; scripts stay
    scripts/
```

### What each new bucket is for

| Path | Put | Don’t put |
| --- | --- | --- |
| `lessons/` | Dated experiments, keep/drop, transfer lines | Lore, pack pins, 200-page design |
| `docs/adr/` | Durable *decisions* (e.g. “diplomacy lives in SavedData, not scoreboards”) | Brainstorms |
| `docs/` (other) | Specs that implement vision (packet list, JSON schema) | A second CAMPAIGN.md |
| `mods/rallous-allegiance/` | The first Forge source tree, when you are ready to version it | The 69-mod pack, Prism `minecraft/` |
| `pack/` | Pins for **play** | Your unfinished MDK |

Until the MDK `build` works, the Java tree may live **outside** git (`~/rallous/mdk-rallous-allegiance/`). The week it produces a jar, move it under `mods/rallous-allegiance/`, add a `.gitignore` copied from the MDK, and commit **source + `gradle.properties`**, never `run/` worlds.

### ADRs (Architecture Decision Records)

When a lesson’s “Keep” is still true a month later, promote it:

```text
docs/adr/0001-world-diplomacy-is-saveddata.md
```

Short template:

- Status: accepted / superseded
- Context (one paragraph)
- Decision
- Consequences (including ASA)

Number from `0001`. Do not ADR “we use Java” — ADR “standing is a player capability, treaties are world SavedData.”

---

## 3. Grand scale without drowning — the ladder

The fantasy is TWW3 + Civ + Ark + RDR + New World. That is a **studio**. You are one person with a banner.

**Vision docs already exist.** Do not enlarge them until a jar exists. Implementation is a **ladder**; you stand on one rung until it bears weight.

```text
0  Datapack spike     scoreboard / function “claim” you will throw away
1  Tiny Forge mod     Rallous Allegiance v1  ← you are here
2  Pack integration   jar in Prism + Frontier; OPAC coexistence
3  Overlay mods       Recruits / NPCs as *consumers* of your treaty flags
4  Content            FTB Quests reading rallous:* advancements
5  ASA prototype      one totem + tribe alliance bit, original names
6  (maybe) Unreal     only if ASA is the wrong home
```

**Warn:** an MMORPG is not rung 0. Dedicated auth, sharding, a custom dimension “continent,” voice, cash shop, hero classes — that is how the project dies before a banner plants.

### How to think “big” on a Tuesday

| Scale | Allowed thought | Forbidden Tuesday action |
| --- | --- | --- |
| TWW3 campaign map | Write a *province id* in a JSON comment | Generate 400 settlements |
| Civ diplomacy | Treaty **enum** with two values | AI agenda matrix |
| Ark taming | Note “faction can own a pen later” | GeckoLib apex |
| RDR chapters | One envoy line that mentions a rumor | Five-act quest graph |
| New World regions | Camp is in a biome; standing is global | Territory control plugin network |

When a big idea appears, add a **bullet under “Out of v1”** in FIRST-MOD or a lesson titled `parked-…`. Do not open a second MDK.

---

## 4. Cursor: rules, skills, memories — use sparingly

Docs: [Rules](https://cursor.com/docs/context/rules) · [Plugins](https://cursor.com/docs/plugins) · [MCP](https://cursor.com/docs/context/mcp).

| Mechanism | Use for | Do not use for |
| --- | --- | --- |
| **Project rules** `.cursor/rules/*.mdc` | Invariants: analogue names, no GW IP, 1.20.1 Forge, don’t clobber vision docs | 40 pages of lore (point at files instead) |
| **AGENTS.md** | Only if you hate frontmatter; we already use `.mdc` | Duplicating the rule |
| **Skills** | Later: “run `gradlew runData` and summarize errors” | Day-one ceremony |
| **Memories** | Personal: “Prism path is D:\Games\Prism” | Faction roster (that is git) |
| **MCP Context7** | Live Forge/Java docs | Replacing [TOOLING.md](TOOLING.md) |
| **MCP GitHub** | PRs on this repo | Rewriting history |
| **MCP Sentry** | After you have players | Week one |

The committed rule `rallous-modding.mdc` is **alwaysApply**. Keep it under ~40 lines. If you need more, add a *glob* rule for `mods/rallous-allegiance/**/*.java` (“no Mixin in v1”, “log treaty at INFO”).

User rules in Cursor settings are **your** voice (“be terse”). They are not team policy; team policy is git.

---

## 5. Pack vs mod vs docs — ownership

| Question | Owner file |
| --- | --- |
| What the soldier *feels* on the road | `CAMPAIGN.md` |
| Civ/TW verbs and analogue roster | `FACTIONS-AND-DIPLOMACY.md` |
| Which existing mods to download | `CURATED-PACK.md` / `pack/` |
| Which diplomacy mods *might* overlay | `FACTION-MODS.md` |
| What **you** code first | `FIRST-MOD.md` |
| How you sit down | `BEFORE-YOU-BEGIN.md` / `TOOLING.md` |

Agents (and you) **add files**. Do not “clean up” by merging vision docs. Do not retitle the public pack “Warhammer.”

---

## 6. Knowledge that must transfer

Every kept lesson maps to a sentence in [FIRST-MOD.md](FIRST-MOD.md#port-sheet-pin-this-in-every-allegiance-lesson). If you cannot map it, it is Minecraft trivia (UV on wool). Trivia can stay in lessons; it does not get an ADR.

When you open the ASA DevKit months from now, you should be able to `rg "ASA transfer" warhammer-ark-minecraft/lessons` and get a checklist, not a blank stare.

---

## Sources (accessed 2026-08-31)

- https://cursor.com/docs/context/rules
- https://cursor.com/docs/plugins
- https://cursor.com/docs/context/mcp
- Pack layout already in this folder (`pack/`, `.gitignore` jar policy)
