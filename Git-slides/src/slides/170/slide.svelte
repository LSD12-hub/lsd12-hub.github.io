<script lang="ts">
	import { onMount } from 'svelte';
	import { tween } from '@animotion/motion';
	import { generateGitFractalGraph } from '$lib';

	let containerEl: HTMLElement | undefined = $state();

	// Animotion Tweens for smooth continuous transitions
	const treeGrowth = tween(0, { duration: 2200 });
	const spreadAngle = tween(0.35, { duration: 2000 });
	const mergeVisibility = tween(0, { duration: 1200 });
	const nodeScale = tween(1, { duration: 400 });

	let isRunning = false;
	let playCount = 0;

	// Reactive derived Git DAG graph computed via fractal generator
	let gitGraph = $derived.by(() => {
		return generateGitFractalGraph({
			startX: 480,
			startY: 460,
			initialLength: 116,
			initialAngle: -Math.PI / 2,
			maxDepth: 6,
			growth: treeGrowth.current,
			spread: spreadAngle.current,
			lengthRatio: 0.74,
			baseStrokeWidth: 5.5,
			widthDecay: 0.7,
			depthColors: [
				'#1e9a8e', // 0: Trunk (Teal)
				'#1e9a8e', // 1: Main (Teal)
				'#0d9488', // 2: Develop (Teal-Cyan)
				'#0284c7', // 3: Features (Sky Blue)
				'#4f46e5', // 4: Sub-features (Indigo)
				'#7c3aed', // 5: Purple
				'#db2777' // 6: Pink
			],
			showMerges: mergeVisibility.current > 0.05
		});
	});

	function resetValues() {
		playCount++;
		isRunning = false;
		treeGrowth.reset();
		spreadAngle.reset();
		mergeVisibility.reset();
		nodeScale.reset();
	}

	// Continuous automated transition to render the whole tree and DAG merges
	async function playTreeTransition() {
		if (isRunning) return;
		isRunning = true;
		const currentSession = ++playCount;

		resetValues();

		// Smooth continuous growth of the fractal tree
		spreadAngle.to(0.46, { duration: 2400 });
		await treeGrowth.to(6.0, { duration: 2600 });
		if (currentSession !== playCount) return;

		// Subtle pulse on nodes as full depth is reached
		await nodeScale.to(1.18, { duration: 250 });
		if (currentSession !== playCount) return;
		await nodeScale.to(1.0, { duration: 250 });
		if (currentSession !== playCount) return;

		// Merges transition in to complete the DAG
		await mergeVisibility.to(1.0, { duration: 900 });
		if (currentSession !== playCount) return;

		isRunning = false;
	}

	export const props = {
		background: '#faf7f2',
		in: () => playTreeTransition(),
		out: () => resetValues()
	};

	onMount(() => {
		const section = containerEl?.closest('section');
		if (!section) return;

		if (section.classList.contains('present')) {
			playTreeTransition();
		} else {
			resetValues();
		}

		const handleIn = () => playTreeTransition();
		const handleOut = () => resetValues();

		section.addEventListener('in', handleIn);
		section.addEventListener('out', handleOut);

		// Watch for Reveal.js slide transition via class change
		const observer = new MutationObserver(() => {
			if (section.classList.contains('present')) {
				playTreeTransition();
			} else {
				resetValues();
			}
		});

		observer.observe(section, { attributes: true, attributeFilter: ['class'] });

		return () => {
			section.removeEventListener('in', handleIn);
			section.removeEventListener('out', handleOut);
			observer.disconnect();
			resetValues();
		};
	});
</script>

<!-- Slide 170: Pure Fractal Tree with Automated Transition -->
<div
	bind:this={containerEl}
	class="flex flex-col items-center justify-center h-full w-[1100px] text-[#1a202c]"
>
	<!-- Clean SVG Fractal Git Tree Graph -->
	<div class="w-full h-[560px] flex items-center justify-center">
		<svg
			width="960"
			height="500"
			viewBox="0 0 960 500"
			class="w-full h-full object-contain select-none overflow-visible"
		>
			<defs>
				<!-- Root Node Glow -->
				<radialGradient id="root-halo" cx="50%" cy="50%" r="50%">
					<stop offset="0%" stop-color="#1e9a8e" stop-opacity="0.35" />
					<stop offset="100%" stop-color="#1e9a8e" stop-opacity="0" />
				</radialGradient>
			</defs>

			<!-- Root Anchor Halo -->
			{#if treeGrowth.current > 0}
				<circle cx="480" cy="460" r="24" fill="url(#root-halo)" />
			{/if}

			<!-- 1. Fractal Git Branches -->
			{#each gitGraph.branches as b (b.id)}
				<line
					x1={b.x1}
					y1={b.y1}
					x2={b.x2}
					y2={b.y2}
					stroke={b.color}
					stroke-width={b.width}
					stroke-linecap="round"
					opacity="0.9"
				/>
			{/each}

			<!-- 2. Git Merge Curves (DAG) -->
			{#each gitGraph.merges as merge (merge.id)}
				<g opacity={merge.opacity}>
					<path
						d={merge.pathD}
						fill="none"
						stroke={merge.color}
						stroke-width="2.2"
						stroke-dasharray="4 3"
						stroke-linecap="round"
					/>
					<circle
						cx={(merge.fromX + merge.toX) / 2}
						cy={(merge.fromY + merge.toY) / 2}
						r="3"
						fill="#faf7f2"
						stroke={merge.color}
						stroke-width="1.8"
					/>
				</g>
			{/each}

			<!-- 3. Git Commit Nodes & Tags -->
			{#each gitGraph.commits as commit (commit.id)}
				<g opacity={commit.opacity}>
					<!-- Outer Commit Circle -->
					<circle
						cx={commit.x}
						cy={commit.y}
						r={(commit.isMerge ? 6.5 : commit.depth === 0 ? 7.5 : 5) * nodeScale.current}
						fill="#faf7f2"
						stroke={commit.color}
						stroke-width="2.2"
					/>

					<!-- Inner Commit Core Dot -->
					<circle
						cx={commit.x}
						cy={commit.y}
						r={(commit.isMerge ? 3.2 : commit.depth === 0 ? 3.8 : 2.2) * nodeScale.current}
						fill={commit.color}
					/>

					<!-- Commit Short SHA -->
					{#if commit.depth <= 3}
						<text
							x={commit.x + (commit.x >= 480 ? 9 : -9)}
							y={commit.y + 4}
							fill="#475569"
							font-size="10"
							font-family="monospace"
							font-weight="600"
							text-anchor={commit.x >= 480 ? 'start' : 'end'}
						>
							{commit.hash}
						</text>
					{/if}

					<!-- Branch / HEAD Pill Badge for Tip Nodes -->
					{#if commit.tag && (treeGrowth.current >= commit.depth || commit.isHead)}
						<g
							transform="translate({commit.x + (commit.x >= 480 ? 12 : -12)}, {commit.y - 10})"
						>
							<rect
								x={commit.x >= 480 ? 0 : -76}
								y="-9"
								width="76"
								height="17"
								rx="8.5"
								fill="#ffffff"
								stroke={commit.color}
								stroke-width="1.4"
								filter="drop-shadow(0 1px 2px rgba(0,0,0,0.08))"
							/>
							<text
								x={commit.x >= 480 ? 38 : -38}
								y="3"
								fill={commit.color}
								font-size="8.5"
								font-family="monospace"
								font-weight="bold"
								text-anchor="middle"
							>
								{commit.tag}
							</text>
						</g>
					{/if}
				</g>
			{/each}

			<!-- 4. Active Leaves / Growth Tips -->
			{#each gitGraph.leaves as leaf (leaf.id)}
				<circle
					cx={leaf.x}
					cy={leaf.y}
					r={leaf.r * nodeScale.current}
					fill={leaf.color}
					opacity={leaf.opacity * Math.min(1, nodeScale.current)}
				/>
			{/each}
		</svg>
	</div>
</div>
