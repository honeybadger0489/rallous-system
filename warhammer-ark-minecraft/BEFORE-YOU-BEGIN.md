# Before you begin

Read this **before** you write Java, download a dinosaur model, or open Unreal. The vision already lives in this folder. Your job now is a **desk, a JDK, and one small Forge mod** — not the whole Rallous MMO.

Companion docs: [TOOLING.md](TOOLING.md) (what to install and why) · [FIRST-MOD.md](FIRST-MOD.md) (what to ship first) · [LOGGING-AND-LESSONS.md](LOGGING-AND-LESSONS.md) · [ORGANIZATION.md](ORGANIZATION.md). Legal: [LEGAL-NOTES.md](LEGAL-NOTES.md) · [IP-FANTASY.md](IP-FANTASY.md).

**Locked runtime:** Minecraft **1.20.1** + **Forge 47.4.x** · **Java 17** (Eclipse Temurin). Do not start on Java 21 / NeoForge 1.21 “because it’s newer.”

Accessed **2026-08-31**.

---

## 0. The one-line plan

Ship **Rallous Allegiance**: a warband banner you craft and plant, a claimed camp, standing with analogue factions, one envoy, one ally/war verb saved on the world. Then stop and write a lesson. Details: [FIRST-MOD.md](FIRST-MOD.md).

---

## 1. Accounts (do these first; they are not optional)

| Account | Why | Official |
| --- | --- | --- |
| **Minecraft: Java Edition** | Legal client. Forge MDK `runClient` and Prism both need a real Microsoft/Mojang login. | https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc |
| **Microsoft account** tied to that purchase | Launcher + Prism auth. | Same store page |
| **GitHub** | This repo (`honeybadger0489/rallous-system`) is source of truth. Issues, PRs, not a folder on the Desktop. | https://github.com/ |
| **Modrinth** (free) | Import the v0.1 pack; later publish *your* original mod. | https://modrinth.com/ |
| **CurseForge** (free, later) | Magistu Epic Knights and the ASA pipeline live here. Do **not** need it on day one. | https://www.curseforge.com/ |

Do **not** create a “Warhammer” or “Ark” branded CurseForge/Modrinth project. Public name is **Rallous**. See [IP-FANTASY.md](IP-FANTASY.md).

No cracked launchers. No 9Minecraft jars. No GW/Wildcard asset packs.

---

## 2. Downloads — install this set before a single Java file

Full “why” and later/skip lists: [TOOLING.md](TOOLING.md). **Must-install (seven):**

1. **Git** — https://git-scm.com/downloads (Windows: https://git-scm.com/download/win or https://gitforwindows.org/)
2. **Eclipse Temurin JDK 17** (64-bit, **JDK** not JRE) — https://adoptium.net/temurin/releases/?version=17
3. **Prism Launcher** — https://prismlauncher.org/download/
4. **Minecraft Forge 1.20.1 MDK** (Recommended **47.4.10** or Latest **47.4.x**; click **MDK**, not Installer) — https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html
5. **IntelliJ IDEA** (unified installer; core Java is free after the Ultimate trial) — https://www.jetbrains.com/idea/download/
6. **Blockbench** (desktop) — https://www.blockbench.net/
7. **This GitHub repo cloned** (you are already in it if you are reading this file in Cursor)

Optional **the same day** if Cursor MCP will not start: **Node.js LTS** — https://nodejs.org/ (needed for some local MCP servers, not for compiling the mod).

Verify JDK 17:

```bash
java -version
# openjdk version "17.x.x" ... Temurin
```

If that prints 21, 25, or 8, fix `JAVA_HOME` before you run Gradle. 1.20.1 Forge **compiles on 17**. Cursor’s Java language server may *want* a newer JDK to *run itself* — that is a separate install; see [TOOLING.md](TOOLING.md#java-17-vs-the-language-server).

---

## 3. Cursor plugins (extensions + MCP)

Cursor = VS Code–compatible **extensions** + Cursor **plugins/MCP**. Install from Cursor’s Extensions view (Open VSX / VS Marketplace IDs below). Full table: [TOOLING.md](TOOLING.md).

**Must install before writing Java**

| What | ID / where | Why |
| --- | --- | --- |
| **Extension Pack for Java** | `vscjava.vscode-java-pack` | Language support (Red Hat), debugger, tests. |
| **Gradle for Java** | `vscjava.vscode-gradle` | Forge is a Gradle project. Forge docs call this out for VS Code. |
| **GitHub Pull Requests** | `GitHub.vscode-pull-request-github` | Review this repo’s PRs in the editor. |

**MCP (day one, two servers)**

| Server | Why now |
| --- | --- |
| **Context7** | Live library docs (Forge/Gradle/Java) so the agent does not invent 1.12 APIs. |
| **GitHub** (official `github/github-mcp-server`) | Issues/PRs against *this* repo. |

Skip Sentry, Unreal, ASA DevKit MCP, and “50 game-dev plugins” until you have a jar in `build/libs`.

Also install **IntelliJ’s Minecraft Development plugin** *inside IntelliJ*, not Cursor: JetBrains Marketplace [Minecraft Development (plugin 8327)](https://plugins.jetbrains.com/plugin/8327-minecraft-development).

---

## 4. Folder layout (create this on disk)

Do **not** dump the MDK into the GitHub repo root. The repo is **docs + pack metadata + lessons**. The Java workspace is a **sibling** (or `mods/rallous-allegiance/` later, gitignored `build/` and `run/`).

Suggested home (Windows example; adjust drive):

```text
~/rallous/
  rallous-system/          ← this git clone (source of truth)
    warhammer-ark-minecraft/
      pack/                ← already exists; do not rewrite
      lessons/             ← you write here
      mods/                ← future: git submodule or nested project
  mdk-rallous-allegiance/  ← extracted Forge 1.20.1 MDK (day-one workspace)
  prism/                   ← Prism instances (the playable pack)
  art/                     ← Blockbench .bbmodel files (your originals)
```

First week you may keep the MDK **outside** git until `gradlew build` works, then move it to `warhammer-ark-minecraft/mods/rallous-allegiance/` with a proper `.gitignore` (no `run/`, no `build/`, no Minecraft jars). See [ORGANIZATION.md](ORGANIZATION.md).

---

## 5. First week (ordered; skip a day and you skip the week)

| Day | Done when | Not done when |
| --- | --- | --- |
| **1** | Accounts + seven downloads. `java -version` is 17. GitHub clone pulls. Prism launches **vanilla 1.20.1** once. | You imported the full 69-file pack and spent the night dying to Cataclysm. |
| **2** | Cursor Java pack + Gradle extension. IntelliJ opens. Minecraft Development plugin installed. Context7 MCP answers a Forge docs question. | You installed MCreator, 20 themes, and GitLens. |
| **3** | Forge **MDK extracted**, `gradlew genIntellijRuns` (or `genVSCodeRuns`) succeeds, **examplemod** `runClient` reaches the title screen. | You renamed packages for three hours and never launched. |
| **4** | Prism imports `pack/rallous-frontier-0.1.0.mrpack` **or** you play the existing instance. Walk one region. Take notes in `lessons/`. | You start rewriting `CAMPAIGN.md`. |
| **5** | Replace `examplemod` with `rallous_allegiance`. One **banner item** appears in the creative tab. Data gen emits the recipe. | Custom dinosaur entity. |
| **6** | Plant the banner. **SavedData** (or a level capability) remembers the camp chunk after `/reload` or a full restart. Log the claim at INFO. | Scoreboard hacks you will throw away. |
| **7** | Write `lessons/001-*.md` from the template. Read [FIRST-MOD.md](FIRST-MOD.md) milestones 3–4. **Stop.** Do not start a quest pack. | “I’ll just add taming real quick.” |

If day 3 fails, **do not** “just use Fabric.” Stay on 1.20.1 Forge; paste `latest.log` into a lesson, not into a rewrite of the vision.

---

## 6. Hard no’s for week one

- Unreal Engine, ASA DevKit, Blender full pipeline, Substance, Mixamo.
- Mixing Ice and Fire + Fossils + Alex’s Mobs as *your first code*.
- GW names, 40k gunpacks, ripped Ark models.
- A MOBA, an MMORPG backend, a custom dimension “Old World.”
- Java 21 as the **project** toolchain for this Minecraft version.

---

## 7. Where knowledge goes

| Kind | Put it |
| --- | --- |
| Invariants (no GW IP, 1.20.1 Forge, analogue names) | Project rule `.cursor/rules/rallous-modding.mdc` |
| Experiments (what you tried) | `lessons/` journal |
| Vision | Existing `CAMPAIGN.md` / `FACTIONS-AND-DIPLOMACY.md` — **do not clobber** |
| Runtime failures | Prism/`run/logs/latest.log` + a lesson that cites the logger line |

---

## Sources (accessed 2026-08-31)

- Forge Getting Started (Java 17 Temurin, MDK, VS Code Gradle plugin): https://docs.minecraftforge.net/en/1.20.1/gettingstarted/
- Forge 1.20.1 files (Recommended 47.4.10, Latest 47.4.23 on this date): https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html
- Adoptium Temurin 17: https://adoptium.net/temurin/releases/?version=17
- Prism: https://prismlauncher.org/download/
- Blockbench: https://www.blockbench.net/
- IntelliJ download: https://www.jetbrains.com/idea/download/
- Cursor MCP: https://cursor.com/docs/context/mcp
- Cursor plugins: https://cursor.com/docs/plugins
- Cursor rules: https://cursor.com/docs/context/rules
