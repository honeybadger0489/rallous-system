# Logging and lessons

Two layers that must not be mixed:

1. **Runtime** — what the game process writes while you play or `runClient`.
2. **Learning** — what *you* write so next month’s ASA/Unreal/Unity you still remember *why*.

---

## Layer 1 — Runtime (Minecraft / Forge)

Minecraft uses **Log4j 2** (`org.apache.logging.log4j`), not `java.util.logging` and not `System.out.println` as your real API.

### Where the files are

| Context | Directory | Files |
| --- | --- | --- |
| Prism instance | `<instance>/logs/` | `latest.log` (INFO+), `debug.log` (DEBUG+ if enabled) |
| Forge MDK `runClient` | `<mdk>/run/logs/` | same names |
| Dedicated `runServer` | `<mdk>/run/logs/` | same; plus you accepted `eula.txt` |

Forge’s own support note: `latest.log` is INFO and above from Forge *and* mods; `debug.log` is that plus DEBUG. When you file a bug, attach **debug.log**, not a screenshot of chat. ([MinecraftForge SUPPORT.md](https://github.com/MinecraftForge/MinecraftForge/blob/1.20.1/SUPPORT.md) — equivalent text lives on the 1.20.1 branch.)

Prism: open the instance → **Folder** → `logs`. The vanilla Mojang launcher uses `.minecraft/logs/` — do not hunt there if you launched from Prism.

Crash reports: `crash-reports/crash-*-client.txt`. Read the **first** “caused by” that is *your* package, not the 80-line Mixin dump below it.

### Your mod logger

```java
package io.github.honeybadger0489.rallousallegiance;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public final class RallousAllegiance {
    public static final String MODID = "rallous_allegiance";
    public static final Logger LOGGER = LogManager.getLogger(MODID);
}
```

Use **`RallousAllegiance.LOGGER`**, not a new logger per class, until you have a reason. The log line will look like:

```text
[14:02:11] [Server thread/INFO] [rallous_allegiance/]: treaty elector_league -> war (camp 12 64 -88)
```

That prefix is how you `grep rallous_allegiance latest.log`.

### What to log (Allegiance)

| Event | Level | Example |
| --- | --- | --- |
| Mod common setup finished | INFO | `Allegiance loaded` |
| Camp claimed / abandoned | INFO | pos + player UUID |
| Treaty change | INFO | faction id, old → new |
| Standing crossed a **band** (−50, 0, +50) | INFO | not every +1 |
| Datapack faction JSON failed to parse | ERROR | file path + exception message |
| Packet from client failed validation | WARN | “ignored ally request, not envoy range” |
| “Envoy tick walked one block” | **never** | that is how you 400 MB a log |

DEBUG is for “opened dialogue id `vellbruck_hear`” while *you* are iterating. Turn console down to INFO before you play the full pack (`forge.logging.console.level=info`).

Do **not** log other players’ chat, tokens, or Microsoft emails. UUIDs are enough.

### Forge / MDK knobs

In the MDK `runs { configureEach { ... } }` block you typically already have:

```gradle
property 'forge.logging.markers', 'REGISTRIES'
property 'forge.logging.console.level', 'debug'
```

- `REGISTRIES` marker: noisy but useful the day an item silent-fails registration.
- For a **pack** instance in Prism, leave logging at default; enable debug only when reproducing a bug.

`F3` + `debug.log` is not a substitute for **your** INFO lines on diplomacy. Vanilla debug (pie chart, hitboxes) does not record treaty state.

### Client vs server

Diplomacy is **server** data. Log treaty changes on the **logical server** (`!level.isClientSide` / `ServerLevel`). If you log on both sides you will think the packet ran twice. The client may log “received sync: war” at DEBUG.

### When the game “just vanishes”

1. `latest.log` last 80 lines.
2. `crash-reports/`.
3. Mixin: `./gradlew` with mixin `debug.export = true` only if you added mixins (you should not have in v1).
4. Paste **paths + logger name** into a lesson, not a Discord dump without the file.

---

## Layer 2 — Learning (`lessons/` journal)

Runtime logs die with the instance. **Lessons persist in git.** They are how a Minecraft week becomes an ASA month.

Format lives in [`lessons/TEMPLATE.md`](lessons/TEMPLATE.md). First filled example: [`lessons/000-why-not-the-whole-game.md`](lessons/000-why-not-the-whole-game.md).

### Rules

1. **One experiment per file.** Not a diary of the weekend.
2. Filename: `NNN-short-kebab.md` starting at `000`. Numbers are order of *learning*, not git history.
3. Fill **Expected / Actual / Keep-drop / Transfer** every time, even when you “already know.”
4. Link a log line (`rallous_allegiance` + timestamp) when the experiment is runtime.
5. Transfer column is mandatory: Unreal/ASA **or** Unity **or** “engine-agnostic state machine.” If you cannot fill it, the experiment was too Minecraft-pixel-specific to be a *lesson* — still keep it, mark transfer `n/a (art pipeline)`.
6. Do not put GW/Wildcard IP in lesson titles you might screenshot.

### What belongs in lessons vs other places

| Belongs in `lessons/` | Belongs elsewhere |
| --- | --- |
| “SavedData did not write because I forgot `setDirty`” | Fix in code |
| “Java 21 broke FG 1.20.1” | [TOOLING.md](TOOLING.md) if it is now policy |
| “Envoy JSON schema v1” | ADR under `docs/adr/` once it is a *decision* |
| “I hate the banner UV” | Maybe skip; art taste is not a transfer lesson |
| Campaign lore | `CAMPAIGN.md` (do not duplicate) |

### Cursor

- Do **not** dump lessons into Cursor Memories. Memories are for *your* editor prefs (“I use Prism, not the Mojang launcher”).
- You may `@lessons/TEMPLATE.md` when asking the agent to write the next file.
- Project rule already says analogue names; lessons still use analogue names in **Actual** if they quote in-game strings.

### Review cadence

Every milestone in [FIRST-MOD.md](FIRST-MOD.md): one lesson. Every *failed* day 3 Gradle sync: one lesson. Once a month, skim keep/drop and promote survivors into `docs/adr/` or TOOLING.

---

## Minimal grep cheatsheet

```bash
# MDK
rg "rallous_allegiance" run/logs/latest.log

# Prism (adjust path)
rg "rallous_allegiance|Exception" ~/PrismLauncher/instances/rallous-frontier/logs/latest.log
```

Windows PowerShell: `Select-String -Path logs\latest.log -Pattern "rallous_allegiance"`.

---

## Sources (accessed 2026-08-31)

- Log4j as used by Minecraft/Forge: `org.apache.logging.log4j.LogManager` (Forge sources; community confirmation that `java.util.logging` is the wrong import — Forge forums, Choonster).
- https://docs.minecraftforge.net/en/1.20.1/gettingstarted/ (run dirs, `runClient`)
- MinecraftForge support text on `latest.log` / `debug.log`: https://github.com/MinecraftForge/MinecraftForge/blob/1.20.1/SUPPORT.md
- SavedData dirty flag: https://docs.minecraftforge.net/en/1.20.1/datastorage/saveddata/
