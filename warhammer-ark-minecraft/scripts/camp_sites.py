"""War-host camp layouts for compile_factions.py.

A camp is a picket that reads as a host, not 3 blocks and a villager.
Site kinds: settled / hold / temple / herd / waaagh / under-empire / khorne.
Vanilla blocks only. Two Recruits soldiers (summon) — `/recruits spawn
recruitPatrol` exists but is a generic admin patrol, not this host.
"""

from __future__ import annotations

import json

# Visual archetype per race. Faction JSON only stores settled/roaming.
SITE_KIND = {
    "empire": "settled",
    "vampire_counts": "settled",
    "dwarfs": "hold",
    "lizardmen": "temple",
    "beastmen": "herd",
    "greenskins": "waaagh",
    "skaven": "under-empire",
    "khorne": "khorne",
}

RACE_SOLDIERS = {
    "empire": (("recruits:recruit_shieldman", "State Troop"), ("recruits:bowman", "Handgunner")),
    "vampire_counts": (("recruits:recruit", "Grave Guard"), ("recruits:bowman", "Sylvanian Levy")),
    "lizardmen": (("recruits:recruit", "Temple Guard"), ("recruits:scout", "Skink Scout")),
    "beastmen": (("recruits:recruit", "Gor"), ("recruits:recruit_shieldman", "Bestigor")),
    "greenskins": (("recruits:recruit", "Orc Boy"), ("recruits:bowman", "Arrer Boy")),
    "dwarfs": (("recruits:recruit_shieldman", "Dwarf Warrior"), ("recruits:crossbowman", "Quarreller")),
    "skaven": (("recruits:recruit", "Clanrat"), ("recruits:scout", "Night Runner")),
    "khorne": (("recruits:recruit", "Bloodreaver"), ("recruits:recruit_shieldman", "Blood Warrior")),
}

MIN_CAMP_BLOCKS = 20


def rel(x: int, y: int, z: int) -> str:
    def axis(n: int) -> str:
        return "~" if n == 0 else f"~{n}"

    return f"{axis(x)} {axis(y)} {axis(z)}"


def snbt_name(obj) -> str:
    dumped = json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("'", "\u2019")
    return "'" + dumped + "'"


def palisade_posts(fence: str, radius: int = 3) -> list[str]:
    """2-high posts at corners and mid-sides. +Z left open as a gate."""
    r = radius
    spots = [(r, r), (-r, r), (r, -r), (-r, -r), (r, 0), (-r, 0), (0, -r)]
    lines: list[str] = []
    for x, z in spots:
        lines.append(f"setblock {rel(x, 0, z)} minecraft:{fence}")
        lines.append(f"setblock {rel(x, 1, z)} minecraft:{fence}")
    return lines


def twin_banners(banner: str, radius: int = 3) -> list[str]:
    return [
        f"setblock {rel(radius, 2, 0)} minecraft:{banner}",
        f"setblock {rel(-radius, 2, 0)} minecraft:{banner}",
    ]


def camp_blocks(race_id: str, site: str, settlement: str, banner: str) -> list[str]:
    """War-host picket by site kind. Thicker than a stub; not a city."""
    kind = SITE_KIND.get(race_id, "settled")
    roaming = site == "roaming" or settlement == "roaming"
    if kind == "khorne":
        return _camp_khorne(banner)
    if kind == "herd":
        return _camp_herd(banner)
    if kind == "waaagh":
        return _camp_waaagh(banner, crag=not roaming)
    if kind == "under-empire":
        return _camp_under_empire(banner)
    if kind == "hold":
        return _camp_hold(banner, expedition=roaming)
    if kind == "temple":
        return _camp_temple(banner)
    return _camp_settled(race_id, banner)


def _camp_settled(race_id: str, banner: str) -> list[str]:
    crypt = race_id == "vampire_counts"
    floor = "deepslate_bricks" if crypt else "packed_mud"
    fence = "dark_oak_fence" if crypt else "oak_fence"
    fire = "soul_campfire" if crypt else "campfire"
    light = "soul_lantern" if crypt else "lantern"
    lines = [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:{floor}",
        f"setblock {rel(0, -1, 0)} minecraft:cobblestone",
        f"setblock {rel(0, 0, 0)} minecraft:{fire}",
        f"setblock {rel(2, 0, -2)} minecraft:campfire",
        *palisade_posts(fence),
        *twin_banners(banner),
        f"setblock {rel(-2, 0, 2)} minecraft:{light}",
        f"setblock {rel(-2, 0, -2)} minecraft:barrel",
        f"setblock {rel(2, 0, 2)} minecraft:hay_block",
    ]
    if crypt:
        lines.extend(
            [
                f"setblock {rel(3, 2, 3)} minecraft:skeleton_skull",
                f"setblock {rel(-3, 2, 3)} minecraft:skeleton_skull",
                f"setblock {rel(1, 0, -1)} minecraft:cobweb",
                f"setblock {rel(-1, 0, -1)} minecraft:cobweb",
            ]
        )
    else:
        lines.extend(
            [
                f"setblock {rel(0, 2, -3)} minecraft:{banner}",
                f"setblock {rel(1, 0, 2)} minecraft:crafting_table",
            ]
        )
    return lines


def _camp_hold(banner: str, expedition: bool) -> list[str]:
    lines = [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:stone_bricks",
        f"setblock {rel(0, -1, 0)} minecraft:cobblestone",
        f"setblock {rel(0, 0, 0)} minecraft:campfire",
        f"setblock {rel(2, 0, -2)} minecraft:campfire",
        *palisade_posts("cobblestone_wall"),
        *twin_banners(banner),
        f"setblock {rel(-2, 0, 2)} minecraft:lantern",
        f"setblock {rel(-2, 0, -2)} minecraft:anvil",
        f"setblock {rel(2, 0, 2)} minecraft:smithing_table",
        f"setblock {rel(0, 0, 3)} minecraft:iron_bars",
        f"setblock {rel(0, 1, 3)} minecraft:iron_bars",
    ]
    if not expedition:
        lines.append(f"setblock {rel(0, 2, -3)} minecraft:{banner}")
    return lines


def _camp_temple(banner: str) -> list[str]:
    return [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:mossy_stone_bricks",
        f"setblock {rel(0, -1, 0)} minecraft:chiseled_stone_bricks",
        f"setblock {rel(0, 0, 0)} minecraft:campfire",
        f"setblock {rel(2, 0, -2)} minecraft:sea_lantern",
        *palisade_posts("jungle_fence"),
        *twin_banners(banner),
        f"setblock {rel(0, 2, -3)} minecraft:{banner}",
        f"setblock {rel(-2, 0, 2)} minecraft:lantern",
        f"setblock {rel(-2, -1, -2)} minecraft:gold_block",
        f"setblock {rel(2, 0, 2)} minecraft:moss_carpet",
        f"setblock {rel(-1, 0, -1)} minecraft:moss_carpet",
        f"setblock {rel(1, 0, 1)} minecraft:vine",
    ]


def _camp_herd(banner: str) -> list[str]:
    return [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:coarse_dirt",
        f"setblock {rel(0, -1, 0)} minecraft:rooted_dirt",
        f"setblock {rel(0, 0, 0)} minecraft:campfire",
        f"setblock {rel(2, 0, -2)} minecraft:soul_campfire",
        *palisade_posts("dark_oak_fence"),
        *twin_banners(banner),
        f"setblock {rel(0, 0, -2)} minecraft:dark_oak_log",
        f"setblock {rel(0, 1, -2)} minecraft:dark_oak_log",
        f"setblock {rel(3, 2, 3)} minecraft:skeleton_skull",
        f"setblock {rel(-3, 2, 3)} minecraft:wither_skeleton_skull",
        f"setblock {rel(-2, 0, 2)} minecraft:bone_block",
        f"setblock {rel(2, 0, 2)} minecraft:hay_block",
    ]


def _camp_waaagh(banner: str, crag: bool) -> list[str]:
    lines = [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:coarse_dirt",
        f"setblock {rel(0, -1, 0)} minecraft:cobblestone",
        f"setblock {rel(0, 0, 0)} minecraft:campfire",
        f"setblock {rel(2, 0, -2)} minecraft:campfire",
        *palisade_posts("oak_fence"),
        *twin_banners(banner),
        f"setblock {rel(0, 2, -3)} minecraft:{banner}",
        f"setblock {rel(3, 2, 3)} minecraft:skeleton_skull",
        f"setblock {rel(-2, 0, 2)} minecraft:hay_block",
        f"setblock {rel(2, 0, 2)} minecraft:cobblestone",
        f"setblock {rel(-2, 0, -2)} minecraft:mossy_cobblestone",
    ]
    if crag:
        lines.extend(
            [
                f"setblock {rel(0, 0, 3)} minecraft:cobblestone_wall",
                f"setblock {rel(0, 1, 3)} minecraft:cobblestone_wall",
            ]
        )
    return lines


def _camp_under_empire(banner: str) -> list[str]:
    return [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:deepslate",
        f"setblock {rel(0, -1, 0)} minecraft:deepslate_tiles",
        f"setblock {rel(0, 0, 0)} minecraft:campfire",
        f"setblock {rel(2, 0, -2)} minecraft:campfire",
        *palisade_posts("cobblestone_wall"),
        *twin_banners(banner),
        f"setblock {rel(1, 0, -1)} minecraft:cobweb",
        f"setblock {rel(-1, 0, -1)} minecraft:cobweb",
        f"setblock {rel(1, 0, 1)} minecraft:cobweb",
        f"setblock {rel(-2, 0, 2)} minecraft:cobweb",
        f"setblock {rel(-2, 0, -2)} minecraft:cauldron",
        f"setblock {rel(2, 0, 2)} minecraft:iron_bars",
        f"setblock {rel(2, 1, 2)} minecraft:iron_bars",
    ]


def _camp_khorne(banner: str) -> list[str]:
    return [
        f"fill {rel(-3, -1, -3)} {rel(3, -1, 3)} minecraft:red_nether_bricks",
        f"setblock {rel(0, -1, 0)} minecraft:magma_block",
        f"setblock {rel(0, 0, 0)} minecraft:soul_campfire",
        f"setblock {rel(2, 0, -2)} minecraft:soul_campfire",
        *palisade_posts("nether_brick_fence"),
        *twin_banners(banner),
        f"setblock {rel(0, 2, -3)} minecraft:{banner}",
        f"setblock {rel(3, 2, 3)} minecraft:skeleton_skull",
        f"setblock {rel(-3, 2, 3)} minecraft:skeleton_skull",
        f"setblock {rel(3, 2, -3)} minecraft:wither_skeleton_skull",
        f"setblock {rel(-2, 0, 2)} minecraft:nether_wart_block",
        f"setblock {rel(2, 0, 2)} minecraft:blackstone",
    ]


def camp_soldiers(race_id: str, slug: str, color: str) -> list[str]:
    """1–2 named Recruits at the picket. Not a six-lord court."""
    pair = RACE_SOLDIERS.get(race_id) or RACE_SOLDIERS["empire"]
    spots = ((2, 1), (-2, 1))
    lines: list[str] = []
    for (typ, name), (x, z) in zip(pair, spots):
        name_snbt = snbt_name({"text": name, "color": color})
        lines.append(
            f"summon {typ} {rel(x, 0, z)} "
            f"{{CustomName:{name_snbt},CustomNameVisible:1b,PersistenceRequired:1b,"
            f'CanPickUpLoot:0b,Tags:["rallous.soldier","rallous.fac.{slug}"]}}'
        )
    return lines


def assert_camps_thick(race_ids: list[str] | tuple[str, ...]) -> None:
    for race_id in race_ids:
        blocks = camp_blocks(race_id, "settled", "settled", "red_banner")
        if len(blocks) < MIN_CAMP_BLOCKS:
            raise SystemExit(f"{race_id} camp too thin: {len(blocks)} setblocks (need {MIN_CAMP_BLOCKS})")
        if len(camp_soldiers(race_id, "probe", "white")) != 2:
            raise SystemExit(f"{race_id} must place exactly 2 named soldiers")
