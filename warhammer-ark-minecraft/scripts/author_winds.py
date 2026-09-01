#!/usr/bin/env python3
"""Author rallous_winds: camp lecterns + barrel loot pointing to Iron's ink/scroll.

No filled spellbook. No /give of irons_spellbooks:*_spell_book.
Writes content/datapacks/rallous_winds/ and copies to pack-src + cf-overrides.
Does not rebuild the zip.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "content" / "datapacks" / "rallous_winds"
COPIES = (
    ROOT / "pack" / "cf-overrides" / "datapacks" / "rallous_winds",
    ROOT / "pack-src" / "overrides" / "datapacks" / "rallous_winds",
    ROOT / "pack-src" / "datapacks" / "rallous_winds",
)

SCHOOLS = {
    1: {
        "id": "colleges",
        "title": "College Letter",
        "author": "A licensed scribe",
        "stand": "College Letter",
        "color": "gold",
        "icon": "minecraft:blaze_powder",
        "adv_title": "Path to the Colleges",
        "adv_desc": "A lectern letter. Iron's ink, then a scroll. rallous.magic=1",
        "found": "A College path. Ink and a scroll, not a crater book.",
        "found_color": "gold",
        "pages": [
            "Altdorf does not mail a book into the crater. You walked here.",
            "Find Iron's common ink in this camp barrel, or in dungeon and library chests. Inscribe a scroll at an inscription table.",
            "Fire and holy light are College work. The spell wheel (R) stays dead until you have earned a book. Do not expect a filled spellbook in the wreckage.",
        ],
    },
    2: {
        "id": "ice",
        "title": "Kislevite Ice Primer",
        "author": "A northern courtier",
        "stand": "Ice Primer",
        "color": "aqua",
        "icon": "minecraft:packed_ice",
        "adv_title": "Path to Ice",
        "adv_desc": "North talk on a lectern. Iron's ink in the cold. rallous.magic=2",
        "found": "An Ice path. A court, not a novelty. Ink first.",
        "found_color": "aqua",
        "pages": [
            "Ice is a court, not a novelty. The north does not hand you a staff at the crash.",
            "Hunt this barrel and snow ruins for Iron's ink. Inscribe ice on a scroll. The crater had none.",
            "Spell wheel (R) waits. Steel and thirst until the ink is yours.",
        ],
    },
    3: {
        "id": "death",
        "title": "Grave Missive",
        "author": "A priest who does not smile",
        "stand": "Grave Missive",
        "color": "dark_purple",
        "icon": "minecraft:wither_skeleton_skull",
        "adv_title": "Path to Death",
        "adv_desc": "Grave-talk on a lectern. Crypt ink, not a necronomicon. rallous.magic=3",
        "found": "A Death path. Grave-talk. Ink in crypts, not a starter necronomicon.",
        "found_color": "dark_purple",
        "pages": [
            "A priest who does not smile left this on the lectern.",
            "Iron's ink and scrolls hide in crypts, dungeon chests, and this barrel. Necromancy is a path you walk.",
            "No starter necronomicon. The wreckage was bread and leather.",
        ],
    },
    4: {
        "id": "blood",
        "title": "Vein Rite",
        "author": "A cellar scribe",
        "stand": "Vein Rite",
        "color": "dark_red",
        "icon": "minecraft:redstone",
        "adv_title": "Path to Blood",
        "adv_desc": "A cellar letter. Iron's ink, then the wheel. rallous.magic=4",
        "found": "A Blood path. A rite. Ink first, then a scroll.",
        "found_color": "dark_red",
        "pages": [
            "A count's cellar. A wheel that smells of iron. Blood is a school you walk to.",
            "Take Iron's ink from this barrel or from ruin chests. Inscribe a scroll. Do not expect a filled spellbook.",
            "Lahmia and the Blood Host keep the rumour. The crater did not.",
        ],
    },
    0: {
        "id": "primer",
        "title": "The Winds Are a Path",
        "author": "A nameless survivor",
        "stand": "The Winds",
        "color": "gray",
        "icon": "minecraft:amethyst_shard",
        "adv_title": "The Winds",
        "adv_desc": "No starter spellbook. Walk to a camp lectern.",
        "found": "The Winds are not a hotbar.",
        "found_color": "gray",
        "pages": [
            "You crashed with steel and thirst. There is no college letter in the crater chest.",
            "Walk to a bannered camp. Read the named lectern. That letter is the path.",
            "Iron's ink and scrolls hide in dungeon and library chests. Inscribe later. Do not /give yourself a filled spellbook.",
        ],
    },
}


def dump_json(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n", encoding="utf-8")


def pages_snbt(pages: list[str]) -> str:
    parts = []
    for p in pages:
        p = p.replace("'", "\u2019")
        parts.append("'" + json.dumps({"text": p}, ensure_ascii=False) + "'")
    return "[" + ",".join(parts) + "]"


def book_tag(school: dict) -> str:
    return (
        f'title:"{school["title"]}",author:"{school["author"]}",'
        f'pages:{pages_snbt(school["pages"])},'
        f'rallous:{{winds:1b,school:"{school["id"]}"}}'
    )


def book_item_nbt(school: dict) -> str:
    return "{" + book_tag(school) + "}"


def lectern_command(school: dict) -> str:
    name = json.dumps({"text": school["stand"], "color": school["color"]}, ensure_ascii=False)
    stand = json.dumps({"text": school["stand"], "color": school["color"], "bold": True}, ensure_ascii=False)
    tag = book_tag(school)
    return (
        f"setblock ~ ~ ~ minecraft:lectern[facing=south,has_book=true]"
        f"{{CustomName:'{name}',Book:{{id:\"minecraft:written_book\",Count:1b,tag:{{{tag}}}}}}}\n"
        f"summon minecraft:armor_stand ~ ~ ~ "
        f"{{CustomName:'{stand}',CustomNameVisible:1b,Invisible:1b,Marker:1b,"
        f"NoGravity:1b,Invulnerable:1b,Small:1b,"
        f'Tags:["rallous.winds","rallous.winds.mark","rallous.winds.{school["id"]}"]}}\n'
    )


def loot_table(school: dict) -> dict:
    book_nbt = (
        f'{{title:"{school["title"]}",author:"{school["author"]}",'
        f'pages:{pages_snbt(school["pages"])},'
        f'rallous:{{winds:1b,school:"{school["id"]}"}}}}'
    )
    return {
        "type": "minecraft:chest",
        "pools": [
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:written_book",
                        "functions": [
                            {"function": "minecraft:set_nbt", "tag": book_nbt}
                        ],
                    }
                ],
            },
            {
                "rolls": 1,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": "irons_spellbooks:common_ink",
                        "weight": 3,
                    },
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:ink_sac",
                        "weight": 4,
                        "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 3}}],
                    },
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:book",
                        "weight": 3,
                    },
                    {
                        "type": "minecraft:item",
                        "name": "minecraft:paper",
                        "weight": 4,
                        "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 4}}],
                    },
                    {"type": "minecraft:empty", "weight": 6},
                ],
            },
        ],
    }


def adv(title: str, desc: str, icon: str, parent: str | None, criteria: dict, rewards_fn: str | None = None) -> dict:
    obj: dict = {
        "display": {
            "icon": {"item": icon},
            "title": {"text": title},
            "description": {"text": desc},
            "frame": "task",
            "announce_to_chat": False,
            "show_toast": True,
            "hidden": False,
        },
        "criteria": criteria,
        "requirements": [[k] for k in criteria],
    }
    if parent:
        obj["parent"] = parent
    else:
        obj["display"]["background"] = "minecraft:textures/block/amethyst_block.png"
        obj["display"]["frame"] = "challenge"
    if rewards_fn:
        obj["rewards"] = {"function": rewards_fn}
    return obj


def book_crit(school_id: str) -> dict:
    return {
        "trigger": "minecraft:inventory_changed",
        "conditions": {
            "items": [
                {
                    "items": ["minecraft:written_book"],
                    "nbt": f'{{rallous:{{school:"{school_id}"}}}}',
                }
            ]
        },
    }


def write_pack() -> None:
    if SRC.exists():
        shutil.rmtree(SRC)

    dump_json(
        SRC / "pack.mcmeta",
        {
            "pack": {
                "pack_format": 15,
                "description": "Rallous Winds — camp lecterns point to Iron's ink/scroll. No starter spellbook.",
            }
        },
    )
    w(
        SRC / "META-INF" / "mods.toml",
        """modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="rallous_winds"
version="1.0.0"
displayName="Rallous Winds"
authors="Rallous System"
description='''Camp lecterns and rare barrel loot point to Iron's ink and scrolls. No filled spellbook. No new mods.'''
""",
    )
    w(
        SRC / "README.md",
        """# Rallous Winds

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
""",
    )

    dump_json(SRC / "data" / "minecraft" / "tags" / "functions" / "load.json", {"values": ["rallous_winds:load"]})
    dump_json(SRC / "data" / "minecraft" / "tags" / "functions" / "tick.json", {"values": ["rallous_winds:tick"]})

    fn = SRC / "data" / "rallous_winds" / "functions"
    w(
        fn / "load.mcfunction",
        """# rallous_winds — lectern path to Iron's ink/scroll. No starter spellbook.
scoreboard objectives add rallous.winds dummy
scoreboard objectives add rallous.magic dummy
scoreboard objectives add rallous.kislev dummy
scoreboard objectives add rallous.fac.race dummy
execute unless score #clock rallous.winds = #clock rallous.winds run scoreboard players set #clock rallous.winds 0
""",
    )
    w(
        fn / "tick.mcfunction",
        """# Pulse: strip crash magic once, plant lecterns on new camps.
scoreboard players add #clock rallous.winds 1
execute if score #clock rallous.winds matches 20.. run function rallous_winds:pulse
execute if score #clock rallous.winds matches 20.. run scoreboard players set #clock rallous.winds 0
""",
    )
    w(
        fn / "pulse.mcfunction",
        """execute as @a[tag=rallous.warp_landed,tag=!rallous.winds.stripped] run function rallous_winds:strip
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds] at @s run function rallous_winds:place
""",
    )
    w(
        fn / "strip.mcfunction",
        """# Once after crash. Clears a default Iron's book if the jar still handed one out.
# Does not run again, so later ink/scroll finds stay.
function rallous_old_world:crash/strip_starter_magic
tag @s add rallous.winds.stripped
""",
    )
    w(
        fn / "hint.mcfunction",
        """tellraw @s {"text":"The Winds (first hour)","color":"dark_purple","bold":true}
tellraw @s {"text":"Crash chest: bread, leather, stone. No Iron's spellbook.","color":"gray"}
tellraw @s {"text":"1. Walk to the nearest bannered camp.","color":"white"}
tellraw @s {"text":"2. Read the named lectern. Take the letter. That is the path.","color":"white"}
tellraw @s {"text":"3. Open the camp barrel. Rare: Iron's common ink. Never a filled spellbook.","color":"white"}
tellraw @s {"text":"4. Dungeon / library / stronghold chests also hide Iron's ink and scrolls.","color":"white"}
tellraw @s {"text":"5. Inscribe at an inscription table. Spell wheel (R) waits until you have earned a book.","color":"white"}
tellraw @s {"text":"Empire / Lizardmen lecterns → Colleges. Snow / Nordland / Ostland / Hochland / Middenland → Ice. Vampire graves → Death. Lahmia, Khorne, Beastmen → Blood.","color":"gray"}
""",
    )
    w(
        fn / "place.mcfunction",
        """# As a rallous.camp marker. One lectern + barrel loot. No spellbook.
tag @s add rallous.winds
scoreboard players set $school rallous.winds 0
execute if score @s rallous.fac.race matches 1 run scoreboard players set $school rallous.winds 1
execute if score @s rallous.fac.race matches 3 run scoreboard players set $school rallous.winds 1
execute if score @s rallous.fac.race matches 2 run scoreboard players set $school rallous.winds 3
execute if score @s rallous.fac.race matches 4 run scoreboard players set $school rallous.winds 4
execute if score @s rallous.fac.race matches 8 run scoreboard players set $school rallous.winds 4
execute if entity @s[tag=rallous.fac.nordland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.ostland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.hochland] run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.middenland] run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_plains run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_taiga run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_beach run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:ice_spikes run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:frozen_peaks run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:snowy_slopes run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:frozen_river run scoreboard players set $school rallous.winds 2
execute if biome ~ ~ ~ minecraft:jagged_peaks run scoreboard players set $school rallous.winds 2
execute if entity @s[tag=rallous.fac.lahmian_sisterhood] run scoreboard players set $school rallous.winds 4
function rallous_winds:try_lectern
function rallous_winds:try_barrel
""",
    )
    w(
        fn / "place_here.mcfunction",
        """# Cheats: plant a path lectern at your feet. Uses nearest camp race if any.
scoreboard players set $school rallous.winds 0
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest,distance=..48] run scoreboard players operation $tmp rallous.winds = @s rallous.fac.race
execute if score $tmp rallous.winds matches 1 run scoreboard players set $school rallous.winds 1
execute if score $tmp rallous.winds matches 3 run scoreboard players set $school rallous.winds 1
execute if score $tmp rallous.winds matches 2 run scoreboard players set $school rallous.winds 3
execute if score $tmp rallous.winds matches 4 run scoreboard players set $school rallous.winds 4
execute if score $tmp rallous.winds matches 8 run scoreboard players set $school rallous.winds 4
execute align xyz positioned ~0.5 ~ ~0.5 run function rallous_winds:set_lectern
tellraw @s {"text":"A Winds lectern. The letter points to Iron's ink. No spellbook.","color":"gray"}
""",
    )
    w(
        fn / "try_lectern.mcfunction",
        """execute positioned ~1 ~ ~-1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~-1 ~ ~1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~2 ~ ~-1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~0 ~ ~2 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:set_lectern
execute unless entity @e[tag=rallous.winds.mark,distance=..4,limit=1] positioned ~1 ~ ~-1 run function rallous_winds:set_lectern
""",
    )
    w(
        fn / "set_lectern.mcfunction",
        """execute if score $school rallous.winds matches 1 run function rallous_winds:place/colleges
execute if score $school rallous.winds matches 2 run function rallous_winds:place/ice
execute if score $school rallous.winds matches 3 run function rallous_winds:place/death
execute if score $school rallous.winds matches 4 run function rallous_winds:place/blood
execute unless score $school rallous.winds matches 1..4 run function rallous_winds:place/primer
""",
    )
    w(
        fn / "try_barrel.mcfunction",
        """execute if block ~-2 ~ ~-2 minecraft:barrel positioned ~-2 ~ ~-2 run function rallous_winds:fill_barrel
execute unless block ~-2 ~ ~-2 minecraft:barrel positioned ~-1 ~ ~-2 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:put_barrel
execute unless block ~-2 ~ ~-2 minecraft:barrel unless block ~-1 ~ ~-2 minecraft:barrel positioned ~1 ~ ~1 if block ~ ~ ~ #minecraft:replaceable run function rallous_winds:put_barrel
""",
    )
    w(
        fn / "put_barrel.mcfunction",
        """setblock ~ ~ ~ minecraft:barrel[facing=up]{CustomName:'{"text":"Scribe Cache","color":"gray"}'}
function rallous_winds:fill_barrel
""",
    )
    w(
        fn / "fill_barrel.mcfunction",
        """execute if score $school rallous.winds matches 1 run data modify block ~ ~ ~ LootTable set value "rallous_winds:chests/path_colleges"
execute if score $school rallous.winds matches 2 run data modify block ~ ~ ~ LootTable set value "rallous_winds:chests/path_ice"
execute if score $school rallous.winds matches 3 run data modify block ~ ~ ~ LootTable set value "rallous_winds:chests/path_death"
execute if score $school rallous.winds matches 4 run data modify block ~ ~ ~ LootTable set value "rallous_winds:chests/path_blood"
execute unless score $school rallous.winds matches 1..4 run data modify block ~ ~ ~ LootTable set value "rallous_winds:chests/path_primer"
""",
    )

    for num, school in SCHOOLS.items():
        if school["id"] == "primer":
            w(fn / "place" / "primer.mcfunction", lectern_command(school))
            dump_json(SRC / "data" / "rallous_winds" / "loot_tables" / "chests" / "path_primer.json", loot_table(school))
            continue
        w(fn / "place" / f"{school['id']}.mcfunction", lectern_command(school))
        dump_json(
            SRC / "data" / "rallous_winds" / "loot_tables" / "chests" / f"path_{school['id']}.json",
            loot_table(school),
        )
        magic = {1: 1, 2: 2, 3: 3, 4: 4}[num]
        extra = ""
        if school["id"] == "ice":
            extra = "scoreboard players add @s rallous.kislev 1\n"
        w(
            fn / "found" / f"{school['id']}.mcfunction",
            f"scoreboard players set @s rallous.magic {magic}\n"
            f"{extra}"
            f"advancement grant @s only rallous_winds:root\n"
            f"advancement grant @s only rallous_contact:magic/root\n"
            f"advancement grant @s only rallous_contact:magic/{school['id']}\n"
            f'tellraw @s {{"text":"{school["found"]}","color":"{school["found_color"]}"}}\n',
        )

    w(
        fn / "found" / "ink.mcfunction",
        """advancement grant @s only rallous_winds:root
advancement grant @s only rallous_contact:magic/root
tellraw @s {"text":"Iron's ink. Inscribe a scroll. The crater never had a book.","color":"gray"}
""",
    )

    adv_root = SRC / "data" / "rallous_winds" / "advancements"
    dump_json(
        adv_root / "root.json",
        {
            "display": {
                "icon": {"item": "minecraft:amethyst_shard"},
                "title": {"text": "The Winds"},
                "description": {"text": "No starter spellbook. A camp lectern or Iron's ink is the path."},
                "frame": "challenge",
                "announce_to_chat": False,
                "show_toast": True,
                "hidden": False,
                "background": "minecraft:textures/block/amethyst_block.png",
            },
            "criteria": {
                "colleges_letter": book_crit("colleges"),
                "ice_letter": book_crit("ice"),
                "death_letter": book_crit("death"),
                "blood_letter": book_crit("blood"),
                "primer": book_crit("primer"),
                "ink": {
                    "trigger": "minecraft:inventory_changed",
                    "conditions": {
                        "items": [
                            {
                                "items": [
                                    "irons_spellbooks:common_ink",
                                    "irons_spellbooks:uncommon_ink",
                                    "irons_spellbooks:rare_ink",
                                ]
                            }
                        ]
                    },
                },
            },
            "requirements": [
                ["colleges_letter", "ice_letter", "death_letter", "blood_letter", "primer", "ink"]
            ],
        },
    )
    dump_json(
        adv_root / "ink.json",
        adv(
            "Iron's Ink",
            "A vial, not a crater book. Inscribe a scroll.",
            "minecraft:ink_sac",
            "rallous_winds:root",
            {
                "ink": {
                    "trigger": "minecraft:inventory_changed",
                    "conditions": {
                        "items": [
                            {
                                "items": [
                                    "irons_spellbooks:common_ink",
                                    "irons_spellbooks:uncommon_ink",
                                    "irons_spellbooks:rare_ink",
                                ]
                            }
                        ]
                    },
                }
            },
            "rallous_winds:found/ink",
        ),
    )
    for num, school in SCHOOLS.items():
        if school["id"] == "primer":
            continue
        dump_json(
            adv_root / f"{school['id']}.json",
            adv(
                school["adv_title"],
                school["adv_desc"],
                school["icon"],
                "rallous_winds:root",
                {"letter": book_crit(school["id"])},
                f"rallous_winds:found/{school['id']}",
            ),
        )


def copy_out() -> None:
    for dest in COPIES:
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(SRC, dest, ignore=shutil.ignore_patterns())


def validate() -> None:
    banned_give = (
        "give @s irons_spellbooks:iron_spell_book",
        "give @s irons_spellbooks:gold_spell_book",
        "give @s irons_spellbooks:copper_spell_book",
        "give @s irons_spellbooks:diamond_spell_book",
        "give @s irons_spellbooks:netherite_spell_book",
        "give @s irons_spellbooks:necronomicon",
    )
    text = ""
    for p in SRC.rglob("*"):
        if p.is_file() and p.suffix in {".mcfunction", ".json", ".md"}:
            text += p.read_text(encoding="utf-8")
    for b in banned_give:
        if b in text:
            raise SystemExit(f"winds pack gives a filled spellbook: {b}")
    if "rallous_winds:hint" not in (SRC / "README.md").read_text():
        raise SystemExit("README missing hint")
    for rel in (
        "data/rallous_winds/functions/hint.mcfunction",
        "data/rallous_winds/advancements/colleges.json",
        "data/rallous_winds/advancements/ice.json",
        "data/rallous_winds/advancements/death.json",
        "data/rallous_winds/advancements/blood.json",
        "data/rallous_winds/loot_tables/chests/path_colleges.json",
    ):
        if not (SRC / rel).exists():
            raise SystemExit(f"missing {rel}")
    # Lecterns must exist; spellbooks must not be loot item ids.
    for p in (SRC / "data" / "rallous_winds" / "loot_tables").rglob("*.json"):
        data = json.loads(p.read_text())
        names: list[str] = []

        def walk(node) -> None:
            if isinstance(node, dict):
                if node.get("type") == "minecraft:item" and "name" in node:
                    names.append(str(node["name"]))
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)

        walk(data)
        for n in names:
            if "spell_book" in n or n.endswith(":necronomicon"):
                raise SystemExit(f"loot table has a spellbook item: {p} {n}")


def main() -> None:
    write_pack()
    copy_out()
    validate()
    print("authored rallous_winds → content + pack-src + cf-overrides")


if __name__ == "__main__":
    main()
