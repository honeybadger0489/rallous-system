# Install

Import the **latest** zip as a **new** CurseForge profile. Do not update 0.2.x / 0.3.0–0.3.8. **0.3.9** is this ship.

**Download (latest on this branch):**  
https://github.com/honeybadger0489/rallous-system/raw/cursor/warhammer-ark-minecraft-d8d1/warhammer-ark-minecraft/dist/rallous-warhammer-fantasy-0.3.9.zip

Older `dist/rallous-warhammer-fantasy-0.3.7.zip` still exists if you need that pin.

## CurseForge

1. CurseForge app → Minecraft → **Create Custom Profile → Import**.
2. Java **17**. ~8 GB RAM.
3. Minecraft **1.20.1** + **Forge 47.4.10**.
4. New world: Survival, Hard, **cheats ON** (smoke / force functions). Terralith default.
5. Private pack — do not upload.

Prism can import the same zip. Do **not** import the old 0.1 `.mrpack` kitchen sink.

## Java 17

Forge 1.20.1 wants **17**. Java 21 / 25 will fight you. Temurin 17 is fine.

```
java -version
# openjdk version "17.x.x"
```

## Rallous Continuity (ours — not Fabric)

**Rallous Continuity** is a **lang overlay**: Elector / Waaagh / Under-Empire / von Carstein / Dawi / herd / temple-city / Bloodbound. It is **not** the Fabric **Continuity** connected-textures mod. That Fabric-leaning jar stays **out** so the instance boots.

`options.txt` already puts Rallous Continuity last (on) in pack order. If a profile resets packs: Options → Resource Packs → move **Rallous Continuity** up. Without it, Recruits still says Team 2 / Recruit.

## Boot fail

Send `crash-*-fml.txt`. Grim sky, gothic font, Complementary Unbound are expected. The Fabric Continuity mod must stay absent.
