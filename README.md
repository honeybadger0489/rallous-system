# rallous-system

**Rallous System — Warhammer Frontier** is a playable HTML title: a small,
self-contained browser game where you hold a frontier outpost against waves of
chaos warbands.

The game is pure client-side HTML5 Canvas + vanilla JavaScript — no build step
and no runtime dependencies. The only tooling is a static file server for local
development.

## Project layout

```
index.html        # Page shell, HUD, and start/overlay screens
src/styles.css    # Presentation
src/game.js       # Game loop, input, spawning, collisions
package.json      # Dev static-server scripts
```

## Getting started

Requires Node.js 18+ (ships with npm).

```bash
npm install      # installs the http-server dev dependency
npm run dev      # serves the title at http://localhost:8080
```

Then open http://localhost:8080 in a browser.

Because the title is fully static, you can also serve it with any static file
server, e.g. `python3 -m http.server 8080`.

## How to play

- **W A S D** / **Arrow keys** — move your ranger
- **Mouse** — aim
- **Click** / **Space** — fire
- Survive all 5 waves to hold the frontier.

## Cloud Agent environment

`.cursor/environment.json` configures the Cloud Agent development environment:
`npm install` as the install step and `npm run dev` (the static server on port
8080) as a persistent terminal.
