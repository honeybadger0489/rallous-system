#!/usr/bin/env python3
"""Thicker Temple-Spawn courtyard and herdstone pit. Vanilla blocks only. No creature mods."""

from __future__ import annotations

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
GEN = HERE.parent.parent / "_gen_temple_herd.py"


def _load_gen():
    spec = importlib.util.spec_from_file_location("rallous_temple_herd_gen", GEN)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Grid:
    def __init__(self, gen):
        self.gen = gen
        self.palette: list[dict] = []
        self._idx: dict = {}
        self.blocks: dict[tuple[int, int, int], dict] = {}
        self.entities: list[dict] = []

    def sid(self, name: str, props: dict | None = None) -> int:
        key = (name, tuple(sorted((props or {}).items())))
        if key not in self._idx:
            entry: dict = {"Name": name}
            if props:
                entry["Properties"] = dict(props)
            self._idx[key] = len(self.palette)
            self.palette.append(entry)
        return self._idx[key]

    def put(self, x: int, y: int, z: int, name: str, props: dict | None = None, nbt=None) -> None:
        block = {"pos": [x, y, z], "state": self.sid(name, props)}
        if nbt is not None:
            block["nbt"] = nbt
        self.blocks[(x, y, z)] = block

    def fill(self, x0: int, y0: int, z0: int, x1: int, y1: int, z1: int, name: str, props: dict | None = None) -> None:
        xa, xb = sorted((x0, x1))
        ya, yb = sorted((y0, y1))
        za, zb = sorted((z0, z1))
        for x in range(xa, xb + 1):
            for y in range(ya, yb + 1):
                for z in range(za, zb + 1):
                    self.put(x, y, z, name, props)

    def stand(self, x: float, y: float, z: float, name: str, color: str, tags: list[str], head: str) -> None:
        bx, by, bz = int(x), int(y), int(z)
        self.entities.append(
            {
                "pos": [x, y, z],
                "blockPos": [bx, by, bz],
                "nbt": self.gen.stand_nbt(name, color, tags, head),
            }
        )

    def write(self, path: Path, size: list[int]) -> None:
        self.gen.write_structure(path, size, self.palette, list(self.blocks.values()), self.entities)


FENCE = {"north": "false", "south": "false", "east": "false", "west": "false", "waterlogged": "false"}
WATER = {"level": "0"}
CHEST_W = {"facing": "west", "type": "single", "waterlogged": "false"}
CHEST_E = {"facing": "east", "type": "single", "waterlogged": "false"}
CHEST_N = {"facing": "north", "type": "single", "waterlogged": "false"}
LEAVES = {"persistent": "true", "distance": "1", "waterlogged": "false"}
CAMPFIRE = {"facing": "north", "lit": "true", "signal_fire": "false", "waterlogged": "false"}
LOG_Y = {"axis": "y"}


def make_temple_nbt(path: Path, gen=None) -> None:
    """13x13 mossy courtyard, 5x5 glowing spawning-pool pit, banners, two caches, named stands."""
    g = Grid(gen or _load_gen())
    n = 13
    last = n - 1
    g.fill(0, 0, 0, last, 0, last, "minecraft:mossy_cobblestone")
    g.fill(0, 1, 0, last, 1, last, "minecraft:mossy_stone_bricks")
    for x in (0, last):
        for z in (0, last):
            g.put(x, 0, z, "minecraft:jungle_planks")
            g.put(x, 1, z, "minecraft:jungle_planks")
    g.fill(4, 0, 4, 8, 0, 8, "minecraft:prismarine")
    g.put(6, 0, 6, "minecraft:gold_block")
    for x, z in ((5, 6), (7, 6), (6, 5), (6, 7)):
        g.put(x, 0, z, "minecraft:sea_lantern")
    g.fill(4, 1, 4, 8, 1, 8, "minecraft:air")
    g.fill(4, 1, 4, 8, 1, 8, "minecraft:water", WATER)
    for x in (0, last):
        for z in (0, last):
            g.put(x, 2, z, "minecraft:jungle_fence", FENCE)
            g.put(x, 3, z, "minecraft:jungle_fence", FENCE)
            g.put(x, 4, z, "minecraft:lime_banner", {"rotation": "0" if z == 0 else "8"})
    for x, z, rot in ((6, 0, "0"), (6, last, "8"), (0, 6, "12"), (last, 6, "4")):
        g.put(x, 2, z, "minecraft:lime_banner", {"rotation": rot})
    g.put(10, 2, 6, "minecraft:chest", CHEST_W, nbt=g.gen.chest_nbt("rallous_temple_herd:chests/temple_cache"))
    g.put(2, 2, 6, "minecraft:chest", CHEST_E, nbt=g.gen.chest_nbt("rallous_temple_herd:chests/temple_cache"))
    g.put(6, 2, 10, "minecraft:chest", CHEST_N, nbt=g.gen.chest_nbt("rallous_temple_herd:chests/temple_cache"))
    g.put(6, 2, 2, "minecraft:gold_block")
    g.put(6, 3, 2, "minecraft:sea_lantern")
    for x, z in ((1, 1), (11, 1), (1, 11), (11, 11), (3, 1), (9, 1), (1, 3), (1, 9)):
        g.put(x, 2, z, "minecraft:jungle_leaves", LEAVES)
    stair = {"half": "bottom", "shape": "straight", "waterlogged": "false"}
    g.put(6, 2, 3, "minecraft:mossy_stone_brick_stairs", {**stair, "facing": "south"})
    g.put(6, 2, 9, "minecraft:mossy_stone_brick_stairs", {**stair, "facing": "north"})
    g.put(3, 2, 6, "minecraft:mossy_stone_brick_stairs", {**stair, "facing": "east"})
    g.put(9, 2, 6, "minecraft:mossy_stone_brick_stairs", {**stair, "facing": "west"})
    g.stand(6.5, 2.0, 3.5, "Temple-Spawn Marker", "dark_green", ["rallous.temple_marker"], "minecraft:lime_banner")
    g.stand(10.5, 2.0, 4.5, "Spawning Pool", "aqua", ["rallous.temple_marker", "rallous.temple_pit"], "minecraft:heart_of_the_sea")
    g.write(path, [n, 6, n])


def make_herd_nbt(path: Path, gen=None) -> None:
    """13x13 dirt ring, 5x5 soul pit, 5-high herdstone, skull banners, two caches, named stands."""
    g = Grid(gen or _load_gen())
    n = 13
    last = n - 1
    g.fill(0, 0, 0, last, 0, last, "minecraft:cobbled_deepslate")
    g.fill(0, 1, 0, last, 1, last, "minecraft:coarse_dirt")
    for x in range(n):
        for z in range(n):
            if x in (0, last) or z in (0, last):
                g.put(x, 0, z, "minecraft:mossy_cobblestone")
                g.put(x, 1, z, "minecraft:dark_oak_planks")
            elif (x + z) % 4 == 0:
                g.put(x, 1, z, "minecraft:mossy_cobblestone")
    g.fill(4, 0, 4, 8, 1, 8, "minecraft:air")
    g.fill(4, 0, 4, 8, 0, 8, "minecraft:soul_soil")
    for x, z in ((4, 4), (8, 4), (4, 8), (8, 8)):
        g.put(x, 0, z, "minecraft:bone_block", LOG_Y)
    g.fill(5, 0, 5, 7, 4, 7, "minecraft:cobbled_deepslate")
    g.fill(6, 0, 6, 6, 5, 6, "minecraft:cracked_stone_bricks")
    g.put(6, 3, 6, "minecraft:bone_block", LOG_Y)
    g.put(6, 5, 6, "minecraft:dark_oak_log", LOG_Y)
    g.put(6, 6, 6, "minecraft:wither_skeleton_skull", {"rotation": "8"})
    g.put(5, 4, 6, "minecraft:skeleton_skull", {"rotation": "12"})
    g.put(7, 4, 6, "minecraft:skeleton_skull", {"rotation": "4"})
    g.put(6, 4, 5, "minecraft:skeleton_skull", {"rotation": "0"})
    g.put(6, 4, 7, "minecraft:wither_skeleton_skull", {"rotation": "8"})
    g.put(6, 1, 9, "minecraft:soul_campfire", CAMPFIRE)
    for x, z, banner, rot in (
        (6, 0, "minecraft:red_banner", "0"),
        (6, last, "minecraft:black_banner", "8"),
        (0, 6, "minecraft:black_banner", "12"),
        (last, 6, "minecraft:red_banner", "4"),
    ):
        g.put(x, 2, z, banner, {"rotation": rot})
    for x, z in ((0, 0), (last, 0), (0, last), (last, last)):
        g.put(x, 2, z, "minecraft:dark_oak_fence", FENCE)
        g.put(x, 3, z, "minecraft:dark_oak_fence", FENCE)
        skull = "minecraft:skeleton_skull" if (x + z) % 2 == 0 else "minecraft:wither_skeleton_skull"
        g.put(x, 4, z, skull, {"rotation": "0"})
    g.put(2, 2, 6, "minecraft:chest", CHEST_E, nbt=g.gen.chest_nbt("rallous_temple_herd:chests/herdstone_cache"))
    g.put(10, 2, 6, "minecraft:chest", CHEST_W, nbt=g.gen.chest_nbt("rallous_temple_herd:chests/herdstone_cache"))
    g.put(6, 2, 2, "minecraft:hay_block")
    g.put(8, 2, 10, "minecraft:red_wool")
    g.put(4, 2, 10, "minecraft:bone_block", LOG_Y)
    g.stand(6.5, 2.0, 9.5, "Herdstone", "dark_red", ["rallous.herdstone"], "minecraft:wither_skeleton_skull")
    g.stand(3.5, 2.0, 6.5, "Broken-Beast Post", "red", ["rallous.herdstone", "rallous.herd_post"], "minecraft:skeleton_skull")
    g.write(path, [n, 8, n])


def main() -> None:
    gen = _load_gen()
    struct = HERE / "data" / "rallous_temple_herd" / "structures"
    make_temple_nbt(struct / "temple_marker.nbt", gen)
    make_herd_nbt(struct / "herdstone.nbt", gen)
    print("wrote", struct / "temple_marker.nbt")
    print("wrote", struct / "herdstone.nbt")


if __name__ == "__main__":
    main()
