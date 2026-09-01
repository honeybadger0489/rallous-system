# rallous-recruits-bridge

Tiny **Forge 1.20.1** Java mod. After Warp-crash assign it **founds or names** the player's Recruits host to the compiled camp (Reikland, Clan Mors, …) so they do not see Team 2.

## Does it actually found a banner?

**Yes — it calls Recruits' own Found-a-Banner server method**, not a datapack hint.

Inspected **Villager Recruits 1.20.1 1.15.2** (`projectID` 523860 / `fileID` **8339846**, same pin as the pack):

| Surface | What this mod does |
| --- | --- |
| `MessageCreateTeam` (U → Found a Banner) | Client packet → `FactionEvents.createTeam(true, …)` |
| This bridge | `FactionEvents.createTeam(false, player, level, teamName, displayName, playerName, banner, ChatFormatting.RED, (byte) 12)` after assign |
| `menu=false` | Same as Recruits' intercepted `/team add`: **skips emerald cost and cloth-banner checks**, still `scoreboard.addPlayerTeam` + `RecruitsFactionManager.addTeam` + `save` |
| stringID | Recruits client sanitizer: `Clan Mors` → `ClanMors` (spaces out of scoreboard id) |
| unitColor | **byte 12** = red on `FactionEditScreen.unitColors` (not dye id 14) |
| `FactionEvent.Created` | Optional confirm log on `MinecraftForge.EVENT_BUS` after successful create. Not a second create path. |

Verified on the published jar (`javap`): `createTeam` is public, unobfuscated, official-mapped class names. Recruits internals were **not** impossible in this environment.

If the player already has a Recruits host named Team 1 / Team 2, the bridge burns that faction and founds the compiled name. If they already have a real host, it **renames the display** to the camp.

## What it reads

After `rallous_factions:contact/assign` → `rallous_recruits_bind:on_contact`:

- score `rallous.rec.id` (fallback `rallous.fac.id` / `rallous.contact_id`)
- storage `rallous_recruits_bind:contact` `{id,name,…}` when the stored id matches
- compiled names 1–129 when storage is missing

On success the player is tagged `rallous.rec.founded` and chat says **Crash-camp host founded: Reikland — not Team 2.**

On `createTeam` not persisting a `RecruitsFaction`, the player is tagged `rallous.rec.bridge_fail` (no silent Team 2).

## Build

Java **17**, Forge **47.4.10**, official mappings. Recruits 1.15.2 is `compileOnly` (Modrinth `2zXpVxK4` = CF 8339846).

```bash
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
./gradlew jar
```

Jar: `build/libs/rallous-recruits-bridge-1.0.0.jar`

Integrator copies any `rallous-recruits-bridge*.jar` into `overrides/mods/`. Ship a copy under `content/mods/` and `pack-src/overrides/mods/`.

## What failed

Nothing required for founding: Recruits jar downloaded, `FactionEvents.createTeam` / `modifyTeam` / `RecruitsFactionManager` readable. Mixin and KubeJS were not needed.

This environment did **not** launch a full Minecraft/Forge server, so in-game U-screen inspect was not clicked here. The call site is the same method Found a Banner uses.
