# Commands

Cheats **ON**. Useful for a two-hour play and for unsticking a world. Forge **1.20.1 / 47.4.10**.

`/function rallous_old_world:summon_lords` is a **refuse** line. It does **not** rebuild the 0.2.2 court.

## Session (one village or one fight)

Stand at the contact camp (or nearest banner).

```
/function rallous_session:start
/function rallous_session:win
/function rallous_session:take_picket
```

`start` works any hour. Night + walking to **that** camp can also auto-start once.

## Roaming

```
/function rallous_old_world:force_roaming
/function rallous_roaming:events/waaagh
/function rallous_roaming:events/herd
/function rallous_roaming:events/khorne_host
/function rallous_roaming:clear
```

## First contact

```
/function rallous_factions:debug/force_contact
/function rallous_warp_crash:first_contact
/function rallous_recruits_bind:on_contact
```

`force_contact` plants a compiled camp at your feet and fires its stance. `first_contact` is the quest hook (assign nearest camp). `on_contact` re-binds Recruits scores / book to that camp.

## Crash / death

```
/function rallous_old_world:crash/demo_friend_elsewhere
/function rallous_old_world:crash/return_crater
/function rallous_warp_crash:test_respawn
```

## Beasts

```
/function rallous_old_world:lm_bm/summon
```

## Diplomacy verbs

Near a camp marker:

```
/function rallous_diplomacy:help
/function rallous_diplomacy:betray
/function rallous_diplomacy:join
/function rallous_diplomacy:leave
```

## Keys (not commands)

| Key | What |
| --- | --- |
| `` ` `` | Warp-Crash quest book |
| `U` | Recruits banner / Diplomacy |
| `R` | Recruits Host Command (later: Iron’s wheel) |
| `V` | Epic Fight melee stance |
| `M` | World map |
