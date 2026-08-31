#!/usr/bin/env python3
"""Author the Old World content layer into pack/cf-overrides/.

Writes FTB Quests campaign chapters, rallous_old_world datapack (jar),
Rallous Continuity lang pack, CNPC lord dialogue JSON, and config glue.
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
        """execute unless entity @s[tag=rallous.old_world] run function rallous_old_world:welcome
function rallous_old_world:ensure_court
""",
    )
    w(
        data / "functions" / "welcome.mcfunction",
        """tag @s add rallous.old_world
scoreboard players set @s rallous.joined 1
title @s times 20 80 20
title @s title {"text":"The Old World","color":"gold","bold":true}
title @s subtitle {"text":"Reikland · Border Princes · Sylvania · Worlds Edge · Kislev · Chaos Wastes","color":"gray"}
tellraw @s [{"text":"A war council waits near you. Trade with a lord for a letter. Quest book: ","color":"gold"},{"text":"`","color":"white"},{"text":" (grave). Re-summon: ","color":"gold"},{"text":"/function rallous_old_world:summon_lords","color":"yellow"}]
advancement grant @s only rallous_old_world:root
function rallous_old_world:give_primer
""",
    )
    w(
        data / "functions" / "ensure_court.mcfunction",
        """execute unless entity @e[tag=rallous.lord,limit=1] at @s run function rallous_old_world:place_court
execute unless entity @e[tag=rallous.lord,limit=1] at @s run function rallous_old_world:summon_lords
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
    w(
        QUESTS / "chapter_groups.snbt",
        """{
	chapter_groups: [
		{
			id: "0A010000"
			title: "The Old World"
		}
		{
			id: "0A020000"
			title: "Boot Smoke Test"
		}
	]
}
""",
    )

    # --- Reikland ---
    q_boot = nid()
    q_karl = nid()
    q_host = nid()
    q_faction = nid()
    q_town = nid()
    q_fight = nid()
    q_win = nid()
    q_plate = nid()
    q_fire = nid()
    q_beast = nid()
    emit_chapter(
        "reikland",
        "0C020100",
        "0A010000",
        "I. Reikland",
        "sonsoftheempire:altdorfbanner",
        0,
        [
            {
                "id": q_boot,
                "title": "A Soldier of Reikland",
                "icon": "minecraft:leather_chestplate",
                "x": -4,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "subtitle": "First person. Not a lord on a campaign map.",
                "description": [
                    "You wake on the Reikland road. The war council — Karl Franz, Grimgor, Mannfred, Thorgrim, Katarin, Archaon — stands near spawn. Trade one emerald for a letter.",
                    "",
                    "Quest book: grave/tilde (`). Combat mode: V. Spell wheel: R. Map: M.",
                    "",
                    "If the court is missing: /function rallous_old_world:summon_lords",
                ],
                "tasks": [{"type": "checkmark", "title": "I am on the ground in Reikland"}],
                "rewards": [
                    {"type": "xp", "xp": 15},
                    {"type": "command", "command": "execute as @p at @s run function rallous_old_world:first_join"},
                ],
            },
            {
                "id": q_karl,
                "title": "Audience: Karl Franz",
                "icon": "sonsoftheempire:ghalmaraz",
                "x": -2,
                "y": 0,
                "deps": [q_boot],
                "description": [
                    "Trade with Karl Franz for Letter from the Emperor. He will tell you what an Elector is, what Recruits are for, and how Ally / War / Tribute work.",
                    "",
                    "Job he gives: raise a state-troop host and keep a coach road open.",
                    "Diplomacy hook: Faction screen = Electors. Vassal & Suzerains = Border Prince tribute.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/karl", "title": "Held the Emperor's letter"}],
                "rewards": [
                    {"type": "xp", "xp": 30},
                    {"type": "item", "item": "sonsoftheempire:altdorfswordsman_armor_helmet"},
                ],
            },
            {
                "id": q_town,
                "title": "Altdorf's hinterland",
                "icon": "minecraft:bell",
                "x": -2,
                "y": -2,
                "deps": [q_boot],
                "description": [
                    "Open the world map (M). Walk a Towns and Towers / CTOV settlement. Guard Villagers are the watch. This is a Reikland town, not six huts.",
                ],
                "tasks": [{"type": "checkmark", "title": "Walked a real town"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
            {
                "id": q_host,
                "title": "Raise the State Troops",
                "icon": "minecraft:emerald",
                "x": 0,
                "y": 0,
                "deps": [q_karl, q_town],
                "description": [
                    "Hire a Recruits soldier (player-model, not a farmer). Open the host command GUI. Follow.",
                    "",
                    "Lang pack calls them State Troopers. They are your first company.",
                ],
                "tasks": [{"type": "checkmark", "title": "Hired a State Trooper"}],
                "rewards": [{"type": "item", "item": "minecraft:emerald", "count": 8}],
            },
            {
                "id": q_faction,
                "title": "Name an Elector Banner",
                "icon": "minecraft:yellow_banner",
                "x": 2,
                "y": 0,
                "deps": [q_host],
                "description": [
                    "Recruits Faction screen: create a banner (Reikland, or your own Elector name). Set Ally and Enemy. Open OPAC and name a warband after a province. Open Vassal & Suzerains even if no one kneels yet.",
                    "",
                    "These UIs are the diplomacy. The lords already told you where to point them.",
                ],
                "tasks": [{"type": "checkmark", "title": "Faction / Ally / Enemy set"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": q_fight,
                "title": "Hold the River Reik",
                "icon": "minecraft:iron_sword",
                "x": 2,
                "y": 2,
                "deps": [q_host],
                "description": [
                    "Night, a dungeon, or a blood moon. Combat mode (V). Take the host. Manage thirst.",
                    "",
                    "This is a soldier's fight, not two zombies at spawn.",
                ],
                "tasks": [{"type": "checkmark", "title": "Fought with the host"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": q_plate,
                "title": "Wear Reikland Plate",
                "icon": "sonsoftheempire:altdorfswordsman_armor_chestplate",
                "x": 0,
                "y": 2,
                "deps": [q_karl],
                "description": [
                    "Commission path: iron chestplate + yellow banner + book (unlocked after Karl's letter). Or wear any Sons of the Empire Reikland / Altdorf kit. Stand next to your trooper.",
                ],
                "tasks": [{"type": "item", "item": "sonsoftheempire:altdorfswordsman_armor_chestplate", "title": "Altdorf chestplate"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
            {
                "id": q_fire,
                "title": "Sigmar's Fire",
                "icon": "minecraft:blaze_powder",
                "x": -2,
                "y": 2,
                "deps": [q_boot],
                "description": [
                    "Iron's spell book in the Curios slot. Spell wheel (R). Cast fire or holy. That is Empire battle magic — not a rainbow gym.",
                ],
                "tasks": [{"type": "checkmark", "title": "Cast fire or holy"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
            {
                "id": q_beast,
                "title": "A Beast for the Host",
                "icon": "minecraft:bone",
                "x": 0,
                "y": -2,
                "deps": [q_boot],
                "description": [
                    "Fossils: fossil → analyzer → culture vat. Or tame a Tameable Beasts mount. Karl will not gift you a horse. You earn it.",
                ],
                "tasks": [{"type": "checkmark", "title": "Owned a living beast"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": q_win,
                "title": "Win Reikland",
                "icon": "sonsoftheempire:reiklandbanner",
                "x": 4,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "deps": [q_faction, q_fight],
                "description": [
                    "Province won when two are true: the host exists, a claim/OPAC party exists, and you have fought for a road.",
                    "",
                    "Rumor south: the Border Princes will sell you a war. East: Sylvania does not stay buried. Tick this when Reikland is yours to leave.",
                ],
                "tasks": [{"type": "checkmark", "title": "Reikland is held"}],
                "rewards": [
                    {"type": "xp", "xp": 80},
                    {"type": "item", "item": "sonsoftheempire:altdorfswordsman_armor_chestplate"},
                ],
            },
        ],
    )

    # --- Border Princes ---
    b0, b1, b2, b3, b4, b5, b6 = nid(), nid(), nid(), nid(), nid(), nid(), nid()
    emit_chapter(
        "border_princes",
        "0C020200",
        "0A010000",
        "II. Border Princes",
        "minecraft:lime_banner",
        1,
        [
            {
                "id": b0,
                "title": "South of the Pass",
                "icon": "minecraft:map",
                "x": -3,
                "y": 0,
                "description": [
                    "The Border Princes have no Emperor. Hills, burned villages, rival banners. Arrive hungry. Sell your sword.",
                    "",
                    "Optional biome check: savanna / badlands / desert reads as the princedoms. You may also just ride south of your Reikland claim.",
                ],
                "tasks": [{"type": "checkmark", "title": "Left Reikland for the princedoms"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
            {
                "id": b1,
                "title": "Audience: Grimgor Ironhide",
                "icon": "minecraft:iron_axe",
                "x": -1,
                "y": 1,
                "deps": [b0],
                "description": [
                    "Trade with Grimgor for Grimgor's Challenge. He will teach you what a Waaagh is (Recruits on Raid, green banner) and that tribute is just paying a bigger boss.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/grimgor", "title": "Took the challenge"}],
                "rewards": [{"type": "xp", "xp": 30}],
            },
            {
                "id": b2,
                "title": "Sell Your Sword",
                "icon": "minecraft:iron_sword",
                "x": -1,
                "y": -1,
                "deps": [b0],
                "description": [
                    "Hire more troops or take a rival's. This is a free company, not a state levy. Name the Faction after a princedom, not an Elector, if you want to stay honest.",
                ],
                "tasks": [{"type": "checkmark", "title": "A company that is not Reikland's"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
            {
                "id": b3,
                "title": "Field Battle",
                "icon": "minecraft:skeleton_skull",
                "x": 1,
                "y": 1,
                "deps": [b1, b2],
                "description": [
                    "Host versus host, or host versus a town watch / pillager camp / dungeon that is not two zombies. Combat mode. This is the Total War army beat in first person.",
                ],
                "tasks": [{"type": "checkmark", "title": "Won a field fight"}],
                "rewards": [{"type": "xp", "xp": 50}],
            },
            {
                "id": b4,
                "title": "Take a Princedom",
                "icon": "minecraft:white_banner",
                "x": 3,
                "y": 0,
                "deps": [b3],
                "description": [
                    "Claim (Recruits) or OPAC party land, or a siege / artillery hit on a keep you do not own. Crown a puppet (Vassal), keep it, or burn it. Any choice completes.",
                ],
                "tasks": [{"type": "checkmark", "title": "A princedom changed hands"}],
                "rewards": [{"type": "xp", "xp": 80}],
            },
            {
                "id": b5,
                "title": "Waaagh or Tribute",
                "icon": "minecraft:lime_banner",
                "x": 1,
                "y": -1,
                "deps": [b1],
                "description": [
                    "Side: set a Faction to Enemy and mean it (Waaagh), or dump emeralds / open Vassal as tribute so a stronger banner looks away. Tick when the UI did that verb.",
                ],
                "tasks": [{"type": "checkmark", "title": "War or tribute happened"}],
                "rewards": [{"type": "xp", "xp": 30}],
            },
            {
                "id": b6,
                "title": "A Knight Errant",
                "icon": "sonsoftheempire:grailknight_armor_helmet",
                "x": -1,
                "y": 3,
                "deps": [b0],
                "description": [
                    "Side: Bretonnia is west of this mess. Commission a grail chestplate (iron chestplate + blue banner + book) or wear any Bretonnian kit. You do not have to take a vow.",
                ],
                "tasks": [{"type": "item", "item": "sonsoftheempire:grailknight_armor_chestplate", "title": "Grail plate"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
        ],
    )

    # --- Sylvania ---
    s0, s1, s2, s3, s4, s5 = nid(), nid(), nid(), nid(), nid(), nid()
    emit_chapter(
        "sylvania",
        "0C020300",
        "0A010000",
        "III. Sylvania",
        "minecraft:red_banner",
        2,
        [
            {
                "id": s0,
                "title": "Stirland's Shadow",
                "icon": "minecraft:dark_oak_sapling",
                "x": -3,
                "y": 0,
                "description": [
                    "East of the Empire the trees close and the bells stop. Swamp, dark forest, crypts. Enter as a warband with a fort behind you. Night is the boss.",
                ],
                "tasks": [{"type": "checkmark", "title": "Entered Sylvania"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
            {
                "id": s1,
                "title": "Audience: Mannfred von Carstein",
                "icon": "minecraft:wither_skeleton_skull",
                "x": -1,
                "y": 0,
                "deps": [s0],
                "description": [
                    "Trade for the Von Carstein Invitation. He offers a pact or a dawn war. Blood magic (Iron's) is the court tongue.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/mannfred", "title": "Read the invitation"}],
                "rewards": [{"type": "xp", "xp": 30}],
            },
            {
                "id": s2,
                "title": "Night of the Dead",
                "icon": "minecraft:zombie_head",
                "x": 1,
                "y": 1,
                "deps": [s1],
                "description": [
                    "Kill the walking dead. Born in Chaos nights count. Take the host. Stay in combat mode. Watch thirst.",
                ],
                "tasks": [{"type": "kill", "entity": "minecraft:zombie", "value": 10, "title": "10 dead put down"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": s3,
                "title": "Blood Magic",
                "icon": "minecraft:redstone",
                "x": 1,
                "y": -1,
                "deps": [s1],
                "description": [
                    "Open the spell wheel and cast a blood / evocation / death-adjacent Iron's spell. Malum is optional occult, slower.",
                ],
                "tasks": [{"type": "checkmark", "title": "Cast the court's magic"}],
                "rewards": [{"type": "xp", "xp": 30}],
            },
            {
                "id": s4,
                "title": "Dawn Siege or Dark Pact",
                "icon": "minecraft:tnt",
                "x": 3,
                "y": 0,
                "deps": [s2],
                "description": [
                    "Living path: siege / claim / artillery at dawn. Dead path: Ally a banner you treat as von Carstein and accept the standing hit with Reikland.",
                    "",
                    "Either wins the county. The Hold-Road will smell it on you.",
                ],
                "tasks": [{"type": "checkmark", "title": "Sylvania decided"}],
                "rewards": [{"type": "xp", "xp": 80}],
            },
            {
                "id": s5,
                "title": "Witch Hunter's Kit",
                "icon": "sonsoftheempire:witchhunter_armor_helmet",
                "x": -1,
                "y": 2,
                "deps": [s0],
                "description": [
                    "Side: wear Witch Hunter plate (Sons of the Empire) if you intend to refuse Mannfred. The hat is the argument.",
                ],
                "tasks": [{"type": "item", "item": "sonsoftheempire:witchhunter_armor_helmet", "title": "Witch Hunter hat"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
        ],
    )

    # --- Worlds Edge ---
    w0, w1, w2, w3, w4, w5 = nid(), nid(), nid(), nid(), nid(), nid()
    emit_chapter(
        "worlds_edge",
        "0C020400",
        "0A010000",
        "IV. Worlds Edge Mountains",
        "sonsoftheempire:highking_armor_helmet",
        3,
        [
            {
                "id": w0,
                "title": "The Hold-Road",
                "icon": "minecraft:stone_bricks",
                "x": -3,
                "y": 0,
                "description": [
                    "Extreme hills, deepslate, fortified stone. Slow travel. The gate is shut to umgi who have not paid a grudge.",
                ],
                "tasks": [{"type": "checkmark", "title": "Took the Hold-Road"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
            {
                "id": w1,
                "title": "Audience: Thorgrim Grudgebearer",
                "icon": "sonsoftheempire:grudgesettler",
                "x": -1,
                "y": 0,
                "deps": [w0],
                "description": [
                    "Trade for the Great Book entry. He will hire you as mercenary artillery if you settle one named thing.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/thorgrim", "title": "Read the grudge"}],
                "rewards": [{"type": "xp", "xp": 30}, {"type": "item", "item": "sonsoftheempire:thane_armor_helmet"}],
            },
            {
                "id": w2,
                "title": "A Grudge in the Deep",
                "icon": "minecraft:deepslate",
                "x": 1,
                "y": 1,
                "deps": [w1],
                "description": [
                    "Clear a fallen hold: YUNG dungeon, When Dungeons Arise, or a stronghold-as-lost-karak. Bring back a named relic (any rare loot you will tell Thorgrim about). Not a chest next to spawn.",
                ],
                "tasks": [{"type": "checkmark", "title": "Relic recovered"}],
                "rewards": [{"type": "xp", "xp": 50}],
            },
            {
                "id": w3,
                "title": "Ancestor Beasts",
                "icon": "minecraft:bone_block",
                "x": 1,
                "y": -1,
                "deps": [w0],
                "description": [
                    "Fossils loop finished, or a Tameable Beasts creature that could pull a cannon. The Dawi will call it ancestor-work if you did not cheat a horse.",
                ],
                "tasks": [{"type": "checkmark", "title": "A warbeast that is not a spawn egg horse"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": w4,
                "title": "Oath-Friend",
                "icon": "sonsoftheempire:thane_armor_chestplate",
                "x": 3,
                "y": 0,
                "deps": [w2],
                "description": [
                    "Ally the Dawi banner (or your own hold-name) on the Faction screen. Commission thane plate (iron chestplate + brown banner + gold). You do not become a dwarf.",
                ],
                "tasks": [{"type": "item", "item": "sonsoftheempire:thane_armor_chestplate", "title": "Thane plate"}],
                "rewards": [{"type": "xp", "xp": 80}],
            },
            {
                "id": w5,
                "title": "Umgi Proof",
                "icon": "minecraft:gold_ingot",
                "x": -1,
                "y": 2,
                "deps": [w1],
                "description": [
                    "Side: pay tribute in gold (give / dump 16 gold at the court, or set a Vassal tribute you can explain). Tick when the gold left your inventory on purpose.",
                ],
                "tasks": [{"type": "item", "item": "minecraft:gold_ingot", "count": 16, "title": "16 gold ingots"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
        ],
    )

    # --- Kislev ---
    k0, k1, k2, k3, k4, k5 = nid(), nid(), nid(), nid(), nid(), nid()
    emit_chapter(
        "kislev",
        "0C020500",
        "0A010000",
        "V. Kislev",
        "sonsoftheempire:gryphonlegion_armor_helmet",
        4,
        [
            {
                "id": k0,
                "title": "The Frozen Oblast",
                "icon": "minecraft:snowball",
                "x": -3,
                "y": 0,
                "description": [
                    "Taiga, snow, frozen peaks. Winter is a faction. LSO temperature is the tax. Drink. Eat. Do not sprint naked into an oblast night.",
                ],
                "tasks": [{"type": "checkmark", "title": "Reached the cold"}],
                "rewards": [{"type": "xp", "xp": 20}],
            },
            {
                "id": k1,
                "title": "Audience: Katarin",
                "icon": "minecraft:packed_ice",
                "x": -1,
                "y": 0,
                "deps": [k0],
                "description": [
                    "Trade for the Ice Court edict. She will tell you ice magic, kossars, and that tribute here is grain and bodies, not manners.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/katarin", "title": "Held the edict"}],
                "rewards": [
                    {"type": "xp", "xp": 30},
                    {"type": "item", "item": "sonsoftheempire:armoredkossar_armor_helmet"},
                ],
            },
            {
                "id": k2,
                "title": "Winter is the Enemy",
                "icon": "minecraft:potion",
                "x": 1,
                "y": -1,
                "deps": [k0],
                "description": [
                    "Stand in the cold until the temperature widget moves. Drink. Warm up. If you die of exposure you still understand Kislev — respawn and tick this when you have lived it.",
                ],
                "tasks": [{"type": "checkmark", "title": "Temperature moved in the snow"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
            {
                "id": k3,
                "title": "Ice Court Magic",
                "icon": "minecraft:ice",
                "x": 1,
                "y": 1,
                "deps": [k1],
                "description": [
                    "Cast an Iron's ice spell. This is the Ice Court, not a novelty snowball.",
                ],
                "tasks": [{"type": "checkmark", "title": "Cast ice"}],
                "rewards": [{"type": "xp", "xp": 30}],
            },
            {
                "id": k4,
                "title": "Defend the Gate",
                "icon": "sonsoftheempire:wingedlancer_armor_helmet",
                "x": 3,
                "y": 0,
                "deps": [k2, k3],
                "description": [
                    "Hold a town, claim, or camp in the cold with the host. A night defense or a convoy that lives is a gate held. If the convoy dies, Kislev still exists — standing suffers; tick only if you actually held.",
                ],
                "tasks": [{"type": "checkmark", "title": "A gate held"}],
                "rewards": [
                    {"type": "xp", "xp": 80},
                    {"type": "item", "item": "sonsoftheempire:armoredkossar_armor_chestplate"},
                ],
            },
            {
                "id": k5,
                "title": "Kossar Kit",
                "icon": "sonsoftheempire:armoredkossar_armor_chestplate",
                "x": -1,
                "y": 2,
                "deps": [k1],
                "description": [
                    "Side: commission kossar plate (iron chestplate + light blue banner + packed ice) or wear Gryphon Legion / winged lancer kit.",
                ],
                "tasks": [{"type": "item", "item": "sonsoftheempire:armoredkossar_armor_chestplate", "title": "Kossar chestplate"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
        ],
    )

    # --- Chaos Wastes ---
    c0, c1, c2, c3, c4, c5 = nid(), nid(), nid(), nid(), nid(), nid()
    emit_chapter(
        "chaos_wastes",
        "0C020600",
        "0A010000",
        "VI. Chaos Wastes",
        "minecraft:netherite_helmet",
        5,
        [
            {
                "id": c0,
                "title": "North of Kislev",
                "icon": "minecraft:crying_obsidian",
                "x": -3,
                "y": 0,
                "description": [
                    "Frozen peaks, ice spikes, windswept extremes, nights that do not care about your banner. There is no town. Only warbands and the Wound.",
                ],
                "tasks": [{"type": "checkmark", "title": "Entered the Wastes"}],
                "rewards": [{"type": "xp", "xp": 25}],
            },
            {
                "id": c1,
                "title": "Audience: Archaon",
                "icon": "minecraft:netherite_sword",
                "x": -1,
                "y": 0,
                "deps": [c0],
                "description": [
                    "Trade for The Everchosen's Terms. Kneel or war. Tribute is not coin.",
                ],
                "tasks": [{"type": "advancement", "advancement": "rallous_old_world:lords/archaon", "title": "Read the terms"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
            {
                "id": c2,
                "title": "Three Trials",
                "icon": "minecraft:nether_star",
                "x": 1,
                "y": 1,
                "deps": [c1],
                "description": [
                    "Complete three: a warbeast, a siege or claim fight, a relic from a dungeon, a duel in combat mode, or a standing flip on the Faction screen. Tick when any three are true.",
                ],
                "tasks": [{"type": "checkmark", "title": "Three trials done"}],
                "rewards": [{"type": "xp", "xp": 60}],
            },
            {
                "id": c3,
                "title": "The Last Battle",
                "icon": "minecraft:tnt",
                "x": 3,
                "y": 0,
                "deps": [c2],
                "description": [
                    "Siege a northern fortress or defend the last Kislev gate with the host. You may walk away and come back. This is not a credits roll.",
                ],
                "tasks": [{"type": "checkmark", "title": "Fought the last place"}],
                "rewards": [{"type": "xp", "xp": 100}],
            },
            {
                "id": c4,
                "title": "A Power on the Map",
                "icon": "minecraft:filled_map",
                "x": 5,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "deps": [c3],
                "description": [
                    "Epilogue: your warband is a Faction with land (OPAC / Recruits claim) and a host. Side chapters in Reikland through Kislev stay open. The Wound remains.",
                ],
                "tasks": [{"type": "checkmark", "title": "The campaign is a map, not a door"}],
                "rewards": [{"type": "xp", "xp": 150}],
            },
            {
                "id": c5,
                "title": "Kneel",
                "icon": "minecraft:purple_banner",
                "x": 1,
                "y": -1,
                "deps": [c1],
                "description": [
                    "Side / ending: Ally a Chaos banner; set Reikland / Kislev to Enemy. The map does not close. Heartland towns become the other war. Tick only if you meant it.",
                ],
                "tasks": [{"type": "checkmark", "title": "The howling powers named you"}],
                "rewards": [{"type": "xp", "xp": 40}],
            },
        ],
    )

    # Smoke test: keep original IDs, move to boot group, shorten copy
    smoke_src = CHAPTERS / "old_world.snbt"
    if smoke_src.exists():
        smoke_src.unlink()
    # Rewrite smoke as a short chapter reusing original quest IDs so existing ticks still match
    emit_smoke()


def emit_smoke() -> None:
    # Keep original quest IDs from 0.2.0/0.2.1 so a mid-test world does not duplicate.
    w(
        CHAPTERS / "smoke_test.snbt",
        """{
	always_invisible: false
	default_hide_dependency_lines: false
	default_quest_shape: "rsquare"
	filename: "smoke_test"
	group: "0A020000"
	icon: "minecraft:redstone_torch"
	id: "0C010001"
	images: [ ]
	order_index: 99
	quest_links: [ ]
	quests: [
		{
			icon: "minecraft:leather_chestplate"
			id: "0A010101"
			rewards: [{
				id: "0A010102"
				type: "xp"
				xp: 5
			}]
			shape: "hexagon"
			size: 1.0d
			tasks: [{
				id: "0A010103"
				title: "Grim packs + Unbound on"
				type: "checkmark"
			}]
			description: [
				"BOOT only — the campaign is the other chapters."
				"Sky not vanilla blue. Gothic font. Thirst/temp widgets. Complementary Unbound."
			]
			title: "1. Boot and look"
			x: -4.0d
			y: 0.0d
		}
		{
			dependencies: ["0A010101"]
			icon: "minecraft:potion"
			id: "0A010201"
			rewards: [{
				id: "0A010202"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010203"
				title: "Thirst and temperature moved"
				type: "checkmark"
			}]
			description: [
				"Sprint. Drink. Sun vs shade. Thirst bar and temperature icon must move."
			]
			title: "2. Body"
			x: -2.0d
			y: -1.0d
		}
		{
			dependencies: ["0A010101"]
			icon: "minecraft:iron_sword"
			id: "0A010301"
			rewards: [{
				id: "0A010302"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010303"
				title: "Combat stance on"
				type: "checkmark"
			}]
			description: [
				"Sword. V = Epic Fight combat mode. Swing. Guard."
			]
			title: "3. Steel"
			x: -2.0d
			y: 1.0d
		}
		{
			dependencies: ["0A010201"]
			icon: "minecraft:bell"
			id: "0A010401"
			rewards: [{
				id: "0A010402"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010403"
				title: "Walked a real town"
				type: "checkmark"
			}]
			description: [
				"Map M. Walk a Towns and Towers / CTOV town. Guards on patrol."
			]
			title: "4. Town"
			x: 0.0d
			y: -1.5d
		}
		{
			dependencies: ["0A010401"]
			icon: "minecraft:emerald"
			id: "0A010501"
			rewards: [{
				count: 4
				id: "0A010502"
				item: "minecraft:emerald"
				type: "item"
			}]
			tasks: [{
				id: "0A010503"
				title: "Hired a recruit"
				type: "checkmark"
			}]
			description: [
				"Hire a Recruits soldier. Follow command."
			]
			title: "5. Host"
			x: 2.0d
			y: -1.5d
		}
		{
			dependencies: ["0A010501"]
			icon: "minecraft:white_banner"
			id: "0A010601"
			rewards: [{
				id: "0A010602"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010603"
				title: "Ally or enemy set"
				type: "checkmark"
			}]
			description: [
				"Faction Ally/Enemy. OPAC party. Open Vassal UI."
			]
			title: "6. Diplomacy UI"
			x: 4.0d
			y: -1.0d
		}
		{
			dependencies: ["0A010301"]
			icon: "minecraft:book"
			id: "0A010701"
			rewards: [{
				id: "0A010702"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010703"
				title: "Opened the spell wheel"
				type: "checkmark"
			}]
			description: [
				"Iron's book in Curios. R = spell wheel. Cast."
			]
			title: "7. Magic"
			x: 0.0d
			y: 1.5d
		}
		{
			dependencies: ["0A010201"]
			icon: "minecraft:bone"
			id: "0A010801"
			rewards: [{
				id: "0A010802"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010803"
				title: "Earned a beast"
				type: "checkmark"
			}]
			description: [
				"Fossils loop or Tameable Beasts. A living creature you own."
			]
			title: "8. Beast"
			x: 2.0d
			y: 0.0d
		}
		{
			dependencies: ["0A010301", "0A010501"]
			icon: "minecraft:skeleton_skull"
			id: "0A010901"
			rewards: [{
				id: "0A010902"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010903"
				title: "Fought with the host"
				type: "checkmark"
			}]
			description: [
				"Night or dungeon with the recruit. Combat mode."
			]
			title: "9. Fight"
			x: 4.0d
			y: 1.0d
		}
		{
			dependencies: ["0A010101"]
			icon: "minecraft:golden_helmet"
			id: "0A010B01"
			rewards: [{
				id: "0A010B02"
				type: "xp"
				xp: 5
			}]
			tasks: [{
				id: "0A010B03"
				title: "Wore faction plate"
				type: "checkmark"
			}]
			description: [
				"Equip any Sons of the Empire kit."
			]
			title: "10. Plate"
			x: -2.0d
			y: 3.0d
		}
	]
	title: "Boot Smoke Test"
}
""",
    )


# ---------------------------------------------------------------------------
# Config glue
# ---------------------------------------------------------------------------

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

    # options.txt — keep grim stack, add Continuity last (highest priority)
    opt = OV / "options.txt"
    text = opt.read_text()
    old = 'resourcePacks:["vanilla","mod_resources","file/Faithful 32x - 1.20.1.zip","file/FreshAnimations_v1.10.4.zip","file/GrimdarkBattlepack-v27.zip","file/Grimdark-Sky-v1-1-15.zip","file/Gothic RPG Font.zip"]'
    new = 'resourcePacks:["vanilla","mod_resources","file/Faithful 32x - 1.20.1.zip","file/FreshAnimations_v1.10.4.zip","file/GrimdarkBattlepack-v27.zip","file/Grimdark-Sky-v1-1-15.zip","file/Gothic RPG Font.zip","file/Rallous Continuity"]'
    if old in text:
        text = text.replace(old, new)
    elif "Rallous Continuity" not in text:
        text = text.replace('","file/Gothic RPG Font.zip"]', '","file/Gothic RPG Font.zip","file/Rallous Continuity"]')
    opt.write_text(text)


def main() -> None:
    write_datapack()
    write_cnpc()
    write_continuity()
    write_quests()
    write_configs()
    print("authored Old World overrides under", OV)


if __name__ == "__main__":
    main()
