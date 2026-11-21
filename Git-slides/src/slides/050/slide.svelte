<script lang="ts">
	import { onMount } from 'svelte';
	import { tween } from '@animotion/motion';

	let containerEl: HTMLElement | undefined = $state();

	// Animotion tween for standalone walls
	const wallsProgress = tween(0, { duration: 650 });
	let wallsActive = $state(false);
	let isRunning = false;
	let playCount = 0;

	function resetAnimation() {
		playCount++;
		isRunning = false;
		wallsProgress.reset();
		wallsActive = false;
	}

	async function playAnimation() {
		if (isRunning) return;
		isRunning = true;
		const currentSession = ++playCount;
		wallsProgress.reset();
		wallsActive = true;
		await wallsProgress.to(1, { duration: 650 });
		if (currentSession !== playCount) return;
		isRunning = false;
	}

	onMount(() => {
		const section = containerEl?.closest('section');
		if (!section) return;

		if (section.classList.contains('present')) {
			playAnimation();
		} else {
			resetAnimation();
		}

		const handleIn = () => playAnimation();
		const handleOut = () => resetAnimation();

		section.addEventListener('in', handleIn);
		section.addEventListener('out', handleOut);

		const observer = new MutationObserver(() => {
			if (section.classList.contains('present')) {
				if (!isRunning) playAnimation();
			} else {
				resetAnimation();
			}
		});

		observer.observe(section, { attributes: true, attributeFilter: ['class'] });

		if (section.classList.contains('present')) {
			playAnimation();
		}

		return () => {
			section.removeEventListener('in', handleIn);
			section.removeEventListener('out', handleOut);
			observer.disconnect();
			resetAnimation();
		};
	});
</script>

<!-- Slide 050: Top LeetCode Data Structures & Algorithms (100% Visible by Default, Floating Layout) -->
<div bind:this={containerEl} class="relative w-full max-w-5xl min-h-[600px] flex flex-col items-center justify-center select-none px-4 py-2 text-white">
	<!-- Ambient Background Glows -->
	<div class="absolute -top-10 left-1/3 w-72 h-72 bg-fuchsia-600/15 rounded-full blur-3xl pointer-events-none"></div>
	<div class="absolute -bottom-10 right-1/3 w-72 h-72 bg-cyan-600/15 rounded-full blur-3xl pointer-events-none"></div>
	<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-96 h-96 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>

	<!-- Minimal Floating Header -->
	<div class="mb-5 z-30">
		<div class="px-5 py-1.5 rounded-full bg-neutral-900/85 backdrop-blur-md border {wallsActive ? 'border-amber-400 shadow-[0_0_25px_rgba(251,191,36,0.4)]' : 'border-white/15 shadow-xl'} flex items-center gap-2.5 transition-all duration-500">
			<span class="w-2.5 h-2.5 rounded-full {wallsActive ? 'bg-amber-400 animate-ping' : 'bg-cyan-400 animate-pulse'}"></span>
			<span class="text-xs font-semibold tracking-wider {wallsActive ? 'text-amber-300 font-bold' : 'text-neutral-100'}">
				{wallsActive ? 'Self-Contained Primitives (Each Stands By Itself)' : 'Top LeetCode Patterns & Primitives'}
			</span>
		</div>
	</div>

	<!-- 8 Floating Diagrams Grid (4 Columns x 2 Rows) - ALWAYS 100% VISIBLE -->
	<div class="grid grid-cols-4 gap-x-6 gap-y-7 w-full max-w-4xl opacity-100">

		<!-- 01. Two Pointers / Sliding Window -->
		<div class="float-card-1 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-pink-500/50 shadow-2xl shadow-pink-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-pink-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-pink-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-pink-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-pink-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-pink-950 text-pink-300 border border-pink-500/50 rounded shadow">UNIT 01</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-pink-400 tracking-wide">Two Pointers</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(244,114,182,0.4)]">
						{#each [2, 7, 11, 15, 20] as val, i}
							<g transform="translate({12 + i * 28}, 22)">
								<rect width="24" height="20" rx="3" fill={i >= 1 && i <= 3 ? '#831843' : '#371424'} stroke={i >= 1 && i <= 3 ? '#f472b6' : '#701a75'} stroke-width="1.2" />
								<text x="12" y="14" font-size="9" fill={i >= 1 && i <= 3 ? '#fdf2f8' : '#a21caf'} font-family="monospace" text-anchor="middle" font-weight="bold">{val}</text>
							</g>
						{/each}

						<path d="M 40 18 L 40 14 L 124 14 L 124 18" fill="none" stroke="#ec4899" stroke-width="1.4" stroke-dasharray="2 1" />
						<text x="82" y="10" font-size="7" fill="#fbcfe8" font-family="monospace" text-anchor="middle">Window [L..R]</text>

						<g transform="translate(46, 44)">
							<polygon points="6,0 0,6 12,6" fill="#f472b6" />
							<text x="6" y="14" font-size="8" fill="#fbcfe8" font-family="monospace" text-anchor="middle" font-weight="bold">L</text>
						</g>

						<g transform="translate(102, 44)">
							<polygon points="6,0 0,6 12,6" fill="#f472b6" />
							<text x="6" y="14" font-size="8" fill="#fbcfe8" font-family="monospace" text-anchor="middle" font-weight="bold">R</text>
						</g>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-pink-300 font-semibold' : ''}">Sliding Window • O(N)</span>
			</div>
		</div>

		<!-- 02. Binary Search -->
		<div class="float-card-2 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-sky-500/50 shadow-2xl shadow-sky-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-sky-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-sky-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-sky-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-sky-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-sky-950 text-sky-300 border border-sky-500/50 rounded shadow">UNIT 02</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-sky-400 tracking-wide">Binary Search</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(56,189,248,0.4)]">
						{#each [
							{ v: 1, state: 'dim' },
							{ v: 3, state: 'dim' },
							{ v: 8, state: 'mid' },
							{ v: 14, state: 'active' },
							{ v: 22, state: 'active' }
						] as cell, i}
							<g transform="translate({12 + i * 28}, 20)">
								<rect
									width="24"
									height="22"
									rx="3"
									fill={cell.state === 'mid' ? '#0369a1' : cell.state === 'active' ? '#0c4a6e' : '#1e293b'}
									stroke={cell.state === 'mid' ? '#38bdf8' : cell.state === 'active' ? '#0284c7' : '#475569'}
									stroke-width={cell.state === 'mid' ? '1.6' : '1'}
									opacity={cell.state === 'dim' ? 0.35 : 1}
								/>
								<text
									x="12"
									y="15"
									font-size="9.5"
									fill={cell.state === 'mid' ? '#ffffff' : cell.state === 'active' ? '#e0f2fe' : '#64748b'}
									font-family="monospace"
									text-anchor="middle"
									font-weight={cell.state === 'mid' ? 'bold' : 'normal'}
								>
									{cell.v}
								</text>
							</g>
						{/each}

						<line x1="14" y1="31" x2="64" y2="31" stroke="#ef4444" stroke-width="1.2" opacity="0.6" stroke-dasharray="2 2" />

						<g transform="translate(68, 44)">
							<polygon points="6,0 0,6 12,6" fill="#38bdf8" />
							<text x="6" y="14" font-size="7.5" fill="#7dd3fc" font-family="monospace" text-anchor="middle" font-weight="bold">MID</text>
						</g>

						<g transform="translate(124, 44)">
							<polygon points="6,0 0,6 12,6" fill="#38bdf8" />
							<text x="6" y="14" font-size="7.5" fill="#7dd3fc" font-family="monospace" text-anchor="middle" font-weight="bold">R</text>
						</g>

						<text x="80" y="10" font-size="7.5" fill="#38bdf8" font-family="monospace" text-anchor="middle">target = 8 ✓</text>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-sky-300 font-semibold' : ''}">Git Bisect • O(log N)</span>
			</div>
		</div>

		<!-- 03. Dynamic Programming (DP) -->
		<div class="float-card-3 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-emerald-500/50 shadow-2xl shadow-emerald-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-emerald-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-emerald-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-emerald-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-emerald-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-emerald-950 text-emerald-300 border border-emerald-500/50 rounded shadow">UNIT 03</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-emerald-400 tracking-wide">Dynamic Prog.</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(52,211,153,0.4)]">
						<g transform="translate(32, 4)">
							<rect x="0" y="0" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />
							<rect x="22" y="0" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />
							<rect x="44" y="0" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />
							<rect x="66" y="0" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />

							<rect x="0" y="13" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />
							<rect x="22" y="13" width="22" height="13" fill="#047857" stroke="#34d399" stroke-width="1" />
							<rect x="44" y="13" width="22" height="13" fill="#047857" stroke="#34d399" stroke-width="1" />
							<rect x="66" y="13" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />

							<rect x="0" y="26" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />
							<rect x="22" y="26" width="22" height="13" fill="#047857" stroke="#34d399" stroke-width="1" />
							<rect x="44" y="26" width="22" height="13" fill="#10b981" stroke="#a7f3d0" stroke-width="1.4" />
							<rect x="66" y="26" width="22" height="13" fill="#064e3b" stroke="#059669" stroke-width="0.8" />

							<text x="11" y="10" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">0</text>
							<text x="33" y="10" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">1</text>
							<text x="55" y="10" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">2</text>
							<text x="77" y="10" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">3</text>

							<text x="33" y="23" font-size="7" fill="#a7f3d0" font-family="monospace" text-anchor="middle">1</text>
							<text x="55" y="23" font-size="7" fill="#a7f3d0" font-family="monospace" text-anchor="middle">2</text>
							<text x="33" y="36" font-size="7" fill="#a7f3d0" font-family="monospace" text-anchor="middle">2</text>
							<text x="55" y="36" font-size="8" fill="#ffffff" font-family="monospace" text-anchor="middle" font-weight="bold">4</text>

							<path d="M 55 24 L 55 26" stroke="#34d399" stroke-width="1.2" />
							<path d="M 38 33 L 44 33" stroke="#34d399" stroke-width="1.2" />
						</g>

						<text x="80" y="58" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">dp[i][j] = dp[i-1][j] + dp[i][j-1]</text>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-emerald-300 font-semibold' : ''}">Myers Diff / LCS • O(N×M)</span>
			</div>
		</div>

		<!-- 04. Trees & BST -->
		<div class="float-card-4 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-fuchsia-500/50 shadow-2xl shadow-fuchsia-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-fuchsia-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-fuchsia-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-fuchsia-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-fuchsia-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-fuchsia-950 text-fuchsia-300 border border-fuchsia-500/50 rounded shadow">UNIT 04</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-fuchsia-400 tracking-wide">Trees & BST</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(217,70,239,0.4)]">
						<line x1="80" y1="12" x2="44" y2="28" stroke="#c026d3" stroke-width="1.6" />
						<line x1="80" y1="12" x2="116" y2="28" stroke="#c026d3" stroke-width="1.6" />
						<line x1="44" y1="28" x2="26" y2="46" stroke="#e879f9" stroke-width="1.2" />
						<line x1="44" y1="28" x2="62" y2="46" stroke="#e879f9" stroke-width="1.2" />
						<line x1="116" y1="28" x2="98" y2="46" stroke="#e879f9" stroke-width="1.2" />
						<line x1="116" y1="28" x2="134" y2="46" stroke="#e879f9" stroke-width="1.2" />

						<g transform="translate(80, 12)">
							<circle r="9" fill="#a21caf" stroke="#f5d0fe" stroke-width="1.4" />
							<text y="3.5" font-size="8" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">10</text>
						</g>
						<g transform="translate(44, 28)">
							<circle r="8" fill="#86198f" stroke="#f5d0fe" stroke-width="1.2" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">5</text>
						</g>
						<g transform="translate(116, 28)">
							<circle r="8" fill="#86198f" stroke="#f5d0fe" stroke-width="1.2" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">15</text>
						</g>
						<g transform="translate(26, 46)">
							<circle r="6.5" fill="#701a75" stroke="#f0abfc" stroke-width="1" />
							<text y="2.5" font-size="6.5" fill="#fdf4ff" font-family="monospace" text-anchor="middle">2</text>
						</g>
						<g transform="translate(62, 46)">
							<circle r="6.5" fill="#701a75" stroke="#f0abfc" stroke-width="1" />
							<text y="2.5" font-size="6.5" fill="#fdf4ff" font-family="monospace" text-anchor="middle">7</text>
						</g>
						<g transform="translate(98, 46)">
							<circle r="6.5" fill="#701a75" stroke="#f0abfc" stroke-width="1" />
							<text y="2.5" font-size="6.5" fill="#fdf4ff" font-family="monospace" text-anchor="middle">12</text>
						</g>
						<g transform="translate(134, 46)">
							<circle r="6.5" fill="#701a75" stroke="#f0abfc" stroke-width="1" />
							<text y="2.5" font-size="6.5" fill="#fdf4ff" font-family="monospace" text-anchor="middle">20</text>
						</g>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-fuchsia-300 font-semibold' : ''}">Merkle Tree / DFS • O(N)</span>
			</div>
		</div>

		<!-- 05. Graph Traversal (BFS / DFS / DAG) -->
		<div class="float-card-3 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-amber-500/50 shadow-2xl shadow-amber-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-amber-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-amber-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-amber-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-amber-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-amber-950 text-amber-300 border border-amber-500/50 rounded shadow">UNIT 05</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-amber-400 tracking-wide">Graph (BFS/DFS)</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(245,158,11,0.4)]">
						<path d="M 28 32 L 64 16" stroke="#f59e0b" stroke-width="1.6" />
						<polygon points="64,16 57,18 61,22" fill="#f59e0b" />

						<path d="M 28 32 L 64 48" stroke="#f59e0b" stroke-width="1.6" />
						<polygon points="64,48 61,42 57,46" fill="#f59e0b" />

						<path d="M 72 16 L 108 32" stroke="#fbbf24" stroke-width="1.6" />
						<polygon points="108,32 101,31 103,36" fill="#fbbf24" />

						<path d="M 72 48 L 108 32" stroke="#fbbf24" stroke-width="1.6" />
						<polygon points="108,32 103,28 101,33" fill="#fbbf24" />

						<path d="M 116 32 L 142 32" stroke="#fde047" stroke-width="1.8" />
						<polygon points="142,32 136,29 136,35" fill="#fde047" />

						<g transform="translate(24, 32)">
							<circle r="8.5" fill="#d97706" stroke="#fef3c7" stroke-width="1.4" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">u</text>
						</g>
						<g transform="translate(68, 16)">
							<circle r="8" fill="#f59e0b" stroke="#fef3c7" stroke-width="1.4" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">v1</text>
						</g>
						<g transform="translate(68, 48)">
							<circle r="8" fill="#f59e0b" stroke="#fef3c7" stroke-width="1.4" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">v2</text>
						</g>
						<g transform="translate(112, 32)">
							<circle r="9" fill="#fbbf24" stroke="#ffffff" stroke-width="1.6" />
							<text y="3" font-size="8" fill="#451a03" font-family="monospace" text-anchor="middle" font-weight="bold">w</text>
						</g>
						<g transform="translate(144, 32)">
							<circle r="6.5" fill="#f59e0b" stroke="#fef3c7" stroke-width="1" />
							<text y="2.5" font-size="6" fill="#fff" font-family="monospace" text-anchor="middle">z</text>
						</g>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-amber-300 font-semibold' : ''}">Commit DAG • O(V+E)</span>
			</div>
		</div>

		<!-- 06. Heap / Priority Queue -->
		<div class="float-card-4 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-purple-500/50 shadow-2xl shadow-purple-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-purple-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-purple-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-purple-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-purple-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-purple-950 text-purple-300 border border-purple-500/50 rounded shadow">UNIT 06</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-purple-400 tracking-wide">Min / Max Heap</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(192,132,252,0.4)]">
						<line x1="80" y1="18" x2="48" y2="34" stroke="#a855f7" stroke-width="1.6" />
						<line x1="80" y1="18" x2="112" y2="34" stroke="#a855f7" stroke-width="1.6" />
						<line x1="48" y1="34" x2="32" y2="52" stroke="#c084fc" stroke-width="1.2" />
						<line x1="48" y1="34" x2="64" y2="52" stroke="#c084fc" stroke-width="1.2" />
						<line x1="112" y1="34" x2="96" y2="52" stroke="#c084fc" stroke-width="1.2" />

						<g transform="translate(80, 18)">
							<circle r="9" fill="#6b21a8" stroke="#e9d5ff" stroke-width="1.6" />
							<text y="3.5" font-size="8.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">1</text>
						</g>

						<path d="M 80 8 L 80 2" stroke="#f472b6" stroke-width="1.4" />
						<text x="80" y="6" font-size="6" fill="#f472b6" font-family="monospace" text-anchor="middle">pop(min)</text>

						<g transform="translate(48, 34)">
							<circle r="7.5" fill="#581c87" stroke="#d8b4fe" stroke-width="1.2" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle">3</text>
						</g>
						<g transform="translate(112, 34)">
							<circle r="7.5" fill="#581c87" stroke="#d8b4fe" stroke-width="1.2" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle">6</text>
						</g>

						<g transform="translate(32, 52)">
							<circle r="6" fill="#3b0764" stroke="#c084fc" stroke-width="1" />
							<text y="2.5" font-size="6" fill="#faf5ff" font-family="monospace" text-anchor="middle">7</text>
						</g>
						<g transform="translate(64, 52)">
							<circle r="6" fill="#3b0764" stroke="#c084fc" stroke-width="1" />
							<text y="2.5" font-size="6" fill="#faf5ff" font-family="monospace" text-anchor="middle">4</text>
						</g>
						<g transform="translate(96, 52)">
							<circle r="6" fill="#3b0764" stroke="#c084fc" stroke-width="1" />
							<text y="2.5" font-size="6" fill="#faf5ff" font-family="monospace" text-anchor="middle">9</text>
						</g>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-purple-300 font-semibold' : ''}">Packfile Priority • O(log K)</span>
			</div>
		</div>

		<!-- 07. Trie (Prefix Tree) -->
		<div class="float-card-1 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-teal-500/50 shadow-2xl shadow-teal-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-teal-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-teal-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-teal-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-teal-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-teal-950 text-teal-300 border border-teal-500/50 rounded shadow">UNIT 07</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-teal-400 tracking-wide">Trie (Prefix)</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(45,212,191,0.4)]">
						<g transform="translate(40, 14)">
							<circle r="7.5" fill="#134e4a" stroke="#2dd4bf" stroke-width="1.4" />
							<text y="3" font-size="7" fill="#ccfbf1" font-family="monospace" text-anchor="middle">root</text>
						</g>

						<line x1="40" y1="14" x2="80" y2="28" stroke="#14b8a6" stroke-width="1.6" />
						<g transform="translate(80, 28)">
							<circle r="8" fill="#0f766e" stroke="#5eead4" stroke-width="1.3" />
							<text y="3" font-size="8" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">g</text>
						</g>

						<line x1="80" y1="28" x2="116" y2="18" stroke="#2dd4bf" stroke-width="1.4" />
						<g transform="translate(116, 18)">
							<circle r="7.5" fill="#115e59" stroke="#5eead4" stroke-width="1.2" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle">i</text>
						</g>

						<line x1="116" y1="18" x2="146" y2="18" stroke="#2dd4bf" stroke-width="1.4" />
						<g transform="translate(146, 18)">
							<circle r="8" fill="#0d9488" stroke="#99f6e4" stroke-width="1.5" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">t*</text>
						</g>

						<line x1="80" y1="28" x2="116" y2="44" stroke="#2dd4bf" stroke-width="1.4" />
						<g transform="translate(116, 44)">
							<circle r="8" fill="#0d9488" stroke="#99f6e4" stroke-width="1.5" />
							<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">o*</text>
						</g>

						<text x="36" y="52" font-size="6.5" fill="#5eead4" font-family="monospace">words: "git", "go"</text>
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-teal-300 font-semibold' : ''}">Hex Prefix Trie • O(L)</span>
			</div>
		</div>

		<!-- 08. Monotonic Stack -->
		<div class="float-card-2 flex flex-col items-center text-center relative group">
			{#if wallsProgress.current > 0 || wallsActive}
				<div
					class="absolute inset-0 -m-2 rounded-2xl bg-neutral-900/95 backdrop-blur-xl border border-orange-500/50 shadow-2xl shadow-orange-950/40 transition-all duration-500 pointer-events-none"
					style="opacity: {Math.max(wallsProgress.current, wallsActive ? 1 : 0)};"
				>
					<div class="absolute -top-1 -left-1 w-2.5 h-2.5 border-t-2 border-l-2 border-orange-400 rounded-tl-xs"></div>
					<div class="absolute -top-1 -right-1 w-2.5 h-2.5 border-t-2 border-r-2 border-orange-400 rounded-tr-xs"></div>
					<div class="absolute -bottom-1 -left-1 w-2.5 h-2.5 border-b-2 border-l-2 border-orange-400 rounded-bl-xs"></div>
					<div class="absolute -bottom-1 -right-1 w-2.5 h-2.5 border-b-2 border-r-2 border-orange-400 rounded-br-xs"></div>
					<span class="absolute -top-2.5 right-2 px-1.5 py-0.2 text-[8px] font-mono font-bold bg-orange-950 text-orange-300 border border-orange-500/50 rounded shadow">UNIT 08</span>
				</div>
			{/if}

			<div class="relative z-10 w-full flex flex-col items-center">
				<div class="flex items-center gap-1.5 mb-1.5">
					<span class="text-xs font-bold text-orange-400 tracking-wide">Monotonic Stack</span>
				</div>

				<div class="w-full h-24 flex items-center justify-center p-1">
					<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(249,115,22,0.4)]">
						<g transform="translate(20, 6)">
							<rect width="28" height="52" rx="3" fill="#431407" stroke="#ea580c" stroke-width="1.2" />
							<rect x="2" y="36" width="24" height="14" fill="#9a3412" stroke="#ea580c" stroke-width="0.8" />
							<text x="14" y="47" font-size="8.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">75</text>

							<rect x="2" y="20" width="24" height="14" fill="#c2410c" stroke="#ea580c" stroke-width="0.8" />
							<text x="14" y="31" font-size="8.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">71</text>

							<rect x="2" y="4" width="24" height="14" fill="#ea580c" stroke="#fed7aa" stroke-width="1" />
							<text x="14" y="15" font-size="8.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">69</text>
						</g>

						<g transform="translate(74, 10)">
							<rect width="24" height="16" rx="2" fill="#f97316" stroke="#ffedd5" stroke-width="1.4" />
							<text x="12" y="12" font-size="9" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">73</text>
						</g>

						<path d="M 72 18 L 50 18" stroke="#f97316" stroke-width="1.4" stroke-dasharray="2 1" />
						<polygon points="50,15 44,18 50,21" fill="#f97316" />
					</svg>
				</div>
				<span class="text-[11px] text-neutral-400 font-mono mt-1 {wallsActive ? 'text-orange-300 font-semibold' : ''}">Daily Temps / Histograms • O(N)</span>
			</div>
		</div>

	</div>

</div>

<style>
	@keyframes float-1 {
		0%, 100% { transform: translateY(0px) rotate(0deg); }
		50% { transform: translateY(-8px) rotate(0.8deg); }
	}
	@keyframes float-2 {
		0%, 100% { transform: translateY(0px) rotate(0deg); }
		50% { transform: translateY(9px) rotate(-0.9deg); }
	}
	@keyframes float-3 {
		0%, 100% { transform: translateY(0px) rotate(0deg); }
		50% { transform: translateY(-7px) rotate(-0.6deg); }
	}
	@keyframes float-4 {
		0%, 100% { transform: translateY(0px) rotate(0deg); }
		50% { transform: translateY(8px) rotate(0.7deg); }
	}

	.float-card-1 {
		animation: float-1 5.2s ease-in-out infinite;
	}
	.float-card-2 {
		animation: float-2 6.1s ease-in-out infinite;
	}
	.float-card-3 {
		animation: float-3 5.7s ease-in-out infinite;
	}
	.float-card-4 {
		animation: float-4 6.5s ease-in-out infinite;
	}
</style>
