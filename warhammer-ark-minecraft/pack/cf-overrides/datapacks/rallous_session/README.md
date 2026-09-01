# rallous_session

Minecraft **1.20.1** datapack (`pack_format` **15**). After first contact, a night the player can finish in ~30–50 minutes: **one village or one fight**.

No new mods. This folder only. Zip agent may ingest it (jar **or** world datapack, not both).

## How to start / win

Need `rallous.contact` **or** a `rallous.camp` in range (nearest banner). Cheats ON:

```
/function rallous_session:start
```

That binds the contact camp (or nearest), reads `rallous.fac.stance`, and speaks in that lord’s voice.

- **help / prove** (`fac.stance` 1 or 2; also daemon 4 and joined 5): a short wave of vanilla pillagers and zombies **named as that race’s enemies**, at a tagged village if one is near, else the camp. Clear them to finish.
- **hostile** (`fac.stance` 3 or war 6): the camp’s raid **is** the session. Adopt existing `rallous.raid` mobs, or spawn the race wave at the picket. Survive (foes dead) **or** take the picket (stand on the banner ~3s, or break it).

```
/function rallous_session:win
```

Sets `rallous.session` **1** (FTB can task on that). Also `rallous.proved` 1, `rallous.crash` 2 (village/defend) or 3 (fight). Manual complete is allowed.

```
/function rallous_session:take_picket
```

Hostile shortcut: claim the banner site.

Night + contact + walking to **that** camp also auto-starts once (`time` 13000–23000). Command `start` works any hour.

## FTB scores

| Objective | Meaning |
| --- | --- |
| `rallous.session` | **1** = night won (the check FTB should read) |
| `rallous.session_on` | 1 while the wave/raid is live |
| `rallous.session_kind` | 1 defend / 2 prove / 3 hostile |
| `rallous.session_race` | 1–8 (empire…khorne), copied from the camp |
| `rallous.proved` | 1 on win |
| `rallous.crash` | 2 village-defend / 3 fight (same numbers as `rallous_contact`) |

Writes those dummies on load. Does not wipe other packs’ scores.

## Files

`start` `win` `take_picket` `load` `tick` `bind` `try_autostart` `start_go` `begin_help` `begin_prove` `begin_hostile` `pick_site` `wave/by_race` `voice/start` `voice/win`
