# rallous_factions (compiled)

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
