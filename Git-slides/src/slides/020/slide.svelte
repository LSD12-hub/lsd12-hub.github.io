<script lang="ts">
	import { Action, Notes } from '@animotion/core';
	import { tween } from '@animotion/motion';
	import { createTypewriter, generateFractalTree } from '$lib';

	const tw = createTypewriter('git checkout -b side-quest/build-git', { speed: 35 });

	// Animotion Tweens for the Fractal Tree
	const treeGrowth = tween(0, { duration: 900 });
	const spreadAngle = tween(0.35, { duration: 900 });
	const leafScale = tween(1, { duration: 350 });

	// Reactive derived fractal tree geometry computed via utility
	let tree = $derived.by(() => {
		return generateFractalTree({
			startX: 480,
			startY: 440,
			initialLength: 122,
			initialAngle: -Math.PI / 2,
			maxDepth: 8,
			growth: treeGrowth.current,
			spread: spreadAngle.current,
			lengthRatio: 0.735,
			baseStrokeWidth: 7,
			widthDecay: 0.7
		});
	});

	// Action 1: Type command & sprout initial trunk + primary levels
	async function step1() {
		await tw.start();
		await spreadAngle.to(0.42, { duration: 750 });
		await treeGrowth.to(4, { duration: 850 });
	}

	function undoStep1() {
		tw.reset();
		treeGrowth.reset();
		spreadAngle.reset();
		leafScale.reset();
	}

	// Action 2: Deep recursive explosion to depth 8 with blooming canopy
	async function step2() {
		await spreadAngle.to(0.47, { duration: 950 });
		await treeGrowth.to(8, { duration: 1200 });
		await leafScale.to(1.35, { duration: 250 });
		await leafScale.to(1.0, { duration: 250 });
	}

	function undoStep2() {
		treeGrowth.to(4, { duration: 400 });
		spreadAngle.to(0.42, { duration: 400 });
		leafScale.to(1, { duration: 200 });
	}

	export const props = {
		out: () => {
			tw.reset();
			treeGrowth.reset();
			spreadAngle.reset();
			leafScale.reset();
		}
	};
</script>

<Notes>
	- Enjoy side quests instead of actual work <br>
	- side quest lead to other things <br>
	- Eventually they lead to escape <br>
</Notes>

<!-- Action 1: Command + Initial Sprout -->
<Action do={step1} undo={undoStep1} />

<!-- Action 2: Full Recursive Fractal Bloom -->
<Action do={step2} undo={undoStep2} />

<!-- Slide 020: Large Recursive Fractal Tree Branching Visual -->
<div class="flex flex-col items-center justify-center max-w-6xl w-full text-center px-2">
	<div class="w-full bg-neutral-950/90 border border-neutral-800 rounded-2xl p-6 shadow-2xl text-left">
		<!-- Typed Command Prompt & Live Stats -->
		<div
			class="font-mono text-base bg-black/90 px-5 py-3.5 rounded-xl border border-emerald-500/40 text-emerald-400 shadow-inner mb-4 flex items-center justify-between min-h-[54px]"
		>
			<div class="flex items-center">
				<span class="text-neutral-500 mr-2">$</span>
				{#if !tw.hasStarted}
					<span class="inline-block w-2.5 h-5 bg-emerald-400 align-middle animate-pulse"></span>
				{:else}
					<span>{tw.text}</span>
					{#if !tw.isDone}
						<span class="inline-block w-2.5 h-5 bg-emerald-400 ml-1.5 align-middle animate-pulse"
						></span>
					{/if}
				{/if}
			</div>

			{#if treeGrowth.current > 0}
				<div
					class="hidden sm:flex items-center gap-2.5 text-xs font-mono px-3.5 py-1.5 rounded-lg bg-neutral-900 border border-neutral-800 text-neutral-300"
				>
					<span
						class="inline-block w-2.5 h-2.5 rounded-full {treeGrowth.current >= 7
							? 'bg-fuchsia-400 animate-ping'
							: 'bg-emerald-400 animate-pulse'}"
					></span>
					<span>depth: {Math.floor(treeGrowth.current)} / 8</span>
					<span class="text-neutral-600">•</span>
					<span>branches: {tree.branches.length}</span>
				</div>
			{/if}
		</div>

		<!-- Full-Width Large SVG Fractal Tree Display -->
		<div class="bg-neutral-900/80 p-4 rounded-xl border border-neutral-800 overflow-hidden relative">
			<svg width="960" height="480" viewBox="0 0 960 480" class="w-full h-auto max-h-[58vh]">
				<defs>
					<!-- Subtle Background Grid Pattern -->
					<pattern id="grid-pattern" width="28" height="28" patternUnits="userSpaceOnUse">
						<circle cx="14" cy="14" r="0.9" fill="#374151" opacity="0.35" />
					</pattern>

					<!-- Glow Filter for High-Order Branches & Leaves -->
					<filter id="fractal-glow" x="-30%" y="-30%" width="160%" height="160%">
						<feGaussianBlur stdDeviation="4" result="coloredBlur" />
						<feMerge>
							<feMergeNode in="coloredBlur" />
							<feMergeNode in="SourceGraphic" />
						</feMerge>
					</filter>

					<!-- Root Node Ambient Radial Glow -->
					<radialGradient id="root-glow" cx="50%" cy="50%" r="50%">
						<stop offset="0%" stop-color="#10b981" stop-opacity="0.85" />
						<stop offset="100%" stop-color="#10b981" stop-opacity="0" />
					</radialGradient>
				</defs>

				<!-- Subtle Background Grid -->
				<rect width="960" height="480" fill="url(#grid-pattern)" />

				<!-- Root Anchor Marker -->
				<circle cx="480" cy="440" r="22" fill="url(#root-glow)" />
				<circle cx="480" cy="440" r="6" fill="#10b981" />
				<text
					x="480"
					y="462"
					fill="#6ee7b7"
					font-size="12"
					font-family="monospace"
					text-anchor="middle"
				>
					HEAD
				</text>

				<!-- Render Fractal Branches -->
				{#each tree.branches as b (b.id)}
					<line
						x1={b.x1}
						y1={b.y1}
						x2={b.x2}
						y2={b.y2}
						stroke={b.color}
						stroke-width={b.width}
						stroke-linecap="round"
						filter={b.depth >= 4 ? 'url(#fractal-glow)' : undefined}
					/>
				{/each}

				<!-- Glowing Leaf / Active Growth Tip Nodes -->
				{#each tree.leaves as leaf (leaf.id)}
					<circle
						cx={leaf.x}
						cy={leaf.y}
						r={leaf.r * leafScale.current}
						fill={leaf.color}
						opacity={leaf.opacity * Math.min(1, leafScale.current)}
						filter="url(#fractal-glow)"
					/>
				{/each}
			</svg>

			<!-- Bottom Decorative Footer Badge -->
			<div
				class="mt-2.5 flex items-center justify-between text-xs font-mono text-neutral-500 border-t border-neutral-800/80 pt-2.5 px-2"
			>
				<div class="flex items-center gap-2">
					<span class="text-emerald-400 font-medium">🌿 side-quest</span>
					<span>•</span>
					<span>recursive DAG branching</span>
				</div>
				<div>
					{#if treeGrowth.current >= 7}
						<span class="text-fuchsia-400 font-semibold animate-pulse">256 leaf nodes • full recursion</span>
					{:else if treeGrowth.current > 0}
						<span class="text-cyan-400">expanding branches...</span>
					{:else}
						<span class="text-neutral-500">awaiting branch trigger</span>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>
