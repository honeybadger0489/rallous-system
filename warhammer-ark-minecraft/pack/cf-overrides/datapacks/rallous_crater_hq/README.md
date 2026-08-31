# rallous_crater_hq (MC 1.20.1, pack_format 15)
Cheap crater HQ hook for a later custom-faction DLC. Not faction gameplay.
Call as the landed player after warp-crash has set `rallous.crater_x/y/z`:
`/function rallous_crater_hq:mark`
Missing crater scores → no-op. Existing HQ marker within 8 blocks → refresh storage only.
## What it writes
- Storage `rallous_crater_hq:data` `{owner:[I;UUID], pos:{x,y,z}}`
- Forceloaded marker `rallous.hq` / `rallous.crater_hq` with `data.Owner` and `data.pos`
- Oak fence + white banner at crater +2 X (player claim, not a contact camp)
## DLC hook
Crash pack (after `store_crater`): `execute as <player> run function rallous_crater_hq:mark`
Recruit into that player's faction: read `data get storage rallous_crater_hq:data` or
`execute as @e[type=marker,tag=rallous.hq] at @s` and copy `data.Owner` onto the recruit.
Match a player with `if score @e[tag=rallous.hq] rallous.pid = @s rallous.pid` when pid exists.
