# Tooling — Cursor, IntelliJ, JDKs, MDK, art

Opinionated. Short. **2026-08-31** sources at the bottom. If a tool is not on this page, you do not need it to start [FIRST-MOD.md](FIRST-MOD.md).

---

## How Cursor and IntelliJ share the desk

This is not a religious war.

| Tool | What it is *for* on this project |
| --- | --- |
| **Cursor** | Agents, docs, `lessons/`, pack TOML, Java *editing*, GitHub, MCP (live Forge docs). You think and write here. |
| **IntelliJ IDEA** | The Java gold standard: Gradle import, `runClient` / `runData` / `runServer`, breakpoints in Forge event handlers, Mixin/AT navigation, the **Minecraft Development** plugin. You **compile and debug** here. |

Forge’s own 1.20.1 getting-started page **explicitly supports Eclipse and IntelliJ**; VS Code/Cursor work with extra Gradle/Java extensions and `genVSCodeRuns`. That is accurate: Cursor will autocomplete and refactor; it will still lose to IntelliJ on mixed mapping sources, run-config JVM args, and “why is this mixin not applying.”

**Practical split**

1. Extract the Forge MDK once.
2. Open that folder in **IntelliJ** → trust Gradle → `genIntellijRuns` → play with the debugger.
3. Open the **same folder** (or the git repo that contains it) in **Cursor** for agents and docs.
4. Do not commit both IDEs’ junk. Keep `.idea/` and `.vscode/` out of git unless you have a reason. Prefer `gradlew` tasks so either editor can build.

Community Edition vs Ultimate: as of IntelliJ **2025.3**, JetBrains ships a **unified** IntelliJ IDEA. Core Java/Kotlin stays free after the 30-day Ultimate trial. You do **not** need to pay to write a Forge mod. Download: https://www.jetbrains.com/idea/download/

IntelliJ plugin (install *in IntelliJ* → Plugins → Marketplace):

- **Minecraft Development** — https://plugins.jetbrains.com/plugin/8327-minecraft-development — also https://mcdev.io/ — GitHub https://github.com/minecraft-dev/MinecraftDev — latest release seen **1.8.15-2026.1** (2026-04-14). Templates go stale; **still use the official Forge MDK zip**, then let the plugin help with Mixins, `mods.toml`, and Mcfunction/JSON.

---

## Java 17 vs the language server

**Project / Gradle toolchain: Java 17.** Minecraft 1.20.1 Forge requires a **64-bit Java 17 JDK**. Forge “recommends and officially supports Eclipse Temurin.”

**Do not** set `java.toolchain.languageVersion = 21` on this MDK. Java 21 is for newer Minecraft (1.20.5+ / 1.21 lines), not this pack.

**Cursor/VS Code gotcha (2026):** Language Support for Java (Red Hat) may insist on **JDK 21+** to *launch the JDT language server*, while your *mod* still compiles with 17.

| JDK | Role |
| --- | --- |
| Temurin **17** | `JAVA_HOME` for `gradlew`, IntelliJ project SDK, `java.configuration.runtimes` `name: JavaSE-17` |
| Temurin **21** (optional) | Only `java.jdt.ls.java.home` if the Java extension refuses to start |

If you only install 21 and point Gradle at it, ForgeGradle 1.20.1 will hurt you. If you only install 17 and Cursor’s Java pack is recent, set the LS home to 21 *or* pin an older Red Hat Java extension. Do not “upgrade the game” to make the editor happy.

---

## Must install before writing a line of Java

Desktop downloads first. Cursor extensions immediately after.

### A. Desktop / SDKs

| # | What | Official URL | Why *this* project |
| --- | --- | --- | --- |
| 1 | **Git** | https://git-scm.com/downloads | Lessons, PRs, this repo. Windows extra: https://gitforwindows.org/ |
| 2 | **Eclipse Temurin JDK 17** (64-bit **JDK**) | https://adoptium.net/temurin/releases/?version=17 · install notes https://adoptium.net/installation/?variant=openjdk17 | Forge 1.20.1 compile + runtime. Not 8, not 21. |
| 3 | **Prism Launcher** | https://prismlauncher.org/download/ · GitHub releases https://github.com/PrismLauncher/PrismLauncher/releases (11.0.3 as of 2026-07-11) | Isolated 1.20.1 Forge instances; import `pack/*.mrpack`. Better than stuffing jars into the Mojang launcher. |
| 4 | **Forge 1.20.1 MDK** | https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html | Skeleton Gradle project. Click **MDK** (skip the ad), **not** Installer. Recommended **47.4.10** matches this pack’s 47.4.x line; Latest was **47.4.23** on 2026-08-31. Docs: https://docs.minecraftforge.net/en/1.20.1/gettingstarted/ |
| 5 | **IntelliJ IDEA** | https://www.jetbrains.com/idea/download/ | Debugger + Gradle + Minecraft Development plugin. |
| 6 | **Blockbench** (desktop app) | https://www.blockbench.net/ | Banner / item / later entity models. Mojang’s own creator-tools page points here; it is **not** a Mojang download. |
| 7 | **Minecraft: Java Edition** (purchased) | https://www.minecraft.net/en-us/store/minecraft-java-bedrock-edition-pc | Legal. EULA: https://www.minecraft.net/en-us/eula |

**Mappings (not a separate installer):** the MDK defaults to Mojang **official** mappings. Add **Parchment** for parameter names + javadocs:

- Site: https://parchmentmc.org/docs/getting-started
- Maven: https://maven.parchmentmc.org/
- Librarian (ForgeGradle plugin): https://github.com/ParchmentMC/Librarian/blob/dev/docs/FORGEGRADLE.md
- **1.20.1 release export:** `2023.09.03` (confirmed from https://maven.parchmentmc.org/org/parchmentmc/data/parchment-1.20.1/maven-metadata.xml — `<release>2023.09.03</release>`). In `build.gradle`:

```gradle
mappings channel: 'parchment', version: '2023.09.03-1.20.1'
```

(Use double quotes if your Groovy parser is picky; see Parchment issue #351.)

**Mixin:** ships **with Forge**. You do not download a second Mixin zip. Wiki: https://github.com/SpongePowered/Mixin/wiki and https://github.com/SpongePowered/Mixin/wiki/Mixins-on-Minecraft-Forge . **Do not Mixin in week one.** Allegiance v1 is events + SavedData + networking. Mixins are for “vanilla will not let me,” not for planting a banner.

### B. Cursor extensions (VS Marketplace IDs)

Cursor’s Extensions view installs the same IDs as VS Code. **Must:**

| Extension | ID | Why |
| --- | --- | --- |
| **Extension Pack for Java** | `vscjava.vscode-java-pack` | Bundles Language Support for Java (Red Hat `redhat.java`), Debugger for Java, Test Runner, Maven (ignore Maven), Java Project Manager. Marketplace: https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack |
| **Language Support for Java (Red Hat)** | `redhat.java` | Comes with the pack; listed so you can pin/downgrade if a 2026 JDT regression hits Gradle. https://marketplace.visualstudio.com/items?itemName=redhat.java |
| **Gradle for Java** | `vscjava.vscode-gradle` | Forge getting-started: VS Code needs this to import Gradle the way IntelliJ does natively. Tasks: `runClient`, `runData`, `build`. https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-gradle |
| **GitHub Pull Requests** | `GitHub.vscode-pull-request-github` | This repo’s PR reviews. https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github |

If the Java pack and Gradle fight over `build/libs` jars (known Red Hat issue in 2026), set `"java.jdt.ls.scalaSupport.enabled": false` and run **Java: Clean Language Server Workspace**. Do not disable Gradle.

### C. Cursor MCP (day one)

Install from **Customize → MCPs** or `~/.cursor/mcp.json` / project `.cursor/mcp.json`. Docs: https://cursor.com/docs/context/mcp

| Server | Why now | Official |
| --- | --- | --- |
| **Context7** | Pulls *current* Forge/Gradle/Java docs into the agent. Without it you get 1.12 `FMLPreInitializationEvent` fanfic. | https://context7.com/ · `@upstash/context7-mcp` or hosted `https://mcp.context7.com/mcp` |
| **GitHub** (official) | Issues, PR text, code search on `rallous-system`. | https://github.com/github/github-mcp-server — Cursor guide: `docs/installation-guides/install-cursor.md`. Hosted: `https://api.githubcopilot.com/mcp/` with a PAT. **Do not** use deprecated npm `@modelcontextprotocol/server-github` (unsupported since 2025-04). |

Node.js LTS (https://nodejs.org/) is required only if you run local `npx` MCP servers. Hosted Context7/GitHub HTTP transports skip that.

**Cursor “plugins”** (Marketplace bundles of rules/skills/MCP, https://cursor.com/docs/plugins): install a **GitHub** or **Context7** plugin if the Marketplace offers the same servers one-click. Do not hunt for a “Minecraft Forge Cursor plugin” — language support is the Java/Gradle *extensions* above. There is no official Mojang Cursor plugin.

---

## Strongly useful for this project

Install in week two, not instead of the must list.

| Tool | URL | Why |
| --- | --- | --- |
| **Temurin JDK 21** | https://adoptium.net/temurin/releases/?version=21 | Optional LS runtime only (see above). |
| **Markdown All in One** | `yzhang.markdown-all-in-one` https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one | This repo is mostly Markdown. TOC, lists, preview. |
| **XML** (Red Hat) | `redhat.vscode-xml` | `mods.toml` is TOML-ish in resources; XML still helps `mixins.json` adjacent configs and some Gradle metadata. Optional if IntelliJ owns those files. |
| **Datapack Helper Plus / Spyglass** | `SPGoding.datapack-language-server` https://marketplace.visualstudio.com/items?itemName=SPGoding.datapack-language-server · docs https://spyglassmc.com/ | Ladder step 0 is a datapack. Completions for `.mcfunction` / pack JSON. Use when you open a `pack.mcmeta`, not on day one of Java. |
| **GIMP** or **Krita** | https://www.gimp.org/ · https://krita.org/ | 32×32 item textures if you hate Blockbench’s 2D paint. Both FOSS. **Aseprite** is excellent and *paid* (https://www.aseprite.org/) — buy it or use **LibreSprite** (https://libresprite.github.io/); do not pirate Aseprite. |
| **packwiz** | https://packwiz.infra.link/ | This repo already has `pack/pack.toml`. Use it when you pin *your* mod into the Frontier pack. |
| **Modrinth App** (optional vs Prism) | https://modrinth.com/app | Fine if you already live there; Prism is still the default in [README.md](README.md). |
| **GitHub CLI `gh`** | https://cli.github.com/ | Nice locally; this environment already has it. Not required to compile. |
| **JDK flight / VisualVM** | skip until a tick loop is hot | Diplomacy SavedData will not need a profiler in v1. |

**MixinExtras** (`io.github.llamalad7:mixinextras-forge`): only when you actually write a mixin. Not a download; a Gradle dep.

---

## Later / skip for now

Mentioned so you do **not** install them this month.

| Tool | When it becomes real | Why skip |
| --- | --- | --- |
| **Unreal Engine 5** | ASA / a from-scratch 3D prototype | 100 GB and a different career. Minecraft is the cheap table. |
| **ARK: Survival Ascended DevKit** | After Allegiance v1 taught persistence + replication | Official: https://devkit.studiowildcard.com/getting-started/cooking-publishing — Wildcard *wants* mods; still a week of Epic launcher + cook. Map lessons, don’t dual-wield engines. |
| **Epic Games Launcher / Visual Studio (MSVC)** | Required by the ASA DevKit later | Not for Forge. |
| **Blender** full pipeline | Custom creature for ASA or a GeckoLib mob | Banner v1 is a vanilla-shaped pole + wool. Learn Blender *after* a jar exists. |
| **Substance / Marvelous Designer** | Never for a first Minecraft mod | Paid texture/cloth stacks. |
| **MCreator** | Never for *this* mod | Generates undebuggable soup. You need SavedData and packets you can read. |
| **Sinytra Connector / Fabric on this pack** | After Forge pack is stable | [RESEARCH.md](RESEARCH.md) already said no. |
| **Sentry MCP / Sentry Java agent** | When you have users | Day-one crash reports are `latest.log`. Sentry is for shipped packs. |
| **Datadog, Linear, Stripe plugins** | Unrelated | Noise. |
| **GitLens / 12 Git GUIs** | If you already love them | GitHub PR extension is enough. |
| **Minecraft-branded “mod maker” VS Code toys** | No | They target datapacks or Bedrock. You are on Forge Java. |

---

## Recommended IntelliJ run hygiene

After MDK extract:

```bash
./gradlew genIntellijRuns
./gradlew runClient          # or the IntelliJ “runClient” config
./gradlew runData            # data generation (recipes, lang)
./gradlew build              # jar → build/libs
```

VS Code / Cursor: `./gradlew genVSCodeRuns` then Run and Debug. Same Gradle, different button.

Give the **run** JVM 4 GB while developing the tiny mod; give **Prism** 8–12 GB for the full Rallous pack. Do not debug Allegiance inside the 69-mod kitchen sink until the jar works alone.

Enable Forge debug in the MDK `build.gradle` `runs` block (already typical):

```text
forge.logging.markers=REGISTRIES
forge.logging.console.level=debug
```

Logs: [LOGGING-AND-LESSONS.md](LOGGING-AND-LESSONS.md).

---

## Art pipeline (legal)

You paint **original** banners and envoy skins. Tone-refs in parentheses in design docs are **not** a licence to trace TW loading screens or GW heraldry.

| Do | Don’t |
| --- | --- |
| Blockbench cuboids, your palette | GW aquila, eight-pointed *logo*, ripped TW flags |
| Vanilla banner patterns + your `Item` | “Empire state troop” ripped resource packs |
| Later: GeckoLib *your* meshes | Fossils Revival models in an ASA upload you don’t own |

---

## Sources (accessed 2026-08-31)

- https://docs.minecraftforge.net/en/1.20.1/gettingstarted/
- https://docs.minecraftforge.net/en/1.20.1/datastorage/saveddata/
- https://docs.minecraftforge.net/en/1.20.1/datastorage/capabilities/
- https://files.minecraftforge.net/net/minecraftforge/forge/index_1.20.1.html
- https://adoptium.net/temurin/releases/?version=17
- https://parchmentmc.org/docs/getting-started
- https://maven.parchmentmc.org/org/parchmentmc/data/parchment-1.20.1/maven-metadata.xml (`release` = `2023.09.03`)
- https://github.com/SpongePowered/Mixin/wiki
- https://plugins.jetbrains.com/plugin/8327-minecraft-development
- https://blog.jetbrains.com/idea/2025/12/intellij-idea-unified-release/
- https://prismlauncher.org/download/
- https://www.blockbench.net/
- https://minecraft.net/en-us/creator/tools (Blockbench as third-party)
- https://cursor.com/docs/context/mcp
- https://cursor.com/docs/plugins
- https://cursor.com/docs/context/rules
- https://github.com/github/github-mcp-server
- https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack
- https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-gradle
- https://marketplace.visualstudio.com/items?itemName=redhat.java
- https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-pull-request-github
- https://spyglassmc.com/
