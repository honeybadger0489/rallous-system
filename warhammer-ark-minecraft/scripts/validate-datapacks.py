#!/usr/bin/env python3
"""Validate authored datapacks (report only; does not rewrite packs or rebuild zip).

Walks content/datapacks/** and pack-src datapack trees if present:
  - pack.mcmeta exists and pack_format is 15
  - every .json / .mcmeta parses
  - every `function namespace:path` reference resolves to a .mcfunction

Sibling packs in the same tree can see each other. Extra function trees
(pack/content, pack/cf-overrides/datapacks) are indexed for cross-pack
refs such as rallous_old_world:load — they are not themselves scored
unless they sit under a walk root.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WALK_REL = (
    "content/datapacks",
    "pack-src/datapacks",
    "pack-src/overrides/datapacks",
)
# Resolution-only: loaded alongside authored packs in the zip / runtime.
EXTRA_FN_REL = (
    "pack/content",
    "pack/cf-overrides/datapacks",
)

EXPECTED_PACK_FORMAT = 15

# Command / tag / reward IDs. Do not match loot `minecraft:set_nbt` via this.
FN_ID = r"([a-z0-9_.-]+:[a-z0-9_./-]+)"
RE_FUNCTION_CMD = re.compile(
    rf"(?:schedule\s+)?function\s+#?{FN_ID}",
    re.IGNORECASE,
)
RE_SLASH_FUNCTION = re.compile(rf"/function\s+#?{FN_ID}", re.IGNORECASE)
RE_LOOT_FN = re.compile(r"^minecraft:(set_|enchant_|exploration_|furnace_|fill_|limit_|looting_|explosion_|copy_|sequence|alternatives|filtered|reference)")

WARP_CRASH_NAME = "rallous_warp_crash"


@dataclass
class Finding:
    ok: bool
    kind: str
    path: str
    detail: str


@dataclass
class PackResult:
    root: Path
    rel: str
    findings: list[Finding] = field(default_factory=list)
    json_ok: int = 0
    json_fail: int = 0
    fn_ok: int = 0
    fn_fail: int = 0
    pack_format_ok: bool = False
    flake_notes: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.pack_format_ok and self.json_fail == 0 and self.fn_fail == 0 and all(
            f.ok for f in self.findings if f.kind == "meta"
        )


def rel_to_root(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def discover_packs(base: Path) -> list[Path]:
    if not base.is_dir():
        return []
    packs: list[Path] = []
    for meta in sorted(base.rglob("pack.mcmeta")):
        pack = meta.parent
        if (pack / "data").is_dir():
            packs.append(pack)
    return packs


def walk_roots() -> list[Path]:
    found: list[Path] = []
    for rel in WALK_REL:
        p = ROOT / rel
        if p.is_dir():
            found.append(p)
    return found


def extra_function_trees() -> list[Path]:
    trees: list[Path] = []
    for rel in EXTRA_FN_REL:
        p = ROOT / rel
        if p.is_dir():
            trees.append(p)
    return trees


def index_functions(pack_roots: list[Path]) -> dict[str, list[str]]:
    """Map namespace:path -> list of .mcfunction relative paths."""
    index: dict[str, list[str]] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for pack in pack_roots:
        data = pack / "data"
        if not data.is_dir():
            continue
        for ns_dir in sorted(p for p in data.iterdir() if p.is_dir()):
            fn_root = ns_dir / "functions"
            if not fn_root.is_dir():
                continue
            for mcfn in sorted(fn_root.rglob("*.mcfunction")):
                rel = mcfn.relative_to(fn_root).with_suffix("").as_posix()
                ident = f"{ns_dir.name}:{rel}"
                loc = rel_to_root(mcfn)
                key = (ident, loc)
                if key in seen:
                    continue
                seen.add(key)
                index[ident].append(loc)
    return index


def parse_json_file(path: Path) -> tuple[object | None, str | None]:
    raw = path.read_text(encoding="utf-8")
    try:
        return json.loads(raw), None
    except json.JSONDecodeError as exc:
        return None, f"{exc.msg} (line {exc.lineno} col {exc.colno})"


def json_files(pack: Path) -> list[Path]:
    files: list[Path] = []
    for path in sorted(pack.rglob("*")):
        if not path.is_file():
            continue
        if path.name in {".DS_Store"}:
            continue
        if path.suffix.lower() in {".json", ".mcmeta"}:
            files.append(path)
    return files


def is_function_tag_json(path: Path) -> bool:
    parts = path.parts
    return "tags" in parts and "functions" in parts and path.suffix == ".json"


def extract_fn_ids_from_json(path: Path, data: object) -> list[str]:
    ids: list[str] = []

    def walk(node: object, parent_key: str | None = None) -> None:
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, k)
        elif isinstance(node, list):
            for item in node:
                walk(item, parent_key)
        elif isinstance(node, str):
            if ":" not in node or node.startswith("#"):
                return
            if not re.fullmatch(FN_ID, node):
                return
            if parent_key == "function":
                if RE_LOOT_FN.match(node):
                    return
                # Loot tables use "function": "minecraft:set_count"; skip those files.
                if "loot_tables" in path.parts:
                    return
                ids.append(node)
            elif is_function_tag_json(path) and parent_key in {"values", "id"}:
                ids.append(node)

    if is_function_tag_json(path):
        values = []
        if isinstance(data, dict):
            raw_vals = data.get("values") or []
            for item in raw_vals:
                if isinstance(item, str):
                    values.append(item)
                elif isinstance(item, dict) and isinstance(item.get("id"), str):
                    values.append(item["id"])
        for ident in values:
            if ident.startswith("#"):
                continue
            if re.fullmatch(FN_ID, ident):
                ids.append(ident)
        # Advancement-style rewards may still appear; walk for rewards.function.
        walk(data)
        # Dedup while keeping order
        seen: set[str] = set()
        out: list[str] = []
        for ident in ids:
            if ident not in seen:
                seen.add(ident)
                out.append(ident)
        return out

    walk(data)
    seen: set[str] = set()
    out: list[str] = []
    for ident in ids:
        if ident not in seen:
            seen.add(ident)
            out.append(ident)
    return out


def extract_fn_ids_from_mcfunction(path: Path) -> list[tuple[int, str]]:
    found: list[tuple[int, str]] = []
    seen_line: set[tuple[int, str]] = set()
    text = path.read_text(encoding="utf-8")
    for lineno, line in enumerate(text.splitlines(), 1):
        stripped = line.lstrip()
        # Comments still mention /function cheats; skip # lines so we only
        # score executable commands (plus tellraw/book text on those lines).
        if stripped.startswith("#"):
            continue
        for rx in (RE_FUNCTION_CMD, RE_SLASH_FUNCTION):
            for match in rx.finditer(line):
                ident = match.group(1)
                if ident.startswith("#"):
                    continue
                key = (lineno, ident)
                if key in seen_line:
                    continue
                seen_line.add(key)
                found.append(key)
    return found


IN_FLIGHT_NAMESPACES = frozenset({"rallous_factions"})


def note_flakes(pack: Path, result: PackResult, fn_index: dict[str, list[str]]) -> None:
    if pack.name == WARP_CRASH_NAME:
        data = pack / "data" / WARP_CRASH_NAME / "functions"
        if not data.is_dir():
            result.flake_notes.append(
                f"{result.rel}: functions/ missing — warp_crash may be mid-edit"
            )
        else:
            files = list(data.rglob("*.mcfunction"))
            if len(files) < 8:
                result.flake_notes.append(
                    f"{result.rel}: only {len(files)} .mcfunction files — warp_crash may be mid-edit"
                )
            empties = [rel_to_root(p) for p in files if p.stat().st_size == 0]
            if empties:
                result.flake_notes.append(
                    "empty mcfunction (mid-edit flake?): " + ", ".join(empties)
                )

    missing_ns: set[str] = set()
    for finding in result.findings:
        if finding.ok or finding.kind != "function":
            continue
        ident = finding.detail.removeprefix("missing ").strip()
        ns = ident.split(":", 1)[0] if ":" in ident else ""
        if ns and ns not in {k.split(":", 1)[0] for k in fn_index}:
            missing_ns.add(ns)
        if ns in IN_FLIGHT_NAMESPACES:
            result.flake_notes.append(
                f"{finding.path}: {ident} — {ns} pack not on disk (sibling agent in-flight)"
            )
        elif pack.name == WARP_CRASH_NAME:
            result.flake_notes.append(
                f"{finding.path}: warp_crash missing {ident} (treat as flake if mid-edit)"
            )
    for ns in sorted(missing_ns - IN_FLIGHT_NAMESPACES):
        result.flake_notes.append(
            f"{result.rel}: referenced namespace {ns!r} has no indexed .mcfunction"
        )


def validate_pack(pack: Path, fn_index: dict[str, list[str]]) -> PackResult:
    result = PackResult(root=pack, rel=rel_to_root(pack))
    meta_path = pack / "pack.mcmeta"
    if not meta_path.is_file():
        result.findings.append(Finding(False, "meta", result.rel, "missing pack.mcmeta"))
        return result

    data, err = parse_json_file(meta_path)
    if err:
        result.json_fail += 1
        result.findings.append(Finding(False, "json", rel_to_root(meta_path), err))
        return result
    result.json_ok += 1
    fmt = None
    if isinstance(data, dict) and isinstance(data.get("pack"), dict):
        fmt = data["pack"].get("pack_format")
    if fmt == EXPECTED_PACK_FORMAT:
        result.pack_format_ok = True
        result.findings.append(
            Finding(True, "meta", rel_to_root(meta_path), f"pack_format={fmt}")
        )
    else:
        result.findings.append(
            Finding(
                False,
                "meta",
                rel_to_root(meta_path),
                f"pack_format={fmt!r} expected {EXPECTED_PACK_FORMAT}",
            )
        )

    for path in json_files(pack):
        if path == meta_path:
            continue
        parsed, err = parse_json_file(path)
        if err:
            result.json_fail += 1
            result.findings.append(Finding(False, "json", rel_to_root(path), err))
            continue
        result.json_ok += 1
        for ident in extract_fn_ids_from_json(path, parsed):
            if ident in fn_index:
                result.fn_ok += 1
            else:
                result.fn_fail += 1
                result.findings.append(
                    Finding(False, "function", rel_to_root(path), f"missing {ident}")
                )

    for mcfn in sorted((pack / "data").rglob("*.mcfunction")) if (pack / "data").is_dir() else []:
        for lineno, ident in extract_fn_ids_from_mcfunction(mcfn):
            if ident in fn_index:
                result.fn_ok += 1
            else:
                result.fn_fail += 1
                result.findings.append(
                    Finding(
                        False,
                        "function",
                        f"{rel_to_root(mcfn)}:{lineno}",
                        f"missing {ident}",
                    )
                )

    note_flakes(pack, result, fn_index)
    return result


def render_report(
    roots: list[Path],
    packs: list[PackResult],
    fn_index: dict[str, list[str]],
    extra_trees: list[Path],
) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    pack_pass = sum(1 for p in packs if p.ok)
    pack_fail = len(packs) - pack_pass
    json_ok = sum(p.json_ok for p in packs)
    json_fail = sum(p.json_fail for p in packs)
    fn_ok = sum(p.fn_ok for p in packs)
    fn_fail = sum(p.fn_fail for p in packs)
    flakes = [n for p in packs for n in p.flake_notes]
    lines = [
        "DATAPACK VALIDATE",
        f"generated: {now}",
        f"root: {ROOT.as_posix()}",
        "walk:",
    ]
    if roots:
        for r in roots:
            lines.append(f"  {rel_to_root(r)}")
    else:
        lines.append("  (none found)")
    if extra_trees:
        lines.append("function index extras (resolution only):")
        for r in extra_trees:
            lines.append(f"  {rel_to_root(r)}")
    lines.append(f"indexed functions: {len(fn_index)}")
    lines.append("")
    lines.append("COUNTS")
    lines.append(f"  packs:     pass={pack_pass} fail={pack_fail}")
    lines.append(f"  json:      pass={json_ok} fail={json_fail}")
    lines.append(f"  functions: pass={fn_ok} fail={fn_fail}")
    lines.append(
        f"  TOTAL     pass={pack_pass + json_ok + fn_ok} fail={pack_fail + json_fail + fn_fail}"
    )
    lines.append("")
    if flakes:
        lines.append("FLAKES")
        lines.append("  warp_crash may be mid-edit; treat missing refs as possibly transient.")
        for note in flakes:
            lines.append(f"  - {note}")
        lines.append("")
    else:
        lines.append("FLAKES")
        lines.append("  none recorded.")
        lines.append("")

    lines.append("PACKS")
    if not packs:
        lines.append("  (no datapacks discovered)")
    for pack in packs:
        status = "PASS" if pack.ok else "FAIL"
        lines.append(
            f"  [{status}] {pack.rel}  json={pack.json_ok}/{pack.json_ok + pack.json_fail}  "
            f"fn={pack.fn_ok}/{pack.fn_ok + pack.fn_fail}  pack_format15={'yes' if pack.pack_format_ok else 'no'}"
        )
        for f in pack.findings:
            if f.ok and f.kind == "meta":
                lines.append(f"           ok  {f.kind}  {f.path}  {f.detail}")
            elif not f.ok:
                lines.append(f"           FAIL {f.kind}  {f.path}  {f.detail}")
    lines.append("")
    lines.append("END")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report",
        type=Path,
        default=ROOT / "content" / "DATAPACK-VALIDATE.txt",
        help="Write the text report here (default: content/DATAPACK-VALIDATE.txt)",
    )
    parser.add_argument(
        "--no-write",
        action="store_true",
        help="Print only; do not write the report file",
    )
    args = parser.parse_args()

    roots = walk_roots()
    pack_dirs: list[Path] = []
    seen: set[Path] = set()
    for base in roots:
        for pack in discover_packs(base):
            resolved = pack.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            pack_dirs.append(pack)

    extra_trees = extra_function_trees()
    index_roots = list(pack_dirs)
    for tree in extra_trees:
        for pack in discover_packs(tree):
            resolved = pack.resolve()
            if resolved not in seen:
                index_roots.append(pack)

    fn_index = index_functions(index_roots)
    results = [validate_pack(p, fn_index) for p in pack_dirs]
    report = render_report(roots, results, fn_index, extra_trees)
    sys.stdout.write(report)

    if not args.no_write:
        out = args.report
        if not out.is_absolute():
            out = Path.cwd() / out
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
        print(f"wrote {rel_to_root(out) if out.is_relative_to(ROOT) else out.as_posix()}", file=sys.stderr)

    pack_fail = sum(1 for p in results if not p.ok)
    json_fail = sum(p.json_fail for p in results)
    fn_fail = sum(p.fn_fail for p in results)
    return 1 if pack_fail or json_fail or fn_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
