# Rallous roaming wars

Minecraft **1.20.1** datapack (`pack_format` **15**). Mid-game roaming hosts with **no capital**: a Greenhost **Waaagh**, a Horned Woods **herd**, and a **Khorne** Blood Host. They are scheduled while you play (not worldgen) and can be forced with `/function` for the 1-hour smoke test.

Ship as this folder (world `datapacks/`) **or** jar it with the included `META-INF/mods.toml` (LowCodeFML, same pattern as `rallous_old_world`). Do not enable both.

## Event IDs

| ID | Function (force) | Voice | Host |
| --- | --- | --- | --- |
| `waaagh` | `/function rallous_roaming:events/waaagh` | Greenhost / boyz slang | Named pillagers, choppa vindicators, gobbo zombies, lime skull banners |
| `herd` | `/function rallous_roaming:events/herd` | Horned Woods | Bray-shaman witch, nerfed ravager, gor vindicators, ungor husks, brown skull banners |
| `khorne_host` | `/function rallous_roaming:events/khorne_host` | Blood Host | Champion + bloodreavers, skull-tithe wither skeletons, red skull banners |

Also: `/function rallous_roaming:events/random` (rolls one of the three).

Force functions **skip** play-time and crater gates so QA can fire them on day 0.

## How it schedules

1. `#minecraft:load` → `rallous_roaming:load`  
   Creates scoreboards / team `rallous_roam`, then  
   `schedule function rallous_roaming:clock 1200t replace` (60s, `replace` so `/reload` does not stack).
2. `#minecraft:tick` → `rallous_roaming:tick`  
   Adds **1** to each player's `rallous.roam.play` every tick (20 min = 24000, 40 min = 48000).  
   Every 10 ticks, any living host **marches** toward the nearest player and may leave a **limited** scar (leaves / crops / short grass, at most 12 actions, fire only on grass and only 16+ blocks from a player). Hosts fade after **5 minutes**.
3. `rallous_roaming:clock` re-schedules itself every 1200 ticks.  
   If no host is up, it rolls `$need` = current max play + **24000–48000** (UUID %, 1.20.1 has no `/random`).  
   When a player’s play ≥ `$need` **and** the crash gate passes **and** a 25% predicate hits, `clock/pick` chooses `waaagh` / `herd` / `khorne_host` and spawns ~28–56 blocks away (`spreadplayers`). Then it rolls the next 20–40 min window.

Natural events are **not** worldgen. They happen on the clock while someone is online.

## Crash gate (do not brick a new crater)

Natural spawn is blocked until **either**:

- `time query day` ≥ **1**, or
- the player is **128+** blocks from the crater origin (horizontal, chunk-safe scores).

Origin, in order:

- warp-crash marker `rallous.crater` (also `rallous.crash.crater` / `rallous.crash.origin`)
- the considering player's `rallous.crater_x` / `rallous.crater_z`
- scores `$x`/`$z` on `rallous.crash.pos`
- else first online player position

Force `/function rallous_roaming:events/*` does **not** use this gate.

## Force-test (1-hour smoke)

Cheats / op:

```
/function rallous_roaming:events/waaagh
/function rallous_roaming:events/herd
/function rallous_roaming:events/khorne_host
/function rallous_roaming:events/random
/function rallous_roaming:clear
/function rallous_roaming:debug/status
```

Expect: title + tellraw in faction voice, a named bannered host that walks toward you, light leaf/crop scars, then scatter or `/function rallous_roaming:clear`.

To exercise the **scheduled** path without waiting 20–40 min:

```
/function rallous_roaming:debug/ready
```

That sets play ticks high, clears the 2-minute lock, and `time add 24000` (day ≥ 1). The next clock (~60s) has a 25% chance to roll a host. Force-test does not need this.

## Function map

| Function | Role |
| --- | --- |
| `rallous_roaming:load` | Scoreboards, team, first `schedule` |
| `rallous_roaming:tick` | Play-time + march pulse |
| `rallous_roaming:clock` | 60s natural ticker (`schedule … replace`) |
| `rallous_roaming:clock/idle` | Need / ready player |
| `rallous_roaming:clock/roll_need` | 20–40 min window |
| `rallous_roaming:clock/consider` | Crash gate + 25% |
| `rallous_roaming:clock/pick` | UUID % 3 → spawn |
| `rallous_roaming:safety/*` | Origin + crater / day gate |
| `rallous_roaming:events/<id>` | **Force** spawn (smoke test) |
| `rallous_roaming:spawn/<id>` | Shared spawn (force + clock) |
| `rallous_roaming:announce/<id>` | Title / tellraw / horns |
| `rallous_roaming:march/*` | Move, limited grief, timeout |
| `rallous_roaming:clear` | Despawn host |
| `rallous_roaming:debug/status` | Scores |
| `rallous_roaming:debug/ready` | Fast-forward the clock |

## Zip agent

Source of truth: `warhammer-ark-minecraft/content/datapacks/rallous_roaming/`.  
Include as `overrides/mods/rallous-roaming-1.0.0.jar` (LowCodeFML) **or** a world datapack. This folder does not rebuild `dist/`.
