<script lang="ts">
	import { onMount } from 'svelte';
	import { tween, all } from '@animotion/motion';

	const entrance = tween(0, { duration: 600 });
	const circleStroke = tween(0, { duration: 900 });
	const ringGlow = tween(0, { duration: 800 });

	async function playEntrance() {
		await all(
			entrance.to(1, { duration: 500 }),
			circleStroke.to(1, { duration: 900 }),
			ringGlow.to(1, { duration: 800 })
		);
	}

	function resetEntrance() {
		entrance.reset();
		circleStroke.reset();
		ringGlow.reset();
	}

	onMount(() => {
		playEntrance();
	});

	export const props = {
		in: () => playEntrance(),
		out: () => resetEntrance()
	};
</script>

<!-- Slide 060: Highlighted Common LeetCode Patterns Powered in Git -->
<div class="relative w-full max-w-5xl min-h-[590px] flex flex-col items-center justify-center select-none px-4 py-2">
	
	<!-- Ambient Red Background Glow -->
	<div class="absolute -top-10 left-1/3 w-72 h-72 bg-rose-600/15 rounded-full blur-3xl pointer-events-none"></div>
	<div class="absolute -bottom-10 right-1/3 w-72 h-72 bg-red-600/10 rounded-full blur-3xl pointer-events-none"></div>

	<!-- Minimal Floating Header -->
	<div class="mb-5 z-20 transition-all duration-700" style="opacity: {entrance.current};">
		<div class="px-6 py-1.5 rounded-full bg-rose-950/80 backdrop-blur-md border border-rose-500/80 shadow-[0_0_25px_rgba(244,63,94,0.4)] flex items-center gap-2.5">
			<span class="w-2 h-2 rounded-full bg-rose-400 animate-ping"></span>
			<span class="text-xs font-bold tracking-wider text-rose-300 uppercase">
				Every LeetCode Pattern Powers Real Systems Architecture lol
			</span>
		</div>
	</div>

	<!-- 8 Highlighted Floating Diagrams Grid (4 Columns x 2 Rows) -->
	<div
		class="grid grid-cols-4 gap-x-6 gap-y-7 w-full max-w-4xl transition-all duration-700"
		style="opacity: {entrance.current}; transform: scale({0.95 + 0.05 * entrance.current});"
	>

		<!-- 01. Two Pointers -->
		<div class="float-card-1 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-pink-400 tracking-wide">Two Pointers</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(-2 80 50)"
					/>
				</svg>

				<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(244,114,182,0.4)]">
					{#each [2, 7, 11, 15, 20] as val, i}
						<g transform="translate({12 + i * 28}, 22)">
							<rect width="24" height="20" rx="3" fill={i >= 1 && i <= 3 ? '#831843' : '#371424'} stroke={i >= 1 && i <= 3 ? '#f472b6' : '#701a75'} stroke-width="1.2" />
							<text x="12" y="14" font-size="9" fill={i >= 1 && i <= 3 ? '#fdf2f8' : '#a21caf'} font-family="monospace" text-anchor="middle" font-weight="bold">{val}</text>
						</g>
					{/each}
					<path d="M 40 18 L 40 14 L 124 14 L 124 18" fill="none" stroke="#ec4899" stroke-width="1.4" stroke-dasharray="2 1" />
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
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Myers Diff Comparison</span>
		</div>

		<!-- 02. Binary Search -->
		<div class="float-card-2 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-sky-400 tracking-wide">Binary Search</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(1 80 50)"
					/>
				</svg>

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
					<text x="80" y="10" font-size="7.5" fill="#38bdf8" font-family="monospace" text-anchor="middle">git bisect run</text>
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Git Bisect & Packfile Search</span>
		</div>

		<!-- 03. Dynamic Programming -->
		<div class="float-card-3 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-emerald-400 tracking-wide">Dynamic Prog.</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(-3 80 50)"
					/>
				</svg>

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
						<text x="55" y="36" font-size="8" fill="#ffffff" font-family="monospace" text-anchor="middle" font-weight="bold">4</text>
					</g>
					<text x="80" y="58" font-size="7" fill="#6ee7b7" font-family="monospace" text-anchor="middle">LCS Edit Distance</text>
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Git Diff Engine</span>
		</div>

		<!-- 04. Trees & BST -->
		<div class="float-card-4 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-fuchsia-400 tracking-wide">Trees & BST</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(2 80 50)"
					/>
				</svg>

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
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Merkle Object Directory</span>
		</div>

		<!-- 05. Graph Traversal -->
		<div class="float-card-3 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-amber-400 tracking-wide">Graph (BFS/DFS)</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(-1 80 50)"
					/>
				</svg>

				<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(245,158,11,0.4)]">
					<path d="M 28 32 L 64 16" stroke="#f59e0b" stroke-width="1.6" />
					<path d="M 28 32 L 64 48" stroke="#f59e0b" stroke-width="1.6" />
					<path d="M 72 16 L 108 32" stroke="#fbbf24" stroke-width="1.6" />
					<path d="M 72 48 L 108 32" stroke="#fbbf24" stroke-width="1.6" />
					<path d="M 116 32 L 142 32" stroke="#fde047" stroke-width="1.8" />
					<g transform="translate(24, 32)">
						<circle r="8.5" fill="#d97706" stroke="#fef3c7" stroke-width="1.4" />
						<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">u</text>
					</g>
					<g transform="translate(68, 16)">
						<circle r="8" fill="#f59e0b" stroke="#fef3c7" stroke-width="1.4" />
						<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">v1</text>
					</g>
					<g transform="translate(112, 32)">
						<circle r="9" fill="#fbbf24" stroke="#ffffff" stroke-width="1.6" />
						<text y="3" font-size="8" fill="#451a03" font-family="monospace" text-anchor="middle" font-weight="bold">w</text>
					</g>
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Commit Graph & Merging</span>
		</div>

		<!-- 06. Heap / Priority Queue -->
		<div class="float-card-4 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-purple-400 tracking-wide">Min / Max Heap</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(2 80 50)"
					/>
				</svg>

				<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(192,132,252,0.4)]">
					<line x1="80" y1="18" x2="48" y2="34" stroke="#a855f7" stroke-width="1.6" />
					<line x1="80" y1="18" x2="112" y2="34" stroke="#a855f7" stroke-width="1.6" />
					<g transform="translate(80, 18)">
						<circle r="9" fill="#6b21a8" stroke="#e9d5ff" stroke-width="1.6" />
						<text y="3.5" font-size="8.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">1</text>
					</g>
					<g transform="translate(48, 34)">
						<circle r="7.5" fill="#581c87" stroke="#d8b4fe" stroke-width="1.2" />
						<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle">3</text>
					</g>
					<g transform="translate(112, 34)">
						<circle r="7.5" fill="#581c87" stroke="#d8b4fe" stroke-width="1.2" />
						<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle">6</text>
					</g>
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Packfile Delta Queues</span>
		</div>

		<!-- 07. Trie -->
		<div class="float-card-1 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-teal-400 tracking-wide">Trie (Prefix)</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(-2 80 50)"
					/>
				</svg>

				<svg viewBox="0 0 160 64" class="w-full h-full drop-shadow-[0_0_8px_rgba(45,212,191,0.4)]">
					<line x1="40" y1="14" x2="80" y2="28" stroke="#14b8a6" stroke-width="1.6" />
					<line x1="80" y1="28" x2="116" y2="18" stroke="#2dd4bf" stroke-width="1.4" />
					<line x1="116" y1="18" x2="146" y2="18" stroke="#2dd4bf" stroke-width="1.4" />
					<g transform="translate(40, 14)">
						<circle r="7.5" fill="#134e4a" stroke="#2dd4bf" stroke-width="1.4" />
						<text y="3" font-size="7" fill="#ccfbf1" font-family="monospace" text-anchor="middle">root</text>
					</g>
					<g transform="translate(80, 28)">
						<circle r="8" fill="#0f766e" stroke="#5eead4" stroke-width="1.3" />
						<text y="3" font-size="8" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">g</text>
					</g>
					<g transform="translate(146, 18)">
						<circle r="8" fill="#0d9488" stroke="#99f6e4" stroke-width="1.5" />
						<text y="3" font-size="7.5" fill="#fff" font-family="monospace" text-anchor="middle" font-weight="bold">t*</text>
					</g>
				</svg>
			</div>
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Hex Hash Autocomplete</span>
		</div>

		<!-- 08. Monotonic Stack -->
		<div class="float-card-2 flex flex-col items-center text-center relative">
			<div class="flex items-center gap-1.5 mb-1.5">
				<span class="text-xs font-bold text-orange-400 tracking-wide">Monotonic Stack</span>
				<span class="px-1.5 py-0.2 text-[8px] font-bold bg-rose-600/90 text-white rounded shadow animate-pulse">✓ IN GIT</span>
			</div>

			<div class="w-full h-24 flex items-center justify-center p-1 relative">
				<svg class="absolute inset-0 w-full h-full pointer-events-none -m-1" viewBox="0 0 160 100">
					<ellipse
						cx="80"
						cy="50"
						rx="74"
						ry="44"
						fill="none"
						stroke="#ef4444"
						stroke-width="2.2"
						stroke-dasharray="400"
						stroke-dashoffset={400 * (1 - circleStroke.current)}
						stroke-linecap="round"
						opacity={0.85 + 0.15 * ringGlow.current}
						transform="rotate(1 80 50)"
					/>
				</svg>

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
			<span class="text-[11px] text-rose-300 font-bold font-mono mt-1">Ancestry & Histograms</span>
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
