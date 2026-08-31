# Lesson 000 — why not the whole game

- **Date:** 2026-08-31
- **Engine / stack:** none yet (process lesson, before `runClient`)
- **Related:** [FIRST-MOD.md](../FIRST-MOD.md), [ORGANIZATION.md](../ORGANIZATION.md), vision in `CAMPAIGN.md` + `FACTIONS-AND-DIPLOMACY.md`

## Experiment

Treat the locked fantasy (TWW3 tone, soldier-eye, RDR campaign, New World regions, Ark survival/tame, Civ factions/lords, large wars, no MOBA, original Rallous names) as a **single first Minecraft mod** versus as a **ladder** whose first ship is a warband banner + camp claim + one envoy + one ally/war flag.

## Expected

Starting with a custom dinosaur, a full FTB quest graph, or an Unreal/ASA DevKit “real game” would get closer to the dream faster because those are the *visible* parts of Ark and Total War.

## Actual

Those starts optimize for **content and art**, which do not transfer and do not finish. Forge fundamentals that *do* transfer (items, data gen, SavedData, player capabilities/attachments, networking, datapack-driven faction ids) are all present in a banner/allegiance slice. A dino is a GeckoLib month. A quest pack is an infinity. An MMORPG backend is how the repo dies. The vision docs already hold the dream; they do not need a second copy in Java on week one.

## Keep / drop

- **Keep:** First jar = `rallous_allegiance` (plant banner, persist camp, one NPC, one treaty). Java 17 + Forge 1.20.1. Analogue names only.
- **Drop:** Week-one dinosaur, guns, colonies, custom dimension, Java 21 “because newer,” MCreator, GW/Wildcard assets.
- **Park:** Recruits armies, five campaign acts, ASA totem, Blender creature — rungs 3–5 in ORGANIZATION.md.

## Transfer

| Target | Mapping |
| --- | --- |
| **ASA / Unreal** | Tribe totem + replicated alliance enum + DataTable of faction ids. Not a Minecraft rex mesh. |
| **Unity** | ScriptableObject faction list + save blob + Interactable NPC. Same state machine. |
| **Engine-agnostic** | Owner id + standing int + treaty enum + a talker. Scope is a **ladder**, not a studio simulation. |
