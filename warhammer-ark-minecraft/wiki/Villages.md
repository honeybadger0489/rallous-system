# Villages that grow

Millénaire’s trick: a camp gets **bigger** because you helped it, not because you placed a town hall.

This pack does **not** ship MineColonies in the 0.3.6 zip. Recruits already owns banners and claims. Guard Villagers and Towns and Towers already make *other people’s* towns look alive. The cheap loop that ships is **`rallous_grow`** on the 7×7 crash camp.

Research and CurseForge fileIDs: [content/VILLAGES.md](../content/VILLAGES.md).

## One night

1. Crash. Walk to the nearest **bannered picket** (`rallous.camp`).
2. Do the **help** night — `/function rallous_session:start` or wait for night at that camp. When `rallous.session` is **1**, the camp gains growth. Help/defend is worth **two** marks.
3. **Pay emeralds** within 24 blocks (hire a levy, or trade the lord). Each spend or villager trade is **+1**.
4. Watch the pad:

| `rallous.grow` | What appears (outside the 7×7) |
| --- | --- |
| **1** | First hut + banner (east) |
| **2** | Second hut (west) |
| **3** | Hall (south), extra banners, one settler |

Cap **3**. FTB can task on `rallous.grow` **3**.

## What it is called (not a town hall)

The same 7×7, race-flavoured:

| Race | Score | The grown place |
| --- | --- | --- |
| Empire | 1 | Elector outpost |
| Vampire Counts | 2 | von Carstein hamlet |
| Lizardmen | 3 | Temple-city outpost |
| Beastmen | 4 | Herd camp |
| Greenskins | 5 | Waaagh camp |
| Dwarfs | 6 | Hold outpost |
| Skaven | 7 | Under-Empire warren |
| Khorne | 8 | Bloodbound shrine |

## Cheats

```
/function rallous_grow:on_session
```

Or set the nearest camp to tier 3 and walk up to it:

```
/scoreboard players set @e[tag=rallous.camp,limit=1,sort=nearest] rallous.grow 3
```

## MineColonies (later, optional)

1.20.1 Forge **fileIDs exist** on CurseForge (`245506` / release **8615315**). Not on Modrinth. Needs Structurize, BlockUI, Domum Ornamentum, MultiPiston. Catalog-only — do not stack with Recruits as a second capital. If you enable it later, name the colony an Elector / temple-city / hold / Under-Empire **outpost**.
