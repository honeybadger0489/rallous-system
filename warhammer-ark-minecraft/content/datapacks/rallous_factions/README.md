# rallous_factions (compiled)

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
