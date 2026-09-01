#!/usr/bin/env python3
"""Author the Old World content layer into pack/cf-overrides/.

Writes rallous_old_world datapack (jar), CNPC lord dialogue JSON, and config glue.
FTB first-contact quests are owned by scripts/author_contact.py.
Does not touch CurseForge fileIDs.
"""

from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OV = ROOT / "pack" / "cf-overrides"
QUESTS = OV / "config" / "ftbquests" / "quests"
CHAPTERS = QUESTS / "chapters"
CONTENT = ROOT / "pack" / "content" / "rallous_old_world"


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n")


def dump_json(path: Path, data) -> None:
    w(path, json.dumps(data, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# Lore
# ---------------------------------------------------------------------------

LORDS = [
    {
        "id": "karl",
        "name": "Karl Franz",
        "title": "Prince of Altdorf, Emperor",
        "faction": "The Empire — Reikland",
        "color": "gold",
        "job": "Raise a state-troop host. Recruits are your State Troops; the Faction screen is the Electors.",
        "diplomacy": "Create a Faction named Reikland. Ally other Elector banners. Vassal the Border Princes (Vassal & Suzerains) or take the field yourself.",
        "profession": "armorer",
        "type": "plains",
        "offset": (3, 0, 2),
        "helmet": "sonsoftheempire:emperors_armor_helmet",
        "chest": "sonsoftheempire:emperors_armor_chestplate",
        "legs": "sonsoftheempire:emperors_armor_leggings",
        "boots": "sonsoftheempire:emperors_armor_boots",
        "hand": "sonsoftheempire:ghalmaraz",
        "book_title": "Letter from the Emperor",
        "pages": [
            "Soldier. I am Karl Franz, Prince of Altdorf and Emperor. You are not a general on a campaign map. You are a body on the Reikland road: thirsty, armed, and small.",
            "The Empire is Elector Counts, state troops, and Sigmar's fire. Recruits are those troops. Open the command screen. Hire. Form a host. The Faction screen is how Electors name their banners.",
            "Your job: raise a company, claim a stretch of the Reik, and keep grain moving. Wear Reikland plate when you have earned it.",
            "Diplomacy: ally fellow Electors. Set Enemy on anything that burns the coach roads. If a Border Prince will kneel, open Vassal & Suzerains and take tribute. If he will not, it is war.",
        ],
    },
    {
        "id": "grimgor",
        "name": "Grimgor Ironhide",
        "title": "Once-Gitsnik, Da Greatest",
        "faction": "Greenskins — Waaagh!",
        "color": "green",
        "job": "Smash. Take heads. A Waaagh is Recruits on Aggressive/Raid with a green banner.",
        "diplomacy": "War is the default. Tribute is you paying him to look the other way — or him paying you if you are the bigger boss.",
        "profession": "butcher",
        "type": "savanna",
        "offset": (4, 0, 0),
        "helmet": "minecraft:zombie_head",
        "chest": "minecraft:leather_chestplate",
        "legs": "minecraft:leather_leggings",
        "boots": "minecraft:leather_boots",
        "hand": "minecraft:iron_axe",
        "book_title": "Grimgor's Challenge",
        "pages": [
            "I'z Grimgor. Da greatest. You'z umie. Talk is fer gits that ain't fightin'.",
            "Greenskins don't vote. We WAAAGH. Your Recruits on Raid, green banner, that's a Waaagh. Hire boyz. Point 'em at a town. That's the Border Princes.",
            "Job: find me a scrap worth havin'. Field battle. Not two zombies. A host versus a host.",
            "Diplomacy: Ally? Only if you'z bigger. Enemy is honest. Tribute is you dumpin' emeralds so I don't krump your camp. Open the Faction screen and pick. Don't waste my time.",
        ],
    },
    {
        "id": "mannfred",
        "name": "Mannfred von Carstein",
        "title": "Vampire Count of Sylvania",
        "faction": "Vampire Counts — Sylvania",
        "color": "dark_red",
        "job": "Night is the province. Iron's blood school is the court magic. Crypts are the tax.",
        "diplomacy": "A dark pact (Ally the dead, lose the living) or a dawn siege. No third pose.",
        "profession": "cleric",
        "type": "swamp",
        "offset": (3, 0, -2),
        "helmet": "sonsoftheempire:witchhunter_armor_helmet",
        "chest": "minecraft:leather_chestplate",
        "legs": "minecraft:leather_leggings",
        "boots": "minecraft:leather_boots",
        "hand": "minecraft:wither_skeleton_skull",
        "book_title": "Von Carstein Invitation",
        "pages": [
            "I am Mannfred von Carstein. Sylvania is not a forest with a rumor. It is a county that voted for the grave.",
            "The living bar their gates at dusk. The dead do not. Iron's blood and death magics are how my court speaks. Malum is the slower occult — useful, not polite.",
            "Job: walk my fens after dark. Kill what walks. Or bring me a living captain and kneel. Either is a province won.",
            "Diplomacy: Ally me and Heartland towns will learn your name the wrong way. Enemy me and come at dawn with Recruits and a siege engine. Tribute is blood or bodies. Choose before the moon is up.",
        ],
    },
    {
        "id": "thorgrim",
        "name": "Thorgrim Grudgebearer",
        "title": "High King of the Dawi",
        "faction": "Dwarfs — Worlds Edge Mountains",
        "color": "gold",
        "job": "Settle a named grudge. Recover a relic from a fallen hold. Artillery with the host.",
        "diplomacy": "Oath-friend (Ally + gold) or remain umgi at the gate. Tribute is gold and grudges paid.",
        "profession": "weaponsmith",
        "type": "taiga",
        "offset": (-3, 0, 2),
        "helmet": "sonsoftheempire:highking_armor_helmet",
        "chest": "sonsoftheempire:highking_armor_chestplate",
        "legs": "sonsoftheempire:highking_armor_leggings",
        "boots": "sonsoftheempire:highking_armor_boots",
        "hand": "sonsoftheempire:grudgesettler",
        "book_title": "Entry in the Great Book of Grudges",
        "pages": [
            "Thorgrim Grudgebearer, High King. The Worlds Edge does not open for umgi who smell of graves and excuses.",
            "A hold is a province made of stone and memory. Recruits are acceptable mercenaries. Fossils and old bones are ancestor-work — raise a beast properly and we will call it respect, not witchcraft.",
            "Job: take the Hold-Road. Clear a fallen hall (YUNG, Dungeons Arise, a deepslate wound). Bring back a named thing. Then stand our artillery.",
            "Diplomacy: Ally is oath-friend. We do not forget. Enemy is a grudge I will read aloud. Tribute is gold on the book. Open the Faction screen when you have something written down.",
        ],
    },
    {
        "id": "katarin",
        "name": "Katarin Bokha",
        "title": "Tzarina, Ice Queen of Kislev",
        "faction": "Kislev — the Oblast",
        "color": "aqua",
        "job": "Survive the cold. Ice Court magic. Keep the gate so the Wastes stay north.",
        "diplomacy": "Northern alliance against Chaos. Tribute is grain, fur, and bodies on the line.",
        "profession": "librarian",
        "type": "snow",
        "offset": (-4, 0, 0),
        "helmet": "sonsoftheempire:armoredkossar_armor_helmet",
        "chest": "sonsoftheempire:boyar_armor_chestplate",
        "legs": "sonsoftheempire:boyar_armor_leggings",
        "boots": "sonsoftheempire:boyar_armor_boots",
        "hand": "minecraft:packed_ice",
        "book_title": "Edict of the Ice Court",
        "pages": [
            "I am Katarin, Tzarina of Kislev. The oblast is not scenery. Winter kills you here. Drink. Wear fur. Legendary Survival is not a HUD toy.",
            "The Ice Court is battle magic: Iron's ice school. Winged lancers and kossars are Recruits you keep paid and pointed north.",
            "Job: reach the taiga and the snow. Live. Then hold a gate. If a convoy dies, Kislev still stands — you just paid in standing.",
            "Diplomacy: Ally the Empire if they send grain. Enemy the Wastes. Vassal is a southern word; we take tribute as land and blood owed. Open Recruits and OPAC. Name your warband after an oblast stanitsa.",
        ],
    },
    {
        "id": "archaon",
        "name": "Archaon the Everchosen",
        "title": "Lord of the End Times",
        "faction": "Warriors of Chaos — Chaos Wastes",
        "color": "dark_purple",
        "job": "Three trials. Then a last battle you can walk away from and return to.",
        "diplomacy": "Kneel (Ally the howling powers; Heartland turns Enemy) or war. Tribute is a soul, not coin.",
        "profession": "toolsmith",
        "type": "plains",
        "offset": (-3, 0, -2),
        "helmet": "minecraft:netherite_helmet",
        "chest": "minecraft:netherite_chestplate",
        "legs": "minecraft:netherite_leggings",
        "boots": "minecraft:netherite_boots",
        "hand": "minecraft:netherite_sword",
        "book_title": "The Everchosen's Terms",
        "pages": [
            "I am Archaon. The Chaos Wastes are not a dungeon level. They are the north after Kislev stops pretending the world has a wall.",
            "Fire and death are honest schools. Holy is the Empire's lie. Ice is Kislev delaying me. Come with a host or do not come.",
            "Job: three trials — a beast, a siege, a relic. Then a fortress. You may leave. The Wound remains. That is a campaign, not a credits roll.",
            "Diplomacy: kneel and the Electors become Enemy. War and I will be here when you have the stomach. Tribute is not emeralds. Open the Faction screen and mean it.",
        ],
    },
]


def book_pages_component(pages: list[str]) -> str:
    chunks = []
    for p in pages:
        # Avoid apostrophes inside SNBT single-quoted page components.
        safe = p.replace("'", "\u2019")
        chunks.append("'" + json.dumps({"text": safe}, ensure_ascii=False) + "'")
    return "[" + ",".join(chunks) + "]"


def written_book_nbt(title: str, author: str, pages: list[str]) -> str:
    pages_snbt = book_pages_component(pages)
    title_j = json.dumps(title, ensure_ascii=False)
    author_j = json.dumps(author, ensure_ascii=False)
    return f"title:{title_j},author:{author_j},pages:{pages_snbt}"


# ---------------------------------------------------------------------------
# Datapack
# ---------------------------------------------------------------------------

def write_datapack() -> None:
    # Warp-crash overlay (author_warp_crash.py) rewrites first-join after this
    # function. Do not restore the 0.2.2 court in welcome / first_join.
    data = CONTENT / "data" / "rallous_old_world"
    assets = CONTENT / "assets" / "rallous_old_world"

    w(
        CONTENT / "pack.mcmeta",
        json.dumps(
            {
                "pack": {
                    "pack_format": 15,
                    "description": "Rallous Old World — campaign, lords, letters",
                }
            },
            indent=2,
        ),
    )
    w(
        CONTENT / "META-INF" / "mods.toml",
        """modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="rallous_old_world"
version="1.0.0"
displayName="Rallous Old World"
authors="Rallous System"
description='''Authored Old World campaign layer: lords, letters, advancements, commission recipes.'''
""",
    )

    dump_json(
        CONTENT / "data" / "minecraft" / "tags" / "functions" / "load.json",
        {"values": ["rallous_old_world:load"]},
    )
    dump_json(
        CONTENT / "data" / "minecraft" / "tags" / "functions" / "tick.json",
        {"values": ["rallous_old_world:tick"]},
    )

    w(
        data / "functions" / "load.mcfunction",
        """# Rallous Old World — scoreboards only. No chat spam on /reload.
scoreboard objectives add rallous.joined dummy
scoreboard objectives add rallous.empire dummy
scoreboard objectives add rallous.waaagh dummy
scoreboard objectives add rallous.vampire dummy
scoreboard objectives add rallous.dwarf dummy
scoreboard objectives add rallous.kislev dummy
scoreboard objectives add rallous.chaos dummy
""",
    )
    w(
        data / "functions" / "tick.mcfunction",
        """execute as @a[tag=!rallous.old_world] at @s run function rallous_old_world:first_join
""",
    )
    w(
        data / "functions" / "first_join.mcfunction",
        """# Court is gone. First join is a Warp-crash only.
execute unless entity @s[tag=rallous.old_world] run function rallous_old_world:welcome
""",
    )
    w(
        data / "functions" / "welcome.mcfunction",
        """tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
title @s times 20 80 20
title @s title {"text":"The Old World","color":"gold","bold":true}
title @s subtitle {"text":"Reikland · Border Princes · Sylvania · Worlds Edge · Kislev · Chaos Wastes","color":"gray"}
tellraw @s [{"text":"Warp-crash. No war council. Quest book: ","color":"light_purple"},{"text":"`","color":"white"}]
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
""",
    )
    w(
        data / "functions" / "ensure_court.mcfunction",
        """# Intentionally empty. 0.2.2 summoned Karl Franz's court here. Warp-crash does not.
""",
    )

    primer_pages = [
        "You are a soldier in the Old World. Mods are the engine. This book, the quest campaign, the six lords, and the advancements are ours.",
        "Geography is Total War: Reikland (Altdorf), the Border Princes, Sylvania, the Worlds Edge Mountains, Kislev, the Chaos Wastes. Ride; do not teleport the plot.",
        "Verbs: Recruits = hosts and Elector banners. OPAC = warband land. Vassal & Suzerains = tribute. Iron's = fire, ice, holy, blood. Fossils = warbeasts. Epic Fight = the melee.",
        "Talk to the six lords (trade a letter). Tick the campaign in the quest book. The Boot Smoke Test chapter is only a 10-step boot check.",
        "Re-summon the court: /function rallous_old_world:summon_lords  (cheats / op). Graphics are Faithful + Grimdark packs + Unbound + Sons of the Empire kits. We did not sculpt Total War models.",
    ]
    primer_nbt = written_book_nbt("Letters Patent of the Old World", "The War Council", primer_pages)
    w(
        data / "functions" / "give_primer.mcfunction",
        f"give @s minecraft:written_book{{{primer_nbt}}} 1\n",
    )

    court_lines = [
        "execute positioned ~ ~ ~6 if block ~ ~-1 ~ #minecraft:replaceable run setblock ~ ~-1 ~ packed_mud",
        "execute positioned ~ ~ ~6 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ campfire",
        "execute positioned ~1 ~ ~6 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ yellow_banner",
        "execute positioned ~-1 ~ ~6 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ lime_banner",
        "execute positioned ~2 ~ ~5 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ red_banner",
        "execute positioned ~-2 ~ ~5 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ brown_banner",
        "execute positioned ~1 ~ ~7 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ light_blue_banner",
        "execute positioned ~-1 ~ ~7 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ purple_banner",
        "execute positioned ~ ~ ~8 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ lectern[facing=south]",
        "execute positioned ~ ~1 ~8 if block ~ ~ ~ #minecraft:replaceable run setblock ~ ~ ~ lantern",
    ]
    w(data / "functions" / "place_court.mcfunction", "\n".join(court_lines) + "\n")

    summon_all = [
        "execute unless entity @e[tag=rallous.lord,limit=1] run tellraw @a {\"text\":\"The war council takes the field.\",\"color\":\"gold\"}",
        "execute unless entity @e[tag=rallous.lord,limit=1] run function rallous_old_world:place_court",
    ]
    for lord in LORDS:
        summon_all.append(f"execute unless entity @e[tag=rallous.lord.{lord['id']},limit=1] run function rallous_old_world:lords/{lord['id']}")
        nbt = written_book_nbt(lord["book_title"], lord["name"], lord["pages"])
        ox, oy, oz = lord["offset"]
        book = "{" + nbt + "}"
        # Villager courtier: invulnerable, named, letter trade.
        villager = (
            f'summon villager ~{ox} ~{oy} ~{oz} {{'
            f'Tags:["rallous.lord","rallous.lord.{lord["id"]}"],'
            f'CustomName:\'{{"text":"{lord["name"]}","color":"{lord["color"]}"}}\','
            f"CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,"
            f"VillagerData:{{profession:\"minecraft:{lord['profession']}\",level:5,type:\"minecraft:{lord['type']}\"}},"
            f"Offers:{{Recipes:[{{buy:{{id:\"minecraft:emerald\",Count:1}},sell:{{id:\"minecraft:written_book\",Count:1,tag:{book}}},maxUses:999,rewardExp:0b,xp:0}}]}}}}"
        )
        stand = (
            f'summon armor_stand ~{ox} ~{oy} ~{oz + 1} {{'
            f'Tags:["rallous.lord_stand","rallous.lord.{lord["id"]}"],'
            f'CustomName:\'{{"text":"{lord["title"]}","color":"{lord["color"]}"}}\','
            f"CustomNameVisible:1b,ShowArms:1b,NoBasePlate:1b,NoGravity:1b,PersistenceRequired:1b,Invulnerable:1b,DisabledSlots:4144959,"
            f"ArmorItems:[{{id:\"{lord['boots']}\",Count:1}},{{id:\"{lord['legs']}\",Count:1}},{{id:\"{lord['chest']}\",Count:1}},{{id:\"{lord['helmet']}\",Count:1}}],"
            f"HandItems:[{{id:\"{lord['hand']}\",Count:1}},{{}}]}}"
        )
        w(
            data / "functions" / "lords" / f"{lord['id']}.mcfunction",
            villager + "\n" + stand + "\n",
        )
        w(
            data / "functions" / f"give_{lord['id']}_letter.mcfunction",
            f"give @s minecraft:written_book{{{nbt}}} 1\n"
            f"scoreboard players add @s rallous.{_score(lord['id'])} 1\n"
            f"advancement grant @s only rallous_old_world:lords/{lord['id']}\n",
        )
    w(data / "functions" / "summon_lords.mcfunction", "\n".join(summon_all) + "\n")

    # Advancements
    dump_json(
        data / "advancements" / "root.json",
        {
            "display": {
                "icon": {"item": "minecraft:iron_sword"},
                "title": {"text": "The Old World", "color": "gold"},
                "description": {"text": "A soldier on the ground. Not a campaign-map general."},
                "background": "minecraft:textures/block/packed_mud.png",
                "frame": "challenge",
                "announce_to_chat": True,
                "show_toast": True,
            },
            "criteria": {"joined": {"trigger": "minecraft:tick"}},
            "requirements": [["joined"]],
        },
    )

    def letter_adv(lord, parent):
        return {
            "parent": parent,
            "display": {
                "icon": {"item": "minecraft:written_book"},
                "title": {"text": lord["name"]},
                "description": {"text": f"{lord['faction']}. {lord['job']}"},
                "frame": "goal",
            },
            "criteria": {
                "letter": {
                    "trigger": "minecraft:inventory_changed",
                    "conditions": {
                        "items": [
                            {
                                "items": ["minecraft:written_book"],
                                "nbt": f'{{title:"{lord["book_title"]}"}}',
                            }
                        ]
                    },
                }
            },
            "rewards": {"experience": 25, "recipes": _recipes_for(lord["id"])},
        }

    for lord in LORDS:
        dump_json(data / "advancements" / "lords" / f"{lord['id']}.json", letter_adv(lord, "rallous_old_world:root"))

    chapters = [
        ("reikland", "Reikland", "Altdorf and the Electors. Raise a host. Claim a province.", "minecraft:plains", "sonsoftheempire:altdorfbanner"),
        ("border_princes", "Border Princes", "No one law. Sell your sword. Take a princedom.", "minecraft:savanna", "minecraft:lime_banner"),
        ("sylvania", "Sylvania", "The dead voted. Night is the boss.", "minecraft:swamp", "minecraft:red_banner"),
        ("worlds_edge", "Worlds Edge Mountains", "The Hold-Road. Grudges. Ancestor beasts.", "minecraft:windswept_hills", "sonsoftheempire:highking_armor_helmet"),
        ("kislev", "Kislev", "The oblast. Ice. The last gate.", "minecraft:snowy_plains", "sonsoftheempire:gryphonlegion_armor_helmet"),
        ("chaos_wastes", "Chaos Wastes", "North of the last city. The Wound remains.", "minecraft:frozen_peaks", "minecraft:netherite_helmet"),
    ]
    for cid, title, desc, biome, icon in chapters:
        dump_json(
            data / "advancements" / cid / "root.json",
            {
                "parent": "rallous_old_world:root",
                "display": {
                    "icon": {"item": icon if icon.startswith("minecraft:") or icon.startswith("sonsoftheempire:") else "minecraft:map"},
                    "title": {"text": title},
                    "description": {"text": desc},
                    "frame": "task",
                },
                "criteria": {
                    "there": {
                        "trigger": "minecraft:location",
                        "conditions": {
                            "player": [
                                {
                                    "condition": "minecraft:entity_properties",
                                    "entity": "this",
                                    "predicate": {"location": {"biome": biome}},
                                }
                            ]
                        },
                    }
                },
            },
        )

    dump_json(
        data / "advancements" / "reikland" / "host.json",
        {
            "parent": "rallous_old_world:lords/karl",
            "display": {
                "icon": {"item": "minecraft:emerald"},
                "title": {"text": "State Troop Host"},
                "description": {"text": "Hire Recruits. This is an Elector's company, not a pet wolf."},
                "frame": "task",
            },
            "criteria": {"emerald": {"trigger": "minecraft:inventory_changed", "conditions": {"items": [{"items": ["minecraft:emerald"], "count": {"min": 8}}]}}},
            "rewards": {"recipes": ["rallous_old_world:commission_reikland_chestplate", "rallous_old_world:commission_reikland_helmet"]},
        },
    )
    dump_json(
        data / "advancements" / "sylvania" / "night.json",
        {
            "parent": "rallous_old_world:lords/mannfred",
            "display": {
                "icon": {"item": "minecraft:skeleton_skull"},
                "title": {"text": "Night of the Dead"},
                "description": {"text": "Put down ten of the walking dead in Sylvania's shadow."},
                "frame": "goal",
            },
            "criteria": {
                "zombies": {"trigger": "minecraft:player_killed_entity", "conditions": {"entity": [{"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"type": "minecraft:zombie"}}]}},
            },
        },
    )

    # Commission recipes (lore path; Sote's own recipes still exist)
    recipes = [
        (
            "commission_reikland_chestplate",
            ["minecraft:iron_chestplate", "minecraft:yellow_banner", "minecraft:book"],
            "sonsoftheempire:altdorfswordsman_armor_chestplate",
        ),
        (
            "commission_reikland_helmet",
            ["minecraft:iron_helmet", "minecraft:yellow_banner", "minecraft:book"],
            "sonsoftheempire:altdorfswordsman_armor_helmet",
        ),
        (
            "commission_bretonnia_chestplate",
            ["minecraft:iron_chestplate", "minecraft:blue_banner", "minecraft:book"],
            "sonsoftheempire:grailknight_armor_chestplate",
        ),
        (
            "commission_kislev_chestplate",
            ["minecraft:iron_chestplate", "minecraft:light_blue_banner", "minecraft:packed_ice"],
            "sonsoftheempire:armoredkossar_armor_chestplate",
        ),
        (
            "commission_kislev_helmet",
            ["minecraft:iron_helmet", "minecraft:light_blue_banner", "minecraft:packed_ice"],
            "sonsoftheempire:armoredkossar_armor_helmet",
        ),
        (
            "commission_dawi_chestplate",
            ["minecraft:iron_chestplate", "minecraft:brown_banner", "minecraft:gold_ingot"],
            "sonsoftheempire:thane_armor_chestplate",
        ),
        (
            "commission_empire_knight_chestplate",
            ["minecraft:diamond_chestplate", "minecraft:yellow_banner", "minecraft:book"],
            "sonsoftheempire:empireknight_armor_chestplate",
        ),
    ]
    for rid, ings, result in recipes:
        dump_json(
            data / "recipes" / f"{rid}.json",
            {
                "type": "minecraft:crafting_shapeless",
                "category": "equipment",
                "ingredients": [{"item": i} for i in ings],
                "result": {"item": result, "count": 1},
            },
        )

    dump_json(
        assets / "lang" / "en_us.json",
        {
            "advancements.rallous_old_world.root.title": "The Old World",
            "advancements.rallous_old_world.root.description": "A soldier on the ground.",
        },
    )

    # Build LowCodeFML jar into overrides/mods
    jar_path = OV / "mods" / "rallous-old-world-1.0.0.jar"
    jar_path.parent.mkdir(parents=True, exist_ok=True)
    if jar_path.exists():
        jar_path.unlink()
    with zipfile.ZipFile(jar_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(CONTENT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(CONTENT).as_posix())
    print(f"wrote {jar_path} ({jar_path.stat().st_size} bytes)")


def _score(lord_id: str) -> str:
    return {
        "karl": "empire",
        "grimgor": "waaagh",
        "mannfred": "vampire",
        "thorgrim": "dwarf",
        "katarin": "kislev",
        "archaon": "chaos",
    }[lord_id]


def _recipes_for(lord_id: str) -> list[str]:
    return {
        "karl": ["rallous_old_world:commission_reikland_chestplate", "rallous_old_world:commission_reikland_helmet", "rallous_old_world:commission_empire_knight_chestplate"],
        "grimgor": [],
        "mannfred": [],
        "thorgrim": ["rallous_old_world:commission_dawi_chestplate"],
        "katarin": ["rallous_old_world:commission_kislev_chestplate", "rallous_old_world:commission_kislev_helmet"],
        "archaon": [],
    }[lord_id]


# ---------------------------------------------------------------------------
# CNPC / dialogue export (authored text; spawn is the datapack)
# ---------------------------------------------------------------------------

def write_cnpc() -> None:
    root = OV / "customnpcs" / "rallous_lords"
    for lord in LORDS:
        dump_json(
            root / f"{lord['id']}.json",
            {
                "id": lord["id"],
                "name": lord["name"],
                "title": lord["title"],
                "faction": lord["faction"],
                "job": lord["job"],
                "diplomacy": lord["diplomacy"],
                "book_title": lord["book_title"],
                "pages": lord["pages"],
                "spawn": "datapack function rallous_old_world:summon_lords on first join (named villager + armored stand). Not a hand-placed CNPC clone.",
                "skin": "Steve-like villager body + Sons of the Empire / vanilla armor on the stand. No pirated GW meshes.",
            },
        )


# ---------------------------------------------------------------------------
# Resource pack
# ---------------------------------------------------------------------------

def write_continuity() -> None:
    from author_contact import write_continuity as write_contact_continuity
    write_contact_continuity()
    rp = OV / "resourcepacks" / "Rallous Continuity"
    return
    rp = OV / "resourcepacks" / "Rallous Continuity"
    dump_json(
        rp / "pack.mcmeta",
        {
            "pack": {
                "pack_format": 15,
                "description": "Old World names for Recruits / warband UI",
            }
        },
    )
    dump_json(
        rp / "assets" / "recruits" / "lang" / "en_us.json",
        {
            "entity.recruits.recruit": "State Trooper",
            "entity.recruits.bowman": "Handgunner-Bow",
            "entity.recruits.recruit_shieldman": "Swordsman",
            "entity.recruits.nomad": "Kislev Horse Archer",
            "entity.recruits.horseman": "Reiksguard Hopeful",
            "entity.recruits.crossbowman": "Pavise Crossbow",
            "entity.recruits.scout": "Outrider",
            "entity.recruits.captain": "State Captain",
            "entity.recruits.commander": "Sergeant-at-Arms",
            "entity.recruits.messenger": "Imperial Courier",
            "entity.recruits.siege_engineer": "Great Cannon Engineer",
            "item.recruits.recruit_spawn_egg": "State Trooper Spawn Egg",
            "item.recruits.bowman_spawn_egg": "Handgunner-Bow Spawn Egg",
            "item.recruits.nomad_spawn_egg": "Kislev Horse Archer Spawn Egg",
            "item.recruits.horseman_spawn_egg": "Reiksguard Hopeful Spawn Egg",
            "item.recruits.recruit_shieldman_spawn_egg": "Swordsman Spawn Egg",
            "item.recruits.crossbowman_spawn_egg": "Pavise Crossbow Spawn Egg",
            "item.recruits.villager_noble_spawn_egg": "Elector Courtier Spawn Egg",
            "block.recruits.recruit_block": "State Troop Table",
            "block.recruits.recruit_shield_block": "Swordsman Table",
            "block.recruits.bowman_block": "Handgunner Table",
            "block.recruits.nomad_block": "Horse Archer Table",
            "block.recruits.horseman_block": "Reiksguard Table",
            "block.recruits.crossbowman_block": "Crossbow Table",
            "category.recruits": "Hosts of the Old World",
            "key.recruits.command_screen_key": "Open Host Command",
            "key.recruits.team_screen_key": "Open Elector / Faction Screen",
            "key.recruits.map_screen_key": "Open Provincial Claim Map",
            "gui.recruits.hire_gui.text.hire": "Levy for",
            "gui.recruits.command.text.team": "Electors",
            "gui.recruits.command.tooltip.team": "Opens the Elector / Faction screen",
            "gui.recruits.command.text.raid": "Waaagh!",
            "gui.recruits.inv.text.raid": "Waaagh!",
            "gui.recruits.inv.info.text.raid": "Waaagh",
            "gui.recruits.team_creation.create_team": "Found an Elector Banner",
            "gui.recruits.team_creation.inspect_team": "Inspect Faction",
            "gui.recruits.team_creation.teams_list": "List of Factions",
            "gui.recruits.diplomacy.teams_list": "Diplomacy: Factions of the Old World",
            "chat.recruits.team_creation.team_exists": "An Elector banner already uses that name!",
            "chat.recruits.team_creation.noname": "Name the banner (Reikland, Waaagh, von Carstein…).",
            "gui.recruits.toast.allyTitle": "Elector Alliance",
            "gui.recruits.toast.enemyTitle": "War Declared",
            "gui.recruits.toast.neutralTitle": "Tribute / Neutrality",
            "gui.recruits.team.diplomacy": "Diplomacy",
            "gui.recruits.team.claim": "Province Claim",
            "recruits": "State Troops",
            "chat.recruits.text.recruited1": "%s: For Sigmar and the province.",
            "chat.recruits.text.recruited2": "%s: Point me at the enemy, captain.",
            "chat.recruits.text.recruited3": "%s: Your banner is my banner.",
            "gui.recruits.text.recruited": "%s: An honour to stand in the host.",
            "gui.recruits.inv.text.governor": "Elector Steward",
            "gui.recruits.inv.tooltip.governor": "A steward claims chunks, hires state troops in towns, and takes provincial tax.",
        },
    )
    dump_json(
        rp / "assets" / "openpartiesandclaims" / "lang" / "en_us.json",
        {
            "key.openpartiesandclaims.open_party_menu": "Open Warband (OPAC)",
            "gui.openpartiesandclaims.parties": "Warbands",
            "gui.openpartiesandclaims.party": "Warband",
        },
    )
    dump_json(
        rp / "assets" / "rallous_old_world" / "lang" / "en_us.json",
        {"modmenu.descriptionTranslation.rallous_old_world": "Authored Old World campaign layer."},
    )


# ---------------------------------------------------------------------------
# FTB Quests
# ---------------------------------------------------------------------------

_qid = 0x0C030000


def nid() -> str:
    global _qid
    _qid += 1
    return f"{_qid:08X}"


def snbt_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_quest(q: dict) -> str:
    lines = ["\t\t{"]
    if q.get("deps"):
        deps = ", ".join(snbt_escape(d) for d in q["deps"])
        lines.append(f"\t\t\tdependencies: [{deps}]")
    lines.append(f"\t\t\ticon: {snbt_escape(q['icon'])}")
    lines.append(f"\t\t\tid: {snbt_escape(q['id'])}")
    # rewards
    lines.append("\t\t\trewards: [")
    reward_blocks = []
    for r in q.get("rewards") or [{"type": "xp", "xp": 20}]:
        rid = r.get("id") or nid()
        if r["type"] == "xp":
            reward_blocks.append(
                "\t\t\t\t{\n"
                f"\t\t\t\t\tid: {snbt_escape(rid)}\n"
                f"\t\t\t\t\ttype: \"xp\"\n"
                f"\t\t\t\t\txp: {r.get('xp', 20)}\n"
                "\t\t\t\t}"
            )
        elif r["type"] == "item":
            extra = f"\n\t\t\t\t\tcount: {r.get('count', 1)}" if r.get("count") else ""
            reward_blocks.append(
                "\t\t\t\t{"
                f"{extra}\n"
                f"\t\t\t\t\tid: {snbt_escape(rid)}\n"
                f"\t\t\t\t\titem: {snbt_escape(r['item'])}\n"
                f"\t\t\t\t\ttype: \"item\"\n"
                "\t\t\t\t}"
            )
        elif r["type"] == "command":
            reward_blocks.append(
                "\t\t\t\t{\n"
                f"\t\t\t\t\tcommand: {snbt_escape(r['command'])}\n"
                f"\t\t\t\t\televate_perms: true\n"
                f"\t\t\t\t\tid: {snbt_escape(rid)}\n"
                f"\t\t\t\t\tsilent: true\n"
                f"\t\t\t\t\ttype: \"command\"\n"
                "\t\t\t\t}"
            )
    lines.append(",\n".join(reward_blocks))
    lines.append("\t\t\t]")
    if q.get("shape"):
        lines.append(f"\t\t\tshape: {snbt_escape(q['shape'])}")
    if q.get("size"):
        lines.append(f"\t\t\tsize: {q['size']}d")
    if q.get("subtitle"):
        lines.append(f"\t\t\tsubtitle: {snbt_escape(q['subtitle'])}")
    # tasks
    lines.append("\t\t\ttasks: [")
    task_blocks = []
    for t in q["tasks"]:
        tid = t.get("id") or nid()
        inner = [f"\t\t\t\t\tid: {snbt_escape(tid)}"]
        if t.get("title"):
            inner.append(f"\t\t\t\t\ttitle: {snbt_escape(t['title'])}")
        inner.append(f"\t\t\t\t\ttype: {snbt_escape(t['type'])}")
        if t["type"] == "item":
            inner.append(f"\t\t\t\t\titem: {snbt_escape(t['item'])}")
            if t.get("count"):
                inner.append(f"\t\t\t\t\tcount: {t['count']}")
        if t["type"] == "advancement":
            inner.append(f"\t\t\t\t\tadvancement: {snbt_escape(t['advancement'])}")
        if t["type"] == "biome":
            inner.append(f"\t\t\t\t\tbiome: {snbt_escape(t['biome'])}")
        if t["type"] == "kill":
            inner.append(f"\t\t\t\t\tentity: {snbt_escape(t['entity'])}")
            inner.append(f"\t\t\t\t\tvalue: {t.get('value', 1)}")
        task_blocks.append("\t\t\t\t{\n" + "\n".join(inner) + "\n\t\t\t\t}")
    lines.append(",\n".join(task_blocks))
    lines.append("\t\t\t]")
    lines.append("\t\t\tdescription: [")
    desc_lines = []
    for d in q["description"]:
        desc_lines.append("\t\t\t\t" + snbt_escape(d))
    lines.append("\n".join(desc_lines))
    lines.append("\t\t\t]")
    lines.append(f"\t\t\ttitle: {snbt_escape(q['title'])}")
    lines.append(f"\t\t\tx: {q['x']}d")
    lines.append(f"\t\t\ty: {q['y']}d")
    lines.append("\t\t}")
    return "\n".join(lines)


def emit_chapter(filename: str, chapter_id: str, group: str, title: str, icon: str, order: int, quests: list[dict]) -> None:
    body = ",\n".join(emit_quest(q) for q in quests)
    w(
        CHAPTERS / f"{filename}.snbt",
        "{\n"
        "\talways_invisible: false\n"
        "\tdefault_hide_dependency_lines: false\n"
        "\tdefault_quest_shape: \"rsquare\"\n"
        f"\tfilename: {snbt_escape(filename)}\n"
        f"\tgroup: {snbt_escape(group)}\n"
        f"\ticon: {snbt_escape(icon)}\n"
        f"\tid: {snbt_escape(chapter_id)}\n"
        "\timages: [ ]\n"
        f"\torder_index: {order}\n"
        "\tquest_links: [ ]\n"
        "\tquests: [\n"
        f"{body}\n"
        "\t]\n"
        f"\ttitle: {snbt_escape(title)}\n"
        "}\n",
    )


def write_quests() -> None:
    """Court campaign FTB removed. First-contact book is scripts/author_contact.py."""
    from author_contact import write_all_quests
    write_all_quests()


def write_configs() -> None:
    # LSO: grim, not sadistic — longer first-spawn grace, keep thirst/temp/limbs
    lso = OV / "config" / "legendarysurvivaloverhaul" / "legendarysurvivaloverhaul-common.toml"
    w(
        lso,
        """# Rallous Old World — grim, not sadistic.
# Exposure and thirst matter. You get a short march to the first town.

[core]
	"Temperature Enabled" = true
	"Thirst Enabled" = true
	"Health Overhaul Enabled" = false
	"Localized Body Damage Enabled" = true

	[core.advanced]
		"Routine Packet Sync" = 30

	[core.misc]
		"Natural Regeneration Enabled" = true
		"Vanilla Freeze Enabled" = false
		"Initial Player Health" = 20.0
		"Hide Info From Debug" = false

[temperature]
	"Dangerous Heat Temperature Effects" = true
	"Dangerous Cold Temperature Effects" = true

	[temperature.temperature-immunity]
		"Temperature Immunity On Death Enabled" = true
		"Temperature Immunity On First Spawn Enabled" = true
		"Temperature Immunity On First Spawn Time" = 6000

[thirst]
	"Dangerous Dehydration" = true

[body-damage]
	"Body Part Health Mode" = "DYNAMIC"
""",
    )

    # Recruits: provincial war defaults + Empire-looking start kits
    w(
        OV / "defaultconfigs" / "recruits-server.toml",
        """# Rallous Old World — Recruits as provincial war, not a toy army.
# Server configs copy into a new world's serverconfig/ on first create.

[Recruits]
	MaxRecruitsForPlayer = 48
	RecruitCurrency = "minecraft:emerald"
	RecruitCost = 6
	BowmanCost = 8
	CrossbowmanCost = 10
	ShieldmanCost = 12
	HorsemanCost = 22
	NomadCost = 20
	RecruitsPayment = true
	RecruitsPaymentInterval = 20
	RecruitsPaymentAmount = 1
	RecruitsStarving = false
	RecruitsUpdateHungerAndMorale = true
	RecruitHorseUnitsHorse = true
	ShouldRecruitPatrolsSpawn = true
	RecruitPatrolsSpawnChance = 18.0

[Villages]
	OverrideIronGolemSpawn = true
	MaxSpawnRecruitsInVillage = 2
	NobleVillagerSpawns = true

[Equipments]
	RecruitStartEquipments = [["minecraft:iron_sword", "", "", "", "sonsoftheempire:altdorfswordsman_armor_chestplate", "sonsoftheempire:altdorfswordsman_armor_helmet"], ["minecraft:stone_sword", "", "", "", "sonsoftheempire:swordsman_armor_chestplate", "sonsoftheempire:swordsman_armor_helmet"]]
	ShieldmanStartEquipments = [["minecraft:iron_sword", "minecraft:shield", "", "sonsoftheempire:altdorfswordsman_armor_leggings", "sonsoftheempire:altdorfswordsman_armor_chestplate", "sonsoftheempire:altdorfswordsman_armor_helmet"]]
	BowmanStartEquipments = [["minecraft:bow", "", "", "", "sonsoftheempire:hochlandarmor_chestplate", "sonsoftheempire:archer_armor_helmet"]]
	HorsemanStartEquipments = [["minecraft:iron_sword", "minecraft:shield", "sonsoftheempire:empireknight_armor_boots", "sonsoftheempire:empireknight_armor_leggings", "sonsoftheempire:empireknight_armor_chestplate", "sonsoftheempire:empireknight_armor_helmet"]]
	NomadStartEquipments = [["minecraft:bow", "", "sonsoftheempire:armoredkossar_armor_boots", "", "sonsoftheempire:armoredkossar_armor_chestplate", "sonsoftheempire:armoredkossar_armor_helmet"]]

[Patrols]
	ShouldRecruitPatrolsSpawn = true
	RecruitPatrolsSpawnChance = 18.0
	RecruitPatrolSpawnInterval = 25

[Factions]
	FactionCreationCost = 16
	MaxPlayersInFaction = 8
	MaxNPCsInFaction = 200
	ShouldFactionEditingBeAllowed = true
	ShouldFactionManagingBeAllowed = true

	["Global Faction/Team Settings"]
		GlobalTeamSetting = true
		GlobalTeamFriendlyFireSetting = false
		GlobalTeamSeeFriendlyInvisibleSetting = true

[Claiming]
	AllowClaiming = true
	ClaimingCost = 48
	ChunkCost = 12
	MaxClaimChunks = 80
	CascadeThePriceOfClaims = false
	SiegeRequiresOwnerOnline = false
	SiegeClaimsRecruitsAmount = 8
	SiegeClaimsConquerTime = 8
	FogOfWarEnabled = true
""",
    )

    # Iron's: do not ship a full server toml (per-spell schema is generated).
    # A short note file next to client config would be extra docs — skip.
    # Quest copy already points players at fire / ice / holy / blood.

    # options.txt — grim stack then Continuity last (highest priority).
    # Last in the list wins. Do not add the Fabric Continuity connected-textures jar.
    opt = OV / "options.txt"
    text = opt.read_text()
    packs = (
        'resourcePacks:["vanilla","mod_resources",'
        '"file/Faithful 32x - 1.20.1.zip",'
        '"file/FreshAnimations_v1.10.4.zip",'
        '"file/GrimdarkBattlepack-v27.zip",'
        '"file/Grimdark-Sky-v1-1-15.zip",'
        '"file/Gothic RPG Font.zip",'
        '"file/Rallous Temple Herd",'
        '"file/Rallous Continuity"]'
    )
    if "resourcePacks:" in text:
        lines = []
        for line in text.splitlines(keepends=True):
            if line.startswith("resourcePacks:"):
                nl = "\n" if line.endswith("\n") else ""
                lines.append(packs + nl)
            else:
                lines.append(line)
        text = "".join(lines)
    else:
        text = text.rstrip() + "\n" + packs + "\n"
    opt.write_text(text)
    src_opt = ROOT / "pack-src" / "overrides" / "options.txt"
    src_opt.parent.mkdir(parents=True, exist_ok=True)
    src_opt.write_text(text)
    shaders = OV / "optionsshaders.txt"
    if shaders.is_file():
        src_sh = ROOT / "pack-src" / "overrides" / "optionsshaders.txt"
        src_sh.write_text(shaders.read_text())


def main() -> None:
    write_datapack()
    write_cnpc()
    write_continuity()
    write_quests()
    write_configs()
    from author_warp_crash import apply_warp_crash, strip_court_hooks

    apply_warp_crash()
    strip_court_hooks()
    print("authored Old World overrides under", OV)


if __name__ == "__main__":
    main()
