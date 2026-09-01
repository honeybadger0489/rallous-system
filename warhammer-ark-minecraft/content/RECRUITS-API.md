# Recruits 1.20.1 Java API — banners / factions

Research note for **rallous-recruits-bridge**. Do not start a second Java project. Call Recruits’ own Found-a-Banner server method.

Pinned pack jar: Villager Recruits **1.20.1-1.15.2** (`recruits`, CurseForge `fileID` 8339846 / Modrinth `2zXpVxK4`). Source: [talhanation/recruits](https://github.com/talhanation/recruits) `main` (Forge **47.4.10**, official mappings, `mods.toml` `version='1.15.2'`, last push 2026-06-29). File paths below are that tree.

There is **no** datapack or `/recruits admin` create. `/recruits admin factionManager` is get/set NPC count, get/set leader, **delete**. Vanilla `/team add` is intercepted and must not be used as a scoreboard-only host (that is how Team 2 happens).

---

## The one class to hook

**`com.talhanation.recruits.FactionEvents`**

That is the Found-a-Banner server entry. Mixin is optional. Prefer a direct call (same as Recruits’ intercepted `/team add`).

```java
// menu=false skips emerald cost + cloth-banner uniqueness (same as /team add intercept)
FactionEvents.createTeam(
    false,
    serverPlayer,
    serverLevel,
    teamName,          // scoreboard / stringID, max 32 chars
    displayName,       // pretty name shown in U inspect
    serverPlayer.getScoreboardName(),
    bannerStack,       // ItemStack; null becomes brown banner
    ChatFormatting.RED,
    (byte) 12          // unitColors INDEX, not a vanilla dye id (12 = red)
);
```

Manager singleton (null until `ServerStartingEvent`):

```java
RecruitsFactionManager mgr = FactionEvents.recruitsFactionManager;
RecruitsFaction faction = mgr.getFactionByStringID(teamName);
mgr.save(server.overworld());
```

---

## Recommended mixin / event (rallous-recruits-bridge)

**Do not mixin to found a host.** Call `FactionEvents.createTeam(false, …)` after `rallous_recruits_bind:on_contact` writes `rallous.rec.id` / storage `rallous_recruits_bind:contact`. Recruits already exposes this as a public static.

**Subscribe (confirm / diplomacy / tag), do not invent a second create path:**

```java
@SubscribeEvent
public void onFactionCreated(com.talhanation.recruits.FactionEvent.Created event) {
    RecruitsFaction faction = event.getFaction();
    ServerPlayer leader = event.getCreator(); // null if console
    // event.setCanceled(true) rolls back via FactionEvents.removeTeam
}
```

Bus: `MinecraftForge.EVENT_BUS`. Posted **after** scoreboard team + `addTeam` + `save`. Cancelable.

**Mixin only if** you must rewrite a player-typed U-screen name (not needed for crash-camp founding):

```java
@Mixin(com.talhanation.recruits.FactionEvents.class)
public class MixinFactionEvents {
    @Inject(
        method = "createTeam(ZLnet/minecraft/server/level/ServerPlayer;Lnet/minecraft/server/level/ServerLevel;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lnet/minecraft/world/item/ItemStack;Lnet/minecraft/ChatFormatting;B)V",
        at = @At("HEAD")
    )
    private static void rallous$createTeamHead(boolean menu, ServerPlayer serverPlayer, ServerLevel level,
            String teamName, String displayName, String playerName, ItemStack banner,
            ChatFormatting color, byte colorByte, CallbackInfo ci) {
        // inspect / rewrite locals — do not add a second create implementation
    }
}
```

Do **not** mixin `MessageCreateTeam` (client packet only). Do **not** write `recruitsTeamSaveData` NBT by hand.

---

## Create path (Java)

```
U key → FactionMainScreen
  → FactionEvents.openTeamEditScreen(player)
  → FactionEditScreen (create)
  → Main.SIMPLE_CHANNEL.sendToServer(new MessageCreateTeam(stringID, displayName, banner, teamColor, unitIndex))
  → MessageCreateTeam.executeServerSide
  → FactionEvents.createTeam(true, sender, world, teamName, displayName, playerName, banner, color, (byte) index)
      → scoreboard.addPlayerTeam(teamName)
      → newTeam.setDisplayName / setColor / friendly-fire flags
      → scoreboard.addPlayerToTeam(playerName, newTeam)
      → doPayment if menu
      → RecruitsFactionManager.addTeam(...)
      → RecruitsFaction.addMember(uuid, name)
      → add existing AbstractRecruitEntity owners onto the team
      → RecruitsFactionManager.save(overworld)
      → MinecraftForge.EVENT_BUS.post(new FactionEvent.Created(...))
```

`/team add <name>` (player): `FactionEvents.onTypeCommandEvent` → `createTeam(false, …)` using main-hand banner or brown. Console: private `createTeamConsole` (leader UUID `0,0`, name `"none"`, **13**-char cap — do not use).

---

## Copy-paste method names

### `com.talhanation.recruits.FactionEvents`

```java
public static RecruitsFactionManager recruitsFactionManager;
public static RecruitsDiplomacyManager recruitsDiplomacyManager;
public static RecruitsTreatyManager recruitsTreatyManager;

public static void createTeam(boolean menu, ServerPlayer serverPlayer, @NotNull ServerLevel level,
        String teamName, String displayName, String playerName,
        ItemStack banner, ChatFormatting color, byte colorByte);

public static void modifyTeam(ServerLevel level, String stringID, RecruitsFaction editedTeam,
        @Nullable ServerPlayer serverPlayer, int cost);

public static void removeTeam(ServerLevel level, String teamName);
public static void leaveTeam(boolean command, ServerPlayer player, String teamName, ServerLevel level, boolean fromLeader);
public static void addPlayerToTeam(@Nullable ServerPlayer player, ServerLevel level, String teamName, String namePlayerToAdd);
public static void addRecruitToTeam(AbstractRecruitEntity recruit, Team team, ServerLevel level);
public static void addNPCToData(ServerLevel level, String teamName, int x);
public static void serverSideUpdateTeam(ServerLevel level);
public static boolean isPlayerAlreadyAFactionLeader(ServerPlayer playerToCheck);
public static void openTeamEditScreen(Player player);
```

`createTeam` gates (in order): team already exists → name `chars().count() > 32` → blank → `isNameInUse` → (if `menu`) not enough currency → (if `menu`) `isBannerBlank` → (if `menu`) `isBannerInUse`. Failures only send `chat.recruits.team_creation.*` and return. Success always `save`s then posts `FactionEvent.Created`.

### `com.talhanation.recruits.world.RecruitsFactionManager`

```java
public void load(ServerLevel level);
public void save(ServerLevel level);          // writes SavedData + broadcasts
public Collection<RecruitsFaction> getFactions();
@Nullable public RecruitsFaction getFactionByStringID(String stringID);
public void addTeam(String teamName, String teamDisplayName, UUID leaderUUID, String leaderName,
        CompoundTag bannerNbt, byte color, ChatFormatting teamColor);
public void removeTeam(String teamName);
public boolean isNameInUse(String factionName);
public boolean isDisplayNameInUse(String displayName);
public boolean isBannerInUse(CompoundTag bannerNbt);
public static boolean isBannerBlank(ItemStack itemStack); // no BlockEntityTag.Patterns
public void broadcastFactionsToPlayer(Player player);
public void broadcastFactionsToAll(ServerLevel serverLevel);
```

Lookup key is **stringID** (`teamName`), not display name. Vanilla `/team add` without this map → `getFactionByStringID` is null → Team 1 / Team 2.

### `com.talhanation.recruits.world.RecruitsFaction`

```java
public String getStringID();
public String getTeamDisplayName();
public UUID getTeamLeaderUUID();
public String getTeamLeaderName();
public CompoundTag getBanner();
public byte getUnitColor();
public int getTeamColor();
public void setTeamDisplayName(String teamDisplayName);
public void setBanner(CompoundTag nbt);
public void setUnitColor(byte unitColor);
public void setTeamColor(int color);
public void addMember(UUID uuid, String name);
public CompoundTag toNBT();
public static RecruitsFaction fromNBT(CompoundTag nbt);
public static CompoundTag toNBT(List<RecruitsFaction> list); // {Teams:[...]}
```

### Diplomacy

```java
// FactionEvents.recruitsDiplomacyManager
public void setRelation(String team, String otherTeam, DiplomacyStatus relation, ServerLevel level);
public DiplomacyStatus getRelation(String team, String otherTeam); // default NEUTRAL

// RecruitsDiplomacyManager.DiplomacyStatus
NEUTRAL((byte) 0), ALLY((byte) 1), ENEMY((byte) 2);
public static DiplomacyStatus fromByte(byte value);

// admin (both directions). Requires two existing stringIDs.
// /recruits admin diplomacyManager setRelations <A> <B> Ally|Neutral|Enemy
```

`setRelation` posts cancelable `com.talhanation.recruits.DiplomacyEvent.RelationChanged`.

### Hire (not a faction create)

```java
// client → server
new MessageHire(playerUUID, recruitUUID, groupUUID);
// server
CommandEvents.handleRecruiting(player, group, recruit, true);
```

No `/recruits hire`.

---

## Packets (`com.talhanation.recruits.network`)

Channel: `Main.SIMPLE_CHANNEL` (`recruits` / `"default"`, de.maxhenkel.corelib `Message`).

| Class | Side | Payload |
| --- | --- | --- |
| `MessageCreateTeam` | C→S | `readUtf teamName`, `readUtf displayName`, `readItem banner`, `readInt ChatFormatting id`, `readInt unitColorIndex` → `createTeam(true, …)` |
| `MessageSaveTeamSettings` | C→S | edited `RecruitsFaction` + cost → `modifyTeam` |
| `MessageChangeDiplomacyStatus` | C→S | `ownTeam` utf, `otherTeam` utf, `status` byte → `setRelation` |
| `MessageToClientUpdateFactions` | S→C | `RecruitsFaction.toNBT(list)` + editing/managing flags + currency + prices |
| `MessageToClientUpdateOwnFaction` | S→C | one `RecruitsFaction.toNBT()` (empty = no host) |
| `MessageToClientUpdateDiplomacyList` | S→C | diplomacy map |
| `MessageHire` | C→S | player / recruit / group UUIDs |

Client create send (from `FactionEditScreen`):

```java
Main.SIMPLE_CHANNEL.sendToServer(new MessageCreateTeam(
    getCorrectFormatStringID(text),  // spaces → then strip [^\\p{L}\\p{N} ]
    getCorrectFormatName(text),      // strip [^\\p{L}\\p{N} ], keep spaces
    banner,
    teamColor,
    unitColors.indexOf(unitColor)
));
```

ID sanitizer: `"Clan Mors"` → stringID **`ClanMors`**, display **`Clan Mors`**. `"The Drakenhof Conclave"` → **`TheDrakenhofConclave`**. Bridge should use the same (spaces out of stringID) so U-inspect and `getFactionByStringID` match. Length 3–32 on the typed name.

---

## NBT

### World save — `RecruitsTeamSaveData`

`ServerLevel` overworld `SavedData` file id **`recruitsTeamSaveData`**.

```
Teams: ListTag of CompoundTag
  TeamName            String   stringID
  TeamDisplayName     String
  TeamLeaderID        UUID
  TeamLeaderName      String
  TeamBanner          Compound  ItemStack.serializeNBT() of the banner
  Players             Int
  NPCs                Int
  MaxPlayers          Int
  MaxNPCs             Int
  JoinRequests        ListTag of String
  Color               Byte     unitColors index
  TeamColor           Int      ChatFormatting.getId()
  maxNpcsPerPlayer    Int
```

Members are **not** in this file. `FactionEvents.onPlayerJoin` re-`addMember`s if the player is on the scoreboard team.

Do not confuse with `RecruitsFaction.toNBT()` (packets / `fromNBT`), which uses different keys: `teamName`, `teamDisplayName`, `teamLeaderID`, `teamLeaderName`, `banner`, `joinRequests`, `members`, `players`, `npcs`, `maxPlayers`, `maxNpcs`, `unitColor`, `teamColor`, `biome`, `maxNPCsPerPlayer`. List wrapper `{Teams:[...]}`.

### Diplomacy save — `RecruitsDiplomacySaveData`

File id **`diplomacy_data`**.

```
teams: Compound
  <stringID>: Compound
    <otherStringID>: Byte   0 Neutral / 1 Ally / 2 Enemy
embargoes: Compound
  <playerUUID>: String      csv of declaring stringIDs
```

### Banner stack

`ItemStack.serializeNBT()` stored as `TeamBanner` / packet `banner`. Blank = no `BlockEntityTag.Patterns` (`isBannerBlank`). `menu=false` skips blank/unique checks; still give a patterned banner so U-inspect is not a void cloth.

`unitColor` **byte is `FactionEditScreen.unitColors` index**, not `DyeColor.getId()`:

| index | colour |
| --- | --- |
| 0 | white |
| 1 | black |
| 9 | green |
| 12 | red |
| 13 | dark red |
| 15 | brown |
| 20 | yellow |

Passing dye id `14` (red dye) is **wrong** (that index is light brown).

---

## Forge events (`com.talhanation.recruits.FactionEvent`)

Package is `com.talhanation.recruits` (file lives under `events/`). Server-only, `MinecraftForge.EVENT_BUS`.

| Event | When | Cancel |
| --- | --- | --- |
| `FactionEvent.Created` | after successful `createTeam` | yes → `removeTeam` |
| `FactionEvent.Disbanded` | before dissolve | no |
| `FactionEvent.PlayerJoined` | before join | yes |
| `FactionEvent.PlayerLeft` | still a member | no |
| `DiplomacyEvent.RelationChanged` | before `setRelation` | yes |

```java
event.getFaction();           // RecruitsFaction
event.getLevel();             // ServerLevel
((FactionEvent.Created) e).getCreator(); // ServerPlayer or null
```

---

## What the datapack cannot do

`rallous_recruits_bind` writes scores / storage / book only. It does not create a `RecruitsFaction`. After assign, the bridge must call `FactionEvents.createTeam`. Then:

```java
// optional: path stance → Recruits Ally / Enemy (needs a second existing stringID)
FactionEvents.recruitsDiplomacyManager.setRelation(
    playerTeamId, otherTeamId,
    RecruitsDiplomacyManager.DiplomacyStatus.ALLY, // or ENEMY
    level);
```

Rename an already-real host (not Team 2): `setTeamDisplayName` + `playerTeam.setDisplayName` + `mgr.save`, or `FactionEvents.modifyTeam`. Burn Team 1 / Team 2: `FactionEvents.removeTeam(level, genericName)` then `createTeam`.

---

## Sources

- [talhanation/recruits](https://github.com/talhanation/recruits) `FactionEvents.java`, `RecruitsFaction.java`, `RecruitsFactionManager.java`, `RecruitsTeamSaveData.java`, `RecruitsDiplomacyManager.java`, `RecruitsDiplomacySaveData.java`, `MessageCreateTeam.java`, `MessageChangeDiplomacyStatus.java`, `MessageToClientUpdateFactions.java`, `MessageToClientUpdateOwnFaction.java`, `events/FactionEvent.java`, `events/DiplomacyEvent.java`, `commands/RecruitsAdminCommands.java`, `client/gui/faction/FactionEditScreen.java`, `client/gui/faction/FactionMainScreen.java`, `META-INF/mods.toml` (`1.15.2`).
- Pack pin: `warhammer-ark-minecraft` Recruits 1.15.2 / CF 8339846.
