# rallous_grow

Minecraft **1.20.1** datapack (`pack_format` **15**). Millénaire analogue for this pack: the **7×7 crash camp grows** when you help, win the night, or pay emeralds. No new mods required.

This folder only. Do not run pack integrate. Zip agent may ingest it (jar **or** world datapack, not both).

## How a player grows a place in one night

1. Crash next to a `rallous.camp` (already a 7×7 picket).
2. Run the help / defend night (`rallous_session` → `rallous.session` **1**). That is **+1**, or **+2** if `rallous.session_kind` is help (**1**).
3. Hire a levy or trade / spend **emeralds** within 24 blocks of the banner. Each spend or villager trade is **+1**.
4. At `rallous.grow` **1 / 2 / 3** the camp places a hut, a second hut, then a hall + banners + one settler.

Cap is **3**. Race palettes: Elector / von Carstein hamlet / temple-city / herd / Waaagh / hold / Under-Empire / Bloodbound. Not a modern town hall.

Cheats ON:

```
/function rallous_grow:on_session
```

Or stand at the camp and `/scoreboard players set @e[tag=rallous.camp,limit=1,sort=nearest] rallous.grow 3` then walk near it.

## FTB scores

| Objective | Meaning |
| --- | --- |
| `rallous.grow` | 0–3 on player **and** camp (copy after credit) |
| `rallous.grow_tier` | Structures already placed on that camp (1–3) |
| `rallous.grow_sess` | 1 after this player’s session win was credited |

FTB can task on `rallous.grow` **3**.

## Why not MineColonies tonight

1.20.1 Forge **fileIDs exist** (see `pack/catalog.json` / `pack/mods.json` listed_not_default). MineColonies also needs Structurize, BlockUI, Domum Ornamentum, MultiPiston (~5 extra jars, ~74MB). Recruits already owns claims and armies in 0.3.6. Stacking both as player capitals is the documented performance tax. This datapack is the cheap loop that ships without a zip rebuild.

## Files

`on_session` `credit/session|help|trade` `tick` `tick_trade` `try_apply` `tier/1|2|3` `hut/by_race` + eight race huts `voice/tier1|2|3` `load`

Writes: `rallous.grow` `rallous.grow_tier` `rallous.grow_sess`. Reads: `rallous.session` `rallous.session_kind` `rallous.fac.race` `rallous.race`.
