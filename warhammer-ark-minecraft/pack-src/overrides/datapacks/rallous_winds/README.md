# Rallous Winds

Minecraft **1.20.1** datapack (`pack_format` **15**). The Winds are a **path**, not a crater loadout.

No new mods. This folder only. Zip agent may ingest it (jar **or** world datapack, not both). Do not rebuild the zip from here. Do not `/give` a filled Iron's spellbook.

## How a player finds magic in the first hour

1. Crash chest is bread / leather / stone. **No** spellbook. `strip` runs once after warp-land if Iron's still handed you a book.
2. Walk to the nearest bannered camp (minutes).
3. A **named lectern** holds a letter (College / Ice / Grave / Vein) that points to Iron's **ink** and **scrolls**.
4. Open the camp barrel. Rare: `irons_spellbooks:common_ink` plus the same letter. Never a filled spellbook.
5. Dungeon / library / stronghold chests already hide Iron's ink and scrolls (the mod). Inscribe at an inscription table.
6. Spell wheel (**R**) waits until you have **earned** a book.

| Camp | Letter |
| --- | --- |
| Empire / Lizardmen | Colleges |
| Nordland, Ostland, Hochland, Middenland, snow | Ice |
| Vampire Counts | Death |
| Lahmian Sisterhood, Khorne, Beastmen | Blood |
| Other races | Primer (points to the four) |

Cheats:

```
/function rallous_winds:hint
/function rallous_winds:place_here
```

`place_here` plants the lectern at your feet from the nearest camp's race (or a primer). It does **not** give a spellbook.

## Scores / advancements

Finding a letter sets `rallous.magic` 1–4 and grants `rallous_winds:*` plus the matching `rallous_contact:magic/*` backup.

## Files

`load` `tick` `hint` `strip` `place` `place_here` `try_lectern` `try_barrel` `set_lectern` `place/*` `found/*`
