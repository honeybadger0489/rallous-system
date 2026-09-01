# Two-hour play — what to TRY

Not a tour. Not coordinates. **Do these verbs.** Tick what held. If it fails, that is the report — not a rewrite of this page.

New world. Survival. Hard. Cheats ON. Grave key `` ` `` for the book. Stress the assumptions below; they are load-bearing.

## Assumptions to break

| Assumption | Try |
| --- | --- |
| You crash, you do not spawn in a court | Look down. Bowl. No six lords. |
| The nearest camp has a **stance** | Walk. A named lord speaks. Not a mute village. |
| One night is one **session fight** | Start it. Win it or take the picket. |
| Recruits is a **banner UI**, not a chat API | Open **U**. Found / inspect. Hire is a right-click. |
| Thirst is real (LSO) | Do not drink. Feel it. Then drink. |
| Tames are race-flavoured, not a hidden LM buff | Offer food. LM extra tags are global. |
| A **Waaagh** (or herd / Blood Host) can walk at you | Force it if the clock is slow. |
| Death is crater or bed, not a second crash | Die twice. |
| A friend crashes **elsewhere** | Invite one, or demo the scatter. |

## Checkbox — two hours

### Crash

- [ ] Look down: blackstone / crying obsidian bowl, campfire, wreckage chest.
- [ ] Title says Warp-crash. Forge 47.4.10.
- [ ] Chest is bread / leather / stone. **No** Iron’s spellbook.
- [ ] Open the quest book (`` ` ``). **The Warp-Crash**, not a Reikland tutorial court.

### Stance

- [ ] Walk to the nearest **bannered** camp. Palisade. Lord. Two soldiers.
- [ ] Chat names a **real faction** (Reikland, Clan Mors, Hexoatl, …). If **U** still says Team 2, Found a Banner and type that chat name.
- [ ] The lord speaks a **stance**: blade gift, prove-yourself, raid, or daemon accusation.
- [ ] If nothing is near: `/function rallous_factions:debug/force_contact` and try again.

### Session fight

- [ ] Stand at that camp. `/function rallous_session:start`.
- [ ] The lord speaks. A wave starts **or** the picket raid is the session.
- [ ] Clear it — or `/function rallous_session:win`. Hostile: stand on the banner ~3s / break it.
- [ ] Optional: wait for night, walk back, see if it auto-starts once.

### Camp growth (7×7 picket huts)

- [ ] After a help night, a hut appears **outside** the 7×7 pad. Chat says Elector / temple-city / hold / Under-Empire — not “town hall”.
- [ ] Spend an emerald at the camp (hire or trade). `rallous.grow` ticks up. Second hut or hall.
- [ ] Force: `/function rallous_grow:on_session` or set the nearest camp `rallous.grow` to **3**.

### Banner UI

- [ ] **U** opens Found a Banner / Diplomacy (Elector / Waaagh / Under-Empire lang if Continuity is on).
- [ ] Inspect the host. Name matches the camp, **or** it still says Team 2 — Found a Banner and type the chat name.
- [ ] Right-click a Levy. Hire GUI exists. There is **no** `/recruits hire`.
- [ ] **R** is Host Command (orders), not a spell wheel.
- [ ] Do **not** `/team add`. Confirm Recruits still warns if you try.

### Thirst

- [ ] Watch the LSO thirst / temp HUD. Walk without drinking until it matters.
- [ ] Drink. Heat in a hot biome or cold in a hold-road should also nag.
- [ ] Eat. This is LSO thirst / temp / hunger, not a creative tour and not Ark.

### Tame

- [ ] Find a Fossils or Tameable Beasts creature, **or** `/function rallous_old_world:lm_bm/summon`.
- [ ] Offer tame food. It works or it does not — note which.
- [ ] If you crashed Lizardmen: extra offerings exist, but they are **global**, not a secret LM-only roll.
- [ ] If you are anyone else: Worse Hands book is flavour. No hidden penalty.

### Waaagh

- [ ] `/function rallous_old_world:force_roaming` — Waaagh, herd, and Blood Host near you.
- [ ] A named bannered host **walks toward you**. Light leaf/crop scars. Then they fade or `/function rallous_roaming:clear`.
- [ ] Optional: do not force; walk 128+ from the crater after day 1 and wait. Clock is slow. Forcing is honest.

### Death

- [ ] Die with **no** bed. Respawn in **your** crater. Same player. No second Warp-hole.
- [ ] Place a bed. Sleep. Die. Respawn at the bed.
- [ ] `/function rallous_old_world:crash/return_crater` still finds your hole.

### Multiplayer scatter

- [ ] A friend joins **this** world — or `/function rallous_old_world:crash/demo_friend_elsewhere`.
- [ ] They wake in a **different** crater. You do not share a spawn circle.
- [ ] Meet on the road. Their contact camp can be a different race. That is the point.

### The Winds

- [ ] Crash hotbar / wreckage: **no** Iron’s spellbook.
- [ ] At a bannered camp, a **named lectern** holds a letter (College / Ice / Grave / Vein / primer).
- [ ] Take the letter. Advancement. Barrel may have Iron’s common ink. **No** filled spellbook in the barrel.
- [ ] `/function rallous_winds:hint` restates the path.

### Continuity (if names are wrong)

- [ ] Options → Resource Packs → **Rallous Continuity** is on (lang overlay, **not** Fabric Continuity).
- [ ] Recruits UI says Levy / Elector / Waaagh, not “Recruit”.

## If the client dies on boot

Send `crash-*-fml.txt`. Do not “just add Fabric Continuity.”

## After two hours

You have crashed, heard a stance, fought one night, touched the banner UI, felt thirst, tried a tame, seen a Waaagh, died, and (if someone showed up) scattered. That is the pack. Everything else is walking.
