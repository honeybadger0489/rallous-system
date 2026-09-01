# Roaming

Mid-game hosts with **no capital**. Scheduled while someone is online — not worldgen. They march toward the nearest player, leave a **limited** scar (leaves / crops / short grass), and fade after about five minutes.

Natural spawn waits until **day ≥ 1** or you are **128+** blocks from the crater, then a 20–40 minute clock and a 25% roll. Force functions skip that gate.

## Three hosts

| Host | Voice | Look |
| --- | --- | --- |
| **Waaagh** | Greenhost / boyz | Named pillagers, choppa vindicators, gobbo zombies, lime skull banners |
| **Herd** | Horned Woods | Bray-shaman witch, nerfed ravager, gor vindicators, ungor husks, brown skull banners |
| **Blood Host** | Khorne | Champion + bloodreavers, skull-tithe wither skeletons, red skull banners |

Beastmen / Waaagh / Khorne **camps** on the faction map are also roaming-style pickets (no pretty capital). These **events** are a different thing: they spawn on a clock and walk at you.

## Force (smoke)

```
/function rallous_old_world:force_roaming
```

That fires a Waaagh scout, a Beastmen herd, and a Khorne pack near you.

Per-host (same night, no wait):

```
/function rallous_roaming:events/waaagh
/function rallous_roaming:events/herd
/function rallous_roaming:events/khorne_host
/function rallous_roaming:events/random
/function rallous_roaming:clear
```

To poke the **scheduled** path without waiting 20–40 min: `/function rallous_roaming:debug/ready` then wait ~60s. The first natural host after the wait is guaranteed; later rolls stay 25%.
