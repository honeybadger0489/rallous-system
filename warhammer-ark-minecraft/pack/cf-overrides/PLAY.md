# Rallous Warhammer Fantasy — play this

You are a **soldier on the ground** in a first-person Old World: Warhammer Fantasy / Total War: Warhammer factions, lords, magic, and wars, with Ark-style hunger, thirst, temperature, and beast-taming. Not a kitchen-sink pack and not 40k.

**Minecraft 1.20.1 + Forge 47.4.10.** Private friends pack — import locally, do not upload to CurseForge/Modrinth.

Game boot was **not** verified in this environment (no Minecraft GUI here). You verify with the checklist below.

---

## Install (CurseForge app)

1. Download `warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.2.0.zip` from this repo.
2. Open the **CurseForge / Overwolf** app → **Minecraft** → **Create Custom Profile** → **Import**.
3. Choose that zip. Wait until every mod finishes downloading (resource packs bundled in the zip appear immediately).
4. Profile settings: **Java 17**, allocate **8 GB** RAM (10 GB if you can).
5. Play. Create a new world: **Survival**, **Hard**, cheats **ON** for this first test (`/locate` helps). Leave world type default (Terralith takes over biomes).

Shaders and the grimdark packs are pre-selected in `options.txt`. If the sky looks vanilla, Options → Resource Packs and Video Settings → Shader Pack → **Complementary Unbound**.

---

## What you should feel in play

- **Look:** Faithful 32x under Grimdark Battlepack + Grimdark Sky + Gothic font; Complementary Unbound via Oculus.
- **Body:** Legendary Survival Overhaul — thirst bar, temperature, wounded limbs. Seasons change the weather. Eat Farmer’s Delight food; drink (canteen / water).
- **Beasts:** Fossils and Archeology Revival (dig, DNA, raise, tame) plus Tameable Beasts. You earn a mount; you do not craft one.
- **Factions / war:** Villager Recruits armies, vanilla-team diplomacy (ally / enemy), claims and sieges; Vassal & Suzerains for liege/tribute; Ranks and Titles; Open Parties and Claims for warband land; Guard Villagers in towns; siege engines.
- **Lords / faces:** Custom NPCs (unofficial) for authored characters when you place or find them; Recruits captains in the field.
- **Magic:** Iron’s Spells ’n Spellbooks (battle magic: fire, ice, holy, blood, evocation) and Malum (grim occult). Not a rainbow wizard school.
- **Steel:** Epic Fight combat mode + Simply Swords + Magistu Epic Knights plate. **Sons of the Empire** overlay: Empire, Bretonnia, Kislev, Dawi, High Elves, Southern Realms armor (pair with Recruits + Epic Knights).
- **World:** Terralith biomes, CTOV / Towns and Towers settlements, When Dungeons Arise, YUNG’s dungeons, Born in Chaos nights, Enhanced Celestials blood moons.

Dropped on purpose: guns (TaCZ), Create factories, Alex’s Caves, Cataclysm anime bosses, Hammercraft 40k.

---

## New-world test checklist (~25–40 min)

Do these in a **new world**. Open the quest book with **`` ` ``** (grave / tilde key, left of `1`) — chapter **Soldier of the Old World** matches this list. Tick each quest when the game did what the “you should see” line says.

1. **Boot and look**  
   **Do:** Load in, F3 for a second (confirm Forge), then F1-off. Look at the sky, HUD, and your fists. Options → Video Settings → Shader Pack should show Complementary Unbound.  
   **See:** Darker grim sky (not default blue), gothic font in menus, temperature/thirst widgets near the hotbar, Xaero minimap. If shaders are black, disable the shader pack once, then re-enable Unbound.

2. **Survive the body**  
   **Do:** Sprint until hungry. Find water; drink (sneak + use on a water source, or a bottle/canteen). Stand in shade vs sun; wait a minute.  
   **See:** Hunger drops; **thirst** drops with it; the temperature icon moves toward hot or cold. You are not a creative super-soldier.

3. **Find steel and fight like a soldier**  
   **Do:** Punch wood, make a crafting table, craft any sword (or grab Simply Swords / Epic Knights from JEI in cheat-mode if you enabled cheats — or `/give` a `minecraft:iron_sword`). Open **Controls**, search `Epic Fight`, bind **Combat Mode** to `V` if it is still on `R` (JEI uses R). Press combat mode, then left-click / right-click guard.  
   **See:** Third-person-ish combat stance, directional attacks, a guard pose. This is melee, not click-spam.

4. **Town**  
   **Do:** Open **Xaero’s World Map** (default `M`). Look for village / town markers. Walk or `/locate structure minecraft:village_plains` (or any village). Enter the settlement.  
   **See:** Overhauled / Towns-and-Towers architecture, not a six-house vanilla village. **Guard Villagers** with swords or crossbows on patrol. Jade overlay names blocks/mobs when you look at them.

5. **Recruit a host**  
   **Do:** Get emeralds (trade, chest, or `/give @s emerald 16`). Right-click a **Recruit** villager (player-model soldier in town, not a farmer). Hire. Open the Recruits command GUI (Controls → search `Recruit`). Issue a follow / hold command.  
   **See:** A named soldier with a player body, hire cost, then them following you. This is your first warband, not a pet wolf.

6. **Faction / alliance / war verbs**  
   **Do:** Recruits team GUI → create or join a team (your “Elector / lord”). Set another team (or a second player later) to **Ally** then **Enemy**. Place a claim banner / use the Recruits claim tool if the hire GUI mentions claims. Open **Open Parties and Claims** party screen (Controls → search `Parties` or `OPAC`) and create a party named after a province.  
   **See:** Ally = no friendly fire; Enemy = they are valid war targets. Claims show on the map. Vassal & Suzerains adds a hierarchy / tribute screen on the Recruits stack (Controls → search `Vassal` / `Suzerain`) — open it even if you have no vassal yet; the UI should exist.

7. **Magic**  
   **Do:** JEI search `spell book` or `ink`. Craft (or `/give`) Iron’s **iron spell book** plus a simple scroll/ink if the recipe is long — with cheats, `/give @s irons_spellbooks:iron_spell_book`. Put it in the **Curios spellbook slot** (open inventory, cosmetic/curios row). Controls → search `Spell`; open the **spell wheel**.  
   **See:** Spell wheel / bar, mana, a cast animation. Fire / ice / holy should read as battle magic, not rainbow fireworks. (Malum is the slower occult tree — ignore it for this test unless you want a spirit-farm detour.)

8. **Beast (Ark loop)**  
   **Do:** JEI search `fossil` / `bio-fossil` / `analyzer`. Dig in stone and gravel until you get a fossil, **or** `/locate` a Fossils structure / `/give` a fossil item if the clock is running down. Follow the analyzer → culture vat → egg/embryo loop as JEI shows. Alternatively tame a **Tameable Beasts** creature (look at it with Jade; use the food Jade lists).  
   **See:** A living prehistoric (or Tameable Beasts) creature that you own — sit/follow, not a vanilla horse you spawned.

9. **A fight that is not two zombies**  
   **Do:** Night in the wild, or a When Dungeons Arise / YUNG dungeon (`/locate` `dungeons_arise` or `betterdungeons` structures if names show in tab-complete). Take your recruit. Use combat mode. If a **blood moon** is up (Enhanced Celestials), even better.  
   **See:** Recruits fighting with you; grim mobs (Born in Chaos counts); you managing thirst/health during the fight. If you find a **siege engine** (Siege Machines mod), place/fire it at a wall or claim for the Total War beat.

10. **Siege / war if it triggers**  
    **Do:** At a village you do **not** own: Recruits siege / claim capture if the version’s GUI shows Siege. Or build a **siege machine**, crew it, hit a wall. Ring a bell; watch guards aggro.  
    **See:** Either a claim changing hands, guards defending, or artillery doing structure damage. If siege does not start in 40 minutes, you still pass if step 6’s Ally/Enemy UI worked — note that in chat and stop.

11. **Wear the Old World**  
    **Do:** JEI search `empire`, `bretonnia`, `kislev`, `dwarf`, `elf` (Sons of the Empire). Craft or `/give` one helmet + chestplate. Equip. Stand next to your recruit.  
    **See:** WH Fantasy silhouettes, not generic iron. Recruits already use human models so the helmets sit on a soldier’s head.

Tick the matching quest in the book when each line is true. That is the pack working.

---

## Keys worth searching (Controls → search box)

| Search | What it is |
| --- | --- |
| Epic Fight / combat / dodge | Melee stance. Move Combat Mode off `R` if JEI steals it. |
| Spell / spell wheel | Iron’s battle magic |
| Recruit | Army command |
| Vassal / Suzerain | Feudal hierarchy |
| Parties / claims / OPAC | Warband land |
| Quests (`` ` ``) | This checklist in-game |
| Xaero / world map (`M`) | Find towns |

---

## If import complains

- Forge must be **1.20.1**. The zip’s `manifest.json` already asks for Forge 47.4.10.
- “Missing mods” for Sons of the Empire / resource packs: they live in the zip `overrides/` folder (official Modrinth files). Re-import the zip; do not download random jars from other websites.
- This pack is **not** published. Friends get the zip from you, same Import flow.
