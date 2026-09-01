#!/usr/bin/env python3
"""Author first-contact FTB Quests + rallous_contact backup.

Replaces the 0.2.2 six-lords / Reikland tutorial court as the book's identity.
Book identity: warp-crash, skeptical Old World, many paths.

Writes:
  pack-src/overrides/config/ftbquests/          (requested source)
  pack/cf-overrides/config/ftbquests/           (where 0.2.2 actually lives)
  content/datapacks/rallous_contact/            (vanilla advancement + score backup)
  pack-src/overrides/datapacks/rallous_contact/
  pack/cf-overrides/datapacks/rallous_contact/
  Rallous Continuity Recruits / OPAC lang

Does not rebuild the dist zip. Does not spawn a court.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OV = ROOT / "pack" / "cf-overrides"

QUEST_DESTS = [
    ROOT / "pack-src" / "overrides" / "config" / "ftbquests" / "quests",
    ROOT / "pack-src" / "quests",
    OV / "config" / "ftbquests" / "quests",
]
CONTACT_DESTS = [
    ROOT / "content" / "datapacks" / "rallous_contact",
    ROOT / "pack-src" / "datapacks" / "rallous_contact",
    ROOT / "pack-src" / "overrides" / "datapacks" / "rallous_contact",
    OV / "datapacks" / "rallous_contact",
]

COURT_CHAPTERS = (
    "reikland",
    "border_princes",
    "sylvania",
    "worlds_edge",
    "kislev",
    "chaos_wastes",
    "first_contact",
)

# Score contract the crash datapack can read (dummy objectives).
# rallous.path:  1 help / 2 betray / 3 join / 4 align-and-leave
# rallous.race:  1 empire / 2 vampire / 3 lizard / 4 beast / 5 greenskin / 6 dwarf / 7 skaven / 8 khorne
# rallous.magic: 1 colleges / 2 ice / 3 death / 4 blood
# rallous.crash: 1 awake / 2 village / 3 fight
# Flags: rallous.proved, rallous.help, rallous.betray, rallous.join, rallous.leave,
#        rallous.empire, rallous.vampire, rallous.lizard, rallous.beast,
#        rallous.waaagh, rallous.dwarf, rallous.skaven, rallous.khorne,
#        rallous.army, rallous.chaos (khorne also bumps this)

_qid = 0x1E010000


def nid() -> str:
    global _qid
    _qid += 1
    return f"{_qid:08X}"


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if text.endswith("\n") else text + "\n")


def dump_json(path: Path, data) -> None:
    w(path, json.dumps(data, indent=2, ensure_ascii=False))


def snbt_escape(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def emit_quest(q: dict) -> str:
    lines = ["\t\t{"]
    if q.get("deps"):
        deps = ", ".join(snbt_escape(d) for d in q["deps"])
        lines.append(f"\t\t\tdependencies: [{deps}]")
    if q.get("optional"):
        lines.append("\t\t\toptional: true")
    if q.get("min_deps") is not None:
        lines.append(f"\t\t\tmin_required_dependencies: {q['min_deps']}")
    lines.append(f"\t\t\ticon: {snbt_escape(q['icon'])}")
    lines.append(f"\t\t\tid: {snbt_escape(q['id'])}")
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
    lines.append("\n".join("\t\t\t\t" + snbt_escape(d) for d in q["description"]))
    lines.append("\t\t\t]")
    lines.append(f"\t\t\ttitle: {snbt_escape(q['title'])}")
    lines.append(f"\t\t\tx: {q['x']}d")
    lines.append(f"\t\t\ty: {q['y']}d")
    lines.append("\t\t}")
    return "\n".join(lines)


def emit_chapter(filename: str, chapter_id: str, group: str, title: str, icon: str, order: int, quests: list[dict]) -> str:
    body = ",\n".join(emit_quest(q) for q in quests)
    return (
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
        "}\n"
    )


def cmd(fn: str) -> dict:
    return {"type": "command", "command": f"execute as @p at @s run function rallous_contact:{fn}"}


def write_all_quests() -> None:
    groups = """{
	chapter_groups: [
		{
			id: "1A010000"
			title: "The Warp-Crash"
		}
		{
			id: "1A020000"
			title: "Side Paths"
		}
		{
			id: "0A020000"
			title: "Warp-crash Smoke"
		}
		{
			id: "0A030000"
			title: "Temple and Herd"
		}
	]
}
"""
    data = """{
	default_autoclaim_rewards: "disabled"
	default_quest_disable_jei: false
	default_quest_shape: "rsquare"
	detection_delay: 20
	disable_gui: false
	drop_loot_crates: false
	fallback_autolock: false
	loot_crate_no_drop: {
		boss: 0
		monster: 0
		passive: 0
	}
	pause_game: true
	progression_mode: "flexible"
	verify_on_load: true
}
"""

    q_awake = "1D010001"
    q_friend = "1D010005"
    q_village = "1D010002"
    q_fight = "1D010003"
    q_proved = "1D010004"
    q_help = "1D010011"
    q_betray = "1D010012"
    q_join = "1D010013"
    q_leave = "1D010014"
    q_empire = "1D010021"
    q_vampire = "1D010022"
    q_lizard = "1D010023"
    q_beast = "1D010024"
    q_green = "1D010025"
    q_dwarf = "1D010026"
    q_skaven = "1D010027"
    q_khorne = "1D010028"
    q_winds = "1D010031"
    q_colleges = "1D010032"
    q_ice = "1D010033"
    q_death = "1D010034"
    q_blood = "1D010035"
    q_hire = "1D010051"
    q_orders = "1D010052"
    q_banner = "1D010053"

    crash = emit_chapter(
        "crash",
        "1C010000",
        "1A010000",
        "Crash",
        "minecraft:crying_obsidian",
        0,
        [
            {
                "id": q_awake,
                "title": "The Crater",
                "icon": "minecraft:crying_obsidian",
                "x": -4,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "subtitle": "Warp-crash. No court. No letters.",
                "description": [
                    "You crash-landed. Scorched blackstone, crying obsidian, a wreckage chest. Nobody lined six lords at your feet. If a peasant names an Emperor, they mean a rumor on a coin.",
                    "",
                    "This book is not a campaign map. The Old World is skeptical. Quest book: grave (`). Combat: V. Map: M. No starter spellbook.",
                    "",
                    "Prove you can last an hour — village or fight. Then help, betray, join, or align and leave.",
                ],
                "tasks": [{"type": "checkmark", "title": "I woke in the warp crater"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("crash/awake")],
            },
            {
                "id": q_friend,
                "title": "Friend elsewhere",
                "icon": "minecraft:player_head",
                "x": -2,
                "y": -3,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "A friend who joins this world is spread hundreds of blocks away and gets their own crater.",
                    "",
                    "Solo: /function rallous_old_world:crash/demo_friend_elsewhere then /function rallous_old_world:crash/return_crater",
                ],
                "tasks": [{"type": "checkmark", "title": "A second crash exists elsewhere"}],
                "rewards": [{"type": "xp", "xp": 10}],
            },
            {
                "id": q_village,
                "title": "An Hour in a Village",
                "icon": "minecraft:bell",
                "x": -1,
                "y": -2,
                "deps": [q_awake],
                "description": [
                    "Find a real settlement (Towns and Towers / a village the map M can see). Walk it. Drink. Eat. Hear them talk. They will not believe you fell from the warp.",
                    "",
                    "One hour of village life is proof. You do not need a banner yet.",
                ],
                "tasks": [{"type": "checkmark", "title": "Lived an hour among them"}],
                "rewards": [
                    {"type": "xp", "xp": 25},
                    cmd("crash/village"),
                    {
                        "type": "command",
                        "command": "execute as @p at @s run function rallous_warp_crash:first_contact",
                    },
                ],
            },
            {
                "id": q_fight,
                "title": "An Hour in a Fight",
                "icon": "minecraft:iron_sword",
                "x": -1,
                "y": 2,
                "deps": [q_awake],
                "description": [
                    "Or skip the well. Night, a road ambush, a dungeon mouth. Combat mode (V). Eight things that wanted you dead.",
                    "",
                    "The Old World respects a survivor more than a story. Thirst still counts.",
                ],
                "tasks": [{"type": "checkmark", "title": "Lasted an hour of steel"}],
                "rewards": [{"type": "xp", "xp": 25}, cmd("crash/fight")],
            },
            {
                "id": q_proved,
                "title": "Proved Yourself",
                "icon": "minecraft:filled_map",
                "x": 2,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "deps": [q_village, q_fight],
                "min_deps": 1,
                "subtitle": "Village or fight. Then the paths open.",
                "description": [
                    "Either hour is enough. The book will not make you finish both.",
                    "",
                    "Now you may help, betray, join, or align and leave. Race flavors and the Winds are rumors on the side. A host is never required.",
                ],
                "tasks": [{"type": "checkmark", "title": "The first hour is mine"}],
                "rewards": [{"type": "xp", "xp": 40}, cmd("crash/proved")],
            },
        ],
    )

    paths = emit_chapter(
        "paths",
        "1C020000",
        "1A010000",
        "Paths",
        "minecraft:oak_sign",
        1,
        [
            {
                "id": q_help,
                "title": "Help",
                "icon": "minecraft:bread",
                "x": -3,
                "y": -1.5,
                "deps": [q_proved],
                "optional": True,
                "description": [
                    "Stay. Mend a fence. Share food. Walk a coach road with the watch. The village will use you.",
                    "",
                    "Sets rallous.path = 1 (help). The datapack can read it. You may recant later.",
                ],
                "tasks": [{"type": "checkmark", "title": "I stayed and helped"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("path/help")],
            },
            {
                "id": q_betray,
                "title": "Betray",
                "icon": "minecraft:flint_and_steel",
                "x": -1,
                "y": -1.5,
                "deps": [q_proved],
                "optional": True,
                "description": [
                    "Learn their gate hour. Sell the watch. Open a door you were asked to hold. The Old World already expects this.",
                    "",
                    "Sets rallous.path = 2 (betray).",
                ],
                "tasks": [{"type": "checkmark", "title": "I used what they taught me"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("path/betray")],
            },
            {
                "id": q_join,
                "title": "Join",
                "icon": "minecraft:white_banner",
                "x": 1,
                "y": -1.5,
                "deps": [q_proved],
                "optional": True,
                "description": [
                    "Take a colour. Elector, Waaagh, Under-Empire, von Carstein, Dawi, herd, temple-city, Bloodbound — a Recruits banner or a lie you intend to keep.",
                    "",
                    "Sets rallous.path = 3 (join). Host command is still optional.",
                ],
                "tasks": [{"type": "checkmark", "title": "I took a banner"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("path/join")],
            },
            {
                "id": q_leave,
                "title": "Align and Leave",
                "icon": "minecraft:leather_boots",
                "x": 3,
                "y": -1.5,
                "deps": [q_proved],
                "optional": True,
                "description": [
                    "Shake a hand. Mean it. Walk away. Standing can exist without a payroll. The map does not close.",
                    "",
                    "Sets rallous.path = 4 (align-and-leave).",
                ],
                "tasks": [{"type": "checkmark", "title": "I named a side and rode on"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("path/leave")],
            },
        ],
    )

    first_hour = emit_chapter(
        "first_hour",
        "1C030000",
        "1A010000",
        "First Hour",
        "minecraft:compass",
        2,
        [
            {
                "id": q_empire,
                "title": "Empire",
                "icon": "sonsoftheempire:altdorfbanner",
                "x": -3.5,
                "y": -1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Plains, coach roads, a town with a bell. They will call you soldier if you stand still long enough. Electors are banners, not a court at spawn.",
                    "",
                    "Thin first-hour: walk a settlement. Sets rallous.race = 1 and rallous.empire.",
                ],
                "tasks": [{"type": "checkmark", "title": "Heard an Elector named in town"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/empire")],
            },
            {
                "id": q_vampire,
                "title": "Vampire Counts",
                "icon": "minecraft:red_banner",
                "x": -1.5,
                "y": -1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Swamp, dark wood, bells that stop. Night is the county. No invitation is waiting on a stand.",
                    "",
                    "Thin first-hour: stay out after dusk in wet or dark trees. Sets rallous.race = 2 and rallous.vampire.",
                ],
                "tasks": [{"type": "checkmark", "title": "Walked the night counties"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/vampire")],
            },
            {
                "id": q_lizard,
                "title": "Lizardmen",
                "icon": "minecraft:jungle_leaves",
                "x": 0.5,
                "y": -1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Jungle, warm ruin, something older than the Empire's calendar. They will not explain the Great Plan.",
                    "",
                    "Thin first-hour: reach jungle or a temple-shaped pile. Sets rallous.race = 3 and rallous.lizard.",
                ],
                "tasks": [{"type": "checkmark", "title": "Found a warm ruin"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/lizard")],
            },
            {
                "id": q_beast,
                "title": "Beastmen",
                "icon": "minecraft:goat_horn",
                "x": 2.5,
                "y": -1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Herd-sign on a tree. Dark forest. They do not hire. They gather.",
                    "",
                    "Thin first-hour: hear a horn or walk a dark wood at night. Sets rallous.race = 4 and rallous.beast.",
                ],
                "tasks": [{"type": "checkmark", "title": "Read herd-sign"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/beast")],
            },
            {
                "id": q_green,
                "title": "Greenskins",
                "icon": "minecraft:lime_banner",
                "x": -3.5,
                "y": 1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Hills, savanna, a scrap already in progress. A Waaagh is a banner on Raid, not a lord with a letter.",
                    "",
                    "Thin first-hour: win a messy fight in open country. Sets rallous.race = 5 and rallous.waaagh.",
                ],
                "tasks": [{"type": "checkmark", "title": "Joined a scrap, or started one"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/greenskin")],
            },
            {
                "id": q_dwarf,
                "title": "Dwarfs",
                "icon": "minecraft:stone_bricks",
                "x": -1.5,
                "y": 1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Stone, deepslate, a gate that does not care about your crash. Umgi prove themselves with work, not speeches.",
                    "",
                    "Thin first-hour: take the high road or a deep cut. Sets rallous.race = 6 and rallous.dwarf.",
                ],
                "tasks": [{"type": "checkmark", "title": "Walked a hold-road or a deep cut"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/dwarf")],
            },
            {
                "id": q_skaven,
                "title": "Skaven",
                "icon": "minecraft:deepslate",
                "x": 0.5,
                "y": 1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Under-Empire is below the map. Mineshafts, sewers, eyes in the dark. They will sell you, then sell the sale.",
                    "",
                    "Thin first-hour: go under. Sets rallous.race = 7 and rallous.skaven.",
                ],
                "tasks": [{"type": "checkmark", "title": "Heard claws under the floor"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/skaven")],
            },
            {
                "id": q_khorne,
                "title": "Khorne",
                "icon": "minecraft:netherite_axe",
                "x": 2.5,
                "y": 1.5,
                "deps": [q_awake],
                "optional": True,
                "description": [
                    "Skulls. Brass. No wizard's excuse. If you came here for a spellbook, you came to the wrong ruin.",
                    "",
                    "Thin first-hour: take heads in combat mode. Sets rallous.race = 8, rallous.khorne, and rallous.chaos.",
                ],
                "tasks": [
                    {
                        "type": "kill",
                        "title": "Blood for the first hour",
                        "entity": "minecraft:skeleton",
                        "value": 6,
                    }
                ],
                "rewards": [{"type": "xp", "xp": 15}, cmd("race/khorne")],
            },
        ],
    )

    winds = emit_chapter(
        "winds",
        "1C040000",
        "1A010000",
        "The Winds",
        "minecraft:amethyst_shard",
        3,
        [
            {
                "id": q_winds,
                "title": "Not in the Hotbar",
                "icon": "minecraft:book",
                "x": -3,
                "y": 0,
                "shape": "hexagon",
                "size": 1.5,
                "deps": [q_awake],
                "subtitle": "No starter spellbook.",
                "description": [
                    "You did not arrive with Iron's book equipped. The Winds are a path, not a loadout. Walk to a camp lectern.",
                    "",
                    "Colleges (fire / light), Ice, death, and Blood are rumors until you walk to them. Do not craft a book just to tick a boot list.",
                    "",
                    "Spell wheel (R) exists when you have earned a book. Until then, steel and thirst.",
                ],
                "tasks": [{"type": "checkmark", "title": "I have no college letter yet"}],
                "rewards": [{"type": "xp", "xp": 10}, cmd("magic/discover")],
            },
            {
                "id": q_colleges,
                "title": "Path to the Colleges",
                "icon": "minecraft:blaze_powder",
                "x": -0.5,
                "y": -2,
                "deps": [q_winds],
                "optional": True,
                "description": [
                    "Walk to an Empire or Lizardmen camp. Read the named lectern (College Letter). The barrel rarely holds Iron's common ink. Dungeon chests hide ink and scrolls. Do not start with a book in the hotbar.",
                    "",
                    "Sets rallous.magic = 1 (colleges).",
                ],
                "tasks": [{"type": "checkmark", "title": "Found a college path"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("magic/colleges")],
            },
            {
                "id": q_ice,
                "title": "Path to Ice",
                "icon": "minecraft:packed_ice",
                "x": 1.5,
                "y": -1,
                "deps": [q_winds],
                "optional": True,
                "description": [
                    "Nordland, Ostland, Hochland, Middenland, or snow: a Kislevite Ice Primer on the lectern. Ink in the barrel or a cold ruin. Ice is a court, not a novelty.",
                    "",
                    "Sets rallous.magic = 2 (ice).",
                ],
                "tasks": [{"type": "checkmark", "title": "Found an ice path"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("magic/ice")],
            },
            {
                "id": q_death,
                "title": "Path to Death",
                "icon": "minecraft:wither_skeleton_skull",
                "x": 1.5,
                "y": 1,
                "deps": [q_winds],
                "optional": True,
                "description": [
                    "Vampire camp lectern: Grave Missive. A priest who does not smile. Ink in the barrel or a crypt. Malum is slower occult if you want it later.",
                    "",
                    "Sets rallous.magic = 3 (death).",
                ],
                "tasks": [{"type": "checkmark", "title": "Found a death path"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("magic/death")],
            },
            {
                "id": q_blood,
                "title": "Path to Blood",
                "icon": "minecraft:redstone",
                "x": -0.5,
                "y": 2,
                "deps": [q_winds],
                "optional": True,
                "description": [
                    "Lahmia, a Khorne picket, or a Beastmen herd: Vein Rite on the lectern. A count's cellar. Ink first. Blood is a school you walk to.",
                    "",
                    "Sets rallous.magic = 4 (blood).",
                ],
                "tasks": [{"type": "checkmark", "title": "Found a blood path"}],
                "rewards": [{"type": "xp", "xp": 20}, cmd("magic/blood")],
            },
        ],
    )

    host = emit_chapter(
        "host",
        "1C060000",
        "1A020000",
        "The Host",
        "minecraft:emerald",
        91,
        [
            {
                "id": q_hire,
                "title": "Levy a Body",
                "icon": "minecraft:emerald",
                "x": -2,
                "y": 0,
                "optional": True,
                "subtitle": "Optional. Never required.",
                "description": [
                    "SIDE PATH. Crash, Paths, First Hour, and the Winds do not need this.",
                    "",
                    "Hire a Recruits soldier. Continuity calls the UI Elector / Waaagh / Under-Empire / the rest. They are a host, not a tutorial.",
                ],
                "tasks": [{"type": "checkmark", "title": "Hired one soldier"}],
                "rewards": [
                    {"type": "item", "item": "minecraft:emerald", "count": 4},
                    cmd("army/open"),
                ],
            },
            {
                "id": q_orders,
                "title": "Give an Order",
                "icon": "minecraft:iron_sword",
                "x": 0,
                "y": 0,
                "deps": [q_hire],
                "optional": True,
                "description": [
                    "Open Host Command. Follow. Stay. Aggressive. You are allowed to fire them.",
                ],
                "tasks": [{"type": "checkmark", "title": "Command screen used"}],
                "rewards": [{"type": "xp", "xp": 10}, cmd("army/orders")],
            },
            {
                "id": q_banner,
                "title": "Name a Banner",
                "icon": "minecraft:white_banner",
                "x": 2,
                "y": 0,
                "deps": [q_hire],
                "optional": True,
                "description": [
                    "Faction screen: Elector, Waaagh, Under-Empire, von Carstein, Dawi hold, herd, temple-city, Bloodbound. Ally / Enemy. OPAC is warband land.",
                    "",
                    "Still optional. A lone body can finish the first hour.",
                ],
                "tasks": [{"type": "checkmark", "title": "Banner named"}],
                "rewards": [{"type": "xp", "xp": 15}, cmd("army/banner")],
            },
        ],
    )

    files = {
        "chapter_groups.snbt": groups,
        "data.snbt": data,
        "chapters/crash.snbt": crash,
        "chapters/paths.snbt": paths,
        "chapters/first_hour.snbt": first_hour,
        "chapters/winds.snbt": winds,
        "chapters/host.snbt": host,
    }

    smoke_src = OV / "config" / "ftbquests" / "quests" / "chapters" / "smoke_test.snbt"
    smoke_text = smoke_src.read_text() if smoke_src.exists() else ""

    for dest in QUEST_DESTS:
        dest.mkdir(parents=True, exist_ok=True)
        (dest / "chapters").mkdir(parents=True, exist_ok=True)
        for old in COURT_CHAPTERS:
            p = dest / "chapters" / f"{old}.snbt"
            if p.exists():
                p.unlink()
        for rel, text in files.items():
            w(dest / rel, text)
        if smoke_text:
            w(dest / "chapters" / "smoke_test.snbt", smoke_text)


def write_contact_datapack() -> None:
    pack_mcmeta = {
        "pack": {
            "pack_format": 15,
            "description": "Rallous first-contact scores + backup advancements (no court)",
        }
    }
    load_fn = """# rallous_contact — scores the crash datapack / FTB rewards can read.
# rallous.path:  1 help / 2 betray / 3 join / 4 align-and-leave
# rallous.race:  1 empire / 2 vampire / 3 lizard / 4 beast / 5 greenskin / 6 dwarf / 7 skaven / 8 khorne
# rallous.magic: 1 colleges / 2 ice / 3 death / 4 blood
# rallous.crash: 1 awake / 2 village / 3 fight
scoreboard objectives add rallous.contact dummy
scoreboard objectives add rallous.path dummy
scoreboard objectives add rallous.help dummy
scoreboard objectives add rallous.betray dummy
scoreboard objectives add rallous.join dummy
scoreboard objectives add rallous.leave dummy
scoreboard objectives add rallous.race dummy
scoreboard objectives add rallous.empire dummy
scoreboard objectives add rallous.vampire dummy
scoreboard objectives add rallous.lizard dummy
scoreboard objectives add rallous.beast dummy
scoreboard objectives add rallous.waaagh dummy
scoreboard objectives add rallous.dwarf dummy
scoreboard objectives add rallous.skaven dummy
scoreboard objectives add rallous.khorne dummy
scoreboard objectives add rallous.chaos dummy
scoreboard objectives add rallous.kislev dummy
scoreboard objectives add rallous.crash dummy
scoreboard objectives add rallous.proved dummy
scoreboard objectives add rallous.magic dummy
scoreboard objectives add rallous.army dummy
"""

    def fn_crash(kind: str, score: int, adv: str, msg: str) -> str:
        extra = ""
        if kind == "proved":
            extra = "scoreboard players set @s rallous.proved 1\n"
        return (
            f"scoreboard players set @s rallous.crash {score}\n"
            f"{extra}"
            f"advancement grant @s only rallous_contact:{adv}\n"
            f'tellraw @s {{"text":"{msg}","color":"gray"}}\n'
        )

    functions = {
        "load.mcfunction": load_fn,
        "crash/awake.mcfunction": fn_crash(
            "awake",
            1,
            "crash/root",
            "The sky tore. No court. Prove an hour.",
        ),
        "crash/village.mcfunction": fn_crash(
            "village",
            2,
            "crash/village",
            "An hour among them. They still do not believe the warp.",
        ),
        "crash/fight.mcfunction": fn_crash(
            "fight",
            3,
            "crash/fight",
            "An hour of steel. That is a kind of proof.",
        ),
        "crash/proved.mcfunction": fn_crash(
            "proved",
            1,
            "crash/proved",
            "Proved. Help, betray, join, or align and leave.",
        ),
        "path/help.mcfunction": (
            "scoreboard players set @s rallous.path 1\n"
            "scoreboard players set @s rallous.help 1\n"
            "advancement grant @s only rallous_contact:path/help\n"
            'tellraw @s {"text":"Path: help. rallous.path=1","color":"gray"}\n'
            "function rallous_diplomacy:apply_path\n"
            "function rallous_factions:path/sync\n"
        ),
        "path/betray.mcfunction": (
            "scoreboard players set @s rallous.path 2\n"
            "scoreboard players set @s rallous.betray 1\n"
            "advancement grant @s only rallous_contact:path/betray\n"
            'tellraw @s {"text":"Path: betray. rallous.path=2","color":"gray"}\n'
            "function rallous_diplomacy:apply_path\n"
            "function rallous_factions:path/sync\n"
        ),
        "path/join.mcfunction": (
            "scoreboard players set @s rallous.path 3\n"
            "scoreboard players set @s rallous.join 1\n"
            "advancement grant @s only rallous_contact:path/join\n"
            'tellraw @s {"text":"Path: join. rallous.path=3","color":"gray"}\n'
            "function rallous_diplomacy:apply_path\n"
            "function rallous_factions:path/sync\n"
        ),
        "path/leave.mcfunction": (
            "scoreboard players set @s rallous.path 4\n"
            "scoreboard players set @s rallous.leave 1\n"
            "advancement grant @s only rallous_contact:path/leave\n"
            'tellraw @s {"text":"Path: align-and-leave. rallous.path=4","color":"gray"}\n'
            "function rallous_diplomacy:apply_path\n"
            "function rallous_factions:path/sync\n"
        ),
        "race/empire.mcfunction": (
            "scoreboard players set @s rallous.race 1\n"
            "scoreboard players add @s rallous.empire 1\n"
            "advancement grant @s only rallous_contact:race/empire\n"
        ),
        "race/vampire.mcfunction": (
            "scoreboard players set @s rallous.race 2\n"
            "scoreboard players add @s rallous.vampire 1\n"
            "advancement grant @s only rallous_contact:race/vampire\n"
        ),
        "race/lizard.mcfunction": (
            "scoreboard players set @s rallous.race 3\n"
            "scoreboard players add @s rallous.lizard 1\n"
            "advancement grant @s only rallous_contact:race/lizard\n"
        ),
        "race/beast.mcfunction": (
            "scoreboard players set @s rallous.race 4\n"
            "scoreboard players add @s rallous.beast 1\n"
            "advancement grant @s only rallous_contact:race/beast\n"
        ),
        "race/greenskin.mcfunction": (
            "scoreboard players set @s rallous.race 5\n"
            "scoreboard players add @s rallous.waaagh 1\n"
            "advancement grant @s only rallous_contact:race/greenskin\n"
        ),
        "race/dwarf.mcfunction": (
            "scoreboard players set @s rallous.race 6\n"
            "scoreboard players add @s rallous.dwarf 1\n"
            "advancement grant @s only rallous_contact:race/dwarf\n"
        ),
        "race/skaven.mcfunction": (
            "scoreboard players set @s rallous.race 7\n"
            "scoreboard players add @s rallous.skaven 1\n"
            "advancement grant @s only rallous_contact:race/skaven\n"
        ),
        "race/khorne.mcfunction": (
            "scoreboard players set @s rallous.race 8\n"
            "scoreboard players add @s rallous.khorne 1\n"
            "scoreboard players add @s rallous.chaos 1\n"
            "advancement grant @s only rallous_contact:race/khorne\n"
        ),
        "magic/discover.mcfunction": (
            "scoreboard players set @s rallous.magic 0\n"
            "advancement grant @s only rallous_contact:magic/root\n"
            'tellraw @s {"text":"The Winds are not a hotbar.","color":"gray"}\n'
        ),
        "magic/colleges.mcfunction": (
            "scoreboard players set @s rallous.magic 1\n"
            "advancement grant @s only rallous_contact:magic/colleges\n"
        ),
        "magic/ice.mcfunction": (
            "scoreboard players set @s rallous.magic 2\n"
            "scoreboard players add @s rallous.kislev 1\n"
            "advancement grant @s only rallous_contact:magic/ice\n"
        ),
        "magic/death.mcfunction": (
            "scoreboard players set @s rallous.magic 3\n"
            "advancement grant @s only rallous_contact:magic/death\n"
        ),
        "magic/blood.mcfunction": (
            "scoreboard players set @s rallous.magic 4\n"
            "advancement grant @s only rallous_contact:magic/blood\n"
        ),
        "army/open.mcfunction": (
            "scoreboard players add @s rallous.army 1\n"
            "advancement grant @s only rallous_contact:army/root\n"
        ),
        "army/orders.mcfunction": (
            "scoreboard players add @s rallous.army 1\n"
            "advancement grant @s only rallous_contact:army/orders\n"
        ),
        "army/banner.mcfunction": (
            "scoreboard players add @s rallous.army 1\n"
            "advancement grant @s only rallous_contact:army/banner\n"
        ),
    }

    def adv(title: str, desc: str, icon: str, parent: str | None, criteria: dict, frame: str = "task") -> dict:
        display = {
            "icon": {"item": icon},
            "title": {"text": title},
            "description": {"text": desc},
            "frame": frame,
            "announce_to_chat": False,
            "show_toast": True,
            "hidden": False,
        }
        if parent is None:
            display["background"] = "minecraft:textures/block/crying_obsidian.png"
        out: dict = {"display": display, "criteria": criteria, "requirements": [[k] for k in criteria]}
        if parent:
            out["parent"] = parent
        return out

    impossible = {"impossible": {"trigger": "minecraft:impossible"}}
    tick = {"tick": {"trigger": "minecraft:tick"}}

    def loc_biome(biome: str) -> dict:
        return {
            "here": {
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
        }

    def loc_structure(structure: str) -> dict:
        return {
            "here": {
                "trigger": "minecraft:location",
                "conditions": {
                    "player": [
                        {
                            "condition": "minecraft:entity_properties",
                            "entity": "this",
                            "predicate": {"location": {"structure": structure}},
                        }
                    ]
                },
            }
        }

    def kills(entity: str, n: int) -> dict:
        return {
            "kills": {
                "trigger": "minecraft:player_killed_entity",
                "conditions": {"entity": [{"condition": "minecraft:entity_properties", "entity": "this", "predicate": {"type": entity}}]},
            }
        }

    # Keep kill advancements grantable by function even if the player kills something else.
    # Backup path: location / kill where it is honest; choices stay impossible + function grant.

    advancements = {
        "root.json": adv(
            "The Warp-Crash",
            "A skeptical Old World. Many paths. No tutorial court.",
            "minecraft:crying_obsidian",
            None,
            tick,
            "challenge",
        ),
        "crash/root.json": adv(
            "The Sky Tore",
            "On the ground. No six lords.",
            "minecraft:crying_obsidian",
            "rallous_contact:root",
            impossible,
        ),
        "crash/village.json": adv(
            "An Hour in a Village",
            "Walk a settlement. They will not believe the warp.",
            "minecraft:bell",
            "rallous_contact:crash/root",
            loc_structure("minecraft:village"),
        ),
        "crash/fight.json": adv(
            "An Hour in a Fight",
            "Steel is a kind of proof.",
            "minecraft:iron_sword",
            "rallous_contact:crash/root",
            {
                "kills": {
                    "trigger": "minecraft:player_killed_entity",
                    "conditions": {
                        "entity": [
                            {
                                "condition": "minecraft:entity_properties",
                                "entity": "this",
                                "predicate": {"type": "minecraft:zombie"},
                            }
                        ]
                    },
                }
            },
        ),
        "crash/proved.json": adv(
            "Proved Yourself",
            "Village or fight. Paths open.",
            "minecraft:filled_map",
            "rallous_contact:crash/root",
            impossible,
            "goal",
        ),
        "path/help.json": adv("Help", "rallous.path=1", "minecraft:bread", "rallous_contact:crash/proved", impossible),
        "path/betray.json": adv("Betray", "rallous.path=2", "minecraft:flint_and_steel", "rallous_contact:crash/proved", impossible),
        "path/join.json": adv("Join", "rallous.path=3", "minecraft:white_banner", "rallous_contact:crash/proved", impossible),
        "path/leave.json": adv("Align and Leave", "rallous.path=4", "minecraft:leather_boots", "rallous_contact:crash/proved", impossible),
        "race/empire.json": adv("Empire", "rallous.race=1 Elector towns", "minecraft:yellow_banner", "rallous_contact:root", loc_structure("minecraft:village")),
        "race/vampire.json": adv("Vampire Counts", "rallous.race=2", "minecraft:red_banner", "rallous_contact:root", loc_biome("minecraft:swamp")),
        "race/lizard.json": adv("Lizardmen", "rallous.race=3", "minecraft:jungle_leaves", "rallous_contact:root", loc_biome("minecraft:jungle")),
        "race/beast.json": adv("Beastmen", "rallous.race=4", "minecraft:goat_horn", "rallous_contact:root", loc_biome("minecraft:dark_forest")),
        "race/greenskin.json": adv("Greenskins", "rallous.race=5 Waaagh", "minecraft:lime_banner", "rallous_contact:root", loc_biome("minecraft:savanna")),
        "race/dwarf.json": adv("Dwarfs", "rallous.race=6", "minecraft:stone_bricks", "rallous_contact:root", loc_biome("minecraft:windswept_hills")),
        "race/skaven.json": adv("Skaven", "rallous.race=7 Under-Empire", "minecraft:deepslate", "rallous_contact:root", loc_structure("minecraft:mineshaft")),
        "race/khorne.json": adv("Khorne", "rallous.race=8", "minecraft:netherite_axe", "rallous_contact:root", loc_biome("minecraft:nether_wastes")),
        "magic/root.json": adv(
            "Not in the Hotbar",
            "No starter spellbook. The Winds are a path.",
            "minecraft:book",
            "rallous_contact:root",
            impossible,
        ),
        "magic/colleges.json": adv("Path to the Colleges", "rallous.magic=1", "minecraft:blaze_powder", "rallous_contact:magic/root", impossible),
        "magic/ice.json": adv("Path to Ice", "rallous.magic=2", "minecraft:packed_ice", "rallous_contact:magic/root", impossible),
        "magic/death.json": adv("Path to Death", "rallous.magic=3", "minecraft:wither_skeleton_skull", "rallous_contact:magic/root", impossible),
        "magic/blood.json": adv("Path to Blood", "rallous.magic=4", "minecraft:redstone", "rallous_contact:magic/root", impossible),
        "army/root.json": adv("The Host", "Optional Recruits. Never required.", "minecraft:emerald", "rallous_contact:root", impossible),
        "army/orders.json": adv("Give an Order", "Host command used.", "minecraft:iron_sword", "rallous_contact:army/root", impossible),
        "army/banner.json": adv("Name a Banner", "Elector / Waaagh / Under-Empire / …", "minecraft:white_banner", "rallous_contact:army/root", impossible),
    }

    lang = {
        "advancements.rallous_contact.root.title": "The Warp-Crash",
        "advancements.rallous_contact.root.description": "A skeptical Old World. Many paths.",
    }

    first = None
    for dest in CONTACT_DESTS:
        if dest.exists():
            shutil.rmtree(dest)
        dump_json(dest / "pack.mcmeta", pack_mcmeta)
        w(
            dest / "META-INF" / "mods.toml",
            """modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="rallous_contact"
version="1.0.0"
displayName="Rallous Contact"
authors="Rallous System"
description='''First-contact scores and backup advancements. No court.'''
""",
        )
        dump_json(
            dest / "data" / "minecraft" / "tags" / "functions" / "load.json",
            {"values": ["rallous_contact:load"]},
        )
        data = dest / "data" / "rallous_contact"
        for rel, text in functions.items():
            w(data / "functions" / rel, text)
        for rel, payload in advancements.items():
            dump_json(data / "advancements" / rel, payload)
        dump_json(dest / "assets" / "rallous_contact" / "lang" / "en_us.json", lang)
        if first is None:
            first = dest


def recruits_lang() -> dict:
    return {
        "entity.recruits.recruit": "Levy",
        "entity.recruits.bowman": "Bow Levy",
        "entity.recruits.recruit_shieldman": "Shield Levy",
        "entity.recruits.nomad": "Horse Archer",
        "entity.recruits.horseman": "Rider",
        "entity.recruits.crossbowman": "Pavise Crossbow",
        "entity.recruits.scout": "Outrider",
        "entity.recruits.captain": "Captain",
        "entity.recruits.commander": "Sergeant",
        "entity.recruits.messenger": "Runner",
        "entity.recruits.siege_engineer": "Engineer",
        "item.recruits.recruit_spawn_egg": "Levy Spawn Egg",
        "item.recruits.bowman_spawn_egg": "Bow Levy Spawn Egg",
        "item.recruits.nomad_spawn_egg": "Horse Archer Spawn Egg",
        "item.recruits.horseman_spawn_egg": "Rider Spawn Egg",
        "item.recruits.recruit_shieldman_spawn_egg": "Shield Levy Spawn Egg",
        "item.recruits.crossbowman_spawn_egg": "Pavise Crossbow Spawn Egg",
        "item.recruits.villager_noble_spawn_egg": "Banner Courtier Spawn Egg",
        "block.recruits.recruit_block": "Levy Table",
        "block.recruits.recruit_shield_block": "Shield Levy Table",
        "block.recruits.bowman_block": "Bow Levy Table",
        "block.recruits.nomad_block": "Horse Archer Table",
        "block.recruits.horseman_block": "Rider Table",
        "block.recruits.crossbowman_block": "Crossbow Table",
        "category.recruits": "Hosts of the Old World",
        "key.recruits.command_screen_key": "Open Host Command",
        "key.recruits.team_screen_key": "Open Elector / Waaagh / Under-Empire Screen",
        "key.recruits.map_screen_key": "Open Provincial Claim Map",
        "gui.recruits.hire_gui.text.hire": "Levy for",
        "gui.recruits.command.text.team": "Banners",
        "gui.recruits.command.tooltip.team": "Elector · Waaagh · Under-Empire · von Carstein · Dawi · herd · temple-city · Bloodbound",
        "gui.recruits.command.text.raid": "Waaagh!",
        "gui.recruits.inv.text.raid": "Waaagh!",
        "gui.recruits.inv.info.text.raid": "Waaagh",
        "gui.recruits.team_creation.create_team": "Found a Banner",
        "gui.recruits.team_creation.inspect_team": "Inspect Banner",
        "gui.recruits.team_creation.teams_list": "Electors, Waaaghs, the Under-Empire, and the rest",
        "gui.recruits.diplomacy.teams_list": "Diplomacy: Elector / Waaagh / Under-Empire / von Carstein / Dawi",
        "chat.recruits.team_creation.team_exists": "A banner already uses that name!",
        "chat.recruits.team_creation.noname": "Name the banner (Elector, Waaagh, Under-Empire, von Carstein, Dawi hold, herd, temple-city, Bloodbound…).",
        "gui.recruits.toast.allyTitle": "Banner Alliance",
        "gui.recruits.toast.enemyTitle": "War Declared",
        "gui.recruits.toast.neutralTitle": "Tribute / Neutrality",
        "gui.recruits.team.diplomacy": "Diplomacy",
        "gui.recruits.team.claim": "Province Claim",
        "recruits": "Levies",
        "chat.recruits.text.recruited1": "%s: Pay and I stand.",
        "chat.recruits.text.recruited2": "%s: Point me at the enemy.",
        "chat.recruits.text.recruited3": "%s: Your banner is my banner.",
        "gui.recruits.text.recruited": "%s: An honour to stand in the host.",
        "gui.recruits.inv.text.governor": "Banner Steward",
        "gui.recruits.inv.tooltip.governor": "A steward claims chunks, hires levies, and takes provincial tax — Elector, Waaagh, or Under-Empire alike.",
    }


def write_continuity() -> None:
    dests = [
        OV / "resourcepacks" / "Rallous Continuity",
        ROOT / "pack-src" / "overrides" / "resourcepacks" / "Rallous Continuity",
        ROOT / "pack-src" / "resourcepacks" / "Rallous Continuity",
    ]
    for rp in dests:
        dump_json(
            rp / "pack.mcmeta",
            {"pack": {"pack_format": 15, "description": "Old World names: Elector / Waaagh / Under-Empire / warband"}},
        )
        dump_json(rp / "assets" / "recruits" / "lang" / "en_us.json", recruits_lang())
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
        dump_json(
            rp / "assets" / "rallous_contact" / "lang" / "en_us.json",
            {
                "advancements.rallous_contact.root.title": "The Warp-Crash",
                "advancements.rallous_contact.root.description": "A skeptical Old World. Many paths.",
            },
        )


BOOK_BLURB = (
    "**Quest book identity:** **The Warp-Crash** — Crash (crater, then ~1 hour village *or* fight) "
    "→ Paths (help / betray / join / align-and-leave; each sets `rallous.path` for the datapack) "
    "→ First Hour (Empire, Vampire Counts, Lizardmen, Beastmen, Greenskins, Dwarfs, Skaven, Khorne) "
    "→ The Winds (no starter spellbook; Colleges / Ice / death / Blood). "
    "**The Host** is optional Recruits. Smoke is a side checklist. There is no Reikland tutorial court."
)


def write_play() -> None:
    path = ROOT / "PLAY.md"
    if not path.exists():
        return
    text = path.read_text()
    if "rallous.path" not in text:
        needle = "A new world is a **Warp-crash**."
        if needle in text:
            text = text.replace(
                needle,
                BOOK_BLURB + "\n\n" + needle,
                1,
            )
        else:
            text = BOOK_BLURB + "\n\n" + text
    text = text.replace(
        "State Trooper / Elector / Waaagh",
        "Levy / Elector / Waaagh / Under-Empire",
    )
    text = text.replace(
        "**State Trooper** / **Elector** / **Waaagh**",
        "**Levy** / **Elector** / **Waaagh** / **Under-Empire**",
    )
    text = text.replace(
        "Recruits / OPAC lang: State Trooper, Elector, Waaagh",
        "Recruits / OPAC lang: Levy, Elector, Waaagh, Under-Empire",
    )
    text = text.replace(
        "First-contact + Warp-crash Smoke FTB chapters (the 10 checks below)",
        "Warp-Crash FTB book (Crash / Paths / First Hour / The Winds / optional Host) + Smoke (the 10 checks below)",
    )
    text = text.replace(
        "First Contact + Smoke + Old World chapters",
        "Warp-Crash + Smoke",
    )
    w(path, text)
    w(OV / "PLAY.md", text)


def validate() -> None:
    banned = ("Audience: Karl", "Trade with Karl Franz", "summon_lords", "A Soldier of Reikland")
    live = OV / "config" / "ftbquests" / "quests"
    chapters = sorted(p.name for p in (live / "chapters").glob("*.snbt"))
    expect = ["crash.snbt", "first_hour.snbt", "host.snbt", "paths.snbt", "winds.snbt"]
    for name in expect:
        if name not in chapters:
            raise SystemExit(f"missing chapter {name} in {chapters}")
    if "reikland.snbt" in chapters or "first_contact.snbt" in chapters:
        raise SystemExit(f"court / thin first_contact still present: {chapters}")
    for old in COURT_CHAPTERS:
        if (live / "chapters" / f"{old}.snbt").exists():
            raise SystemExit(f"court chapter still present: {old}")
    text = ""
    for name in ("crash.snbt", "paths.snbt", "first_hour.snbt", "winds.snbt", "host.snbt"):
        text += (live / "chapters" / name).read_text()
    for b in banned:
        if b in text:
            raise SystemExit(f"court phrase still in FTB: {b}")
    for needle in (
        "rallous_contact:crash/awake",
        "rallous_contact:path/help",
        "rallous_contact:path/betray",
        "rallous_contact:path/join",
        "rallous_contact:path/leave",
        "rallous_contact:race/skaven",
        "rallous_contact:magic/colleges",
        "College Letter",
        "rallous_contact:army/open",
        "Not in the Hotbar",
        "Align and Leave",
        "optional: true",
    ):
        if needle not in text:
            raise SystemExit(f"missing in FTB: {needle}")
    contact = ROOT / "content" / "datapacks" / "rallous_contact"
    for rel in (
        "data/rallous_contact/functions/load.mcfunction",
        "data/rallous_contact/functions/path/help.mcfunction",
        "data/rallous_contact/advancements/root.json",
        "data/rallous_contact/advancements/path/leave.json",
        "data/rallous_contact/advancements/race/khorne.json",
        "data/rallous_contact/advancements/magic/colleges.json",
    ):
        if not (contact / rel).exists():
            raise SystemExit(f"missing contact file {rel}")
    help_fn = (contact / "data/rallous_contact/functions/path/help.mcfunction").read_text()
    if "rallous_diplomacy:apply_path" not in help_fn or "rallous_factions:path/sync" not in help_fn:
        raise SystemExit("path/help missing diplomacy/factions cross-call")
    rec = json.loads((OV / "resourcepacks" / "Rallous Continuity" / "assets" / "recruits" / "lang" / "en_us.json").read_text())
    for key, frag in (
        ("key.recruits.team_screen_key", "Under-Empire"),
        ("chat.recruits.team_creation.noname", "Waaagh"),
        ("gui.recruits.command.text.raid", "Waaagh"),
        ("gui.recruits.diplomacy.teams_list", "Elector"),
    ):
        if frag not in rec.get(key, ""):
            raise SystemExit(f"continuity missing {key} / {frag}")
    play = (ROOT / "PLAY.md").read_text()
    if "six lords at your feet" in play and "Nobody lined six lords" not in play and "no Karl Franz" not in play.lower():
        raise SystemExit("PLAY.md still sells the court")
    if "rallous.path" not in play:
        raise SystemExit("PLAY.md missing path-score book identity")
    ids: list[str] = []
    for p in live.rglob("*.snbt"):
        for line in p.read_text().splitlines():
            line = line.strip()
            if line.startswith("id: "):
                ids.append(line.split("id: ", 1)[1].strip().strip('"'))
    if len(ids) != len(set(ids)):
        raise SystemExit("duplicate FTB ids")
    src = ROOT / "pack-src" / "overrides" / "config" / "ftbquests" / "quests" / "chapters" / "crash.snbt"
    if not src.exists():
        raise SystemExit("pack-src crash chapter missing")


def main() -> None:
    write_all_quests()
    write_contact_datapack()
    write_continuity()
    write_play()
    validate()
    print("authored first-contact FTB + rallous_contact + Continuity")
    print("chapters: Crash, Paths, First Hour, The Winds, The Host (+ Smoke kept)")
    print("court FTB chapters removed:", ", ".join(COURT_CHAPTERS))


if __name__ == "__main__":
    main()
