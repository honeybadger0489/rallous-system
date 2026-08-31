(() => {
  "use strict";

  const canvas = document.getElementById("game");
  const ctx = canvas.getContext("2d");
  const W = canvas.width;
  const H = canvas.height;

  const overlay = document.getElementById("overlay");
  const overlayTitle = document.getElementById("overlay-title");
  const overlayBody = document.getElementById("overlay-body");
  const primaryBtn = document.getElementById("primary-btn");
  const hud = document.getElementById("hud");
  const hudWave = document.getElementById("hud-wave");
  const hudScore = document.getElementById("hud-score");
  const healthFill = document.getElementById("health-fill");

  const TOTAL_WAVES = 5;

  const state = {
    mode: "start", // start | playing | gameover | victory
    keys: new Set(),
    aim: { x: W / 2, y: 0 },
    firing: false,
    lastShot: 0,
    player: null,
    bullets: [],
    enemies: [],
    particles: [],
    wave: 0,
    waveEnemiesLeft: 0,
    spawnTimer: 0,
    score: 0,
    lastFrame: 0,
  };

  function newPlayer() {
    return { x: W / 2, y: H / 2, r: 16, speed: 260, hp: 100, maxHp: 100 };
  }

  function startGame() {
    state.player = newPlayer();
    state.bullets = [];
    state.enemies = [];
    state.particles = [];
    state.wave = 0;
    state.score = 0;
    state.mode = "playing";
    overlay.setAttribute("hidden", "");
    hud.removeAttribute("hidden");
    nextWave();
    updateHud();
  }

  function nextWave() {
    state.wave += 1;
    if (state.wave > TOTAL_WAVES) {
      victory();
      return;
    }
    state.waveEnemiesLeft = 4 + state.wave * 3;
    state.spawnTimer = 0;
    updateHud();
  }

  function spawnEnemy() {
    const edge = Math.floor(Math.random() * 4);
    let x = 0;
    let y = 0;
    if (edge === 0) { x = Math.random() * W; y = -20; }
    else if (edge === 1) { x = W + 20; y = Math.random() * H; }
    else if (edge === 2) { x = Math.random() * W; y = H + 20; }
    else { x = -20; y = Math.random() * H; }
    const speed = 55 + state.wave * 12 + Math.random() * 20;
    state.enemies.push({ x, y, r: 13, speed, hp: 1 + Math.floor(state.wave / 3) });
  }

  function fire(now) {
    const p = state.player;
    if (!p) return;
    if (now - state.lastShot < 130) return;
    state.lastShot = now;
    const dx = state.aim.x - p.x;
    const dy = state.aim.y - p.y;
    const len = Math.hypot(dx, dy) || 1;
    const speed = 620;
    state.bullets.push({
      x: p.x + (dx / len) * p.r,
      y: p.y + (dy / len) * p.r,
      vx: (dx / len) * speed,
      vy: (dy / len) * speed,
      r: 4,
      life: 1.4,
    });
  }

  function spawnParticles(x, y, color, count) {
    for (let i = 0; i < count; i += 1) {
      const a = Math.random() * Math.PI * 2;
      const s = 40 + Math.random() * 160;
      state.particles.push({
        x, y,
        vx: Math.cos(a) * s,
        vy: Math.sin(a) * s,
        life: 0.4 + Math.random() * 0.3,
        color,
      });
    }
  }

  function updateHud() {
    hudWave.textContent = Math.min(state.wave, TOTAL_WAVES);
    hudScore.textContent = state.score;
    const pct = state.player ? Math.max(0, state.player.hp / state.player.maxHp) : 0;
    healthFill.style.width = `${pct * 100}%`;
  }

  function gameOver() {
    state.mode = "gameover";
    showOverlay(
      "The Line Has Broken",
      `You held for wave ${Math.min(state.wave, TOTAL_WAVES)} with a score of ${state.score}. The frontier remembers the fallen.`,
      "Stand Again"
    );
  }

  function victory() {
    state.mode = "victory";
    showOverlay(
      "The Frontier Holds",
      `Every warband broken across ${TOTAL_WAVES} waves. Final score: ${state.score}. The Rallous System endures!`,
      "Play Again"
    );
  }

  function showOverlay(title, body, btn) {
    overlayTitle.textContent = title;
    overlayBody.textContent = body;
    primaryBtn.textContent = btn;
    overlay.removeAttribute("hidden");
  }

  function update(dt, now) {
    if (state.mode !== "playing") return;
    const p = state.player;

    let mx = 0;
    let my = 0;
    if (state.keys.has("a") || state.keys.has("arrowleft")) mx -= 1;
    if (state.keys.has("d") || state.keys.has("arrowright")) mx += 1;
    if (state.keys.has("w") || state.keys.has("arrowup")) my -= 1;
    if (state.keys.has("s") || state.keys.has("arrowdown")) my += 1;
    const mlen = Math.hypot(mx, my) || 1;
    p.x += (mx / mlen) * p.speed * dt;
    p.y += (my / mlen) * p.speed * dt;
    p.x = Math.max(p.r, Math.min(W - p.r, p.x));
    p.y = Math.max(p.r, Math.min(H - p.r, p.y));

    if (state.firing) fire(now);

    for (const b of state.bullets) {
      b.x += b.vx * dt;
      b.y += b.vy * dt;
      b.life -= dt;
    }
    state.bullets = state.bullets.filter(
      (b) => b.life > 0 && b.x > -20 && b.x < W + 20 && b.y > -20 && b.y < H + 20
    );

    if (state.waveEnemiesLeft > 0) {
      state.spawnTimer -= dt;
      if (state.spawnTimer <= 0) {
        spawnEnemy();
        state.waveEnemiesLeft -= 1;
        state.spawnTimer = Math.max(0.25, 0.9 - state.wave * 0.08);
      }
    }

    for (const e of state.enemies) {
      const dx = p.x - e.x;
      const dy = p.y - e.y;
      const len = Math.hypot(dx, dy) || 1;
      e.x += (dx / len) * e.speed * dt;
      e.y += (dy / len) * e.speed * dt;
    }

    for (const e of state.enemies) {
      for (const b of state.bullets) {
        if (b.dead) continue;
        const rr = e.r + b.r;
        if ((e.x - b.x) ** 2 + (e.y - b.y) ** 2 <= rr * rr) {
          b.dead = true;
          e.hp -= 1;
          if (e.hp <= 0) {
            e.dead = true;
            state.score += 10;
            spawnParticles(e.x, e.y, "#b3402f", 12);
          } else {
            spawnParticles(e.x, e.y, "#e0684d", 4);
          }
        }
      }
    }

    for (const e of state.enemies) {
      if (e.dead) continue;
      const rr = e.r + p.r;
      if ((e.x - p.x) ** 2 + (e.y - p.y) ** 2 <= rr * rr) {
        e.dead = true;
        p.hp -= 12;
        spawnParticles(p.x, p.y, "#6c8cc4", 10);
        if (p.hp <= 0) {
          p.hp = 0;
          updateHud();
          gameOver();
          return;
        }
      }
    }

    state.bullets = state.bullets.filter((b) => !b.dead);
    state.enemies = state.enemies.filter((e) => !e.dead);

    for (const pt of state.particles) {
      pt.x += pt.vx * dt;
      pt.y += pt.vy * dt;
      pt.life -= dt;
    }
    state.particles = state.particles.filter((pt) => pt.life > 0);

    if (state.waveEnemiesLeft === 0 && state.enemies.length === 0) {
      nextWave();
    }

    updateHud();
  }

  function drawBackground() {
    ctx.fillStyle = "#0d1420";
    ctx.fillRect(0, 0, W, H);
    ctx.strokeStyle = "rgba(108, 140, 196, 0.08)";
    ctx.lineWidth = 1;
    for (let x = 0; x <= W; x += 48) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, H);
      ctx.stroke();
    }
    for (let y = 0; y <= H; y += 48) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(W, y);
      ctx.stroke();
    }
  }

  function render() {
    drawBackground();

    for (const pt of state.particles) {
      ctx.globalAlpha = Math.max(0, pt.life * 2);
      ctx.fillStyle = pt.color;
      ctx.fillRect(pt.x - 2, pt.y - 2, 4, 4);
    }
    ctx.globalAlpha = 1;

    ctx.fillStyle = "#f2d27a";
    for (const b of state.bullets) {
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.fill();
    }

    for (const e of state.enemies) {
      ctx.fillStyle = "#b3402f";
      ctx.strokeStyle = "#e0684d";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(e.x, e.y, e.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
    }

    const p = state.player;
    if (p && state.mode === "playing") {
      const ang = Math.atan2(state.aim.y - p.y, state.aim.x - p.x);
      ctx.save();
      ctx.translate(p.x, p.y);
      ctx.rotate(ang);
      ctx.fillStyle = "#6c8cc4";
      ctx.strokeStyle = "#d8a24a";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(0, 0, p.r, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();
      ctx.fillStyle = "#d8a24a";
      ctx.fillRect(p.r - 4, -3, 16, 6);
      ctx.restore();
    }
  }

  function loop(now) {
    const t = now / 1000;
    const dt = Math.min(0.05, t - (state.lastFrame || t));
    state.lastFrame = t;
    update(dt, now);
    render();
    requestAnimationFrame(loop);
  }

  function pointerToCanvas(clientX, clientY) {
    const rect = canvas.getBoundingClientRect();
    return {
      x: ((clientX - rect.left) / rect.width) * W,
      y: ((clientY - rect.top) / rect.height) * H,
    };
  }

  canvas.addEventListener("mousemove", (e) => {
    const pos = pointerToCanvas(e.clientX, e.clientY);
    state.aim.x = pos.x;
    state.aim.y = pos.y;
  });

  canvas.addEventListener("mousedown", (e) => {
    e.preventDefault();
    if (state.mode !== "playing") return;
    const pos = pointerToCanvas(e.clientX, e.clientY);
    state.aim.x = pos.x;
    state.aim.y = pos.y;
    state.firing = true;
  });

  window.addEventListener("mouseup", () => {
    state.firing = false;
  });

  window.addEventListener("keydown", (e) => {
    const k = e.key.toLowerCase();
    if (["arrowup", "arrowdown", "arrowleft", "arrowright", " "].includes(k)) {
      e.preventDefault();
    }
    if (k === " ") {
      state.firing = true;
      return;
    }
    state.keys.add(k);
  });

  window.addEventListener("keyup", (e) => {
    const k = e.key.toLowerCase();
    if (k === " ") {
      state.firing = false;
      return;
    }
    state.keys.delete(k);
  });

  primaryBtn.addEventListener("click", () => {
    startGame();
  });

  // Expose minimal state for smoke testing / automation.
  window.__RALLOUS__ = state;

  requestAnimationFrame(loop);
})();
