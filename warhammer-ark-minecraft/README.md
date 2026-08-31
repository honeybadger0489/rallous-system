# Rallous Frontier — Minecraft prototype kit

This folder is an **inspiration + prototype collection**, not a finished game.

The goal is to overhaul Minecraft into a **grimdark survival world with prehistoric/alien fauna**, in the spirit of Warhammer (tone, not IP) and **ARK: Survival** (taming, tribes, the island is trying to kill you). The same fantasy is meant to travel later into an **ARK: Survival Ascended** mod under original names (**Rallous System / Warhammer Frontier**).

## What you get

| File | What it is |
| --- | --- |
| [CURATED-PACK.md](CURATED-PACK.md) | Recommended Minecraft **1.20.1 Forge** assortment, pillars, tiers, conflicts |
| [RESEARCH.md](RESEARCH.md) | Live-sourced notes on mods, packs, loaders, and dead ends |
| [INSPIRATION.md](INSPIRATION.md) | Gameplay loops that mix the two vibes **without cloning GW/Wildcard IP** |
| [LEGAL-NOTES.md](LEGAL-NOTES.md) | Games Workshop, Mojang, and Wildcard rules of the road |
| [CAMPAIGN.md](CAMPAIGN.md) | **Open-world campaign** (RDR chapters + New World regions + Ark warband) |
| [QUEST-AND-WORLD-MODS.md](QUEST-AND-WORLD-MODS.md) | Quest / faction / siege / map mods for that campaign overlay |
| [OPEN-WORLD-CAMPAIGN-LOOP.md](OPEN-WORLD-CAMPAIGN-LOOP.md) | One-day warband loop |
| [IP-FANTASY.md](IP-FANTASY.md) | Fantasy / Total War analogue branding (addendum to legal notes) |
| [FACTIONS-AND-DIPLOMACY.md](FACTIONS-AND-DIPLOMACY.md) | Soldier’s-eye factions and treaties (pairs with campaign) |
| [pack/mods.json](pack/mods.json) | Importable list: Modrinth slugs, version IDs, CurseForge IDs where known |
| [pack/rallous-frontier-0.1.0.mrpack](pack/rallous-frontier-0.1.0.mrpack) | Modrinth pack file (metadata only — launchers download the jars) |
| [pack/pack.toml](pack/pack.toml) | [packwiz](https://packwiz.infra.link/) pin for Prism / CLI |
| [scripts/download-pack.sh](scripts/download-pack.sh) | Official Modrinth CDN downloader with SHA-1 checks |

Default pack **does not include** Warhammer 40k-branded mods (Hammercraft, Tacz40k, etc.). Those are documented as a high-risk overlay. Use original analogues. See [LEGAL-NOTES.md](LEGAL-NOTES.md).

## Recommended install (30 seconds)

1. Install [Prism Launcher](https://prismlauncher.org/) (or the Modrinth App).
2. Create **Minecraft 1.20.1** with **Forge 47.4.0** (or newer 47.4.x).
3. Import `pack/rallous-frontier-0.1.0.mrpack`, **or** drag projects from `pack/mods.json`.
4. Allocate **8 GB RAM** (10–12 GB if you add Ice and Fire / more biome mods later).
5. In video settings: **Oculus** shader = Complementary Unbound. Resource pack order is in [CURATED-PACK.md](CURATED-PACK.md).

Full import steps: keep reading [CURATED-PACK.md](CURATED-PACK.md#how-to-import).

## Target at a glance

- **Version / loader:** Minecraft **1.20.1** + **Forge 47.4.x** (content-mod sweet spot in 2026).
- **Default creature loop:** Fossils and Archeology: Revival (not three dinosaur mods at once).
- **Default survival:** Legendary Survival Overhaul + Serene Seasons (not Tough As Nails *and* Cold Sweat).
- **Default combat:** Epic Fight + Simply Swords + TaCZ guns (original packs, not 40k gunpacks).
- **Look:** Faithful 32x + Grimdark Battlepack + Grimdark Sky + Complementary Unbound.

## Later: ASA

Minecraft is the cheap table to test **loops** (knockout-adjacent taming, tribe claims, brutal climate, gothic-industrial bases, chapter-as-tribe). ARK: Survival Ascended is the later home for custom creatures, engrams, and tribes — still as **Rallous**, not as licensed 40k or Ark clones. Mapping is in [CURATED-PACK.md](CURATED-PACK.md#bridge-to-ark-survival-ascended) and [INSPIRATION.md](INSPIRATION.md).
