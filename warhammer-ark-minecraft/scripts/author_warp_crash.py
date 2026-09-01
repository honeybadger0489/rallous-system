#!/usr/bin/env python3
"""Overwrite the 0.2.2 six-lord court with a Warp-crash first join.

Keeps letters/recipes/advancements in the jar but they are no longer the
spawn. Safe to re-run. Called by integrate-overrides.py and, if someone
re-authors 0.2.2, from the end of author_old_world.py.
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OV = ROOT / "pack" / "cf-overrides"
CONTENT = ROOT / "pack" / "content" / "rallous_old_world"
DATA = CONTENT / "data" / "rallous_old_world"
FN = DATA / "functions"


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text)


def dump_json(path: Path, data) -> None:
    w(path, json.dumps(data, indent=2, ensure_ascii=False))


def book_pages(pages: list[str]) -> str:
    chunks = []
    for p in pages:
        safe = p.replace("'", "\u2019")
        chunks.append("'" + json.dumps({"text": safe}, ensure_ascii=False) + "'")
    return "[" + ",".join(chunks) + "]"


def apply_warp_crash() -> None:
    write_pack_meta()
    write_functions()
    write_advancement_root()
    write_quests()
    write_cnpc_note()
    play = ROOT / "PLAY.md"
    if play.exists():
        w(OV / "PLAY.md", play.read_text())
    rebuild_jar()
    print("applied Warp-crash first-join (court stripped)")


def write_pack_meta() -> None:
    dump_json(
        CONTENT / "pack.mcmeta",
        {
            "pack": {
                "pack_format": 15,
                "description": "Rallous Old World — Warp-crash spawn, not the six-lord court",
            }
        },
    )
    w(
        CONTENT / "META-INF" / "mods.toml",
        """modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="rallous_old_world"
version="1.1.0"
displayName="Rallous Old World"
authors="Rallous System"
description='''Warp-crash Old World: crater spawn, scattered friends, no Reikland court.'''
""",
    )
    # Own tags only. Sibling jars register their own #minecraft:tick / load.
    dump_json(
        CONTENT / "data" / "minecraft" / "tags" / "functions" / "load.json",
        {"values": ["rallous_old_world:load"]},
    )
    dump_json(
        CONTENT / "data" / "minecraft" / "tags" / "functions" / "tick.json",
        {"values": ["rallous_old_world:tick"]},
    )


def write_functions() -> None:
    w(
        FN / "load.mcfunction",
        """# Warp-crash scoreboards. No chat on /reload.
scoreboard objectives add rallous.joined dummy
scoreboard objectives add rallous.empire dummy
scoreboard objectives add rallous.waaagh dummy
scoreboard objectives add rallous.vampire dummy
scoreboard objectives add rallous.dwarf dummy
scoreboard objectives add rallous.kislev dummy
scoreboard objectives add rallous.chaos dummy
scoreboard objectives add rallous.deaths deathCount
scoreboard objectives add rallous.crashed dummy
scoreboard objectives add rallous.path dummy
scoreboard objectives add rallous.help dummy
scoreboard objectives add rallous.betray dummy
scoreboard objectives add rallous.join dummy
scoreboard objectives add rallous.leave dummy
scoreboard objectives add rallous.race dummy
scoreboard objectives add rallous.lizard dummy
scoreboard objectives add rallous.beast dummy
scoreboard objectives add rallous.skaven dummy
scoreboard objectives add rallous.khorne dummy
scoreboard objectives add rallous.proved dummy
scoreboard objectives add rallous.magic dummy
scoreboard objectives add rallous.army dummy
gamerule spawnRadius 0
""",
    )
    w(
        FN / "tick.mcfunction",
        """# Court never. Spawn is rallous_warp_crash. Primer after that pack lands.
# Do not increment rallous.joined while warp_crash owns the join (join_wait 1+).
execute as @a[tag=!rallous.old_world,tag=rallous.warp_landed] at @s run function rallous_old_world:first_join
execute as @a[tag=!rallous.old_world,tag=!rallous.warp_landed] unless score @s rallous.join_wait matches 1.. unless score @s rallous.joined matches 1.. run scoreboard players add @s rallous.joined 1
execute as @a[tag=!rallous.old_world,tag=!rallous.warp_landed,scores={rallous.joined=100..}] unless score @s rallous.join_wait matches 1.. at @s run function rallous_old_world:first_join
""",
    )
    w(
        FN / "first_join.mcfunction",
        """# Court is gone. First join is a Warp-crash only.
execute unless entity @s[tag=rallous.old_world] run function rallous_old_world:welcome
""",
    )
    w(
        FN / "welcome.mcfunction",
        """tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
scoreboard players set @s rallous.crashed 1
scoreboard players set @s rallous.deaths 0
execute if entity @s[tag=!rallous.warp_landed] run function rallous_old_world:crash/strip_starter_magic
# Spawn/respawn is rallous_warp_crash. Do not carve a second crater or restore the court.
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
""",
    )
    w(
        FN / "ensure_court.mcfunction",
        """# Intentionally empty. 0.2.2 summoned Karl Franz's court here. Warp-crash does not.
""",
    )
    w(
        FN / "summon_lords.mcfunction",
        """tellraw @s {"text":"The six-lord Reikland court was discarded. This pack is a Warp-crash. You wake in a crater, not in front of Karl Franz.","color":"dark_red"}
tellraw @s {"text":"Return to your crater: /function rallous_old_world:crash/return_crater","color":"yellow"}
""",
    )
    w(
        FN / "place_court.mcfunction",
        """# No-op. Court banners are not placed on join.
""",
    )

    primer_pages = [
        "The warp spat you out. There is no war council. The crater under your boots is the world spawn. A friend who joins this world crashes somewhere else.",
        "Mods are the engine. We authored the crash, the first-contact book, faction words (State Trooper / Elector / Waaagh), and the roaming / Lizardmen-Beastmen force functions. We borrowed Recruits, Iron's, Fossils, Epic Fight, Terralith, Sons of the Empire kits, grim packs.",
        "You start with no battle magic. Iron's is in the pack; you find or craft it later. Do not expect a spellbook in the crater chest.",
        "Walk to a bannered camp. Fight. Recruits lang says State Trooper. Die without a claimed village / join civ-bed and the warp hauls you back to YOUR crater. Wilderness beds do not stick.",
        "Cheats: /function rallous_old_world:force_roaming   /function rallous_old_world:lm_bm/summon   /function rallous_old_world:crash/demo_friend_elsewhere   /function rallous_old_world:crash/return_crater",
        "Graphics are Faithful 32x + Grimdark Battlepack + Grimdark Sky + Gothic font + Complementary Unbound + Sons of the Empire on Steve-like bodies. We did not sculpt Total War models. Continuity (the connected-textures mod) is not in this pack.",
    ]
    nbt = f"title:\"Wreckage Journal\",author:\"A nameless survivor\",pages:{book_pages(primer_pages)}"
    w(FN / "give_primer.mcfunction", f"give @s minecraft:written_book{{{nbt}}} 1\n")

    w(
        FN / "crash" / "strip_starter_magic.mcfunction",
        """# First hour: no Iron's book. The pack still contains the mod for later.
clear @s irons_spellbooks:iron_spell_book
clear @s irons_spellbooks:gold_spell_book
clear @s irons_spellbooks:diamond_spell_book
clear @s irons_spellbooks:netherite_spell_book
clear @s irons_spellbooks:copper_spell_book
clear @s irons_spellbooks:blaze_spell_book
clear @s irons_spellbooks:dragonskin_spell_book
clear @s irons_spellbooks:evoker_spell_book
clear @s irons_spellbooks:rotten_spell_book
clear @s irons_spellbooks:graybeard_staff
clear @s irons_spellbooks:blood_staff
clear @s irons_spellbooks:ice_staff
clear @s irons_spellbooks:lightning_rod
clear @s irons_spellbooks:magehunter
clear @s irons_spellbooks:scroll
""",
    )
    w(
        FN / "crash" / "first_crash.mcfunction",
        """tag @s add rallous.anchor
execute align xyz positioned ~0.5 ~ ~0.5 run function rallous_old_world:crash/carve_world_crater
""",
    )
    w(
        FN / "crash" / "carve_world_crater.mcfunction",
        """# Bowl under the first survivor. Sets world spawn + their spawnpoint.
fill ~-6 ~-1 ~-6 ~6 ~5 ~6 air
fill ~-6 ~-4 ~-6 ~6 ~-3 ~6 blackstone
fill ~-4 ~-3 ~-4 ~4 ~-3 ~4 magma_block
fill ~-5 ~-2 ~-5 ~5 ~-2 ~5 polished_blackstone
fill ~-3 ~-2 ~-3 ~3 ~-2 ~3 crying_obsidian
setblock ~ ~-2 ~ crying_obsidian
setblock ~1 ~-2 ~ amethyst_block
setblock ~-1 ~-2 ~ budding_amethyst
setblock ~ ~-2 ~1 obsidian
setblock ~ ~-2 ~-1 crying_obsidian
fill ~-7 ~-1 ~-7 ~7 ~-1 ~7 blackstone
fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 air
setblock ~-3 ~-2 ~2 warped_nylium
setblock ~-3 ~-1 ~2 warped_fungus
setblock ~3 ~-2 ~3 crimson_nylium
setblock ~2 ~-1 ~2 campfire
setblock ~-2 ~-1 ~-2 lantern
setblock ~4 ~-1 ~-1 chest{Items:[{Slot:0b,id:"minecraft:bread",Count:8b},{Slot:1b,id:"minecraft:torch",Count:16b},{Slot:2b,id:"minecraft:leather",Count:4b},{Slot:3b,id:"minecraft:stone_sword",Count:1b},{Slot:4b,id:"minecraft:leather_chestplate",Count:1b},{Slot:5b,id:"minecraft:leather_boots",Count:1b}]}
summon marker ~ ~-1 ~ {Tags:["rallous.world_crater","rallous.crater","rallous.crash.crater","rallous.crash.origin"],CustomName:'{"text":"Warp Crater"}'}
forceload add ~-2 ~-2 ~2 ~2
setworldspawn ~ ~-1 ~
spawnpoint @s ~ ~-1 ~
gamerule spawnRadius 0
tp @s ~ ~-1 ~
tellraw @s {"text":"You hit the Old World. This crater is home until you sleep under a village roof.","color":"dark_purple"}
""",
    )
    w(
        FN / "crash" / "scatter_friend.mcfunction",
        """tag @s add rallous.friend
tellraw @s {"text":"Your friend crashed elsewhere. The warp dropped you far from their crater.","color":"light_purple"}
spreadplayers ~ ~ 800 1800 false @s
execute at @s align xyz positioned ~0.5 ~ ~0.5 run function rallous_old_world:crash/carve_friend_crater
""",
    )
    w(
        FN / "crash" / "carve_friend_crater.mcfunction",
        """fill ~-4 ~-1 ~-4 ~4 ~4 ~4 air
fill ~-4 ~-3 ~-4 ~4 ~-2 ~4 blackstone
fill ~-2 ~-2 ~-2 ~2 ~-2 ~2 crying_obsidian
setblock ~ ~-2 ~ crying_obsidian
fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 blackstone
fill ~-3 ~-1 ~-3 ~3 ~-1 ~3 air
setblock ~2 ~-1 ~1 campfire
setblock ~-2 ~-1 ~-1 chest{Items:[{Slot:0b,id:"minecraft:bread",Count:6b},{Slot:1b,id:"minecraft:torch",Count:12b},{Slot:2b,id:"minecraft:stone_axe",Count:1b}]}
summon marker ~ ~-1 ~ {Tags:["rallous.friend_crater","rallous.crater"]}
spawnpoint @s ~ ~-1 ~
tp @s ~ ~-1 ~
""",
    )
    w(
        FN / "crash" / "on_death.mcfunction",
        """# Vanilla already sent you to bed or to the spawnpoint we set (your crater).
tellraw @s {"text":"If you had no claimed village / join civ-bed, the warp hauled you back to your crater. Wilderness beds do not stick.","color":"dark_purple"}
scoreboard players set @s rallous.deaths 0
""",
    )
    w(
        FN / "crash" / "return_crater.mcfunction",
        """execute if entity @e[type=marker,tag=rallous.world_crater,limit=1] run tp @s @e[type=marker,tag=rallous.world_crater,limit=1]
execute unless entity @e[type=marker,tag=rallous.world_crater,limit=1] run tellraw @s {"text":"No world crater marker. Die without a bed, or rejoin a new world.","color":"red"}
""",
    )
    w(
        FN / "crash" / "demo_friend_elsewhere.mcfunction",
        """# Solo smoke: pretend you are the second player.
tag @s remove rallous.anchor
function rallous_old_world:crash/scatter_friend
tellraw @s {"text":"Solo demo: you were scattered. /function rallous_old_world:crash/return_crater  goes back to the first crater.","color":"yellow"}
""",
    )

    # Public aliases used in PLAY.md
    w(FN / "force_roaming.mcfunction", "function rallous_old_world:roaming/force_roaming\n")
    w(
        FN / "roaming" / "force_roaming.mcfunction",
        """tellraw @s {"text":"Forcing a Waaagh, a Beastmen herd, and a Khorne pack.","color":"red"}
# Sibling jar (rallous_roaming) if present; local proxies always fire.
function rallous_roaming:clear
execute as @s at @s run function rallous_roaming:spawn/waaagh
execute as @s at @s positioned ~18 ~ ~ run function rallous_roaming:spawn/herd
execute as @s at @s positioned ~-18 ~ ~ run function rallous_roaming:spawn/khorne_host
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/waaagh
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/herd
execute at @s unless entity @e[tag=rallous.roam.host,limit=1] run function rallous_old_world:roaming/khorne
""",
    )
    w(
        FN / "roaming" / "waaagh.mcfunction",
        """summon pillager ~8 ~ ~6 {CustomName:'{"text":"Waaagh Boy","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.waaagh"],HandItems:[{id:"minecraft:iron_axe",Count:1b},{}],ArmorItems:[{},{},{id:"minecraft:leather_chestplate",Count:1b},{id:"minecraft:zombie_head",Count:1b}]}
summon pillager ~10 ~ ~4 {CustomName:'{"text":"Waaagh Arrer","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.waaagh"]}
summon ravager ~12 ~ ~5 {CustomName:'{"text":"Waaagh Squig-beast","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.waaagh"]}
summon item ~9 ~ ~5 {Item:{id:"minecraft:lime_banner",Count:1b}}
""",
    )
    w(
        FN / "roaming" / "herd.mcfunction",
        """summon goat ~-8 ~ ~8 {CustomName:'{"text":"Ungor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.herd"]}
summon goat ~-10 ~ ~9 {CustomName:'{"text":"Ungor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.herd"]}
summon ravager ~-12 ~ ~7 {CustomName:'{"text":"Cygor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.herd","rallous.beastmen"]}
summon wolf ~-9 ~ ~11 {CustomName:'{"text":"Chaos Warhound","color":"dark_gray"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.roaming","rallous.herd"]}
""",
    )
    w(
        FN / "roaming" / "khorne.mcfunction",
        """summon hoglin ~6 ~ ~-10 {CustomName:'{"text":"Khorne Flesh-hound","color":"dark_red"}',CustomNameVisible:1b,PersistenceRequired:1b,IsImmuneToZombification:1b,Tags:["rallous.roaming","rallous.khorne"]}
summon zombified_piglin ~8 ~ ~-12 {CustomName:'{"text":"Bloodletter","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b,HandItems:[{id:"minecraft:netherite_axe",Count:1b},{}],Tags:["rallous.roaming","rallous.khorne"]}
summon zombified_piglin ~5 ~ ~-14 {CustomName:'{"text":"Bloodletter","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b,HandItems:[{id:"minecraft:iron_axe",Count:1b},{}],Tags:["rallous.roaming","rallous.khorne"]}
""",
    )
    w(
        FN / "lm_bm" / "summon.mcfunction",
        """# Lizardmen / Beastmen Ark glue. Fossils IDs vary by jar; vanilla proxies always spawn.
tellraw @s {"text":"Jungle-side Lizardmen proxies and forest Beastmen. Fossils dinos spawn if that mod loaded this entity.","color":"aqua"}
summon turtle ~3 ~ ~ {CustomName:'{"text":"Skink","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
summon turtle ~4 ~ ~1 {CustomName:'{"text":"Skink","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
summon goat ~-3 ~ ~2 {CustomName:'{"text":"Ungor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.beastmen"]}
summon ravager ~-5 ~ ~ {CustomName:'{"text":"Cygor","color":"dark_green"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.beastmen"]}
summon fossil:triceratops ~6 ~ ~ {CustomName:'{"text":"Stegadon","color":"aqua"}',CustomNameVisible:1b,PersistenceRequired:1b,Tags:["rallous.lizardmen"]}
""",
    )


def write_advancement_root() -> None:
    dump_json(
        DATA / "advancements" / "root.json",
        {
            "display": {
                "icon": {"item": "minecraft:crying_obsidian"},
                "title": {"text": "Warp-crash", "color": "dark_purple"},
                "description": {"text": "You hit the Old World. No war council."},
                "background": "minecraft:textures/block/crying_obsidian.png",
                "frame": "challenge",
                "announce_to_chat": True,
                "show_toast": True,
            },
            "criteria": {"joined": {"trigger": "minecraft:tick"}},
            "requirements": [["joined"]],
        },
    )
    dump_json(
        CONTENT / "assets" / "rallous_old_world" / "lang" / "en_us.json",
        {
            "advancements.rallous_old_world.root.title": "Warp-crash",
            "advancements.rallous_old_world.root.description": "You hit the Old World. No war council.",
        },
    )


def write_quests() -> None:
    """First-contact FTB is scripts/author_contact.py (court book stays gone)."""
    from author_contact import write_all_quests
    write_all_quests()

def write_cnpc_note() -> None:
    root = OV / "customnpcs" / "rallous_lords"
    if not root.exists():
        return
    for path in root.glob("*.json"):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError:
            continue
        data["spawn"] = (
            "NOT first-join. Warp-crash discarded the Reikland court. "
            "summon_lords is a refuse message. These files are leftover letter text."
        )
        dump_json(path, data)


def rebuild_jar() -> Path:
    jar_path = OV / "mods" / "rallous-old-world-1.0.0.jar"
    jar_path.parent.mkdir(parents=True, exist_ok=True)
    if jar_path.exists():
        jar_path.unlink()
    with zipfile.ZipFile(jar_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(CONTENT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(CONTENT).as_posix())
    print(f"wrote {jar_path} ({jar_path.stat().st_size} bytes)")
    return jar_path


def strip_unused_court_files() -> None:
    """Delete leftover unused court summons and Kislev/Karl letters. Do not restore first-join court."""
    lords_dir = FN / "lords"
    if lords_dir.is_dir():
        for path in lords_dir.glob("*.mcfunction"):
            path.unlink()
    for name in ("give_karl_letter.mcfunction", "give_katarin_letter.mcfunction"):
        p = FN / name
        if p.exists():
            p.unlink()
    cnpc = OV / "customnpcs" / "rallous_lords"
    for name in ("karl.json", "katarin.json"):
        p = cnpc / name
        if p.exists():
            p.unlink()
    adv = DATA / "advancements"
    for rel in ("lords/karl.json", "lords/katarin.json", "kislev/root.json"):
        p = adv / rel
        if p.exists():
            p.unlink()
    kislev = adv / "kislev"
    if kislev.is_dir() and not any(kislev.iterdir()):
        kislev.rmdir()
    host = adv / "reikland" / "host.json"
    if host.exists():
        try:
            data = json.loads(host.read_text())
        except json.JSONDecodeError:
            data = None
        if data and data.get("parent") == "rallous_old_world:lords/karl":
            data["parent"] = "rallous_old_world:root"
            dump_json(host, data)


def strip_court_hooks() -> None:
    """Last-line defense if a sibling rewrote first_join."""
    strip_unused_court_files()
    fj = FN / "first_join.mcfunction"
    if fj.exists():
        text = fj.read_text()
        if "ensure_court" in text or "summon_lords" in text or "place_court" in text:
            w(
                fj,
                """# Court is gone. First join is a Warp-crash only.
execute unless entity @s[tag=rallous.old_world] run function rallous_old_world:welcome
""",
            )
    w(
        FN / "ensure_court.mcfunction",
        """# Intentionally empty. 0.2.2 summoned Karl Franz's court here. Warp-crash does not.
""",
    )
    sl = FN / "summon_lords.mcfunction"
    if sl.exists() and "war council takes the field" in sl.read_text():
        w(
            sl,
            """tellraw @s {"text":"The six-lord Reikland court was discarded. This pack is a Warp-crash.","color":"dark_red"}
""",
        )


if __name__ == "__main__":
    apply_warp_crash()
    strip_court_hooks()
