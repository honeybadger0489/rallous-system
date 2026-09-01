# Diplomacy

First-contact **Paths** open when you wake in the crater (quest book chapter Paths — not after a one-hour prove). Each verb sets `rallous.path` and shifts **that** contact faction’s stance — the camp you crashed next to, not the whole race.

At the picket the lord’s chat offers clickable **[Help] [Betray] [Join] [Leave]**. Flint the pad (or tick **Burned Their Welcome**) is the Khorne path.

You may recant later. Host command stays optional.

## The four verbs

| Path | Do this | Stance on that camp |
| --- | --- | --- |
| **Help** | Stay. Mend a fence. Share food. Walk the coach road. | Ally. One vanilla gift (once). |
| **Betray** | Learn the gate hour. Sell the watch. Open a door you were asked to hold. | War. Marks a Khorne-path stain. Nearby golems get angry. |
| **Burn welcome** | Flint the picket, or fire on the pad. | Same as betray, plus `rallous.khorne`. A raid. |
| **Join** | Take a colour. Mean the banner. | Joined. Eligible for a civ-bed / claim. |
| **Align and leave** | Shake a hand. Walk away. Standing without a payroll. | Neutral. The map does not close. |

Tick the quest, or (cheats) run the verb near a camp:

```
/function rallous_diplomacy:help
/function rallous_diplomacy:betray
/function rallous_diplomacy:join
/function rallous_diplomacy:leave
```

## What this is not

- Not a Civ VI treaty table. No globe, no pause screen.
- Not Recruits Ally / Enemy. That is a **different** graph on the **U** screen, and it needs two Recruits banners that already exist. See [Recruits](Recruits.md).
- Not global. Help Reikland does not make Clan Mors love you.

## Session night

After contact, one night you can finish in ~30–50 minutes: **one village or one fight**, in that lord’s voice.

- Help / prove / joined / daemon: a short wave of named vanilla foes (village if one is near, else the camp).
- Hostile / war: the camp raid **is** the session. Survive, or take the picket (stand on the banner ~3s, or break it).

`/function rallous_session:start` then clear it, or `/function rallous_session:win`. Night + walking back to **that** camp can auto-start once.
