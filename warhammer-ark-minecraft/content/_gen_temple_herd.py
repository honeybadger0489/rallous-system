#!/usr/bin/env python3
"""Generate Temple + Herd content (datapack, lang, RP, FTB chapter)."""

from __future__ import annotations

import gzip
import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DP = ROOT / "datapacks" / "rallous_temple_herd"
RP = ROOT / "resourcepacks" / "Rallous Temple Herd"
LANG = ROOT / "lang"
QUESTS = ROOT / "ftbquests" / "chapters"


def w(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text)


def dump(path: Path, data) -> None:
    w(path, json.dumps(data, indent=2, ensure_ascii=False))


# ---------------------------------------------------------------------------
# NBT (uncompressed payload, gzip-wrapped like vanilla structure files)
# ---------------------------------------------------------------------------

def _enc_str(s: str) -> bytes:
    b = s.encode("utf-8")
    return struct.pack(">H", len(b)) + b


def nbt_end() -> bytes:
    return b""


def nbt_byte(v: int) -> bytes:
    return struct.pack(">b", v)


def nbt_short(v: int) -> bytes:
    return struct.pack(">h", v)


def nbt_int(v: int) -> bytes:
    return struct.pack(">i", v)


def nbt_long(v: int) -> bytes:
    return struct.pack(">q", v)


def nbt_float(v: float) -> bytes:
    return struct.pack(">f", v)


def nbt_double(v: float) -> bytes:
    return struct.pack(">d", v)


def nbt_string(v: str) -> bytes:
    return _enc_str(v)


def nbt_list(tag_id: int, payloads: list[bytes]) -> bytes:
    return struct.pack(">b", tag_id) + struct.pack(">i", len(payloads)) + b"".join(payloads)


def nbt_compound(pairs: list[tuple[int, str, bytes]]) -> bytes:
    out = bytearray()
    for tag_id, name, payload in pairs:
        out.append(tag_id)
        out += _enc_str(name)
        out += payload
    out.append(0)
    return bytes(out)


def nbt_named_compound(name: str, pairs: list[tuple[int, str, bytes]]) -> bytes:
    return bytes([10]) + _enc_str(name) + nbt_compound(pairs)[0:]  # compound already ends


# tag ids
T_BYTE, T_SHORT, T_INT, T_LONG = 1, 2, 3, 4
T_FLOAT, T_DOUBLE, T_BYTE_A, T_STR = 5, 6, 7, 8
T_LIST, T_COMP, T_INT_A = 9, 10, 11


def write_structure(path: Path, size, palette, blocks, entities) -> None:
    pal_payloads = []
    for entry in palette:
        pairs = [(T_STR, "Name", nbt_string(entry["Name"]))]
        if "Properties" in entry:
            props = [(T_STR, k, nbt_string(v)) for k, v in entry["Properties"].items()]
            pairs.append((T_COMP, "Properties", nbt_compound(props)))
        pal_payloads.append(nbt_compound(pairs))

    block_payloads = []
    for b in blocks:
        pairs = [
            (T_LIST, "pos", nbt_list(T_INT, [nbt_int(i) for i in b["pos"]])),
            (T_INT, "state", nbt_int(b["state"])),
        ]
        if "nbt" in b:
            pairs.append((T_COMP, "nbt", b["nbt"]))
        block_payloads.append(nbt_compound(pairs))

    ent_payloads = []
    for e in entities:
        pairs = [
            (T_LIST, "pos", nbt_list(T_DOUBLE, [nbt_double(x) for x in e["pos"]])),
            (T_LIST, "blockPos", nbt_list(T_INT, [nbt_int(i) for i in e["blockPos"]])),
            (T_COMP, "nbt", e["nbt"]),
        ]
        ent_payloads.append(nbt_compound(pairs))

    root = nbt_named_compound(
        "",
        [
            (T_INT, "DataVersion", nbt_int(3465)),
            (T_LIST, "size", nbt_list(T_INT, [nbt_int(i) for i in size])),
            (T_LIST, "palette", nbt_list(T_COMP, pal_payloads)),
            (T_LIST, "blocks", nbt_list(T_COMP, block_payloads)),
            (T_LIST, "entities", nbt_list(T_COMP, ent_payloads)),
        ],
    )
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(root, mtime=0))


def chest_nbt(loot: str) -> bytes:
    return nbt_compound(
        [
            (T_STR, "id", nbt_string("minecraft:chest")),
            (T_STR, "LootTable", nbt_string(loot)),
        ]
    )


def banner_be(color: str) -> bytes:
    return nbt_compound(
        [
            (T_STR, "id", nbt_string("minecraft:banner")),
        ]
    )


def stand_nbt(name: str, color: str, tags: list[str], head_item: str) -> bytes:
    tag_list = nbt_list(T_STR, [nbt_string(t) for t in tags])
    armor = []
    for item_id in ("minecraft:air", "minecraft:air", "minecraft:air", head_item):
        armor.append(
            nbt_compound(
                [
                    (T_STR, "id", nbt_string(item_id)),
                    (T_BYTE, "Count", nbt_byte(1 if item_id != "minecraft:air" else 0)),
                ]
            )
        )
    return nbt_compound(
        [
            (T_STR, "id", nbt_string("minecraft:armor_stand")),
            (T_STR, "CustomName", nbt_string(json.dumps({"text": name, "color": color}))),
            (T_BYTE, "CustomNameVisible", nbt_byte(1)),
            (T_BYTE, "NoGravity", nbt_byte(1)),
            (T_BYTE, "PersistenceRequired", nbt_byte(1)),
            (T_BYTE, "Invulnerable", nbt_byte(1)),
            (T_BYTE, "ShowArms", nbt_byte(1)),
            (T_LIST, "Tags", tag_list),
            (T_LIST, "ArmorItems", nbt_list(T_COMP, armor)),
        ]
    )


def build_platform(palette_index_fn, blocks, sx, sz, y, default_state):
    for x in range(sx):
        for z in range(sz):
            blocks.append({"pos": [x, y, z], "state": default_state})


def make_temple_nbt(path: Path) -> None:
    import sys

    sys.path.insert(0, str(DP))
    import build_sites

    build_sites.make_temple_nbt(path, gen=sys.modules[__name__])


def make_herd_nbt(path: Path) -> None:
    import sys

    sys.path.insert(0, str(DP))
    import build_sites

    build_sites.make_herd_nbt(path, gen=sys.modules[__name__])


# ---------------------------------------------------------------------------
# Lang
# ---------------------------------------------------------------------------

FOSSIL_LANG = {
    "item.fossil.fossil_bio": "Temple-Beast Fossil",
    "item.fossil.fossil_shale": "Shale Temple Fossil",
    "item.fossil.fossil_tar": "Tar Temple Fossil",
    "item.fossil.fossil_plant": "Plant Relic",
    "item.fossil.dinopedia": "Temple-Beast Codex",
    "item.fossil.scarab_gem": "Temple Scarab",
    "item.fossil.scarab_gem_aquatic": "Aquatic Temple Scarab",
    "item.fossil.whip": "Temple Crook",
    "item.fossil.dna": "Temple-Beast Blood",
    "item.fossil.egg": "Temple-Beast Egg",
    "item.fossil.embryo": "Temple-Beast Embryo",
    "item.fossil.bio_goo": "Spawning Ichor",
    "item.fossil.failuresaurus_flesh": "Broken-Beast Offal",
    "item.fossil.essence_stunted": "Broken Growth",
    "item.fossil.frozen_meat": "Herd Carrion",
    "item.fossil.skull_stick": "Herd-Goad Skull",
    "block.fossil.culture_vat": "Spawning Pool",
    "block.fossil.analyzer": "Relic Analyzer",
    "container.fossil.culture_vat": "Spawning Pool",
    "container.fossil.analyzer": "Relic Analyzer",
    "entity.fossil.failuresaurus": "Broken Beast",
    "entity.fossil.prehistoric.tamed": "This %s is loyal to the temple",
    "entity.fossil.order.follow": "%s follows the temple",
    "entity.fossil.order.stay": "%s holds the temple line",
    "entity.fossil.order.wander": "%s patrols for the temple",
    "itemGroup.fossil.fa_mob_item_tab": "Temple-Beasts",
    "advancements.fossil.culture_vat.title": "The Spawning Pool",
    "advancements.fossil.culture_vat.description": "Restore a temple-beast from blood. Fossils stay the engine.",
    "advancements.fossil.scarab_tame.title": "Loyal Temple-Beast",
    "advancements.fossil.scarab_tame.description": "A large predator that chose you. Not a broken herd-slave.",
    "advancements.fossil.dinopedia.title": "Read the Codex",
    "fossil.midnightconfig.whipToTameDino": "Crook To Tame Temple-Beast",
}

TB_LANG = {
    "entity.tameablebeasts.crested_gecko.temperate": "Temple Gecko",
    "entity.tameablebeasts.crested_gecko.warm": "Temple Gecko (Warm)",
    "entity.tameablebeasts.crested_gecko.cold": "Temple Gecko (Pale)",
    "entity.tameablebeasts.quetzalcoatlus.temperate": "Temple Quetzal",
    "entity.tameablebeasts.quetzalcoatlus.warm": "Temple Quetzal (Warm)",
    "entity.tameablebeasts.quetzalcoatlus.cold": "Temple Quetzal (Cold)",
    "entity.tameablebeasts.graptera.temperate": "Temple Graptera",
    "entity.tameablebeasts.graptera.warm": "Temple Graptera (Black)",
    "entity.tameablebeasts.graptera.cold": "Temple Graptera (Blue)",
    "entity.tameablebeasts.tameable_chikote.temperate": "Hauler-Bird",
    "entity.tameablebeasts.tameable_chikote.cold": "Woolly Hauler-Bird",
    "entity.tameablebeasts.tameable_chikote.awrm": "Hauler-Bird Runner",
    "entity.tameablebeasts.argentavis.temperate": "Sky-Hauler",
    "entity.tameablebeasts.argentavis.warm": "Sky-Hauler (Black)",
    "entity.tameablebeasts.argentavis.cold": "Sky-Hauler (White)",
    "entity.tameablebeasts.tameable_racoon.temperate": "Enslaved Herd-Mutt",
    "entity.tameablebeasts.tameable_racoon.warm": "Enslaved Herd-Mutt (Coati)",
    "entity.tameablebeasts.tameable_racoon.cold": "Enslaved Herd-Mutt (Dog)",
    "entity.tameablebeasts.giant_roly_poly.temperate": "Broken Rolling-Beast",
    "entity.tameablebeasts.giant_roly_poly.warm": "Broken Rolling-Beast (Warm)",
    "entity.tameablebeasts.giant_roly_poly.cold": "Broken Rolling-Beast (Cold)",
    "item.tameablebeasts.pteranodon_meal": "Temple Flyer Meal",
    "item.tameablebeasts.pteranodon_meal.tooltip": "Temple offering for flyers. Same engine — more foods now count.",
    "item.tameablebeasts.big_bird_bait": "Temple-Beast Bait",
    "item.tameablebeasts.big_bird_bait.tooltip": "Haul and travel. Temple-Spawn add common seed and meat as offerings.",
    "item.tameablebeasts.ptera_meal_arrow": "Temple Flyer Arrow",
    "item.tameablebeasts.bird_bait_arrow": "Temple-Beast Arrow",
    "item.tameablebeasts.racoon_fur": "Herd-Mutt Hide",
    "item.tameablebeasts.bug_salad": "Temple Bug-Offering",
    "advancements.tameablebeasts.root": "Temple and Herd",
    "advancements.tameablebeasts.root.description": "Loyal temple-beasts haul, fight, travel, tank. Horned Woods break what they steal.",
    "advancements.tameablebeasts.crested_gecko": "Temple Gecko",
    "advancements.tameablebeasts.quetzalcoatlus": "Temple Quetzal",
    "advancements.tameablebeasts.racoon": "A Broken Herd-Mutt",
}

OURS_LANG = {
    "advancements.rallous_temple_herd.root.title": "Temple and Herd",
    "advancements.rallous_temple_herd.root.description": "Fossils and Tameable Beasts stay the engine.",
    "advancements.rallous_temple_herd.lizardmen.warm_canopy.title": "Warm Canopy",
    "advancements.rallous_temple_herd.lizardmen.warm_canopy.description": "Jungle or warm land. Temple-Spawn markers live here — not silent dinos.",
    "advancements.rallous_temple_herd.lizardmen.temple_marker.title": "Temple Marker",
    "advancements.rallous_temple_herd.lizardmen.temple_marker.description": "Lime banners and a named stand. The temple negotiates by omen.",
    "advancements.rallous_temple_herd.lizardmen.loyal_beast.title": "Loyal Temple-Beast",
    "advancements.rallous_temple_herd.lizardmen.loyal_beast.description": "You earned a living creature. Haul, fight, travel, or tank.",
    "advancements.rallous_temple_herd.beastmen.horned_woods.title": "Horned Woods",
    "advancements.rallous_temple_herd.beastmen.horned_woods.description": "Dark forest or taiga. Herdstones, not towns.",
    "advancements.rallous_temple_herd.beastmen.herdstone.title": "Herdstone",
    "advancements.rallous_temple_herd.beastmen.herdstone.description": "Skull banners and a hung stand. The herd enslaves what it cannot hear.",
    "advancements.rallous_temple_herd.beastmen.broken_beast.title": "Broken Beast",
    "advancements.rallous_temple_herd.beastmen.broken_beast.description": "Carrion, a lead, offal. This is a slave, not a companion.",
    "advancements.rallous_temple_herd.other_races.worse_hands.title": "Worse Hands",
    "advancements.rallous_temple_herd.other_races.worse_hands.description": "Empire, Dawi, Kislev, dead, and greenskins use beasts as livestock or engines. They do not hear the temple.",
}


def optional_biome(biome_id: str) -> dict:
    if biome_id.startswith("terralith:"):
        return {"id": biome_id, "required": False}
    return biome_id


def biome_tag(values: list[str]) -> dict:
    return {"replace": False, "values": [optional_biome(v) if isinstance(v, str) else v for v in values]}


def item_tag_extra(items: list[str]) -> dict:
    return {"replace": False, "values": items}


def adv_display(icon: str, title: str, desc: str, frame: str = "task", background: str | None = None, hidden: bool = False) -> dict:
    d = {
        "icon": {"item": icon},
        "title": {"translate": title} if title.startswith("advancements.") else {"text": title},
        "description": {"translate": desc} if desc.startswith("advancements.") else {"text": desc},
        "frame": frame,
        "show_toast": True,
        "announce_to_chat": True,
        "hidden": hidden,
    }
    if background:
        d["background"] = background
    return d


def inventory_items(item_ids: list[str]) -> dict:
    return {
        "trigger": "minecraft:inventory_changed",
        "conditions": {"items": [{"items": item_ids}]},
    }


def write_datapack() -> None:
    dump(
        DP / "pack.mcmeta",
        {"pack": {"pack_format": 15, "description": "Rallous Temple Herd — Lizardmen / Beastmen / Ark glue"}},
    )
    w(
        DP / "META-INF/mods.toml",
        "\n".join(
            [
                'modLoader="lowcodefml"',
                'loaderVersion="[47,)"',
                'license="All Rights Reserved"',
                "",
                "[[mods]]",
                'modId="rallous_temple_herd"',
                'version="1.0.0"',
                'displayName="Rallous Temple Herd"',
                'authors="Rallous System"',
                'description="""Lizardmen / Beastmen / Ark creature glue. Fossils + Tameable Beasts stay the engine."""',
                "",
            ]
        ),
    )
    w(
        DP / "README.md",
        "\n".join(
            [
                "# Rallous Temple Herd",
                "Fossils + Tameable Beasts stay the engine (haul / fight / travel / tank). No new creature mods. No 40k.",
                "Lizardmen own the jungle walk: a 13×13 mossy courtyard, a 5×5 spawning-pool pit, lime banners, named stands, temple-cache chests.",
                "Beastmen own the taiga walk: a 5×5 soul pit and a 5-high herdstone, skull banners, named stands, uglier cache (Broken Collar).",
                "Tame rolls stay global. Fossils 9.3.4 has no per-faction tame tag — only `whipToTameDino` (we do not flip it). Extra TB tame-food tags apply to everyone.",
                "Other races: Worse Hands book + advancement if you already have `rallous.old_world`. No hidden tame penalty.",
                "`/locate structure rallous_temple_herd:temple_marker` in jungle / warm. `/locate structure rallous_temple_herd:herdstone` in taiga / dark forest.",
                "Pickup: this folder → world `datapacks/`. RP `Rallous Temple Herd` or `content/lang`. FTB `temple_and_herd.snbt` → `config/ftbquests/quests/chapters/`.",
                "Place by hand: `/function rallous_temple_herd:place_temple_marker` / `place_herdstone`.",
                "Honest gap: we cannot make only Lizardmen players roll easier Fossils tames without a new mod or KubeJS.",
            ]
        ),
    )

    dump(DP / "data/minecraft/tags/functions/load.json", {"values": ["rallous_temple_herd:load"]})
    dump(DP / "data/minecraft/tags/functions/tick.json", {"values": ["rallous_temple_herd:tick"]})

    w(
        DP / "data/rallous_temple_herd/functions/load.mcfunction",
        "\n".join(
            [
                "# Temple and Herd scoreboards. No chat spam on /reload.",
                "scoreboard objectives add rallous.temple dummy",
                "scoreboard objectives add rallous.herd dummy",
                "scoreboard objectives add rallous.beast dummy",
            ]
        ),
    )
    w(
        DP / "data/rallous_temple_herd/functions/tick.mcfunction",
        "\n".join(
            [
                "execute as @a at @s if biome ~ ~ ~ #rallous_temple_herd:temple_jungles run function rallous_temple_herd:enter_temple_biome",
                "execute as @a at @s if biome ~ ~ ~ #rallous_temple_herd:horned_woods run function rallous_temple_herd:enter_herd_biome",
                "execute as @a at @s if entity @e[type=minecraft:armor_stand,tag=rallous.temple_marker,distance=..8] run advancement grant @s only rallous_temple_herd:lizardmen/temple_marker",
                "execute as @a at @s if entity @e[type=minecraft:armor_stand,tag=rallous.herdstone,distance=..8] run advancement grant @s only rallous_temple_herd:beastmen/herdstone",
                "execute as @a at @s if entity @e[tag=rallous.roam.herd,distance=..16] run advancement grant @s only rallous_temple_herd:beastmen/horned_woods",
            ]
        ),
    )
    w(
        DP / "data/rallous_temple_herd/functions/enter_temple_biome.mcfunction",
        "\n".join(
            [
                "advancement grant @s only rallous_temple_herd:lizardmen/warm_canopy",
                "execute unless entity @s[tag=rallous.temple_primer] run function rallous_temple_herd:give_temple_primer",
                "execute unless entity @s[tag=rallous.temple_primer] if entity @s[tag=rallous.old_world] run function rallous_temple_herd:give_lesser_bond",
                "tag @s add rallous.temple_primer",
            ]
        ),
    )
    w(
        DP / "data/rallous_temple_herd/functions/enter_herd_biome.mcfunction",
        "\n".join(
            [
                "advancement grant @s only rallous_temple_herd:beastmen/horned_woods",
                "execute unless entity @s[tag=rallous.herd_primer] run function rallous_temple_herd:give_herd_primer",
                "tag @s add rallous.herd_primer",
            ]
        ),
    )

    temple_pages = [
        '{"text":"Temple-Spawn. The jungle is not empty dinos. Fossils and Tameable Beasts are the engine: haul, fight, travel, tank."}',
        '{"text":"A living beast that hatches near you, or takes a Temple Scarab, is loyal. We cannot make the vat roll easier for one race. Extra Tameable Beasts offerings (honey, cooked meat, seeds) are the only easier-tame hook."}',
        '{"text":"Look for a mossy courtyard and a glowing spawning-pool pit. Lime banners, named stands, caches. /locate structure rallous_temple_herd:temple_marker"}',
        '{"text":"Empire, Dawi, Kislev, the dead, and greenskins are worse at this. They treat a temple-beast as a horse with teeth."}',
    ]
    herd_pages = [
        '{"text":"Horned Woods. No town. A herdstone is a stone rising from a soul pit, skulls, red and black banners, and a hung stand. The herd does not tame. It enslaves."}',
        '{"text":"Uglier loot: offal, carrion, a Broken Collar (lead). Failuresaurus is a Broken Beast. Rotten flesh and bone now count as herd-mutt / rolling-beast offerings."}',
        '{"text":"/locate structure rallous_temple_herd:herdstone  — dark forest and taiga, including Terralith belts."}',
        '{"text":"Same engine as the temple. The difference is the relationship: loyal companion versus broken slave."}',
    ]
    worse_pages = [
        '{"text":"You are not Temple-Spawn. The vat still works. The bond is thinner. Other races use beasts as livestock, siege engines, or food."}',
        '{"text":"This is framing, not a hidden penalty. Fossils does not read a race tag. Tick Worse Hands when you have read this."}',
    ]

    def book(title: str, author: str, pages: list[str]) -> str:
        joined = ",".join(f"'{p}'" for p in pages)
        return f'give @s minecraft:written_book{{title:"{title}",author:"{author}",pages:[{joined}]}} 1'

    w(
        DP / "data/rallous_temple_herd/functions/give_temple_primer.mcfunction",
        "\n".join(
            [
                book("Temple-Beast Primer", "Temple-Spawn", temple_pages),
                "scoreboard players add @s rallous.temple 1",
                "advancement grant @s only rallous_temple_herd:lizardmen/warm_canopy",
            ]
        ),
    )
    w(
        DP / "data/rallous_temple_herd/functions/give_herd_primer.mcfunction",
        "\n".join(
            [
                book("Herdstone Rite", "Horned Woods", herd_pages),
                "scoreboard players add @s rallous.herd 1",
                "advancement grant @s only rallous_temple_herd:beastmen/horned_woods",
            ]
        ),
    )
    w(
        DP / "data/rallous_temple_herd/functions/give_lesser_bond.mcfunction",
        "\n".join(
            [
                book("Worse Hands", "A Reikland Sergeant", worse_pages),
                "advancement grant @s only rallous_temple_herd:other_races/worse_hands",
            ]
        ),
    )

    # 13x13 courtyard / herdstone pit live in the .mcfunction files. Do not thin them.
    for _place in ("place_temple_marker", "place_herdstone"):
        _p = DP / f"data/rallous_temple_herd/functions/{_place}.mcfunction"
        if "13x13" not in _p.read_text():
            raise SystemExit(f"{_place} is thin; thicken the courtyard/pit, do not regen a 7x7 pad")

    # Advancements
    dump(
        DP / "data/rallous_temple_herd/advancements/root.json",
        {
            "display": adv_display(
                "minecraft:bone",
                "advancements.rallous_temple_herd.root.title",
                "advancements.rallous_temple_herd.root.description",
                "challenge",
                "minecraft:textures/block/mossy_cobblestone.png",
            ),
            "criteria": {"joined": {"trigger": "minecraft:tick"}},
            "requirements": [["joined"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/lizardmen/warm_canopy.json",
        {
            "parent": "rallous_temple_herd:root",
            "display": adv_display(
                "minecraft:jungle_sapling",
                "advancements.rallous_temple_herd.lizardmen.warm_canopy.title",
                "advancements.rallous_temple_herd.lizardmen.warm_canopy.description",
            ),
            "criteria": {"entered": {"trigger": "minecraft:impossible"}},
            "requirements": [["entered"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/lizardmen/temple_marker.json",
        {
            "parent": "rallous_temple_herd:lizardmen/warm_canopy",
            "display": adv_display(
                "minecraft:lime_banner",
                "advancements.rallous_temple_herd.lizardmen.temple_marker.title",
                "advancements.rallous_temple_herd.lizardmen.temple_marker.description",
                "goal",
            ),
            "criteria": {
                "near_stand": {"trigger": "minecraft:impossible"},
                "in_structure": {
                    "trigger": "minecraft:location",
                    "conditions": {
                        "player": [
                            {
                                "condition": "minecraft:entity_properties",
                                "entity": "this",
                                "predicate": {"location": {"structure": "rallous_temple_herd:temple_marker"}},
                            }
                        ]
                    },
                },
            },
            "requirements": [["near_stand", "in_structure"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/lizardmen/loyal_beast.json",
        {
            "parent": "rallous_temple_herd:lizardmen/temple_marker",
            "display": adv_display(
                "minecraft:saddle",
                "advancements.rallous_temple_herd.lizardmen.loyal_beast.title",
                "advancements.rallous_temple_herd.lizardmen.loyal_beast.description",
                "challenge",
            ),
            "criteria": {
                "dinopedia": inventory_items(["fossil:dinopedia"]),
                "scarab": inventory_items(["fossil:scarab_gem"]),
                "egg": inventory_items(["fossil:egg_item_triceratops"]),
                "fossil_bio": inventory_items(["fossil:fossil_bio"]),
                "ptera_meal": inventory_items(["tameablebeasts:pteranodon_meal"]),
                "bird_bait": inventory_items(["tameablebeasts:big_bird_bait"]),
                "bug_salad": inventory_items(["tameablebeasts:bug_salad"]),
                "saddle": inventory_items(["minecraft:saddle"]),
            },
            "requirements": [["dinopedia", "scarab", "egg", "fossil_bio", "ptera_meal", "bird_bait", "bug_salad", "saddle"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/beastmen/horned_woods.json",
        {
            "parent": "rallous_temple_herd:root",
            "display": adv_display(
                "minecraft:dark_oak_sapling",
                "advancements.rallous_temple_herd.beastmen.horned_woods.title",
                "advancements.rallous_temple_herd.beastmen.horned_woods.description",
            ),
            "criteria": {"entered": {"trigger": "minecraft:impossible"}},
            "requirements": [["entered"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/beastmen/herdstone.json",
        {
            "parent": "rallous_temple_herd:beastmen/horned_woods",
            "display": adv_display(
                "minecraft:wither_skeleton_skull",
                "advancements.rallous_temple_herd.beastmen.herdstone.title",
                "advancements.rallous_temple_herd.beastmen.herdstone.description",
                "goal",
            ),
            "criteria": {
                "near_stand": {"trigger": "minecraft:impossible"},
                "in_structure": {
                    "trigger": "minecraft:location",
                    "conditions": {
                        "player": [
                            {
                                "condition": "minecraft:entity_properties",
                                "entity": "this",
                                "predicate": {"location": {"structure": "rallous_temple_herd:herdstone"}},
                            }
                        ]
                    },
                },
            },
            "requirements": [["near_stand", "in_structure"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/beastmen/broken_beast.json",
        {
            "parent": "rallous_temple_herd:beastmen/herdstone",
            "display": adv_display(
                "minecraft:lead",
                "advancements.rallous_temple_herd.beastmen.broken_beast.title",
                "advancements.rallous_temple_herd.beastmen.broken_beast.description",
                "challenge",
            ),
            "criteria": {
                "offal": inventory_items(["fossil:failuresaurus_flesh", "fossil:essence_stunted", "fossil:frozen_meat"]),
                "collar": inventory_items(["minecraft:lead"]),
                "carrion": inventory_items(["minecraft:rotten_flesh"]),
            },
            "requirements": [["offal", "collar", "carrion"]],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/advancements/other_races/worse_hands.json",
        {
            "parent": "rallous_temple_herd:root",
            "display": adv_display(
                "minecraft:iron_horse_armor",
                "advancements.rallous_temple_herd.other_races.worse_hands.title",
                "advancements.rallous_temple_herd.other_races.worse_hands.description",
            ),
            "criteria": {
                "book": {
                    "trigger": "minecraft:inventory_changed",
                    "conditions": {"items": [{"items": ["minecraft:written_book"], "nbt": '{title:"Worse Hands"}'}]},
                },
                "granted": {"trigger": "minecraft:impossible"},
            },
            "requirements": [["book", "granted"]],
        },
    )

    # Biome tags
    dump(
        DP / "data/rallous_temple_herd/tags/worldgen/biome/temple_jungles.json",
        biome_tag(
            [
                "#minecraft:is_jungle",
                "#minecraft:is_savanna",
                "minecraft:sparse_jungle",
                "minecraft:bamboo_jungle",
                "terralith:tropical_jungle",
                "terralith:jungle_mountains",
                "terralith:rocky_jungle",
                "terralith:amethyst_rainforest",
                "terralith:amethyst_canyon",
                "terralith:desert_oasis",
                "terralith:red_oasis",
                "terralith:orchid_swamp",
                "terralith:skylands_summer",
                "terralith:cave/underground_jungle",
                "terralith:lush_desert",
                "terralith:hot_shrubland",
                "terralith:brushland",
                "terralith:ashen_savanna",
                "terralith:arid_highlands",
                "terralith:savanna_slopes",
                "terralith:fractured_savanna",
            ]
        ),
    )
    dump(
        DP / "data/rallous_temple_herd/tags/worldgen/biome/horned_woods.json",
        biome_tag(
            [
                "#minecraft:is_taiga",
                "minecraft:dark_forest",
                "minecraft:old_growth_pine_taiga",
                "minecraft:old_growth_spruce_taiga",
                "minecraft:snowy_taiga",
                "terralith:moonlight_grove",
                "terralith:moonlight_valley",
                "terralith:cloud_forest",
                "terralith:siberian_taiga",
                "terralith:siberian_grove",
                "terralith:forested_highlands",
                "terralith:wintry_forest",
                "terralith:wintry_lowlands",
                "terralith:alpine_grove",
                "terralith:alpine_highlands",
                "terralith:shield",
                "terralith:snowy_shield",
                "terralith:yosemite_lowlands",
                "terralith:birch_taiga",
                "terralith:haze_mountain",
            ]
        ),
    )

    # Entity tags (documentation + future quest filters; Fossils does not read these for tame chance)
    dump(
        DP / "data/rallous_temple_herd/tags/entity_types/temple_beasts.json",
        {
            "replace": False,
            "values": [
                {"id": "fossil:triceratops", "required": False},
                {"id": "fossil:stegosaurus", "required": False},
                {"id": "fossil:ankylosaurus", "required": False},
                {"id": "fossil:parasaurolophus", "required": False},
                {"id": "fossil:gallimimus", "required": False},
                {"id": "fossil:velociraptor", "required": False},
                {"id": "fossil:deinonychus", "required": False},
                {"id": "fossil:dilophosaurus", "required": False},
                {"id": "fossil:spinosaurus", "required": False},
                {"id": "fossil:tyrannosaurus", "required": False},
                {"id": "fossil:pteranodon", "required": False},
                {"id": "fossil:quetzalcoatlus", "required": False},
                {"id": "fossil:sarcosuchus", "required": False},
                {"id": "fossil:brachiosaurus", "required": False},
                {"id": "fossil:diplodocus", "required": False},
                {"id": "tameablebeasts:crested_gecko", "required": False},
                {"id": "tameablebeasts:quetzalcoatlus", "required": False},
                {"id": "tameablebeasts:graptera", "required": False},
                {"id": "tameablebeasts:tameable_beetle", "required": False},
                {"id": "tameablebeasts:ground_beetle", "required": False},
                {"id": "tameablebeasts:argentavis", "required": False},
                {"id": "tameablebeasts:tameable_chikote", "required": False},
            ],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/tags/entity_types/herd_beasts.json",
        {
            "replace": False,
            "values": [
                {"id": "tameablebeasts:tameable_racoon", "required": False},
                {"id": "tameablebeasts:giant_roly_poly", "required": False},
                {"id": "tameablebeasts:giant_grasshopper", "required": False},
                {"id": "fossil:smilodon", "required": False},
                {"id": "fossil:megaloceros", "required": False},
                {"id": "fossil:elasmotherium", "required": False},
            ],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/tags/entity_types/broken_beasts.json",
        {
            "replace": False,
            "values": [
                {"id": "fossil:failuresaurus", "required": False},
            ],
        },
    )

    dump(
        DP / "data/rallous_temple_herd/tags/items/temple_offerings.json",
        item_tag_extra(
            [
                "minecraft:honey_bottle",
                "minecraft:cooked_chicken",
                "minecraft:cooked_cod",
                "minecraft:tropical_fish",
                "minecraft:wheat_seeds",
                "minecraft:melon_slice",
                "minecraft:glow_berries",
                "minecraft:sweet_berries",
                "minecraft:carrot",
                "minecraft:wheat",
                {"id": "tameablebeasts:pteranodon_meal", "required": False},
                {"id": "tameablebeasts:big_bird_bait", "required": False},
                {"id": "tameablebeasts:bug_salad", "required": False},
                {"id": "fossil:scarab_gem", "required": False},
            ]
        ),
    )
    dump(
        DP / "data/rallous_temple_herd/tags/items/herd_uglier_loot.json",
        item_tag_extra(
            [
                "minecraft:rotten_flesh",
                "minecraft:bone",
                "minecraft:lead",
                "minecraft:spider_eye",
                "minecraft:leather",
                "minecraft:skeleton_skull",
                {"id": "fossil:failuresaurus_flesh", "required": False},
                {"id": "fossil:frozen_meat", "required": False},
                {"id": "fossil:essence_stunted", "required": False},
            ]
        ),
    )

    # TB tame-food extras (mechanical, global)
    extras = {
        "quetzal_tame_food": ["minecraft:cooked_chicken", "minecraft:cooked_cod", "minecraft:tropical_fish"],
        "graptera_tame_food": ["minecraft:cooked_chicken", "minecraft:tropical_fish"],
        "argentavis_tame_food": ["minecraft:cooked_chicken", "minecraft:wheat_seeds"],
        "chikote_tame_food": ["minecraft:wheat", "minecraft:carrot"],
        "crested_gecko_tame_food": ["minecraft:honey_bottle", "minecraft:glow_berries"],
        "shiny_beetle_tame_food": ["minecraft:honey_block", "minecraft:sweet_berries"],
        "ground_beetle_tame_food": ["minecraft:honey_block", "minecraft:sweet_berries"],
        "grasshopper_tame_food": ["minecraft:wheat", "minecraft:melon_slice"],
        "racoon_tame_food": ["minecraft:rotten_flesh", "minecraft:bone", "minecraft:spider_eye"],
        "roly_poly_tame_food": ["minecraft:rotten_flesh", "minecraft:bone"],
    }
    for name, items in extras.items():
        dump(DP / f"data/tameablebeasts/tags/items/{name}.json", item_tag_extra(items))

    # Loot
    dump(
        DP / "data/rallous_temple_herd/loot_tables/chests/temple_cache.json",
        {
            "type": "minecraft:chest",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": "minecraft:written_book",
                            "functions": [
                                {
                                    "function": "minecraft:set_nbt",
                                    "tag": '{title:"Temple-Beast Primer",author:"Temple-Spawn",pages:[\'{"text":"Lime banners. Loyal beasts. Fossils stay the engine."}\']}',
                                }
                            ],
                        }
                    ],
                },
                {
                    "rolls": {"min": 3, "max": 6},
                    "entries": [
                        {"type": "minecraft:item", "name": "minecraft:gold_ingot", "weight": 8, "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 4}}]},
                        {"type": "minecraft:item", "name": "minecraft:emerald", "weight": 6, "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 3}}]},
                        {"type": "minecraft:item", "name": "minecraft:bone", "weight": 10, "functions": [{"function": "minecraft:set_count", "count": {"min": 2, "max": 6}}]},
                        {"type": "minecraft:item", "name": "minecraft:honey_bottle", "weight": 6},
                        {"type": "minecraft:item", "name": "minecraft:lime_banner", "weight": 3},
                        {"type": "minecraft:item", "name": "minecraft:saddle", "weight": 2},
                        {"type": "minecraft:item", "name": "minecraft:cooked_chicken", "weight": 8, "functions": [{"function": "minecraft:set_count", "count": {"min": 2, "max": 5}}]},
                        {"type": "minecraft:item", "name": "fossil:fossil_bio", "weight": 4, "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 2}}]},
                        {"type": "minecraft:item", "name": "fossil:dinopedia", "weight": 2},
                        {"type": "minecraft:item", "name": "fossil:scarab_gem", "weight": 1},
                    ],
                },
            ],
        },
    )
    dump(
        DP / "data/rallous_temple_herd/loot_tables/chests/herdstone_cache.json",
        {
            "type": "minecraft:chest",
            "pools": [
                {
                    "rolls": 1,
                    "entries": [
                        {
                            "type": "minecraft:item",
                            "name": "minecraft:lead",
                            "functions": [
                                {
                                    "function": "minecraft:set_name",
                                    "name": {"text": "Broken Collar", "color": "dark_red", "italic": False},
                                },
                                {
                                    "function": "minecraft:set_lore",
                                    "lore": [{"text": "The herd does not ask.", "color": "gray"}],
                                },
                            ],
                        }
                    ],
                },
                {
                    "rolls": {"min": 4, "max": 7},
                    "entries": [
                        {"type": "minecraft:item", "name": "minecraft:rotten_flesh", "weight": 12, "functions": [{"function": "minecraft:set_count", "count": {"min": 3, "max": 8}}]},
                        {"type": "minecraft:item", "name": "minecraft:bone", "weight": 10, "functions": [{"function": "minecraft:set_count", "count": {"min": 2, "max": 6}}]},
                        {"type": "minecraft:item", "name": "minecraft:leather", "weight": 6, "functions": [{"function": "minecraft:set_count", "count": {"min": 1, "max": 3}}]},
                        {"type": "minecraft:item", "name": "minecraft:spider_eye", "weight": 6},
                        {"type": "minecraft:item", "name": "minecraft:skeleton_skull", "weight": 2},
                        {"type": "minecraft:item", "name": "minecraft:red_banner", "weight": 3},
                        {"type": "minecraft:item", "name": "minecraft:black_banner", "weight": 3},
                        {"type": "minecraft:item", "name": "minecraft:coal", "weight": 6, "functions": [{"function": "minecraft:set_count", "count": {"min": 2, "max": 5}}]},
                        {"type": "minecraft:item", "name": "fossil:failuresaurus_flesh", "weight": 3},
                        {"type": "minecraft:item", "name": "fossil:frozen_meat", "weight": 3},
                    ],
                },
            ],
        },
    )

    def jigsaw(biome_tag_name: str, pool: str) -> dict:
        return {
            "type": "minecraft:jigsaw",
            "biomes": biome_tag_name,
            "step": "surface_structures",
            "spawn_overrides": {},
            "terrain_adaptation": "beard_thin",
            "start_pool": pool,
            "size": 1,
            "start_height": {"absolute": -1},
            "project_start_to_heightmap": "WORLD_SURFACE_WG",
            "max_distance_from_center": 16,
            "use_expansion_hack": False,
        }

    def pool(name: str, loc: str) -> dict:
        return {
            "fallback": "minecraft:empty",
            "elements": [
                {
                    "weight": 1,
                    "element": {
                        "element_type": "minecraft:single_pool_element",
                        "location": loc,
                        "projection": "rigid",
                        "processors": "minecraft:empty",
                    },
                }
            ],
        }

    dump(DP / "data/rallous_temple_herd/worldgen/structure/temple_marker.json", jigsaw("#rallous_temple_herd:temple_jungles", "rallous_temple_herd:temple_marker"))
    dump(DP / "data/rallous_temple_herd/worldgen/structure/herdstone.json", jigsaw("#rallous_temple_herd:horned_woods", "rallous_temple_herd:herdstone"))
    dump(DP / "data/rallous_temple_herd/worldgen/template_pool/temple_marker.json", pool("rallous_temple_herd:temple_marker", "rallous_temple_herd:temple_marker"))
    dump(DP / "data/rallous_temple_herd/worldgen/template_pool/herdstone.json", pool("rallous_temple_herd:herdstone", "rallous_temple_herd:herdstone"))
    dump(
        DP / "data/rallous_temple_herd/worldgen/structure_set/temple_markers.json",
        {
            "structures": [{"structure": "rallous_temple_herd:temple_marker", "weight": 1}],
            "placement": {"type": "minecraft:random_spread", "salt": 18472011, "spacing": 20, "separation": 8},
        },
    )
    dump(
        DP / "data/rallous_temple_herd/worldgen/structure_set/herdstones.json",
        {
            "structures": [{"structure": "rallous_temple_herd:herdstone", "weight": 1}],
            "placement": {"type": "minecraft:random_spread", "salt": 18472027, "spacing": 20, "separation": 8},
        },
    )
    dump(
        DP / "data/rallous_temple_herd/tags/worldgen/structure/markers.json",
        {"values": ["rallous_temple_herd:temple_marker", "rallous_temple_herd:herdstone"]},
    )

    make_temple_nbt(DP / "data/rallous_temple_herd/structures/temple_marker.nbt")
    make_herd_nbt(DP / "data/rallous_temple_herd/structures/herdstone.nbt")


def write_lang_and_rp() -> None:
    merged = {}
    merged.update(FOSSIL_LANG)
    merged.update(TB_LANG)
    merged.update(OURS_LANG)
    dump(LANG / "en_us.json", merged)
    dump(
        RP / "pack.mcmeta",
        {"pack": {"pack_format": 15, "description": "Rallous Temple Herd — temple-beasts / broken herd names"}},
    )
    dump(RP / "assets/fossil/lang/en_us.json", FOSSIL_LANG)
    dump(RP / "assets/tameablebeasts/lang/en_us.json", TB_LANG)
    dump(RP / "assets/rallous_temple_herd/lang/en_us.json", OURS_LANG)


def write_quests() -> None:
    w(
        QUESTS / "temple_and_herd.snbt",
        r"""{
	always_invisible: false
	default_hide_dependency_lines: false
	default_quest_shape: "rsquare"
	filename: "temple_and_herd"
	group: "0A030000"
	icon: "minecraft:lime_banner"
	id: "0C020700"
	images: [ ]
	order_index: 10
	quest_links: [ ]
	quests: [
		{
			icon: "minecraft:bone"
			id: "0D010001"
			rewards: [
				{
					id: "0D010101"
					type: "xp"
					xp: 15
				}
			]
			shape: "hexagon"
			size: 1.5d
			subtitle: "Fossils + Tameable Beasts stay the engine."
			tasks: [
				{
					id: "0D010201"
					title: "The engine is Fossils / Tameable Beasts"
					type: "checkmark"
				}
			]
			description: [
				"No new creature mods. Haul, fight, travel, tank."
				""
				"Lizardmen hear temple-beasts. Beastmen break what they steal. Other races are worse at it (book, not a hidden penalty)."
				""
				"Fossils 9.3.4 cannot make only Temple-Spawn roll easier tames. Extra Tameable Beasts foods are the only easier-tame hook."
			]
			title: "The Beast Engine"
			x: -4d
			y: 0d
		}
		{
			dependencies: ["0D010001"]
			icon: "minecraft:jungle_sapling"
			id: "0D010002"
			rewards: [
				{
					id: "0D010102"
					type: "xp"
					xp: 25
				}
			]
			tasks: [
				{
					id: "0D010202"
					title: "Warm canopy"
					type: "advancement"
					advancement: "rallous_temple_herd:lizardmen/warm_canopy"
				}
			]
			description: [
				"Walk Terralith jungle / warm (savanna, oasis, summer skylands). The datapack grants Warm Canopy and a Temple-Beast Primer."
				""
				"These are Temple-Spawn lands. Markers are lime banners, not silent dinos."
			]
			title: "Temple-Spawn Canopy"
			x: -2d
			y: -2d
		}
		{
			dependencies: ["0D010002"]
			icon: "minecraft:lime_banner"
			id: "0D010003"
			rewards: [
				{
					id: "0D010103"
					type: "xp"
					xp: 40
				}
				{
					id: "0D010104"
					item: "minecraft:honey_bottle"
					count: 4
					type: "item"
				}
			]
			tasks: [
				{
					id: "0D010203"
					title: "Found a temple marker"
					type: "advancement"
					advancement: "rallous_temple_herd:lizardmen/temple_marker"
				}
			]
			description: [
				"/locate structure rallous_temple_herd:temple_marker"
				"Or stand on the mossy platform: named armor stand + lime banners + chest."
				"Cheats: /function rallous_temple_herd:place_temple_marker"
			]
			title: "Temple Marker"
			x: 0d
			y: -2d
		}
		{
			dependencies: ["0D010003"]
			icon: "minecraft:saddle"
			id: "0D010004"
			rewards: [
				{
					id: "0D010105"
					type: "xp"
					xp: 50
				}
			]
			tasks: [
				{
					id: "0D010204"
					title: "Loyal temple-beast"
					type: "advancement"
					advancement: "rallous_temple_herd:lizardmen/loyal_beast"
				}
			]
			description: [
				"Fossils: fossil → analyzer → spawning pool → hatch near you or Temple Scarab."
				"Tameable Beasts: Temple Flyer Meal / Temple-Beast Bait, plus extra offerings (honey, cooked meat, seeds)."
				"Name it. It is intelligent and loyal — haul, fight, travel, or tank."
			]
			title: "A Loyal Beast"
			x: 2d
			y: -2d
		}
		{
			dependencies: ["0D010001"]
			icon: "minecraft:dark_oak_sapling"
			id: "0D010005"
			rewards: [
				{
					id: "0D010106"
					type: "xp"
					xp: 25
				}
			]
			tasks: [
				{
					id: "0D010205"
					title: "Horned Woods"
					type: "advancement"
					advancement: "rallous_temple_herd:beastmen/horned_woods"
				}
			]
			description: [
				"Dark forest or taiga (Terralith belts included). No town. A herdstone hung with skulls."
			]
			title: "Into the Horned Woods"
			x: -2d
			y: 2d
		}
		{
			dependencies: ["0D010005"]
			icon: "minecraft:wither_skeleton_skull"
			id: "0D010006"
			rewards: [
				{
					id: "0D010107"
					type: "xp"
					xp: 40
				}
				{
					count: 8
					id: "0D010108"
					item: "minecraft:rotten_flesh"
					type: "item"
				}
			]
			tasks: [
				{
					id: "0D010206"
					title: "Stood at a herdstone"
					type: "advancement"
					advancement: "rallous_temple_herd:beastmen/herdstone"
				}
			]
			description: [
				"/locate structure rallous_temple_herd:herdstone"
				"Red/black banners, skulls, soul fire, uglier chest."
				"Cheats: /function rallous_temple_herd:place_herdstone"
			]
			title: "Herdstone"
			x: 0d
			y: 2d
		}
		{
			dependencies: ["0D010006"]
			icon: "minecraft:iron_sword"
			id: "0D010007"
			rewards: [
				{
					id: "0D010109"
					type: "xp"
					xp: 40
				}
			]
			tasks: [
				{
					id: "0D010207"
					title: "Fought the hostile herd"
					type: "checkmark"
				}
			]
			description: [
				"The herd does not trade. Night in the Horned Woods, or anything that hangs skulls on the stand."
				"If roaming wars are loaded: /function rallous_roaming:events/herd — Bray-Shaman / Gor / Herd-Beast."
				"Combat mode on. This is a raid on a herdstone, not two zombies at spawn."
			]
			title: "Hostile Herd"
			x: 2d
			y: 3d
		}
		{
			dependencies: ["0D010006"]
			icon: "minecraft:lead"
			id: "0D010008"
			rewards: [
				{
					id: "0D01010A"
					type: "xp"
					xp: 50
				}
			]
			tasks: [
				{
					id: "0D010208"
					title: "Broken Beast"
					type: "advancement"
					advancement: "rallous_temple_herd:beastmen/broken_beast"
				}
			]
			description: [
				"Hold a lead (Broken Collar in the chest) and carrion, or Fossils offal / stunted essence / frozen meat."
				"This is enslave framing. Same engine. Worse relationship."
			]
			title: "Broken Beast"
			x: 2d
			y: 1d
		}
		{
			dependencies: ["0D010001"]
			icon: "minecraft:iron_horse_armor"
			id: "0D010009"
			rewards: [
				{
					id: "0D01010B"
					type: "xp"
					xp: 15
				}
			]
			tasks: [
				{
					id: "0D010209"
					title: "Worse Hands"
					type: "advancement"
					advancement: "rallous_temple_herd:other_races/worse_hands"
				}
			]
			description: [
				"Empire, Dawi, Kislev, the dead, greenskins: livestock or siege engines."
				"If you already took an Old World first-join, the canopy primer also gives Worse Hands."
				"Cheats: /function rallous_temple_herd:give_lesser_bond"
				"Not a hidden tame penalty."
			]
			title: "Other Races, Worse Hands"
			x: -2d
			y: 0d
		}
		{
			dependencies: ["0D010004", "0D010008"]
			icon: "minecraft:saddle"
			id: "0D01000A"
			rewards: [
				{
					id: "0D01010C"
					type: "xp"
					xp: 80
				}
			]
			shape: "hexagon"
			size: 1.5d
			tasks: [
				{
					id: "0D01020A"
					title: "Haul, fight, travel, tank"
					type: "checkmark"
				}
			]
			description: [
				"Tick when you have used a living creature for two of: haul (chest/lead), fight (combat), travel (mount/fly), tank (it took hits)."
				"Temple or herd. The engine does not change."
			]
			title: "Warbeast Work"
			x: 4d
			y: 0d
		}
	]
	title: "Temple and Herd"
}
""",
    )
    w(
        ROOT / "ftbquests" / "chapter_groups.snippet.snbt",
        """{\n\tid: \"0A030000\"\n\ttitle: \"Temple and Herd\"\n}\n# Merge into config/ftbquests/quests/chapter_groups.snbt chapter_groups list.\n""",
    )


def write_handoff() -> None:
    w(
        ROOT / "TEMPLE-AND-HERD.md",
        """# Temple and Herd — integrator pickup

Owned by the Lizardmen / Beastmen / Ark-creature glue agent. Do not rebuild the dist zip here. Do not rewrite PLAY.md.

## Copy

| Source | Into pack |
| --- | --- |
| `content/datapacks/rallous_temple_herd/` | world `datapacks/` or `overrides/datapacks/` |
| `content/resourcepacks/Rallous Temple Herd/` | `overrides/resourcepacks/` (enable in options) |
| `content/lang/en_us.json` | split into RP namespaces if you skip the folder RP |
| `content/ftbquests/chapters/temple_and_herd.snbt` | `config/ftbquests/quests/chapters/` |
| `content/ftbquests/chapter_groups.snippet.snbt` | merge group `0A030000` into `chapter_groups.snbt` |

## Mechanical vs cosmetic

**Mechanical**

- Worldgen structures `temple_marker` (jungle/warm tag) and `herdstone` (dark forest/taiga tag): platforms, banners, chests, armor stands.
- Tick: biome enter grants advancements + one-time primer books; proximity to tagged stands grants marker advancements.
- Tameable Beasts `*_tame_food` tags get extra vanilla foods (global, not per-player-race).
- Loot tables: temple cache vs uglier herdstone cache (Broken Collar lead).
- Advancements + FTB chapter tasks that read them.
- Place functions for cheats / quest commands.

**Cosmetic / framing (not a hidden tame buff)**

- Lang: Fossils vat/analyzer/scarab/whip/failuresaurus; TB gecko/quetzal/racoon names.
- Lore books (Temple-Beast Primer, Herdstone Rite, Worse Hands).
- Entity/item tags `temple_beasts` / `herd_beasts` / `broken_beasts` — Fossils does **not** read these for tame chance.
- Other races: Worse Hands book if `rallous.old_world` is already tagged. No damage/tame penalty.

**Cannot force**

- Per-faction Fossils tame difficulty. Config only has global `whipToTameDino` (left default / unset).
""",
    )
    readme = ROOT / "README.md"
    block = (
        "## Temple and Herd (this agent)\n"
        "- `datapacks/rallous_temple_herd/` — datapack (see its 10-line README).\n"
        "- `lang/en_us.json` — merged overlay; or resource pack `Rallous Temple Herd`.\n"
        "- `ftbquests/chapters/temple_and_herd.snbt` — optional FTB chapter.\n"
        "- `TEMPLE-AND-HERD.md` — mechanical vs cosmetic + copy paths.\n"
    )
    if readme.exists():
        text = readme.read_text()
        if "datapacks/rallous_temple_herd/" not in text:
            w(readme, text.rstrip() + "\n\n" + block)
    else:
        w(
            readme,
            "# Content pickup (quest / zip / faction integrator)\n\n"
            "Sibling datapacks may also live here (`rallous_roaming`, `rallous_warp_crash`).\n\n"
            + block,
        )


def main() -> None:
    write_datapack()
    write_lang_and_rp()
    write_quests()
    write_handoff()
    print("wrote", ROOT)


if __name__ == "__main__":
    main()
