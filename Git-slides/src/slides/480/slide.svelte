<script lang="ts">
	export const props = { background: '#0d1117' };  // GitHub dark background
	import { onMount, onDestroy } from 'svelte';

	// ─── Boids config ───────────────────────────────────────────────
	const MAX_SPEED   = 5.6;
	const MAX_FORCE   = 0.07;
	const SEP_RADIUS  = 30;
	const ALI_RADIUS  = 65;
	const COH_RADIUS  = 75;
	const SEP_W       = 1.6;
	const ALI_W       = 1.0;
	const COH_W       = 0.9;
	const EDGE_MARGIN = 80;
	const EDGE_W      = 2.5;
	const TRI         = 8;  // triangle half-size

	// ─── Tree config ────────────────────────────────────────────────
	const DEPTH    = 9;     // 2^8 = 256 leaves
	const B_ANGLE  = 0.42;  // branch split angle (radians)
	const B_RATIO  = 0.67;  // branch length multiplier per level
	const GROW_MS  = 320;   // ms to grow each depth level
	const HOLD_MS  = 1000;  // ms to hold the completed tree
	const FADE_MS  = 1500;  // ms to fade tree while boids launch

	// ─── Colors — Git · LeetCode · YouTube brand palette ───────────
	// Git:      #F05032  (orange-red)
	// LeetCode: #FFA116  (amber-orange)
	// YouTube:  #FF0000  (red)
	const COLORS = [
		'rgba(240, 80, 50, 0.92)',   // Git orange-red
		'rgba(255,161, 22, 0.92)',   // LeetCode amber
		'rgba(255,  0,  0, 0.90)',   // YouTube red
		'rgba(255,255,255, 0.88)',   // white (shared by all three brands)
		'rgba(255,110, 50, 0.88)',   // Git/LeetCode blend
	];

	// ─── Types ──────────────────────────────────────────────────────
	interface V2     { x: number; y: number }
	interface Boid   { pos: V2; vel: V2; acc: V2; color: string }
	interface Branch { x1: number; y1: number; x2: number; y2: number; level: number }
	interface Leaf   { x: number; y: number; angle: number }

	// ─── Vec2 helpers ───────────────────────────────────────────────
	const v2  = (x = 0, y = 0): V2   => ({ x, y });
	const add = (a: V2, b: V2): V2   => ({ x: a.x + b.x, y: a.y + b.y });
	const sub = (a: V2, b: V2): V2   => ({ x: a.x - b.x, y: a.y - b.y });
	const scl = (a: V2, s: number): V2 => ({ x: a.x * s, y: a.y * s });
	const mag = (a: V2)            => Math.sqrt(a.x * a.x + a.y * a.y);
	const nrm = (a: V2): V2        => { const m = mag(a); return m ? scl(a, 1 / m) : v2(); };
	const lim = (a: V2, mx: number): V2 => mag(a) > mx ? scl(nrm(a), mx) : a;
	const dst = (a: V2, b: V2)     => mag(sub(a, b));

	// ─── State ──────────────────────────────────────────────────────
	let canvas:   HTMLCanvasElement | null = null;
	let sentinel: HTMLSpanElement;
	let rafId  = 0;
	let boids:    Boid[]   = [];
	let branches: Branch[] = [];
	let leaves:   Leaf[]   = [];

	type Phase = 'growing' | 'holding' | 'fading' | 'flocking';
	let phase:     Phase = 'growing';
	let phaseT     = 0;
	let treeAlpha  = 1;

	// ─── Tree builder ───────────────────────────────────────────────
	function buildTree(w: number, h: number) {
		branches = [];
		leaves   = [];

		(function grow(x: number, y: number, angle: number, len: number, level: number) {
			const x2 = x + Math.cos(angle) * len;
			const y2 = y + Math.sin(angle) * len;
			branches.push({ x1: x, y1: y, x2, y2, level });
			if (level === DEPTH) {
				leaves.push({ x: x2, y: y2, angle });
			} else {
				const l2 = len * B_RATIO;
				grow(x2, y2, angle - B_ANGLE, l2, level + 1);
				grow(x2, y2, angle + B_ANGLE, l2, level + 1);
			}
		})(w / 2, h, -Math.PI / 2, h * 0.25, 1);
	}

	// ─── Branch stroke color: warm gold trunk → bright teal tips ───
	function branchColor(level: number, alpha: number) {
		// Trunk: deep charcoal → Git orange-red → LeetCode amber at tips
		const t = (level - 1) / (DEPTH - 1); // 0 = trunk, 1 = leaves
		// Lerp: #3a3a3a → #F05032 → #FFA116
		let r: number, g: number, b: number;
		if (t < 0.5) {
			const s = t * 2;
			r = Math.round(58  + s * (240 - 58));   // 58 → 240
			g = Math.round(58  + s * (80  - 58));   // 58 → 80
			b = Math.round(58  + s * (50  - 58));   // 58 → 50
		} else {
			const s = (t - 0.5) * 2;
			r = Math.round(240 + s * (255 - 240));  // 240 → 255
			g = Math.round(80  + s * (161 - 80));   // 80  → 161
			b = Math.round(50  + s * (22  - 50));   // 50  → 22
		}
		return `rgba(${r},${g},${b},${alpha})`;
	}

	// ─── Draw one branch, optionally partially (progress 0–1) ───────
	function drawBranch(ctx: CanvasRenderingContext2D, b: Branch, alpha: number, progress = 1) {
		const ex = b.x1 + (b.x2 - b.x1) * progress;
		const ey = b.y1 + (b.y2 - b.y1) * progress;
		ctx.save();
		ctx.beginPath();
		ctx.moveTo(b.x1, b.y1);
		ctx.lineTo(ex, ey);
		ctx.strokeStyle = branchColor(b.level, alpha);
		ctx.lineWidth   = Math.max(0.5, (DEPTH - b.level + 1) * 1.2);
		ctx.lineCap     = 'round';
		ctx.stroke();
		ctx.restore();
	}

	// ─── Draw a triangle ────────────────────────────────────────────
	function drawTriangle(
		ctx: CanvasRenderingContext2D,
		x: number, y: number,
		angle: number,
		color: string,
	) {
		ctx.save();
		ctx.translate(x, y);
		ctx.rotate(angle);
		ctx.beginPath();
		ctx.moveTo(TRI * 1.5, 0);
		ctx.lineTo(-TRI, TRI * 0.7);
		ctx.lineTo(-TRI, -TRI * 0.7);
		ctx.closePath();
		ctx.fillStyle = color;
		ctx.fill();
		ctx.restore();
	}

	// ─── Boid steering ──────────────────────────────────────────────
	const steer = (a: V2): V2 => lim(a, MAX_FORCE);

	function separation(b: Boid): V2 {
		let s = v2(), n = 0;
		for (const o of boids) {
			if (o === b) continue;
			const d = dst(b.pos, o.pos);
			if (d < SEP_RADIUS && d > 0) { s = add(s, scl(nrm(sub(b.pos, o.pos)), 1 / d)); n++; }
		}
		if (!n) return v2();
		return steer(sub(scl(nrm(scl(s, 1 / n)), MAX_SPEED), b.vel));
	}

	function alignment(b: Boid): V2 {
		let s = v2(), n = 0;
		for (const o of boids) {
			if (o === b) continue;
			if (dst(b.pos, o.pos) < ALI_RADIUS) { s = add(s, o.vel); n++; }
		}
		if (!n) return v2();
		return steer(sub(scl(nrm(scl(s, 1 / n)), MAX_SPEED), b.vel));
	}

	function cohesion(b: Boid): V2 {
		let s = v2(), n = 0;
		for (const o of boids) {
			if (o === b) continue;
			if (dst(b.pos, o.pos) < COH_RADIUS) { s = add(s, o.pos); n++; }
		}
		if (!n) return v2();
		return steer(sub(scl(nrm(sub(scl(s, 1 / n), b.pos)), MAX_SPEED), b.vel));
	}

	function edgeForce(b: Boid, w: number, h: number): V2 {
		let fx = 0, fy = 0;
		if (b.pos.x < EDGE_MARGIN)     fx += (EDGE_MARGIN - b.pos.x) / EDGE_MARGIN;
		if (b.pos.x > w - EDGE_MARGIN) fx -= (b.pos.x - (w - EDGE_MARGIN)) / EDGE_MARGIN;
		if (b.pos.y < EDGE_MARGIN)     fy += (EDGE_MARGIN - b.pos.y) / EDGE_MARGIN;
		if (b.pos.y > h - EDGE_MARGIN) fy -= (b.pos.y - (h - EDGE_MARGIN)) / EDGE_MARGIN;
		return steer(scl({ x: fx, y: fy }, MAX_SPEED));
	}

	function stepBoid(b: Boid, w: number, h: number) {
		b.acc = add(add(scl(separation(b), SEP_W), scl(alignment(b), ALI_W)),
		             add(scl(cohesion(b),   COH_W), scl(edgeForce(b, w, h), EDGE_W)));
		b.vel = lim(add(b.vel, b.acc), MAX_SPEED);
		b.pos = add(b.pos, b.vel);
		b.acc = v2();
		b.pos.x = Math.max(0, Math.min(w, b.pos.x));
		b.pos.y = Math.max(0, Math.min(h, b.pos.y));
	}

	// ─── Main render loop ───────────────────────────────────────────
	function loop(ctx: CanvasRenderingContext2D, w: number, h: number, now: number) {
		const elapsed = now - phaseT;

		// ── GROWING: tree appears level-by-level ──────────────────
		if (phase === 'growing') {
			ctx.fillStyle = '#0d1117';
			ctx.fillRect(0, 0, w, h);

			for (const b of branches) {
				const ls = (b.level - 1) * GROW_MS;
				if (elapsed < ls) continue;
				const progress = Math.min(1, (elapsed - ls) / GROW_MS);
				drawBranch(ctx, b, 1, progress);
			}

			// Once all levels drawn, show leaf triangles then hold
			if (elapsed >= DEPTH * GROW_MS) {
				for (let i = 0; i < leaves.length; i++) {
					const l = leaves[i];
					drawTriangle(ctx, l.x, l.y, l.angle, COLORS[i % COLORS.length]);
				}
				phase  = 'holding';
				phaseT = now;
			}

		// ── HOLDING: full tree + all 256 triangles ────────────────
		} else if (phase === 'holding') {
			ctx.fillStyle = '#0d1117';
			ctx.fillRect(0, 0, w, h);

			for (const b of branches) drawBranch(ctx, b, 1);
			for (let i = 0; i < leaves.length; i++) {
				const l = leaves[i];
				drawTriangle(ctx, l.x, l.y, l.angle, COLORS[i % COLORS.length]);
			}

			if (elapsed > HOLD_MS) {
				// Spawn boids at every leaf tip pointing in branch direction
				boids = leaves.map((l, i) => ({
					pos:   v2(l.x, l.y),
					vel:   scl(v2(Math.cos(l.angle), Math.sin(l.angle)), 0.6 + Math.random() * 0.8),
					acc:   v2(),
					color: COLORS[i % COLORS.length],
				}));
				treeAlpha = 1;
				phase  = 'fading';
				phaseT = now;
			}

		// ── FADING: tree fades out as boids launch ────────────────
		} else if (phase === 'fading') {
			ctx.fillStyle = 'rgba(13,17,23,0.30)';
			ctx.fillRect(0, 0, w, h);

			treeAlpha = Math.max(0, 1 - elapsed / FADE_MS);
			if (treeAlpha > 0) {
				for (const b of branches) drawBranch(ctx, b, treeAlpha * 0.9);
			}

			for (const boid of boids) {
				stepBoid(boid, w, h);
				drawTriangle(ctx, boid.pos.x, boid.pos.y,
					Math.atan2(boid.vel.y, boid.vel.x), boid.color);
			}

			if (elapsed > FADE_MS) {
				phase  = 'flocking';
				phaseT = now;
			}

		// ── FLOCKING: full Boids simulation ──────────────────────
		} else {
			ctx.fillStyle = 'rgba(13,17,23,0.28)';
			ctx.fillRect(0, 0, w, h);

			for (const boid of boids) {
				stepBoid(boid, w, h);
				drawTriangle(ctx, boid.pos.x, boid.pos.y,
					Math.atan2(boid.vel.y, boid.vel.x), boid.color);
			}
		}

		rafId = requestAnimationFrame(t => loop(ctx, w, h, t));
	}

	// ─── Restart (called when slide becomes active) ──────────────────
	function restart(w: number, h: number) {
		boids     = [];
		treeAlpha = 1;
		phase     = 'growing';
		phaseT    = performance.now();
		buildTree(w, h);
	}

	// ─── Lifecycle ──────────────────────────────────────────────────
	onMount(() => {
		canvas = document.createElement('canvas');
		const w = (canvas.width  = window.innerWidth);
		const h = (canvas.height = window.innerHeight);
		canvas.style.cssText =
			'position:fixed;top:0;left:0;width:100vw;height:100vh;z-index:0;pointer-events:none;display:none;';
		document.body.appendChild(canvas);

		const ctx = canvas.getContext('2d')!;
		ctx.fillStyle = '#0d1117';
		ctx.fillRect(0, 0, w, h);

		restart(w, h);
		rafId = requestAnimationFrame(t => loop(ctx, w, h, t));

		// Show/hide + restart when Reveal.js switches slides
		const section = sentinel.closest('section');
		if (section) {
			const show = () => { if (canvas) canvas.style.display = 'block'; };
			const hide = () => { if (canvas) canvas.style.display = 'none'; };

			section.classList.contains('present') ? show() : hide();

			const mo = new MutationObserver(() => {
				if (section.classList.contains('present')) {
					show();
					restart(w, h);
				} else {
					hide();
				}
			});
			mo.observe(section, { attributes: true, attributeFilter: ['class'] });
			(canvas as any)._mo = mo;
		}
	});

	onDestroy(() => {
		if (typeof cancelAnimationFrame !== 'undefined') cancelAnimationFrame(rafId);
		(canvas as any)?._mo?.disconnect();
		canvas?.remove();
	});
</script>

<!-- Sentinel: lets us walk up to the Reveal.js <section> to watch its `present` class -->
<span bind:this={sentinel} style="display:none;" aria-hidden="true"></span>

<!-- Text stays centered by Reveal's flex layout; canvas lives on <body> -->
<h1 class="relative text-7xl font-serif text-white font-normal tracking-wide drop-shadow-lg" style="z-index:1;">
	Questions?
</h1>
