# Beasts (Temple and Herd)

Fossils and Archeology + Tameable Beasts are the engine: haul, fight, travel, tank. No new creature mods. No 40k.

Quest chapter **Temple and Herd**. Markers are banners + named armor stands + chests — not silent dinos.

`/locate structure rallous_temple_herd:temple_marker`  
`/locate structure rallous_temple_herd:herdstone`

## Lizardmen — high

Temple-cities, jungle / warm markers, Temple-Spawn names. Extra Tameable Beasts tame-food tags (those extras are **global** — anyone can use the offerings). Sacred-beast fantasy. Fossils 9.3.4 has **no** per-faction tame tag.

## Beastmen — corrupt

Herdstones in dark forest / taiga. Uglier loot (Broken Collar lead). Herd-mutt names. Rotten flesh / bone on some tame tags. A roaming Horned Woods host also counts as herdstone-adjacent.

They do not keep capitals. A stranger is meat or a rival herd.

## Everyone else — low

Empire, Dwarfs, Vampire Counts, Greenskins, Skaven, Khorne: beasts belong in pens, not on the throne-dais. You get the **Worse Hands** book if you already carry the Old World tag. **No hidden tame penalty** — we cannot make only Lizardmen roll easier Fossils tames without a new mod. Fossils only has a global `whipToTameDino` (we left it).

## Force a look

```
/function rallous_old_world:lm_bm/summon
/function rallous_temple_herd:place_temple_marker
/function rallous_temple_herd:place_herdstone
```

`lm_bm/summon` is jungle-side Lizardmen proxies + forest Beastmen. Fossils dinos spawn **if** that entity id loaded; vanilla turtles / goats / a ravager always do.
