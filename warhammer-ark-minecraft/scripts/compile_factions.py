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

from camp_sites import (
    SITE_KIND,
    assert_camps_thick,
    camp_blocks,
    camp_soldiers,
    lord_armor_nbt,
    lord_sote_replace,
)

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
    """Always-hostile vanilla. Neutral wolves / calm piglins are not a bite."""
    if race_id == "khorne":
        return [
            'summon minecraft:vindicator ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,Johnny:0b,CanJoinRaid:0b,HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}',
            'summon minecraft:zombified_piglin ~-2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,AngerTime:2000,HandItems:[{id:"minecraft:golden_axe",Count:1b},{}]}',
        ]
    if race_id == "beastmen":
        return [
            'summon minecraft:husk ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
            'summon minecraft:vindicator ~-2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,Johnny:0b,CanJoinRaid:0b,HandItems:[{id:"minecraft:stone_axe",Count:1b},{}]}',
        ]
    if race_id == "greenskins":
        return [
            'summon minecraft:pillager ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,CanJoinRaid:0b}',
            'summon minecraft:vindicator ~-2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,Johnny:0b,CanJoinRaid:0b,HandItems:[{id:"minecraft:iron_axe",Count:1b},{}]}',
        ]
    if race_id == "skaven":
        return [
            'summon minecraft:cave_spider ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
            'summon minecraft:silverfish ~-1 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
            'summon minecraft:pillager ~1 ~ ~1 {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,CanJoinRaid:0b}',
        ]
    if race_id == "vampire_counts":
        return [
            'summon minecraft:zombie ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
            'summon minecraft:husk ~-2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
        ]
    return [
        'summon minecraft:pillager ~2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b,CanJoinRaid:0b}',
        'summon minecraft:husk ~-2 ~ ~ {Tags:["rallous.raid","rallous.bite"],PersistenceRequired:1b}',
    ]


# Spoken first-contact lines. Personality JSON is a design note — never dump it.
# Host + host-name only. Eight races, four stances. Starting reaction is NOT identical.
GREET_SPEECH = {
    "empire": {
        1: "The Warp spat you onto {host} soil. Take a blade. Fight with us — hold this road, or be meat for the next banner.",
        2: "Warp-born. You are no guest of {host}. Last this night among the State Troops. Then we will speak of names.",
        3: "This picket is closed. The Warp does not make you a soldier of Sigmar. Run, or die on the palisade.",
        4: "You stink of the Warp. Witch hunters have burned cleaner men. Speak, fight, or be put to the pyre.",
    },
    "vampire_counts": {
        1: "You fell from the Warp onto {host} graves. Take the night-blade. Serve the dead, or feed the levy.",
        2: "Crash-meat. Last the night among the dead of {host}. Then we may name you guest.",
        3: "This host does not treat crash-meat as a guest. Flee {host}, or join the grave-levy.",
        4: "Daemon-stink on living breath. The graves of {host} do not trust Warp-born. Name a path, or hang with the suspected.",
    },
    "lizardmen": {
        1: "The Plan did not name you. Take the weapon. Stand the temple of {host}, or be judged.",
        2: "You smell of the Great Enemy. Last this night at {host}. The plaque will judge.",
        3: "Daemon-stink. The temple of {host} is shut. Survive, or be judged.",
        4: "The Old Ones smell the Great Enemy on you. {host} is wary. An omen must clear the Warp — or the temple will.",
    },
    "beastmen": {
        1: "Warp-meat. Take the axe. Gore with the herd of {host}, or be eaten.",
        2: "Not cattle yet. Last the horns of {host}. Then the herd may keep you.",
        3: "Prey. The herd of {host} does not share this camp. Run, or be eaten.",
        4: "Warp-stink. The herd of {host} has not decided if you are rival or meat.",
    },
    "greenskins": {
        1: "You fell outta the sky onto {host}. Take a choppa. Fight wiv us — da scrap starts now, or get krumped.",
        2: "Prove yer a proper scrap. Last the night wiv {host}. Then da boss might keep ya.",
        3: "Dis is our scrap. Live through it or nick da banner of {host} and die.",
        4: "You smell wrong. Fight till {host} says you ain't a daemon, or get krumped.",
    },
    "dwarfs": {
        1: "The Warp spat you at the gate of {host}. Take the axe. Hold the picket, or be a grudge.",
        2: "You stink of the Warp. Last this night in {host}. Then we mark the grudge paid — or not.",
        3: "This hold is shut. Survive the raid on {host}, or take the banner and be a thief.",
        4: "No oath is sworn. {host} is wary. You stink of the Warp. Kill until the Book names you clean — or entered.",
    },
    "skaven": {
        1: "Yes-yes, Warp-thing. Take-take the shiv. Fight for {host}, or be meat.",
        2: "Prove-prove you are not a spy. Last the night under {host}. Then the Council hears.",
        3: "Man-thing reeks of Warp. Intruder-meat. {host} does not greet. Live the knives, or die-die.",
        4: "Warp-stink, yes-yes. Prove you are not a daemon-spy of {host}, or die-die.",
    },
    "khorne": {
        1: "Blood fell from the sky onto {host}. Take the axe. Spill with the pack, or be the offering.",
        2: "Skulls or cowardice. Last this fight for {host}. Khorne cares not from whom.",
        3: "You are the offering. The Blood Host of {host} does not treat Warp-spawn as guests. Survive, or die on this picket.",
        4: "The Warp spat you here. Bleed until {host} names you, or be the skull.",
    },
}

# Extra stance beat after the lord line. Must differ by race — not one shared pyre sentence.
STANCE_ACTION = {
    "empire": {
        1: "A State Blade is thrown at your feet. Fight with this host.",
        2: "Last this night among the State Troops. Then they will speak of a path.",
        3: "The palisade closes. This is a fight, not a greeting.",
        4: "Witch-hunters have not decided. Steel or the pyre.",
    },
    "vampire_counts": {
        1: "A night-blade is laid on a grave. Serve, or be levied.",
        2: "Last the night among the dead. Guest-right is not given yet.",
        3: "The grave-levy comes for crash-meat.",
        4: "They name you daemon-suspect. The graves watch. Paths still open — at a cost.",
    },
    "lizardmen": {
        1: "A temple weapon is offered. Stand the plaque, or be judged.",
        2: "Last this night at the temple. The plaque has not named you.",
        3: "The temple is shut. Survive the judgement.",
        4: "The temple is wary. Warp-stink is the Great Enemy until an omen — or a verb — clears you.",
    },
    "beastmen": {
        1: "A herd-axe in the dirt. Gore with them, or be cattle.",
        2: "Last the horns. The herd has not kept you yet.",
        3: "Prey. The herd is already moving to eat.",
        4: "Warp-stink. Rival or meat — they have not picked.",
    },
    "greenskins": {
        1: "A choppa lands at your boots. Fight wiv da boyz. Dis is a scrap, not a speech.",
        2: "Last da night. If you still stand, da boss might keep ya.",
        3: "Dis scrap is already on. Live it or nick da banner and die.",
        4: "You smell wrong. Fight till they say you ain't a daemon.",
    },
    "dwarfs": {
        1: "An oath-axe is offered. Hold the gate, or be a grudge.",
        2: "Last this night in the hold. Then the Book is marked.",
        3: "The hold is shut. Survive the raid, or be a thief.",
        4: "The hold is wary. Warp-stink is a grudge until you kill it clean.",
    },
    "skaven": {
        1: "A warp-shiv, yes-yes. Fight-fight, or be meat.",
        2: "Prove-prove you are not a spy. Last the night under the Clan.",
        3: "Knives in the dark. The Clan does not greet man-things.",
        4: "Daemon-spy, they hiss. Paths exist. Trust does not.",
    },
    "khorne": {
        1: "A blood-axe. Spill with the pack, or be the offering.",
        2: "Skulls or cowardice. Last this fight.",
        3: "You are the offering. The Blood Host is already on you.",
        4: "Bleed until they name you, or be the skull.",
    },
}

# Four paths stay clickable. Lead-in is race-skeptical — not one shared \"This host waits on a verb.\"
OFFER_LEAD = {
    "empire": "The captain will take a blade-hand. Help is an oath to fight with this host. Betray is a pyre.",
    "vampire_counts": "The dead do not offer guest-right. Warp-stink is a hanging matter until you name a path.",
    "lizardmen": "The plaque has not named you. The temple is wary. An omen — or a verb — must clear the Warp-stink.",
    "beastmen": "Prey speaks. The herd listens with horns. Help is gore. Betray is meat.",
    "greenskins": "Scrap or nick off. Da boss is waitin'. Help means fight wiv us. Betray means a krumpin'.",
    "dwarfs": "No oath is sworn. The Book is open. The hold is wary of Warp-born until a verb is named.",
    "skaven": "Man-thing reeks. The Clan does not trust-trust. Help-help, or die-die. The Council watches.",
    "khorne": "Blood is the only greeting. Help is a skull. Betray is also a skull. Name it.",
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
from the faction template (race plate), two named Recruits, and a
`/recruits spawn recruitPatrol tiny` levy (same as roaming). A marker
holds `rallous.fac.id` / race / stance / tier. Crash plants mixed-race
rings so a first-hour walk hits other banners. Ocean or unloaded ring
spots forceload a 3x3, hunt land, and fall inward — they do not skip
the race. Hostile camps bite on approach (vanilla raid), not tellraw
alone. First-days mix majors and
minors (cap 16). After every major of a race is placed, that race rolls
minor-only. Walking farther places more from the remaining pool (cap 40).
Never all 129 at once. Warp-crash assigns the nearest camp as
`rallous.contact` and fires the race stance. Help/betray/join/leave
(FTB, clickable chat, or flint-burn) change that contact faction.
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
        "scoreboard objectives add rallous.burn minecraft.used:minecraft.flint_and_steel",
        "scoreboard objectives add rallous.khorne dummy",
        "scoreboard objectives add rallous.chaos dummy",
        "scoreboard objectives add rallous.tries dummy",
        "scoreboard players set #-1 rallous.const -1",
        "scoreboard players set #2 rallous.const 2",
        f"scoreboard players set #cap rallous.const {FIRST_CAP}",
        f"scoreboard players set #xcap rallous.const {EXPLORE_CAP}",
        "execute unless score #placed rallous.gen = #placed rallous.gen run scoreboard players set #placed rallous.gen 0",
        "execute unless score #booted rallous.gen = #booted rallous.gen run scoreboard players set #booted rallous.gen 0",
        "execute unless score #clock rallous.gen = #clock rallous.gen run scoreboard players set #clock rallous.gen 0",
        "execute unless score #next_race rallous.gen = #next_race rallous.gen run scoreboard players set #next_race rallous.gen 0",
        "execute unless score $mix_only rallous.gen = $mix_only rallous.gen run scoreboard players set $mix_only rallous.gen 0",
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
execute as @e[type=minecraft:marker,tag=rallous.probe.pending] at @s unless loaded ~ ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.probe.pending,limit=2] at @s if loaded ~ ~ ~ run function rallous_factions:gen/ring_try
execute unless entity @e[type=minecraft:marker,tag=rallous.probe.pending,limit=1] as @e[type=minecraft:marker,tag=rallous.ring.origin,tag=!rallous.ring.unloaded,limit=1] at @s run function rallous_factions:gen/ring_unload
execute as @a at @s as @e[type=minecraft:marker,tag=rallous.camp,distance=..24] if score @s rallous.fac.stance matches 3 at @s run function rallous_factions:stance/bite
execute as @a at @s as @e[type=minecraft:marker,tag=rallous.camp,distance=..24] if score @s rallous.fac.stance matches 6 at @s run function rallous_factions:stance/bite
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_diplomacy:apply_path
execute as @a[scores={rallous.path=1..}] unless score @s rallous.path = @s rallous.path_seen run function rallous_factions:path/sync
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s if entity @e[tag=rallous.camp,distance=..18,limit=1] run function rallous_factions:contact/assign
execute as @a[tag=rallous.warp_landed,tag=!rallous.fac.greeted] at @s as @e[tag=rallous.camp,limit=1,sort=nearest,distance=..80] at @s run particle minecraft:campfire_signal_smoke ~ ~3 ~ 0.15 0.8 0.15 0.01 3
execute as @a[scores={rallous.burn=1..},tag=rallous.fac.greeted,tag=!rallous.burned] at @s if entity @e[tag=rallous.camp,distance=..14,limit=1] run function rallous_factions:path/burn_welcome
execute as @a[scores={rallous.burn=1..}] unless entity @e[tag=rallous.camp,distance=..14,limit=1] run scoreboard players set @s rallous.burn 0
execute as @a[tag=rallous.fac.greeted,tag=!rallous.burned] at @s at @e[tag=rallous.camp,distance=..14,limit=1,sort=nearest] if block ~1 ~1 ~ minecraft:fire run function rallous_factions:path/burn_welcome
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
        """# One more camp around the first crater / a landed player / an existing camp.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const as @a[tag=rallous.warp_landed,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_far
execute if score #placed rallous.gen < #cap rallous.const unless entity @a[tag=rallous.warp_landed,limit=1] as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_far
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
        """# Guaranteed contact camp just off the crater. Mix-rotate — do not biome-stack.
summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.near"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 20 36 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.near,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_mix
kill @e[type=minecraft:marker,tag=rallous.probe]
""",
    )
    w(
        FN / "gen/place_far.mcfunction",
        """summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe","rallous.probe.far"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run spreadplayers ~ ~ 140 380 false @s
execute as @e[type=minecraft:marker,tag=rallous.probe.far,limit=1,sort=nearest] at @s run function rallous_factions:gen/place_mix
kill @e[type=minecraft:marker,tag=rallous.probe]
""",
    )
    w(
        FN / "gen/place_rings.mcfunction",
        """# Mixed-race pickets on walkable rings. Not TW cities. Cap still 16.
# Target inner ~120 / outer ~220. Forceload each 3x3 (72 chunks, under 256).
# Probes stay at the crash until spreadplayers finds land — never skip a race.
kill @e[type=minecraft:marker,tag=rallous.ring.origin]
kill @e[type=minecraft:marker,tag=rallous.probe.pending]
summon minecraft:marker ~ ~ ~ {Tags:["rallous.ring.origin"]}
execute store result score $origin_x rallous.gen run data get entity @s Pos[0]
execute store result score $origin_z rallous.gen run data get entity @s Pos[2]
execute positioned ~120 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~-120 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~120 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~-120 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~220 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~-220 ~ ~ run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~220 run forceload add ~-1 ~-1 ~1 ~1
execute positioned ~ ~ ~-220 run forceload add ~-1 ~-1 ~1 ~1
scoreboard players set $ring_kind rallous.gen 0
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
scoreboard players set $ring_kind rallous.gen 1
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
function rallous_factions:gen/ring_queue
execute as @e[type=minecraft:marker,tag=rallous.probe.pending] at @s run function rallous_factions:gen/ring_try
schedule function rallous_factions:debug/count_races 100t replace
""",
    )
    w(
        FN / "gen/ring_queue.mcfunction",
        """# Summon at origin (loaded). Inner vs outer radius. spreadplayers hunts land.
summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe.pending","rallous.probe.ring","rallous.probe.new"]}
execute if score $ring_kind rallous.gen matches 0 run tag @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] add rallous.probe.inner
execute if score $ring_kind rallous.gen matches 1 run tag @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] add rallous.probe.outer
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run scoreboard players set @s rallous.tries 0
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run tag @s remove rallous.probe.new
""",
    )
    w(
        FN / "gen/ring_queue_go.mcfunction",
        """# Kept for zip asserts. Probes no longer teleport into unloaded cells.
execute store result score $tx rallous.gen run data get entity @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] Pos[0]
execute store result score $tz rallous.gen run data get entity @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] Pos[2]
scoreboard players operation $tx rallous.gen += $ring_dx rallous.gen
scoreboard players operation $tz rallous.gen += $ring_dz rallous.gen
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run forceload add ~-1 ~-1 ~1 ~1
""",
    )
    w(
        FN / "gen/ring_spot.mcfunction",
        """# Legacy single-spot entry. Queue one pending probe at this offset, then try if loaded.
execute if score #placed rallous.gen >= #cap rallous.const run scoreboard players set $noop rallous.gen 1
execute if score #placed rallous.gen < #cap rallous.const run function rallous_factions:gen/ring_queue_here
""",
    )
    w(
        FN / "gen/ring_queue_here.mcfunction",
        """summon minecraft:marker ~ ~ ~ {Tags:["rallous.probe.pending","rallous.probe.ring","rallous.probe.new"]}
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] at @s run forceload add ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run scoreboard players set @s rallous.tries 0
execute as @e[type=minecraft:marker,tag=rallous.probe.new,limit=1,sort=nearest] run tag @s remove rallous.probe.new
execute as @e[type=minecraft:marker,tag=rallous.probe.pending,limit=1,sort=nearest] at @s if loaded ~ ~ ~ run function rallous_factions:gen/ring_try
""",
    )
    w(
        FN / "gen/ring_try.mcfunction",
        """# Chunk is loaded. Hunt land. If ocean, fall inward. Do not skip the race.
execute if score #placed rallous.gen >= #cap rallous.const run function rallous_factions:gen/ring_done
execute if score #placed rallous.gen < #cap rallous.const run function rallous_factions:gen/ring_try_go
""",
    )
    w(
        FN / "gen/ring_try_go.mcfunction",
        """scoreboard players add @s rallous.tries 1
execute if entity @s[tag=rallous.probe.inner] run spreadplayers ~ ~ 80 140 false @s
execute if entity @s[tag=rallous.probe.outer] run spreadplayers ~ ~ 150 230 false @s
function rallous_factions:gen/ring_far
execute if score $far rallous.gen matches 0 run scoreboard players set $wet rallous.gen 1
execute if score $far rallous.gen matches 1 run function rallous_factions:gen/ring_wet
execute if score $wet rallous.gen matches 1 if entity @s[tag=rallous.probe.outer] run spreadplayers ~ ~ 80 140 false @s
function rallous_factions:gen/ring_far
execute if score $far rallous.gen matches 0 if entity @s[tag=rallous.probe.outer] run function rallous_factions:gen/ring_inward
function rallous_factions:gen/ring_wet
execute if score $wet rallous.gen matches 1 run function rallous_factions:gen/ring_inward
execute at @s if entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/ring_nudge
scoreboard players set $done rallous.gen 0
function rallous_factions:gen/ring_wet
function rallous_factions:gen/ring_far
execute if score $wet rallous.gen matches 0 if score $far rallous.gen matches 1 at @s unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix
execute if score $done rallous.gen matches 1 run function rallous_factions:gen/ring_done
execute if score $done rallous.gen matches 0 if score @s rallous.tries matches 6.. run function rallous_factions:gen/ring_last
""",
    )
    w(
        FN / "gen/ring_wet.mcfunction",
        """scoreboard players set $wet rallous.gen 0
execute at @s if biome ~ ~ ~ #minecraft:is_ocean run scoreboard players set $wet rallous.gen 1
execute at @s if biome ~ ~ ~ #minecraft:is_river run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~ ~ minecraft:water run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:water run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:air run scoreboard players set $wet rallous.gen 1
execute at @s if block ~ ~-1 ~ minecraft:cave_air run scoreboard players set $wet rallous.gen 1
""",
    )
    w(
        FN / "gen/ring_far.mcfunction",
        """# 1 if the probe left the crater (spreadplayers found a ring cell).
execute store result score $px rallous.gen run data get entity @s Pos[0]
execute store result score $pz rallous.gen run data get entity @s Pos[2]
scoreboard players operation $dx rallous.gen = $px rallous.gen
scoreboard players operation $dx rallous.gen -= $origin_x rallous.gen
execute if score $dx rallous.gen matches ..-1 run scoreboard players operation $dx rallous.gen *= #-1 rallous.const
scoreboard players operation $dz rallous.gen = $pz rallous.gen
scoreboard players operation $dz rallous.gen -= $origin_z rallous.gen
execute if score $dz rallous.gen matches ..-1 run scoreboard players operation $dz rallous.gen *= #-1 rallous.const
scoreboard players set $far rallous.gen 0
execute if score $dx rallous.gen matches 40.. run scoreboard players set $far rallous.gen 1
execute if score $dz rallous.gen matches 40.. run scoreboard players set $far rallous.gen 1
""",
    )
    w(
        FN / "gen/ring_unload.mcfunction",
        """# Drop the 8 ring 3x3 forceloads after probes finish. Stay under the 256 cap.
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~120 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~-120 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~120 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~-120 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~220 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~-220 ~ ~ run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~220 run forceload remove ~-1 ~-1 ~1 ~1
execute as @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] at @s positioned ~ ~ ~-220 run forceload remove ~-1 ~-1 ~1 ~1
tag @e[type=minecraft:marker,tag=rallous.ring.origin] add rallous.ring.unloaded
""",
    )
    w(
        FN / "gen/ring_inward.mcfunction",
        """# Halfway toward crash origin, then land-hunt a closer ring.
execute store result score $px rallous.gen run data get entity @s Pos[0]
execute store result score $pz rallous.gen run data get entity @s Pos[2]
scoreboard players operation $px rallous.gen += $origin_x rallous.gen
scoreboard players operation $pz rallous.gen += $origin_z rallous.gen
scoreboard players operation $px rallous.gen /= #2 rallous.const
scoreboard players operation $pz rallous.gen /= #2 rallous.const
execute store result entity @s Pos[0] double 1 run scoreboard players get $px rallous.gen
execute store result entity @s Pos[2] double 1 run scoreboard players get $pz rallous.gen
data modify entity @s Pos[1] set value 80.0d
execute at @s run forceload add ~-1 ~-1 ~1 ~1
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run spreadplayers ~ ~ 36 90 false @s
""",
    )
    w(
        FN / "gen/ring_nudge.mcfunction",
        """# Other picket too close. Step off so this race still lands.
tp @s ~36 ~ ~36
execute at @s run forceload add ~-1 ~-1 ~1 ~1
execute at @s run spreadplayers ~ ~ 8 24 false @s
""",
    )
    w(
        FN / "gen/ring_last.mcfunction",
        """# Last chance: land anywhere in a first-hour walk of the crater. Then stop the probe.
execute at @e[type=minecraft:marker,tag=rallous.ring.origin,limit=1] run spreadplayers ~ ~ 28 80 false @s
execute at @s if entity @e[tag=rallous.camp,distance=..28,limit=1] run tp @s ~40 ~ ~-20
execute at @s unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix
function rallous_factions:gen/ring_done
""",
    )
    w(
        FN / "gen/ring_done.mcfunction",
        """execute at @s run forceload remove ~-1 ~-1 ~1 ~1
kill @s
""",
    )
    w(
        FN / "gen/place_mix.mcfunction",
        """# Ring mix: rotate the eight races. Skip biome prefer so dark woods are not four Beastmen.
# Nearby camp is a block, not a success — caller nudges. Increment rotation only when a camp lands.
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[tag=rallous.camp,distance=..28,limit=1] run function rallous_factions:gen/place_mix_go
scoreboard players set $mix_only rallous.gen 0
""",
    )
    w(
        FN / "gen/place_mix_go.mcfunction",
        """execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 1 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 2 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 3 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 4 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 5 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 6 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 if score #next_race rallous.gen matches 7 run function rallous_factions:pool/khorne/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/empire/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/dwarfs/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/lizardmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/vampire_counts/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/greenskins/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/skaven/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/beastmen/pick
execute if score $done rallous.gen matches 0 run function rallous_factions:pool/khorne/pick
execute if score $done rallous.gen matches 1 run scoreboard players add #next_race rallous.gen 1
execute if score #next_race rallous.gen matches 8.. run scoreboard players set #next_race rallous.gen 0
""",
    )
    levy_types = [
        {"id": "recruits:recruit", "required": False},
        {"id": "recruits:bowman", "required": False},
        {"id": "recruits:recruit_shieldman", "required": False},
        {"id": "recruits:nomad", "required": False},
        {"id": "recruits:horseman", "required": False},
        {"id": "recruits:crossbowman", "required": False},
        {"id": "recruits:scout", "required": False},
        {"id": "recruits:captain", "required": False},
        {"id": "recruits:patrol_leader", "required": False},
        {"id": "recruits:messenger", "required": False},
    ]
    dump_json(OUT / "data" / "rallous_factions" / "tags" / "entity_types" / "levy.json", {"replace": False, "values": levy_types})
    w(
        FN / "host/levy.mcfunction",
        """# Small Recruits patrol at this camp. Same command as roaming. Not an armor-stand host.
execute if entity @s[tag=rallous.host.levied] run scoreboard players set $noop rallous.gen 1
execute unless entity @s[tag=rallous.host.levied] run function rallous_factions:host/levy_go
""",
    )
    w(
        FN / "host/levy_go.mcfunction",
        """# /recruits spawn recruitPatrol tiny = recruit + shieldman + bowman + patrol_leader.
# Command uses getEntity().getOnPos() — must run as an entity at the column.
summon minecraft:armor_stand ~ ~ ~ {Tags:["rallous.host.recsrc"],Invisible:1b,Marker:1b,NoGravity:1b,Small:1b,Invulnerable:1b,DisabledSlots:4144959}
execute as @e[type=minecraft:armor_stand,tag=rallous.host.recsrc,limit=1] at @s run recruits spawn recruitPatrol tiny
kill @e[type=minecraft:armor_stand,tag=rallous.host.recsrc]
scoreboard players set $levy rallous.gen 0
execute if entity @e[type=#rallous_factions:levy,distance=..16,tag=!rallous.soldier,tag=!rallous.roam] run scoreboard players set $levy rallous.gen 1
execute if score $levy rallous.gen matches 1 run function rallous_factions:host/levy_tag
execute if score $levy rallous.gen matches 0 run function rallous_factions:host/levy_fallback
tag @s add rallous.host.levied
""",
    )
    w(
        FN / "host/levy_tag.mcfunction",
        """execute as @e[type=#rallous_factions:levy,distance=..16,tag=!rallous.soldier,tag=!rallous.roam] run tag @s add rallous.soldier
execute as @e[type=#rallous_factions:levy,distance=..16,tag=rallous.soldier] run tag @s add rallous.host.levy
execute as @e[type=#rallous_factions:levy,distance=..16,tag=rallous.soldier] run data merge entity @s {PersistenceRequired:1b}
""",
    )
    w(
        FN / "host/levy_fallback.mcfunction",
        """# Recruits missing or command failed. Help camps must not murder. Hostile camps still bite.
execute if score @s rallous.fac.stance matches 3 run function rallous_factions:host/levy_fallback_hostile
execute if score @s rallous.fac.stance matches 6 run function rallous_factions:host/levy_fallback_hostile
execute unless score @s rallous.fac.stance matches 3 unless score @s rallous.fac.stance matches 6 run function rallous_factions:host/levy_fallback_guard
""",
    )
    w(
        FN / "host/levy_fallback_hostile.mcfunction",
        """summon minecraft:pillager ~2 ~ ~2 {Tags:["rallous.soldier","rallous.host.levy"],CustomName:'{"text":"Levy","color":"gray"}',CustomNameVisible:1b,PersistenceRequired:1b,CanJoinRaid:0b,PatrolLeader:0b,Patrolling:0b,HandItems:[{id:"minecraft:iron_sword",Count:1b},{}]}
summon minecraft:pillager ~-2 ~ ~2 {Tags:["rallous.soldier","rallous.host.levy"],CustomName:'{"text":"Levy","color":"gray"}',CustomNameVisible:1b,PersistenceRequired:1b,CanJoinRaid:0b,PatrolLeader:0b,Patrolling:0b,HandItems:[{id:"minecraft:bow",Count:1b},{}]}
""",
    )
    w(
        FN / "host/levy_fallback_guard.mcfunction",
        """summon minecraft:iron_golem ~2 ~ ~2 {Tags:["rallous.soldier","rallous.host.levy"],CustomName:'{"text":"Levy","color":"gray"}',CustomNameVisible:1b,PersistenceRequired:1b,PlayerCreated:1b}
summon minecraft:iron_golem ~-2 ~ ~2 {Tags:["rallous.soldier","rallous.host.levy"],CustomName:'{"text":"Levy","color":"gray"}',CustomNameVisible:1b,PersistenceRequired:1b,PlayerCreated:1b}
""",
    )
    w(
        FN / "stance/bite.mcfunction",
        """# Approach / greet / betray. Hostile camps fight. Help-leaning never calls this.
execute unless entity @s[tag=rallous.bitten] run function rallous_factions:stance/bite_go
""",
    )
    w(
        FN / "stance/bite_go.mcfunction",
        """execute if entity @s[tag=rallous.bitten] run scoreboard players set $noop rallous.gen 1
execute unless entity @s[tag=rallous.bitten] run function rallous_factions:stance/bite_fire
""",
    )
    w(
        FN / "stance/bite_fire.mcfunction",
        """tag @s add rallous.bitten
scoreboard players add $bite rallous.gen 1
tellraw @a[distance=..48] {"text":"The host lowers spears. Warp-born is meat.","color":"red"}
execute if score @s rallous.fac.race matches 7 run function rallous_factions:stance/bite_skaven
execute if score @s rallous.fac.race matches 4 run function rallous_factions:stance/bite_beastmen
execute if score @s rallous.fac.race matches 8 run function rallous_factions:stance/bite_khorne
execute unless score @s rallous.fac.race matches 4 unless score @s rallous.fac.race matches 7 unless score @s rallous.fac.race matches 8 run function rallous_factions:stance/bite_generic
execute as @e[tag=rallous.raid,distance=..16] run data modify entity @s AngryAt set from entity @p UUID
execute as @e[tag=rallous.raid,distance=..16] run data merge entity @s {AngerTime:2000}
execute store result score $raid_n rallous.gen if entity @e[tag=rallous.raid,distance=..24]
""",
    )
    w(
        FN / "stance/bite_skaven.mcfunction",
        "\n".join(raid_lines("skaven")) + "\n",
    )
    w(
        FN / "stance/bite_beastmen.mcfunction",
        "\n".join(raid_lines("beastmen")) + "\n",
    )
    w(
        FN / "stance/bite_khorne.mcfunction",
        "\n".join(raid_lines("khorne")) + "\n",
    )
    w(
        FN / "stance/bite_generic.mcfunction",
        "\n".join(raid_lines("empire")) + "\n",
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
# Bind scores now. Greet waits until the survivor walks to the picket.
function rallous_factions:gen/boot
execute unless entity @e[tag=rallous.camp,distance=..220,limit=1] run function rallous_factions:gen/place_near
execute unless entity @e[tag=rallous.camp,distance=..260,limit=1] run function rallous_factions:gen/place_one
function rallous_factions:gen/place_rings
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
function rallous_factions:contact/bind_only
""",
    )
    w(
        FN / "contact/assign.mcfunction",
        """# Once per survivor. A second land/tick path cannot greet or kit again.
execute unless entity @s[tag=rallous.contacted] run function rallous_factions:contact/assign_go
""",
    )
    w(
        FN / "contact/bind_only.mcfunction",
        """# Crash bind: scores + Recruits name. Do not greet — the lord is off the bowl.
scoreboard players set @s rallous.joined 1
execute unless entity @e[tag=rallous.camp,distance=..400,limit=1] run function rallous_factions:gen/place_near
tag @e[tag=rallous_contact] remove rallous_contact
execute as @e[tag=rallous.camp,limit=1,sort=nearest] run tag @s add rallous_contact
execute as @e[tag=rallous.lord,limit=1,sort=nearest] run tag @s add rallous_contact
scoreboard players operation @s rallous.contact_id = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.id
scoreboard players operation @s rallous.race = @e[tag=rallous.camp,limit=1,sort=nearest] rallous.fac.race
scoreboard players set @s rallous.contact 1
function rallous_recruits_bind:on_contact
execute as @e[type=minecraft:marker,tag=rallous.camp,tag=!rallous.winds,limit=1,sort=nearest] at @s run function rallous_winds:place
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:contact/beacon
tellraw @s {"text":"Banner-smoke on the horizon. Walk to it. A named lord will speak when you reach the picket — not a mute village.","color":"gold"}
""",
    )
    w(
        FN / "contact/beacon.mcfunction",
        """# Extra smoke so the picket is visible from the crater rim.
execute unless block ~2 ~ ~-2 minecraft:campfire unless block ~2 ~ ~-2 minecraft:soul_campfire run setblock ~2 ~ ~-2 minecraft:campfire
execute unless block ~-2 ~ ~2 minecraft:campfire unless block ~-2 ~ ~2 minecraft:soul_campfire run setblock ~-2 ~ ~2 minecraft:campfire
particle minecraft:campfire_signal_smoke ~ ~4 ~ 0.2 1.2 0.2 0.02 12
""",
    )
    w(
        FN / "contact/assign_go.mcfunction",
        """# Nearest compiled camp becomes this survivor's contact faction.
# Call this at the picket (tick distance..18), not from the crater bowl.
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
function rallous_factions:path/offer
tellraw @s {"text":"When night falls at this picket, the session starts. Or /function rallous_session:start","color":"gray"}
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
execute if score @s rallous.fac.stance matches 1 as @a[tag=rallous.path_actor,limit=1] at @s run function rallous_kit:on_greet
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
        "function rallous_factions:stance/bite\n",
    )
    w(
        FN / "debug/force_contact.mcfunction",
        """# Smoke: plant a real table faction at your feet and fire its stance.
function rallous_factions:gen/place_one
function rallous_factions:contact/assign
tellraw @s {"text":"Forced a compiled faction camp here. Look for a named lord and a stance line.","color":"gold"}
""",
    )
    w(
        FN / "path/offer.mcfunction",
        """# First-hour verbs at the picket. Lead-in is race-skeptical. Four paths stay reachable.
give @s minecraft:flint_and_steel{display:{Name:'{"text":"Burn their welcome","italic":false}',Lore:['{"text":"Use this at the picket. Khorne hears.","color":"dark_red"}']}} 1
give @s minecraft:bread{display:{Name:'{"text":"Share food","italic":false}'}} 4
execute if score @s rallous.race matches 1 run function rallous_factions:path/offer_empire
execute if score @s rallous.race matches 2 run function rallous_factions:path/offer_vampire_counts
execute if score @s rallous.race matches 3 run function rallous_factions:path/offer_lizardmen
execute if score @s rallous.race matches 4 run function rallous_factions:path/offer_beastmen
execute if score @s rallous.race matches 5 run function rallous_factions:path/offer_greenskins
execute if score @s rallous.race matches 6 run function rallous_factions:path/offer_dwarfs
execute if score @s rallous.race matches 7 run function rallous_factions:path/offer_skaven
execute if score @s rallous.race matches 8 run function rallous_factions:path/offer_khorne
execute unless score @s rallous.race matches 1..8 run function rallous_factions:path/offer_empire
""",
    )
    buttons = (
        '{"text":"[Help]","color":"green","bold":true,"clickEvent":{"action":"run_command","value":"/function rallous_contact:path/help"},"hoverEvent":{"action":"show_text","contents":"Ally this camp"}},'
        '{"text":" ","color":"white"},'
        '{"text":"[Betray]","color":"red","bold":true,"clickEvent":{"action":"run_command","value":"/function rallous_contact:path/betray"},"hoverEvent":{"action":"show_text","contents":"War with this camp"}},'
        '{"text":" ","color":"white"},'
        '{"text":"[Join]","color":"yellow","bold":true,"clickEvent":{"action":"run_command","value":"/function rallous_contact:path/join"},"hoverEvent":{"action":"show_text","contents":"Take their colour"}},'
        '{"text":" ","color":"white"},'
        '{"text":"[Leave]","color":"gray","bold":true,"clickEvent":{"action":"run_command","value":"/function rallous_contact:path/leave"},"hoverEvent":{"action":"show_text","contents":"Align and ride on"}},'
        '{"text":" — or flint the pad.","color":"dark_red"}'
    )
    offer_colors = {
        "empire": "gold",
        "vampire_counts": "dark_red",
        "lizardmen": "aqua",
        "beastmen": "dark_green",
        "greenskins": "green",
        "dwarfs": "gold",
        "skaven": "light_purple",
        "khorne": "red",
    }
    for rid, lead in OFFER_LEAD.items():
        lead_json = json.dumps(lead, ensure_ascii=False)
        color = offer_colors[rid]
        w(
            FN / "path" / f"offer_{rid}.mcfunction",
            f'tellraw @s [{{"text":{lead_json},"color":"{color}"}},{{"text":" ","color":"white"}},{buttons}]\n',
        )
    w(
        FN / "path/burn_welcome.mcfunction",
        """# Khorne if you burn welcome. Reachable at the picket, not a wiki sentence.
execute if entity @s[tag=rallous.burned] run scoreboard players set @s rallous.burn 0
execute unless entity @s[tag=rallous.burned] run function rallous_factions:path/burn_welcome_go
""",
    )
    w(
        FN / "path/burn_welcome_go.mcfunction",
        """tag @s add rallous.burned
scoreboard players set @s rallous.burn 0
scoreboard players set @s rallous.path 2
scoreboard players set @s rallous.betray 1
scoreboard players add @s rallous.khorne 1
scoreboard players add @s rallous.chaos 1
function rallous_contact:race/khorne
function rallous_contact:path/betray
tellraw @s {"text":"You burned their welcome. Blood is a path. This camp names you oath-breaker. Khorne hears.","color":"dark_red","bold":true}
execute as @e[tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:contact/raid_generic
execute as @e[tag=rallous.camp,limit=1,sort=nearest] at @s run particle minecraft:lava ~ ~1 ~ 0.6 0.4 0.6 0.02 20
""",
    )
    w(
        FN / "debug/count_races.mcfunction",
        """# Count rallous.camp markers by race. Fresh-world mix proof.
execute store result score $c_emp rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=1}]
execute store result score $c_vc rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=2}]
execute store result score $c_lm rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=3}]
execute store result score $c_bm rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=4}]
execute store result score $c_gs rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=5}]
execute store result score $c_dw rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=6}]
execute store result score $c_sk rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=7}]
execute store result score $c_kh rallous.gen if entity @e[tag=rallous.camp,scores={rallous.fac.race=8}]
scoreboard players set $c_races rallous.gen 0
execute if score $c_emp rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_vc rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_lm rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_bm rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_gs rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_dw rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_sk rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute if score $c_kh rallous.gen matches 1.. run scoreboard players add $c_races rallous.gen 1
execute store result score $c_lords rallous.gen if entity @e[tag=rallous.lord]
execute store result score $c_camps rallous.gen if entity @e[tag=rallous.camp]
execute store result score $c_temple rallous.gen if entity @e[tag=rallous.temple_beast]
execute store result score $c_herd rallous.gen if entity @e[tag=rallous.herd_beast]
tellraw @a [{"text":"[rallous.mix] camps=","color":"gold"},{"score":{"name":"$c_camps","objective":"rallous.gen"}},{"text":" lords=","color":"gold"},{"score":{"name":"$c_lords","objective":"rallous.gen"}},{"text":" races=","color":"gold"},{"score":{"name":"$c_races","objective":"rallous.gen"}},{"text":" emp=","color":"red"},{"score":{"name":"$c_emp","objective":"rallous.gen"}},{"text":" vc=","color":"dark_red"},{"score":{"name":"$c_vc","objective":"rallous.gen"}},{"text":" lm=","color":"aqua"},{"score":{"name":"$c_lm","objective":"rallous.gen"}},{"text":" bm=","color":"dark_green"},{"score":{"name":"$c_bm","objective":"rallous.gen"}},{"text":" gs=","color":"green"},{"score":{"name":"$c_gs","objective":"rallous.gen"}},{"text":" dw=","color":"gold"},{"score":{"name":"$c_dw","objective":"rallous.gen"}},{"text":" sk=","color":"light_purple"},{"score":{"name":"$c_sk","objective":"rallous.gen"}},{"text":" kh=","color":"dark_red"},{"score":{"name":"$c_kh","objective":"rallous.gen"}},{"text":" temple_beasts=","color":"aqua"},{"score":{"name":"$c_temple","objective":"rallous.gen"}},{"text":" herd_beasts=","color":"dark_green"},{"score":{"name":"$c_herd","objective":"rallous.gen"}}]
execute unless score $c_races rallous.gen matches 8 run say [rallous.mix] WARN unique races != 8
execute if score $c_races rallous.gen matches 8 run say [rallous.mix] OK eight races on this fresh field
execute store result score $pending rallous.gen if entity @e[tag=rallous.probe.pending]
tellraw @a [{"text":"[rallous.mix] pending_probes=","color":"gray"},{"score":{"name":"$pending","objective":"rallous.gen"}},{"text":" bite=","color":"red"},{"score":{"name":"$bite","objective":"rallous.gen"}},{"text":" raid=","color":"red"},{"score":{"name":"$raid_n","objective":"rallous.gen"}}]
""",
    )
    w(
        FN / "debug/prove_terrain.mcfunction",
        """# Real-terrain mix. No stone pad. Run at crash/spawn surface.
say [rallous.terrain] ring mix on real land — not a stone pad
function rallous_factions:gen/boot
scoreboard players set #next_race rallous.gen 0
function rallous_factions:gen/place_rings
function rallous_factions:debug/count_races
say [rallous.terrain] inner spots land now; pending probes fall inward over ticks
""",
    )
    w(
        FN / "debug/prove_bite.mcfunction",
        """# Hostile camp must spawn raid entities. Help-leaning must not.
say [rallous.bite] start
scoreboard players set $bite rallous.gen 0
kill @e[tag=rallous.bite.dummy]
kill @e[tag=rallous.help.dummy]
kill @e[tag=rallous.raid]
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/skaven/pick
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/khorne/pick
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1] positioned ~28 ~ ~ run function rallous_factions:pool/beastmen/pick
scoreboard players set $mix_only rallous.gen 0
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1,sort=nearest] at @s run summon minecraft:villager ~1 ~ ~ {Tags:["rallous.bite.dummy"],CustomName:'{"text":"Bite Dummy","color":"red"}',CustomNameVisible:1b,PersistenceRequired:1b}
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=3},limit=1,sort=nearest] at @s run function rallous_factions:stance/bite
execute store result score $raid_n rallous.gen if entity @e[tag=rallous.raid]
execute if score $bite rallous.gen matches 1.. if score $raid_n rallous.gen matches 1.. run say [rallous.bite] OK hostile raid spawned
execute unless score $raid_n rallous.gen matches 1.. run say [rallous.bite] FAIL no raid entities
scoreboard players set $mix_only rallous.gen 1
scoreboard players set $done rallous.gen 0
execute unless entity @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1] positioned ~-28 ~ ~ run function rallous_factions:pool/empire/pick
scoreboard players set $mix_only rallous.gen 0
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] at @s run summon minecraft:villager ~1 ~ ~ {Tags:["rallous.help.dummy"],CustomName:'{"text":"Help Dummy","color":"green"}',CustomNameVisible:1b,PersistenceRequired:1b}
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] if entity @s[tag=rallous.bitten] run say [rallous.bite] FAIL help camp bitten
execute as @e[type=minecraft:marker,tag=rallous.camp,scores={rallous.fac.stance=1},limit=1,sort=nearest] unless entity @s[tag=rallous.bitten] run say [rallous.bite] OK help camp did not bite
execute as @e[tag=rallous.help.dummy,limit=1] at @s if entity @e[type=minecraft:pillager,tag=rallous.host.levy,distance=..8,limit=1] run say [rallous.bite] FAIL help levy is a pillager
execute as @e[tag=rallous.help.dummy,limit=1] at @s unless entity @e[type=minecraft:pillager,tag=rallous.host.levy,distance=..8,limit=1] run say [rallous.bite] OK help dummy not facing camp pillagers
""",
    )
    w(
        FN / "debug/headless_proof.mcfunction",
        """# Function driver: crash / on_land / greet / rings / levy / paths / roaming / death.
# Run at a surface. No CurseForge GPU. Does not claim SHIP_READY.
say [rallous.proof] start field driver
function rallous_factions:gen/boot
execute unless entity @e[tag=rallous.camp,distance=..48,limit=1] run function rallous_factions:gen/place_near
function rallous_factions:gen/place_rings
execute as @e[type=minecraft:marker,tag=rallous.camp,limit=1,sort=nearest] at @s run function rallous_factions:host/levy
execute store result score $proof_camps rallous.gen if entity @e[tag=rallous.camp]
execute store result score $proof_lords rallous.gen if entity @e[tag=rallous.lord]
execute store result score $proof_soldiers rallous.gen if entity @e[tag=rallous.soldier]
execute store result score $proof_levy rallous.gen if entity @e[tag=rallous.host.levy]
scoreboard players operation $proof_placed rallous.gen = #placed rallous.gen
function rallous_factions:debug/count_races
function rallous_factions:debug/prove_bite
function rallous_factions:contact/assign
function rallous_factions:path/offer
function rallous_contact:path/help
function rallous_factions:path/burn_welcome
function rallous_roaming:events/waaagh
function rallous_warp_crash:on_death
function rallous_warp_crash:debug/prove_slots
tellraw @a [{"text":"[rallous.proof] camps=","color":"gold"},{"score":{"name":"$proof_camps","objective":"rallous.gen"}},{"text":" lords=","color":"gold"},{"score":{"name":"$proof_lords","objective":"rallous.gen"}},{"text":" soldiers=","color":"gold"},{"score":{"name":"$proof_soldiers","objective":"rallous.gen"}},{"text":" levy=","color":"gold"},{"score":{"name":"$proof_levy","objective":"rallous.gen"}},{"text":" placed=","color":"gold"},{"score":{"name":"$proof_placed","objective":"rallous.gen"}}]
execute unless score $proof_camps rallous.gen matches 2.. run say [rallous.proof] FAIL camps < 2
execute unless score $proof_lords rallous.gen matches 1.. run say [rallous.proof] FAIL no named lord
execute unless score $proof_soldiers rallous.gen matches 1.. run say [rallous.proof] FAIL no soldiers
execute if score $proof_camps rallous.gen matches 2.. if score $proof_lords rallous.gen matches 1.. if score $proof_soldiers rallous.gen matches 1.. run say [rallous.proof] OK field has lord + host + mixed camps
say [rallous.proof] done
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
                    "execute unless score $mix_only rallous.gen matches 1 run scoreboard players set $need_biome rallous.gen 1",
                    "execute if score $mix_only rallous.gen matches 1 run scoreboard players set $need_biome rallous.gen 0",
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
                f"HandItems:[{{id:\"minecraft:{weapon_id}\",Count:1b}},{{}}],"
                f"{lord_armor_nbt(race['id'])}}}"
            ),
            * [f"execute if score $skip rallous.gen matches 0 run {line}" for line in camp_soldiers(race["id"], sl, color)],
            * [f"execute if score $skip rallous.gen matches 0 run {line}" for line in lord_sote_replace(race["id"], sl)],
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.id {i}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.race {RACE_NUM[race['id']]}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.stance {stance}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] run scoreboard players set @s rallous.fac.tier {tier}",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] at @s run function rallous_factions:host/levy",
            f"execute if score $skip rallous.gen matches 0 as @e[type=minecraft:marker,tag=rallous.fac.{sl},limit=1,sort=nearest] at @s run function rallous_temple_herd:mark_camp",
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
    rid = race["id"]
    actions = STANCE_ACTION[rid]
    default = STANCE_NUM[race["warp_stranger_stance"]]
    lines = [
        tellraw("@a[distance=..48]", texts[default]),
        f"execute if score @s rallous.fac.stance matches 1 run give @p minecraft:{weapon_id}{{display:{{Name:{wname}}}}} 1",
        "execute if score @s rallous.fac.stance matches 1 run "
        + tellraw("@a[distance=..48]", [{"text": actions[1], "color": "gold"}]),
        "execute if score @s rallous.fac.stance matches 2 run scoreboard players set @p rallous.proved 0",
        "execute if score @s rallous.fac.stance matches 2 run "
        + tellraw("@a[distance=..48]", [{"text": actions[2], "color": "yellow"}]),
        "execute if score @s rallous.fac.stance matches 4 run scoreboard players set @p rallous.proved 0",
        "execute if score @s rallous.fac.stance matches 4 run "
        + tellraw("@a[distance=..48]", [{"text": actions[4], "color": "dark_purple"}]),
        "execute if score @s rallous.fac.stance matches 3 run "
        + tellraw("@a[distance=..48]", [{"text": actions[3], "color": "red"}]),
        "execute if score @s rallous.fac.stance matches 3 run function rallous_factions:stance/bite",
        "execute if score @s rallous.fac.stance matches 6 run function rallous_factions:stance/bite",
        "particle minecraft:witch ~ ~2 ~ 0.3 1 0.3 0 16",
    ]
    w(FN / "raid" / f"{fac['_slug']}.mcfunction", "function rallous_factions:stance/bite\n")
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
