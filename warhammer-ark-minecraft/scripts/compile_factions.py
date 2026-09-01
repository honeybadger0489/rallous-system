#!/usr/bin/env python3
"""Compile authored faction JSON into a 1.20.1 datapack.

Vanilla cannot read content/factions/*.json at runtime. This writes
mcfunction pools, camp placement, Warp-crash contact, and path-stance
hooks into content/datapacks/rallous_factions/.

Rules (from content/factions/README.md):
  - Mix majors + minors while a race still has unplaced majors.
  - After every major of a race is placed, further picks are minor-only.
  - Lords come from each faction's lord template.
  - First-contact stance is race.warp_stranger_stance.
  - FTB path scores (help/betray/join/leave) change THAT contact faction.
"""

from __future__ import annotations

import json
import shutil
from pathlib import Path

from camp_sites import SITE_KIND, assert_camps_thick, camp_blocks, camp_soldiers

ROOT = Path(__file__).resolve().parents[1]
FACTIONS_ROOT = ROOT / "content" / "factions"
OUT = ROOT / "content" / "datapacks" / "rallous_factions"
FN = OUT / "data" / "rallous_factions" / "functions"

RACE_NUM = {
    "empire": 1,
    "vampire_counts": 2,
    "lizardmen": 3,
    "beastmen": 4,
    "greenskins": 5,
    "dwarfs": 6,
    "skaven": 7,
    "khorne": 8,
}

STANCE_NUM = {
    "help_with_blade": 1,
    "prove_yourself": 2,
    "hostile": 3,
    "daemon_suspicion": 4,
}

# Soft cap for first-days mix; explore can go higher. Never 129 at once.
FIRST_CAP = 16
EXPLORE_CAP = 40

BIOME_IDS = {
    "plains": ["minecraft:plains", "minecraft:sunflower_plains"],
    "forest": ["#minecraft:is_forest"],
    "river": ["minecraft:river", "minecraft:frozen_river"],
    "swamp": ["minecraft:swamp", "minecraft:mangrove_swamp"],
    "dark_forest": ["minecraft:dark_forest"],
    "mountains": ["#minecraft:is_mountain"],
    "peaks": [
        "minecraft:jagged_peaks",
        "minecraft:frozen_peaks",
        "minecraft:stony_peaks",
        "minecraft:snowy_slopes",
    ],
    "dripstone": ["minecraft:dripstone_caves"],
    "caves": ["minecraft:dripstone_caves", "minecraft:lush_caves", "minecraft:deep_dark"],
    "jungle": ["#minecraft:is_jungle"],
    "taiga": ["#minecraft:is_taiga"],
    "snow": [
        "minecraft:snowy_plains",
        "minecraft:snowy_taiga",
        "minecraft:snowy_beach",
        "minecraft:ice_spikes",
        "minecraft:frozen_peaks",
        "minecraft:snowy_slopes",
    ],
    "nether_waste": ["minecraft:badlands", "minecraft:eroded_badlands", "minecraft:desert"],
    "crimson": ["minecraft:wooded_badlands", "minecraft:eroded_badlands"],
    "badlands": ["#minecraft:is_badlands"],
    "desert": ["minecraft:desert"],
    "savanna": ["#minecraft:is_savanna"],
    "meadow": ["minecraft:meadow"],
    "windswept": [
        "minecraft:windswept_hills",
        "minecraft:windswept_forest",
        "minecraft:windswept_gravelly_hills",
        "minecraft:windswept_savanna",
    ],
    "deep_dark": ["minecraft:deep_dark"],
    "mangrove": ["minecraft:mangrove_swamp"],
    "cherry": ["minecraft:cherry_grove"],
    "beach": ["#minecraft:is_beach"],
    "warm_ocean": ["minecraft:warm_ocean", "minecraft:lukewarm_ocean"],
    "ocean": ["#minecraft:is_ocean"],
}

RACE_BANNER = {
    "empire": "red_banner",
    "vampire_counts": "black_banner",
    "lizardmen": "lime_banner",
    "beastmen": "brown_banner",
    "greenskins": "green_banner",
    "dwarfs": "yellow_banner",
    "skaven": "purple_banner",
    "khorne": "red_banner",
}

RACE_COLOR = {
    "empire": "red",
    "vampire_counts": "dark_red",
    "lizardmen": "aqua",
    "beastmen": "dark_green",
    "greenskins": "green",
    "dwarfs": "gold",
    "skaven": "light_purple",
    "khorne": "dark_red",
}

RACE_PROFESSION = {
    "empire": ("weaponsmith", "plains"),
    "vampire_counts": ("cleric", "swamp"),
    "lizardmen": ("nitwit", "jungle"),
    "beastmen": ("nitwit", "taiga"),
    "greenskins": ("nitwit", "savanna"),
    "dwarfs": ("weaponsmith", "taiga"),
    "skaven": ("toolsmith", "swamp"),
    "khorne": ("weaponsmith", "savanna"),
}

RACE_WEAPON = {
    "empire": ("iron_sword", "State Blade"),
    "vampire_counts": ("iron_sword", "Night Blade"),
    "lizardmen": ("stone_sword", "Temple Macuahuitl"),
    "beastmen": ("stone_axe", "Herd Axe"),
    "greenskins": ("iron_axe", "Choppa"),
    "dwarfs": ("iron_axe", "Oath Axe"),
    "skaven": ("iron_sword", "Warp-shiv"),
    "khorne": ("iron_axe", "Blood Axe"),
}


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text)


def dump_json(path: Path, data) -> None:
    w(path, json.dumps(data, indent=2, ensure_ascii=False))


def slug(fid: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in fid).strip("_").lower()


def json_snbt(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("'", "\u2019")


def snbt_name(obj) -> str:
    return "'" + json_snbt(obj) + "'"


def tellraw(selector: str, parts: list) -> str:
    return f"tellraw {selector} {json.dumps(parts, ensure_ascii=False)}"


def load_tables() -> tuple[dict[str, dict], list[dict]]:
    races: dict[str, dict] = {}
    for path in sorted((FACTIONS_ROOT / "races").glob("*.json")):
        data = json.loads(path.read_text())
        races[data["id"]] = data
    if set(races) != set(RACE_NUM):
        raise SystemExit(f"expected 8 v1 races {sorted(RACE_NUM)}, got {sorted(races)}")
    factions: list[dict] = []
    seen: set[str] = set()
    for path in sorted((FACTIONS_ROOT / "factions").rglob("*.json")):
        data = json.loads(path.read_text())
        if data["id"] in seen:
            raise SystemExit(f"duplicate faction id {data['id']}")
        seen.add(data["id"])
        if data.get("race") not in races:
            raise SystemExit(f"{data['id']} race {data.get('race')} missing")
        if not data.get("lord", {}).get("name"):
            raise SystemExit(f"{data['id']} missing lord.name")
        data["_slug"] = slug(data["id"])
        factions.append(data)
    slugs = [f["_slug"] for f in factions]
    if len(slugs) != len(set(slugs)):
        raise SystemExit("slug collision after sanitize")
    return races, factions


def biome_ok_lines(fac: dict, score: str = "$biome_ok") -> list[str]:
    lines = [f"scoreboard players set {score} rallous.gen 0"]
    seen: set[str] = set()
    for tag in fac.get("biome_tags") or []:
        for biome in BIOME_IDS.get(tag, []):
            if biome in seen:
                continue
            seen.add(biome)
            lines.append(f"execute if biome ~ ~ ~ {biome} run scoreboard players set {score} rallous.gen 1")
    if not seen:
        lines.append(f"scoreboard players set {score} rallous.gen 1")
    return lines


def raid_lines(race_id: str) -> list[str]:
    if race_id == "khorne":
        return [
            'summon minecraft:zombified_piglin ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b,HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}',
            'summon minecraft:zombified_piglin ~-2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        ]
    if race_id == "beastmen":
        return [
            'summon minecraft:husk ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
            'summon minecraft:wolf ~-2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        ]
    if race_id == "greenskins":
        return [
            'summon minecraft:pillager ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
            'summon minecraft:pillager ~-2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        ]
    if race_id == "skaven":
        return [
            'summon minecraft:cave_spider ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
            'summon minecraft:silverfish ~-1 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        ]
    if race_id == "vampire_counts":
        return [
            'summon minecraft:zombie ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
            'summon minecraft:zombie ~-2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        ]
    return [
        'summon minecraft:zombie ~2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
        'summon minecraft:husk ~-2 ~ ~ {Tags:["rallous.raid"],PersistenceRequired:1b}',
    ]


# Spoken first-contact lines. Personality JSON is a design note — never dump it.
# Host + host-name only. Eight races, four stances. No QA verbs.
GREET_SPEECH = {
    "empire": {
        1: "The Warp spat you onto {host} soil. Take a blade. Hold the line — or walk on and be meat for the next banner.",
        2: "Warp-born. You are no guest of {host}. Last this night among us. Then we will speak of names.",
        3: "This picket is closed. The Warp does not make you a soldier of Sigmar. Run, or die on the palisade.",
        4: "You stink of the Warp. Witch hunters have burned cleaner men. Speak, fight, or be put to the pyre.",
    },
    "vampire_counts": {
        1: "You fell from the Warp onto {host} graves. Take the blade. Serve, or feed the levy.",
        2: "Crash-meat. Last the night among the dead of {host}. Then we may name you guest.",
        3: "This host does not treat crash-meat as a guest. Flee {host}, or join the grave-levy.",
        4: "The Warp clings to you. Prove you are flesh, not daemon, or the graves of {host} take you.",
    },
    "lizardmen": {
        1: "The Plan did not name you. Take the weapon. Stand the temple of {host}, or be judged.",
        2: "You smell of the Great Enemy. Last this night at {host}. The plaque will judge.",
        3: "Daemon-stink. The temple of {host} is shut. Survive, or be judged.",
        4: "The Old Ones smell the Great Enemy on you. An omen must clear you — or {host} will.",
    },
    "beastmen": {
        1: "Warp-meat. Take the axe. Gore with the herd of {host}, or be eaten.",
        2: "Not cattle yet. Last the horns of {host}. Then the herd may keep you.",
        3: "Prey. The herd of {host} does not share this camp. Run, or be eaten.",
        4: "Warp-stink. The herd of {host} has not decided if you are rival or meat.",
    },
    "greenskins": {
        1: "You fell outta the sky onto {host}. Take a choppa. Fight wiv us, or get krumped.",
        2: "Prove yer a proper scrap. Last the night wiv {host}. Then da boss might keep ya.",
        3: "Dis is our scrap. Live through it or nick da banner of {host} and die.",
        4: "You smell wrong. Fight till {host} says you ain't a daemon, or get krumped.",
    },
    "dwarfs": {
        1: "The Warp spat you at the gate of {host}. Take the axe. Hold the picket, or be a grudge.",
        2: "You stink of the Warp. Last this night in {host}. Then we mark the grudge paid — or not.",
        3: "This hold is shut. Survive the raid on {host}, or take the banner and be a thief.",
        4: "You stink of the Warp. Kill until {host} names you clean, or be entered in the Book.",
    },
    "skaven": {
        1: "Yes-yes, Warp-thing. Take-take the shiv. Fight for {host}, or be meat.",
        2: "Prove-prove you are not a spy. Last the night under {host}. Then the Council hears.",
        3: "Intruder-meat. Live the raid or steal-take the picket of {host}.",
        4: "Warp-stink, yes-yes. Prove you are not a daemon-spy of {host}, or die-die.",
    },
    "khorne": {
        1: "Blood fell from the sky onto {host}. Take the axe. Spill with the pack, or be the offering.",
        2: "Skulls or cowardice. Last this fight for {host}. Khorne cares not from whom.",
        3: "You are the offering. Survive {host}, or die on this picket.",
        4: "The Warp spat you here. Bleed until {host} names you, or be the skull.",
    },
}


def stance_text(race: dict, fac: dict) -> dict[int, list]:
    lord = fac["lord"]
    who = f"{lord.get('title', 'Lord')} {lord['name']} — {fac['name']}"
    color = RACE_COLOR[race["id"]]
    host = fac.get("name") or race.get("name") or "this camp"
    table = GREET_SPEECH[race["id"]]
    prefix = {"text": f"<{who}> ", "color": color, "bold": True}
    colors = {1: "white", 2: "yellow", 3: "red", 4: "dark_purple"}
    return {
        n: [prefix, {"text": table[n].format(host=host), "color": colors[n]}]
        for n in (1, 2, 3, 4)
    }


def write_meta() -> None:
    dump_json(
        OUT / "pack.mcmeta",
        {
            "pack": {
                "pack_format": 15,
                "description": "Compiled TWW faction camps — majors/minors, lords, stances",
            }
        },
    )
    w(
        OUT / "META-INF" / "mods.toml",
        """modLoader="lowcodefml"
loaderVersion="[47,)"
license="All Rights Reserved"

[[mods]]
modId="rallous_factions"
version="1.0.0"
displayName="Rallous Factions"
authors="Rallous System"
description='''Compiled from content/factions JSON. Living camps, not a silent village.'''
""",
    )
    dump_json(OUT / "data" / "minecraft" / "tags" / "functions" / "load.json", {"values": ["rallous_factions:load"]})
    dump_json(OUT / "data" / "minecraft" / "tags" / "functions" / "tick.json", {"values": ["rallous_factions:tick"]})
    w(
        OUT / "README.md",
        """# rallous_factions (compiled)

Do not edit these mcfunctions by hand. Source is `content/factions/`.
Rebuild: `python3 scripts/compile_factions.py`

Each camp is a war-host picket by site kind (settled / hold / temple /
herd / waaagh / under-empire / khorne): palisade posts, extra banners
and campfires, site props (skulls, cobwebs, anvil, …), the named lord
from the faction template, and two Recruits soldiers. A marker holds
`rallous.fac.id` / race / stance / tier. First-days mix majors and
minors (cap 16). After every major of a race is placed, that race rolls
minor-only. Walking farther places more from the remaining pool (cap 40).
Never all 129 at once. Warp-crash assigns the nearest camp as
`rallous.contact` and fires the race stance. FTB help/betray/join/leave
changes that contact faction.
""",
    )


def write_load(races: dict[str, dict], factions: list[dict]) -> None:
    lines = [
        "# Compiled faction scoreboards. Do not wipe placed camps on /reload.",
        "scoreboard objectives add rallous.gen dummy",
        "scoreboard objectives add rallous.rng dummy",
        "scoreboard objectives add rallous.used dummy",
        "scoreboard objectives add rallous.fac.id dummy",
        "scoreboard objectives add rallous.fac.race dummy",
        "scoreboard objectives add rallous.fac.stance dummy",
        "scoreboard objectives add rallous.fac.tier dummy",
        "scoreboard objectives add rallous.contact dummy",
        "scoreboard objectives add rallous.contact_id dummy",
        "scoreboard objectives add rallous.path dummy",
        "scoreboard objectives add rallous.path_seen dummy",
        "scoreboard objectives add rallous.help dummy",
        "scoreboard objectives add rallous.betray dummy",
        "scoreboard objectives add rallous.join dummy",
        "scoreboard objectives add rallous.leave dummy",
        "scoreboard objectives add rallous.proved dummy",
        "scoreboard objectives add rallous.race dummy",
        "scoreboard objectives add rallous.const dummy",
        "scoreboard players set #-1 rallous.const -1",
        "scoreboard players set #2 rallous.const 2",
        f"scoreboard players set #cap rallous.const {FIRST_CAP}",
        f"scoreboard players set #xcap rallous.const {EXPLORE_CAP}",
        "execute unless score #placed rallous.gen = #placed rallous.gen run scoreboard players set #placed rallous.gen 0",
        "execute unless score #booted rallous.gen = #booted rallous.gen run scoreboard players set #booted rallous.gen 0",
        "execute unless score #clock rallous.gen = #clock rallous.gen run scoreboard players set #clock rallous.gen 0",
        "execute unless score #next_race rallous.gen = #next_race rallous.gen run scoreboard players set #next_race rallous.gen 0",
    ]
    for race_id, race in races.items():
        n_maj = sum(1 for f in factions if f["race"] == race_id and f.get("tier") == "major")
        n_min = sum(1 for f in factions if f["race"] == race_id and f.get("tier") != "major")
        lines.append(f"scoreboard players set #n_maj_{race_id} rallous.const {n_maj}")
        lines.append(f"scoreboard players set #n_min_{race_id} rallous.const {n_min}")
        lines.append(
            f"execute unless score #left_maj_{race_id} rallous.gen = #left_maj_{race_id} rallous.gen run scoreboard players set #left_maj_{race_id} rallous.gen {n_maj}"
        )
        lines.append(
            f"execute unless score #left_min_{race_id} rallous.gen = #left_min_{race_id} rallous.gen run scoreboard players set #left_min_{race_id} rallous.gen {n_min}"
        )
    w(FN / "load.mcfunction", "\n".join(lines) + "\n")


def write_runtime() -> None:
    w(
        FN / "tick.mcfunction",
        """# First-days mix, then explore placements, then path stance sync.
scoreboard players add #clock rallous.gen 1
execute if score #booted rallous.gen matches 1 if score #placed rallous.gen < #cap rallous.const if score #clock rallous.gen matches 40 run function rallous_factions:gen/tick_place
execute if score #clock rallous.gen matches 40 run scoreboard players set #clock rallous.gen 0
execute if score #placed rallous.gen >= #cap rallous.const if score #placed rallous.gen < #xcap rallous.const as @a[tag=rallous.warp_landed] at @s unless entity @e[tag=rallous.camp,distance=..180,limit=1] run function rallous_factions:gen/explore
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_diplomacy:apply_path
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_factions:path/sync
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s if entity @e[tag=rallous.camp,distance=..14,limit=1] run function rallous_factions:contact/assign
""",
    )
    w(
        FN / "abs_rng.mcfunction",
        """execute if score $rng rallous.rng matches ..-1 run scoreboard players operation $rng rallous.rng *= #-1 rallous.const
""",
    )
    w(
        FN / "gen/boot.mcfunction",
        """# Start the first-days mix once. Contact camp is placed separately.
execute if score #booted rallous.gen matches 1 run scoreboard players set $noop rallous.gen 1
execute unless score #booted rallous.gen matches 1 run scoreboard players set #booted rallous.gen 1
""",
    )
    w(
        FN / "gen/tick_place.mcfunction",
        """# One more camp around the first crater / a landed player.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const as @a[tag=rallous.warp_landed,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_far
""",
    )
    w(
        FN / "gen/explore.mcfunction",
        """# Player walked off the first ring. Place from the remaining pool.
execute if score #placed rallous.gen >= #xcap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #xcap rallous.const run function rallous_factions:gen/place_far
""",
    )
    w(
        FN / "gen/place_near.mcfunction",
        """# Guaranteed contact camp just off the crater.
summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.near"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 64 140 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_one
kill @e[type=minecraft:marker,tag=rallous.probe]
""",
    )
    w(
        FN / "gen/place_far.mcfunction",
        """summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.far"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 140 380 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_one
kill @e[type=minecraft:marker,tag=rallous.probe]
""",
    )
    prefer = [
        "scoreboard players set $pref rallous.gen -1",
        "execute if biome ~ ~ ~ #minecraft:is_jungle run scoreboard players set $pref rallous.gen 3",
        "execute if biome ~ ~ ~ minecraft:mangrove_swamp run scoreboard players set $pref rallous.gen 3",
        "execute if biome ~ ~ ~ minecraft:dark_forest run scoreboard players set $pref rallous.gen 4",
        "execute if biome ~ ~ ~ #minecraft:is_forest run scoreboard players set $pref rallous.gen 4",
        "execute if biome ~ ~ ~ #minecraft:is_mountain run scoreboard players set $pref rallous.gen 6",
        "execute if biome ~ ~ ~ minecraft:swamp run scoreboard players set $pref rallous.gen 2",
        "execute if biome ~ ~ ~ #minecraft:is_badlands run scoreboard players set $pref rallous.gen 5",
        "execute if biome ~ ~ ~ #minecraft:is_savanna run scoreboard players set $pref rallous.gen 5",
        "execute if biome ~ ~ ~ minecraft:plains run scoreboard players set $pref rallous.gen 1",
        "execute if biome ~ ~ ~ minecraft:sunflower_plains run scoreboard players set $pref rallous.gen 1",
        "execute if biome ~ ~ ~ minecraft:meadow run scoreboard players set $pref rallous.gen 1",
        "execute if biome ~ ~ ~ minecraft:dripstone_caves run scoreboard players set $pref rallous.gen 7",
        "execute if biome ~ ~ ~ minecraft:lush_caves run scoreboard players set $pref rallous.gen 7",
        "execute if biome ~ ~ ~ minecraft:desert run scoreboard players set $pref rallous.gen 8",
        "execute if biome ~ ~ ~ minecraft:snowy_plains run scoreboard players set $pref rallous.gen 8",
    ]
    pick_pref = [
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 1 run function rallous_factions:pool/empire/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 2 run function rallous_factions:pool/vampire_counts/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 3 run function rallous_factions:pool/lizardmen/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 4 run function rallous_factions:pool/beastmen/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 5 run function rallous_factions:pool/greenskins/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 6 run function rallous_factions:pool/dwarfs/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 7 run function rallous_factions:pool/skaven/pick",
        "execute if score $done rallous.gen matches 0 if score $pref rallous.gen matches 8 run function rallous_factions:pool/khorne/pick",
    ]
    rotate = [
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 0 run function rallous_factions:pool/empire/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 1 run function rallous_factions:pool/vampire_counts/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 2 run function rallous_factions:pool/lizardmen/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 3 run function rallous_factions:pool/beastmen/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 4 run function rallous_factions:pool/greenskins/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 5 run function rallous_factions:pool/dwarfs/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 6 run function rallous_factions:pool/skaven/pick",
        "execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 7 run function rallous_factions:pool/khorne/pick",
        "scoreboard players add #next_race rallous.gen 1",
        "execute if score #next_race rallous.gen matches 8.. run scoreboard players set #next_race rallous.gen 0",
    ]
    fallback = [
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/empire/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/dwarfs/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/lizardmen/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/vampire_counts/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/greenskins/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/skaven/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/beastmen/pick",
        "execute if score $done rallous.gen matches 0 run function rallous_factions:pool/khorne/pick",
    ]
    w(
        FN / "gen/place_one.mcfunction",
        "\n".join(
            [
                "scoreboard players set $done rallous.gen 0",
                "execute if entity @e[tag=rallous.camp,distance=..48,limit=1] run scoreboard players set $done rallous.gen 1",
                *prefer,
                *pick_pref,
                *rotate,
                *fallback,
            ]
        )
        + "\n",
    )
    w(
        FN / "crash/on_land.mcfunction",
        """# Warp-crash: living camp from the tables, not a mute villager.
function rallous_factions:gen/boot
execute unless entity @e[tag=rallous.camp,distance=..220,limit=1] run function rallous_factions:gen/place_near
execute unless entity @e[tag=rallous.camp,distance=..260,limit=1] run function rallous_factions:gen/place_one
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
function rallous_factions:contact/assign
""",
    )
    w(
        FN / "contact/assign.mcfunction",
        """# Once per survivor. A second land/tick path cannot greet or kit again.
execute unless entity @s[tag=rallous.contacted] run function rallous_factions:contact/assign_go
""",
    )
    w(
        FN / "contact/assign_go.mcfunction",
        """# Nearest compiled camp becomes this survivor's contact faction.
tag @s add rallous.contacted
tag @s add rallous.fac.greeted
scoreboard players set @s rallous.joined 1
execute unless entity @e[tag=rallous.camp,distance=..400,limit=1] run function rallous_factions:gen/place_near
tag @e[tag=rallous_contact] remove rallous_contact
execute as @e[tag=rallous.camp,limit=1,sort=nearest] run tag @s add rallous_contact
execute as @e[tag=rallous.lord,limit=1,sort=nearest] run tag @s add rallous_contact
scoreboard players operation @s rallous.contact_id = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.id
scoreboard players operation @s rallous.race = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.race
scoreboard players set @s rallous.contact 1
function rallous_factions:contact/greet
function rallous_recruits_bind:on_contact
function rallous_kit:on_greet
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
""",
    )
    w(
        FN / "contact/greet.mcfunction",
        """# Dispatch to the compiled lord voice + stance action.
execute as @e[tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:contact/dispatch
""",
    )
    w(
        FN / "path/sync.mcfunction",
        """scoreboard players operation @s rallous.path_seen = @s rallous.path
execute if score @s rallous.path matches 1 run function rallous_factions:path/help
execute if score @s rallous.path matches 2 run function rallous_factions:path/betray
execute if score @s rallous.path matches 3 run function rallous_factions:path/join
execute if score @s rallous.path matches 4 run function rallous_factions:path/leave
""",
    )
    w(
        FN / "path/help.mcfunction",
        """tag @s add rallous.path_actor
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.path_actor,limit=1] rallous.contact_id run function rallous_factions:path/help_camp
execute unless entity @e[tag=rallous.camp,limit=1] run tellraw @s {"text":"Path noted: help. Meet a named lord and that faction will remember.","color":"gray"}
tag @s remove rallous.path_actor
""",
    )
    w(
        FN / "path/betray.mcfunction",
        """tag @s add rallous.path_actor
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.path_actor,limit=1] rallous.contact_id run function rallous_factions:path/betray_camp
execute unless entity @e[tag=rallous.camp,limit=1] run tellraw @s {"text":"Path noted: betray. The next camp you named will turn.","color":"gray"}
tag @s remove rallous.path_actor
""",
    )
    w(
        FN / "path/join.mcfunction",
        """tag @s add rallous.path_actor
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.path_actor,limit=1] rallous.contact_id run function rallous_factions:path/join_camp
execute unless entity @e[tag=rallous.camp,limit=1] run tellraw @s {"text":"Path noted: join. A contact lord will take the banner.","color":"gray"}
tag @s remove rallous.path_actor
""",
    )
    w(
        FN / "path/leave.mcfunction",
        """tag @s add rallous.path_actor
execute as @e[tag=rallous.camp] if score @s rallous.fac.id = @a[tag=rallous.path_actor,limit=1] rallous.contact_id run function rallous_factions:path/leave_camp
execute unless entity @e[tag=rallous.camp,limit=1] run tellraw @s {"text":"Path noted: align-and-leave. Standing cools to prove-yourself.","color":"gray"}
tag @s remove rallous.path_actor
""",
    )
    w(
        FN / "path/help_camp.mcfunction",
        """# One step friendlier. Prove first so hostile does not skip to help in one tick.
execute if score @s rallous.fac.stance matches 2 run scoreboard players set @s rallous.fac.stance 1
execute if score @s rallous.fac.stance matches 3 run scoreboard players set @s rallous.fac.stance 2
execute if score @s rallous.fac.stance matches 4 run scoreboard players set @s rallous.fac.stance 2
execute if score @s rallous.fac.stance matches 6 run scoreboard players set @s rallous.fac.stance 3
tellraw @a[distance=..48] {"text":"This faction watched you help. Their stance toward you shifted.","color":"green"}
execute if score @s rallous.fac.stance matches 1 as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
execute if score @s rallous.fac.stance matches 5 as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
""",
    )
    w(
        FN / "path/betray_camp.mcfunction",
        """scoreboard players set @s rallous.fac.stance 6
tellraw @a[distance=..48] {"text":"This faction names you oath-breaker. Their stance is war.","color":"red"}
execute at @s run function rallous_factions:contact/raid_generic
execute as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:war
""",
    )
    w(
        FN / "path/join_camp.mcfunction",
        """scoreboard players set @s rallous.fac.stance 5
tellraw @a[distance=..48] {"text":"This faction takes your colour. You are of the host now.","color":"gold"}
give @p minecraft:white_banner{display:{Name:'{"text":"Taken Colour","italic":false}'}} 1
execute as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_recruits_bind:ally
""",
    )
    w(
        FN / "path/leave_camp.mcfunction",
        """execute unless score @s rallous.fac.stance matches 3 unless score @s rallous.fac.stance matches 6 run scoreboard players set @s rallous.fac.stance 2
tellraw @a[distance=..48] {"text":"You named a side and rode on. This faction cools to prove-yourself.","color":"gray"}
""",
    )
    w(
        FN / "contact/raid_generic.mcfunction",
        "\n".join(raid_lines("empire")) + "\n",
    )
    w(
        FN / "debug/force_contact.mcfunction",
        """# Smoke: plant a real table faction at your feet and fire its stance.
function rallous_factions:gen/place_one
function rallous_factions:contact/assign
tellraw @s {"text":"Forced a compiled faction camp here. Look for a named lord and a stance line.","color":"gold"}
""",
    )


def write_pools(races: dict[str, dict], factions: list[dict]) -> None:
    by_race: dict[str, list[dict]] = {rid: [] for rid in races}
    for fac in factions:
        by_race[fac["race"]].append(fac)
    for race_id, group in by_race.items():
        majors = [f for f in group if f.get("tier") == "major"]
        minors = [f for f in group if f.get("tier") != "major"]
        w(
            FN / "pool" / race_id / "pick.mcfunction",
            "\n".join(
                [
                    "# Mix majors+minors until every major of this race is placed.",
                    "scoreboard players set $need_biome rallous.gen 1",
                    "execute store result score $rng rallous.rng run data get entity @s UUID[0]",
                    "function rallous_factions:abs_rng",
                    "scoreboard players operation $mix rallous.rng = $rng rallous.rng",
                    "scoreboard players operation $mix rallous.rng %= #2 rallous.const",
                    f"execute if score #left_maj_{race_id} rallous.gen matches 1.. if score $mix rallous.rng matches 0 run function rallous_factions:pool/{race_id}/pick_major",
                    f"execute if score #left_maj_{race_id} rallous.gen matches 1.. if score $mix rallous.rng matches 1 run function rallous_factions:pool/{race_id}/pick_minor",
                    f"execute if score #left_maj_{race_id} rallous.gen matches 0 run function rallous_factions:pool/{race_id}/pick_minor",
                    "scoreboard players set $need_biome rallous.gen 0",
                    f"execute if score $done rallous.gen matches 0 if score #left_maj_{race_id} rallous.gen matches 1.. run function rallous_factions:pool/{race_id}/pick_major",
                    f"execute if score $done rallous.gen matches 0 run function rallous_factions:pool/{race_id}/pick_minor",
                    f"execute if score $done rallous.gen matches 0 if score #left_maj_{race_id} rallous.gen matches 1.. run function rallous_factions:pool/{race_id}/pick_major",
                ]
            )
            + "\n",
        )
        write_tier_pick(race_id, "major", majors)
        write_tier_pick(race_id, "minor", minors)


def write_tier_pick(race_id: str, tier: str, group: list[dict]) -> None:
    n = max(len(group), 1)
    lines = [
        f"# {race_id} {tier} pool ({len(group)})",
        "execute store result score $rng rallous.rng run data get entity @s UUID[1]",
        "function rallous_factions:abs_rng",
        f"scoreboard players set #n rallous.const {n}",
        "scoreboard players operation $rng rallous.rng %= #n rallous.const",
    ]
    for i, fac in enumerate(group):
        sl = fac["_slug"]
        lines.append(
            f"execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches ..{i} unless score #{sl} rallous.used matches 1 run function rallous_factions:try/{sl}"
        )
    for i, fac in enumerate(group):
        sl = fac["_slug"]
        if i == 0:
            continue
        lines.append(
            f"execute if score $done rallous.gen matches 0 if score $rng rallous.rng matches {i}.. unless score #{sl} rallous.used matches 1 run function rallous_factions:try/{sl}"
        )
    if group:
        sl0 = group[0]["_slug"]
        lines.append(
            f"execute if score $done rallous.gen matches 0 unless score #{sl0} rallous.used matches 1 run function rallous_factions:try/{sl0}"
        )
    w(FN / "pool" / race_id / f"pick_{tier}.mcfunction", "\n".join(lines) + "\n")


def write_faction_fns(races: dict[str, dict], factions: list[dict]) -> None:
    dispatch = ["# Route greet to the compiled lord function."]
    for i, fac in enumerate(factions, start=1):
        race = races[fac["race"]]
        sl = fac["_slug"]
        stance = STANCE_NUM[race["warp_stranger_stance"]]
        tier = 1 if fac.get("tier") == "major" else 2
        banner = RACE_BANNER[race["id"]]
        color = RACE_COLOR[race["id"]]
        prof, vtype = RACE_PROFESSION[race["id"]]
        weapon_id, weapon_name = RACE_WEAPON[race["id"]]
        lord = fac["lord"]
        lord_name = f"{lord.get('title', 'Lord')} {lord['name']}"
        name_comp = {"text": lord_name, "color": color, "bold": True}
        name_snbt = snbt_name(name_comp)
        try_lines = [
            f"# try {fac['id']} ({fac.get('tier')})",
            *biome_ok_lines(fac),
            "execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 0 run scoreboard players set $skip rallous.gen 1",
            "execute unless score $need_biome rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0",
            "execute if score $need_biome rallous.gen matches 1 if score $biome_ok rallous.gen matches 1 run scoreboard players set $skip rallous.gen 0",
            f"execute if score $skip rallous.gen matches 0 unless score #{sl} rallous.used matches 1 run function rallous_factions:place/{sl}",
        ]
        w(FN / "try" / f"{sl}.mcfunction", "\n".join(try_lines) + "\n")

        place = [
            f"# place {fac['name']} — {lord_name} ({SITE_KIND.get(race['id'], 'settled')} war host)",
            f"execute if score #{sl} rallous.used matches 1 run scoreboard players set $skip rallous.gen 1",
            f"execute unless score #{sl} rallous.used matches 1 run scoreboard players set $skip rallous.gen 0",
            * [f"execute if score $skip rallous.gen matches 0 run {line}" for line in camp_blocks(race["id"], fac.get("site", "settled"), race.get("settlement", "settled"), banner)],
            (
                "execute if score $skip rallous.gen matches 0 run summon minecraft:marker ~ ~ ~ "
                f'{{Tags:["rallous.camp","rallous.fac.{sl}"],'
                f"CustomName:{name_snbt}}}"
            ),
            (
                "execute if score $skip rallous.gen matches 0 run summon minecraft:villager ~0.6 ~ ~ "
                f'{{CustomName:{name_snbt},CustomNameVisible:1b,PersistenceRequired:1b,Invulnerable:1b,NoAI:1b,'
                f'Tags:["rallous.lord","rallous.fac.{sl}"],'
                f'VillagerData:{{profession:"minecraft:{prof}",level:3,type:"minecraft:{vtype}"}},'
                f"HandItems:[{{id:\"minecraft:{weapon_id}\",Count:1b}},{{}}]}}"
            ),
            * [f"execute if score $skip rallous.gen matches 0 run {line}" for line in camp_soldiers(race["id"], sl, color)],
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id {i}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race {RACE_NUM[race['id']]}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance {stance}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier {tier}",
            f"execute if score $skip rallous.gen matches 0 run scoreboard players set #{sl} rallous.used 1",
            (
                f"execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_maj_{race['id']} rallous.gen 1"
                if tier == 1
                else f"execute if score $skip rallous.gen matches 0 run scoreboard players remove #left_min_{race['id']} rallous.gen 1"
            ),
            "execute if score $skip rallous.gen matches 0 run scoreboard players add #placed rallous.gen 1",
            "execute if score $skip rallous.gen matches 0 run scoreboard players set $done rallous.gen 1",
        ]
        w(FN / "place" / f"{sl}.mcfunction", "\n".join(place) + "\n")

        texts = stance_text(race, fac)
        dispatch.append(f"execute if score @s rallous.fac.id matches {i} run function rallous_factions:greet/{sl}")
        w(FN / "greet" / f"{sl}.mcfunction", write_greet_body(race, fac, texts, weapon_id, weapon_name))

    w(FN / "contact/dispatch.mcfunction", "\n".join(dispatch) + "\n")


def write_greet_body(race: dict, fac: dict, texts: dict[int, list], weapon_id: str, weapon_name: str) -> str:
    wname = snbt_name({"text": weapon_name, "italic": False})
    lines = [
        tellraw("@a[distance=..48]", texts[STANCE_NUM[race["warp_stranger_stance"]]]),
        f"execute if score @s rallous.fac.stance matches 1 run give @p minecraft:{weapon_id}{{display:{{Name:{wname}}}}} 1",
        "execute if score @s rallous.fac.stance matches 1 run tellraw @a[distance=..48] {\"text\":\"A blade is thrown at your feet. Take it.\",\"color\":\"gold\"}",
        "execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0",
        "execute if score @s rallous.fac.stance matches 2 run tellraw @a[distance=..48] {\"text\":\"Last this night among them. Then they will speak of a path.\",\"color\":\"yellow\"}",
        "execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0",
        "execute if score @s rallous.fac.stance matches 4 run tellraw @a[distance=..48] {\"text\":\"They smell the Warp on you. Steel or the pyre — they have not decided.\",\"color\":\"dark_purple\"}",
        "execute if score @s rallous.fac.stance matches 3 run function rallous_factions:raid/" + fac["_slug"],
        "execute if score @s rallous.fac.stance matches 6 run function rallous_factions:raid/" + fac["_slug"],
        "particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16",
    ]
    w(FN / "raid" / f"{fac['_slug']}.mcfunction", "\n".join(raid_lines(race["id"])) + "\n")
    return "\n".join(lines) + "\n"


def write_index(races: dict[str, dict], factions: list[dict]) -> None:
    majors = [f for f in factions if f.get("tier") == "major"]
    minors = [f for f in factions if f.get("tier") != "major"]
    index = {
        "races": {
            rid: {
                "name": race["name"],
                "settlement": race.get("settlement"),
                "warp_stranger_stance": race["warp_stranger_stance"],
                "majors": sum(1 for f in factions if f["race"] == rid and f.get("tier") == "major"),
                "minors": sum(1 for f in factions if f["race"] == rid and f.get("tier") != "major"),
            }
            for rid, race in races.items()
        },
        "totals": {"factions": len(factions), "majors": len(majors), "minors": len(minors)},
        "caps": {"first_days": FIRST_CAP, "explore": EXPLORE_CAP},
        "examples": [
            {
                "id": f["id"],
                "race": f["race"],
                "tier": f.get("tier"),
                "lord": f["lord"]["name"],
                "site": f.get("site"),
            }
            for f in factions
            if f["id"]
            in (
                "reikland",
                "karaz-a-karak",
                "itza",
                "vampire-counts",
                "shadowgor-warherd",
                "skull-takerz",
                "clan-mors",
                "exiles-of-khorne",
            )
        ],
    }
    dump_json(OUT / "compiled_index.json", index)


def compile_factions() -> dict:
    if not FACTIONS_ROOT.is_dir():
        raise SystemExit(f"missing {FACTIONS_ROOT}")
    races, factions = load_tables()
    majors = sum(1 for f in factions if f.get("tier") == "major")
    minors = len(factions) - majors
    if majors != 42 or minors != 87:
        raise SystemExit(f"expected 42 major / 87 minor, got {majors}/{minors}")
    assert_camps_thick(RACE_NUM)
    if OUT.exists():
        shutil.rmtree(OUT)
    write_meta()
    write_load(races, factions)
    write_runtime()
    write_pools(races, factions)
    write_faction_fns(races, factions)
    write_index(races, factions)
    n = sum(1 for p in FN.rglob("*.mcfunction"))
    print(f"compiled {len(factions)} factions ({majors} major / {minors} minor) → {n} mcfunctions in {OUT}")
    return {"factions": len(factions), "majors": majors, "minors": minors, "functions": n}


if __name__ == "__main__":
    compile_factions()
