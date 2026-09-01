# PURPOSE

Why this folder exists, what the player is supposed to feel, and how you know v1 worked. One page. Play steps live in [`PLAY.md`](PLAY.md). Agent pickup: [`HANDOFF.md`](HANDOFF.md). Parked later choices: [`FORKS.md`](FORKS.md).

---

## Why this exists

The repo is building a **playable grimdark-fantasy warband** in Minecraft — Total War campaign *feel* and Ark *survival*, first person — without shipping a Games Workshop or Creative Assembly product.

A kitchen-sink 1.20.1 list is not the game. A Karl Franz war-council cutscene is not the game. A 40k gunpack is not the game. The product is: you crash, you meet a **real table faction**, you pick a path, you survive one night, you walk away with a levy and a crater you can die back to.

It stays **private**. Public branding is **Rallous**, original analogues in shipped text where IP policy requires it. Internal docs may say Empire / Reikland / Waaagh so pack builders know the tone-ref. See [`IP-FANTASY.md`](IP-FANTASY.md).

Minecraft **1.20.1 + Forge 47.4.10** is locked because Recruits, the grim stack, and this datapack line already live there. Newer loaders are a different product.

---

## Player fantasy

You are **not** the Emperor. You are a **warp-stranger**: hungry, politically small, dumped in a blackstone bowl.

A named Elector, High King, Beastlord, Slann, von Carstein, Warlord, or Bloodbound — someone from the JSON, not a mute villager — is already camped over the ridge. They offer a blade, a test, a raid, or a daemon accusation. Help, betray, join, or align and leave. That choice sticks to **that** host.

Then the world is a warband loop: ride, eat, hire a levy (Recruits), tame something ugly (Fossils / Tameable Beasts), fight a place (one village or one picket), sleep in a bed you own. The journal is **The Warp-Crash**, not a five-act finale. Friends who join this world crash **somewhere else**.

You should feel: *I landed in someone else’s war.* Not: *I sat in Karl’s court and got a starter spellbook.*

---

## Success test

v1 succeeds if a **new** CurseForge profile of **0.3.13** (do not “update” an older profile) passes the two-hour test in [`wiki/TEST.md`](wiki/TEST.md):

1. **Crash** — Bowl of blackstone / crying obsidian. Wreckage chest. Title says Warp-crash. **No six named lords.** Forge 47.4.10 boots (if not: `crash-*-fml.txt`).
2. **Named lord + stance** — Nearest bannered camp speaks as a real faction. Chat names the camp (Reikland, Clan Mors, …). **U** may still say Team 2 if the bridge misses — Found a Banner and type that chat name.
3. **Session** — `/function rallous_session:start` then a village wave or a picket fight; `/function rallous_session:win` or clear it.
4. **Roaming** — `/function rallous_old_world:force_roaming` drops a Waaagh scout, a herd, a Khorne pack.
5. **Rallous Continuity** — Resource pack on (options.txt should already). Recruits UI says Levy / Elector / Waaagh / Under-Empire, not “Recruit” / Team 2. That pack is **lang**, not Fabric Continuity.

Bonus if time: second player (or `crash/demo_friend_elsewhere`) lands elsewhere; wreckage has no Iron’s spellbook; no-bed death returns to **your** crater.

If those are true, the fantasy landed. Cities, per-race Fossils tames, a final act, MineColonies growth, and 40k DLC are **later forks**, not this test.
