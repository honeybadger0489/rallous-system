# Legal notes — read before you publish anything

This is **not legal advice**. It is a field guide so the prototype stays in the “inspiration” lane. Laws and company guidelines change; check the official pages before you ship, monetize, or put a trailer on YouTube.

Accessed **2026-08-31**.

---

## 1. Games Workshop (Warhammer / 40k / Age of Sigmar)

GW is unusually strict. Their published IP guidelines (fan summary matching the official policy language) state:

- Fan **games and apps** based on GW characters and settings **must not be created** except under licence.
- Fan films/animations: same bar.
- Fan fiction/art/sites: non-commercial, no copied official art/text, must be clearly unofficial, no GW logos.
- Underlying rights in the *worlds and characters* stay with GW even when a fan draws them.
- Zero-tolerance list includes counterfeits, “imitation models,” recasts/scans, and unlicensed trademarks.

Sources:

- Games Workshop Intellectual Property Guidelines (fan reprint of GW policy text). https://40kfan.com/games-workshop-intellectual-property-guidelines/ — accessed 2026-08-31  
- Official GW page (live URL may redirect by region): https://www.games-workshop.com/en-US/Intellectual-Property-Guidelines — accessed 2026-08-31 (direct fetch of the GB URL returned 404 in this environment; use the regional site).  
- Spikey Bits reporting on GW IP updates. https://spikeybits.com/lookout-youtube-gw-just-updated-their-ip-guidelines/ — accessed 2026-08-31  

**What that means for this repo**

| Safer | Dangerous |
| --- | --- |
| Original names: Rallous, Black Tide, Crown-Beasts, Ash-Wights | Space Marine, Adeptus Astartes, bolter, chainsword, God-Emperor, Chaos Gods, Tyranid, Carnifex, Adeptus Mechanicus, Age of Sigmar faction names |
| Original silhouettes inspired by “gothic plate + monster island” | Copying GW sculpt/concept art into a resource pack or TaCZ gunpack |
| Linking to Hammercraft as *research* | Shipping Hammercraft / Tacz40k / Sons of the Empire in a public “Rallous” pack |
| Private experiments you never distribute | Public Modrinth/CurseForge pack titled “Warhammer 40k Survival” |

The default **Rallous Frontier** mrpack **excludes** all Warhammer-branded mods on purpose. They remain in `pack/catalog.json` under `tier: ip-overlay` so you know they exist — not so you publish them.

A Minecraft *mod* is still a **computer game/app** in GW’s wording. “It’s just a mod” is not a shield. “It’s non-commercial” is the bar for some *fan art/fiction*, **not** for unlicensed games.

If you ever want official 40k in a video game, that is a **licence** (the path Total War, Darktide, Space Marine 2 took) — not a CurseForge upload.

---

## 2. Mojang / Microsoft (Minecraft)

Minecraft EULA (Java) allows **Mods** you (or others) created that do **not** contain a substantial part of Mojang’s copyrightable code or content.

You **may**: distribute original mods, datapacks, resource packs; play a modded client you assembled.

You **may not**: distribute a **Modded Version** of the game client/server (no cracked/bundled Minecraft); sell mods for money; make third-party tools look official; ship hate/illegal content.

“Your cathedral is yours; the cobblestone block is Mojang’s.”

Source: https://www.minecraft.net/en-us/eula — accessed 2026-08-31  

Also follow [Minecraft Usage Guidelines](https://www.minecraft.net/en-us/usage-guidelines) (screenshots, videos, commercial use). They can change.

**Pack distribution:** ship **metadata** (mrpack, packwiz, this repo) that points at Modrinth/CurseForge. Do not zip Mojang’s `minecraft.jar`. Do not rehost other people’s mods if their licence forbids it — our download script hits **Modrinth CDN URLs already chosen by those authors**.

Many mods here are **All Rights Reserved**. You can *depend* on them in a pack; you cannot relicense their jars or strip credits.

---

## 3. Studio Wildcard / ARK: Survival Ascended

ASA **wants** mods. That is the opposite of GW.

- Mods go through **CurseForge**, often **cloud-cooked** for PC/console.  
- Official DevKit docs: https://devkit.studiowildcard.com/getting-started/cooking-publishing — accessed 2026-08-31  
- Hub: https://arksa.curseforge.com/ — accessed 2026-08-31  
- Contest/moderation language: submissions must follow CurseForge **and** Wildcard guidelines; **no unlicensed third-party IP**; no prohibited adult/illegal content. https://arkathon.curseforge.com/TC.html — accessed 2026-08-31  
- Fan content guidelines (Wildcard IP, not a licence to use *other* companies’ IP): https://survivetheark.com/index.php?/fan_content_guidelines/ — accessed 2026-08-31  

**What that means**

| Safer | Dangerous |
| --- | --- |
| Original Rallous creatures in the DevKit | Porting Minecraft Fossils models that you don’t own |
| Original engrams / tribes | Using Ark *and* GW names in one mod (“Space Marine Tek Suit”) |
| Studying how Ark taming/tribes feel | Shipping Ark map assets or Wildcard trademarks outside their rules |
| Premium mods only if you qualify and pass review | Assuming Minecraft EULA economics apply to ASA (they don’t) |

Wildcard can still take down anything that uses **their** IP outside the fan/mod rules, or anyone else’s IP (including GW). An ASA mod named “Warhammer 40k Island” would pick a fight with **both** companies.

---

## 4. Other people’s Minecraft mods

Each jar has its own licence (`license` in `pack/mods.json`: MIT, GPL, ARR, custom).

- **ARR / custom:** pack inclusion via official download is usually OK; redistributing modified jars is not.
- **GPL (Epic Fight, TaCZ, etc.):** source terms apply if you ship binaries you modified.
- **GeckoLib / Citadel / Create:** required libraries; keep them updated from Modrinth, don’t vendor forever.

Do not scrape 9Minecraft / random “free download” mirrors. We only documented **Modrinth and CurseForge** official files.

---

## 5. Recommended working policy for Rallous

1. **Minecraft prototype:** original names, original gunpacks, default pack = no GW-branded mods.  
2. **Private curiosity:** if you install Hammercraft in a single-player instance to *study feel*, do not record ads, do not publish the instance, do not merge it into Rallous branding.  
3. **Public pack / trailer / Patreon:** original IP only.  
4. **ASA port:** original creatures, original names, CurseForge pipeline, no GW, no ripped Minecraft assets you don’t own.  
5. **When in doubt, rename.** The fun (tame the apex, hold the wall, fear the night) does not need a trademark.

If this project ever needs a real licence (GW, Microsoft, Wildcard), talk to a lawyer and the rights holder **before** you announce.

Fantasy campaign analogue names, Total War workshop limits, and recommended public branding: [`IP-FANTASY.md`](IP-FANTASY.md).
