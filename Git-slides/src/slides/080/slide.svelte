<script lang="ts">
	import { base } from '$app/paths';
	import { onMount } from 'svelte';
	import { tween } from '@animotion/motion';
	import {
		createTypewriter,
		createYouTubeFourier,
		evaluateEpicycles,
		type FourierEvaluation
	} from '$lib';
	import { Notes } from '@animotion/core';

	let containerEl: HTMLElement | undefined = $state();

	// Terminal command prompt typewriter
	const tw = createTypewriter('fourier-draw --target youtube_logo.png --epicycles', {
		speed: 28
	});

	// Animotion tweens
	const timeProgress = tween(0, { duration: 6500 });
	const harmonics = tween(90, { duration: 800 });
	const circlesOpacity = tween(0.85, { duration: 600 });
	const logoGlow = tween(0.2, { duration: 600 });

	// Initialize Fourier model mathematically aligned 1:1 with youtube logo
	const fourier = createYouTubeFourier({
		scale: 0.72
	});

	const totalPoints = fourier.points.length;

	// Reactive derived current epicycles and tip location
	let evaluation: FourierEvaluation = $derived.by(() => {
		const t = timeProgress.current;
		const numHarmonics = Math.round(harmonics.current);
		return evaluateEpicycles(fourier.coefficients, t, numHarmonics);
	});

	// Reactive derived drawn trail up to current t
	let trailPoints = $derived.by(() => {
		const t = timeProgress.current;
		if (t <= 0) return [];

		const count = Math.min(totalPoints, Math.max(1, Math.floor(t * totalPoints) + 1));
		const pts: { x: number; y: number }[] = [];
		const numHarmonics = Math.round(harmonics.current);

		for (let i = 0; i < count; i++) {
			const stepT = i / totalPoints;
			const ev = evaluateEpicycles(fourier.coefficients, stepT, numHarmonics);
			pts.push(ev.tip);
		}

		pts.push(evaluation.tip);
		return pts;
	});

	// SVG path string for the dynamic trail
	let trailPath = $derived.by(() => {
		if (trailPoints.length < 2) return '';
		return trailPoints.reduce((acc, pt, idx) => {
			return idx === 0
				? `M ${pt.x.toFixed(1)} ${pt.y.toFixed(1)}`
				: `${acc} L ${pt.x.toFixed(1)} ${pt.y.toFixed(1)}`;
		}, '');
	});

	let isRunning = false;
	let playCount = 0;

	function resetAll() {
		playCount++;
		isRunning = false;
		tw.reset();
		timeProgress.reset();
		harmonics.reset();
		circlesOpacity.reset();
		logoGlow.reset();
	}

	// Sequential execution of all animation steps when entering the slide
	async function playAllSteps() {
		if (isRunning) return;
		isRunning = true;
		const currentSession = ++playCount;

		// Reset values cleanly
		tw.reset();
		timeProgress.reset();
		harmonics.reset();
		circlesOpacity.reset();
		logoGlow.reset();

		// Step 1: Start typewriter and epicycle tracing in parallel
		tw.start();
		await circlesOpacity.to(0.9, { duration: 300 });
		if (currentSession !== playCount) return;

		await timeProgress.to(1, { duration: 6500 });
		if (currentSession !== playCount) return;

		await logoGlow.to(0.8, { duration: 500 });
		if (currentSession !== playCount) return;

		// Step 2: Increase harmonics for ultra-crisp corner fidelity
		await harmonics.to(160, { duration: 900 });
		if (currentSession !== playCount) return;

		await logoGlow.to(1.1, { duration: 400 });
		if (currentSession !== playCount) return;

		// Step 3: Fade epicycles into clean completed YouTube vector
		await circlesOpacity.to(0.06, { duration: 600 });
		if (currentSession !== playCount) return;

		await logoGlow.to(1.3, { duration: 400 });
		if (currentSession !== playCount) return;

		isRunning = false;
	}

	onMount(() => {
		const section = containerEl?.closest('section');
		if (!section) return;

		if (section.classList.contains('present')) {
			playAllSteps();
		} else {
			resetAll();
		}

		const handleIn = () => playAllSteps();
		const handleOut = () => resetAll();

		section.addEventListener('in', handleIn);
		section.addEventListener('out', handleOut);

		// Watch for Reveal.js slide transition via class change
		const observer = new MutationObserver(() => {
			if (section.classList.contains('present')) {
				playAllSteps();
			} else {
				resetAll();
			}
		});

		observer.observe(section, { attributes: true, attributeFilter: ['class'] });

		return () => {
			section.removeEventListener('in', handleIn);
			section.removeEventListener('out', handleOut);
			observer.disconnect();
			resetAll();
		};
	});
</script>

<Notes>
	- What I learned on youtube. <br>
	- Never take what people say seriouly <br>
	- Scripted 
</Notes>

<!-- Slide 080: Fourier Series Drawing of YouTube Logo -->
<div bind:this={containerEl} class="flex flex-col items-center justify-center max-w-6xl w-full text-center px-2">
	<div
		class="w-full bg-neutral-950/90 border border-neutral-800 rounded-2xl p-6 shadow-2xl text-left"
	>
		<!-- Typed Command Prompt & Live Fourier HUD -->
		<div
			class="font-mono text-base bg-black/90 px-5 py-3.5 rounded-xl border border-red-500/40 text-red-400 shadow-inner mb-4 flex items-center justify-between min-h-[54px]"
		>
			<div class="flex items-center">
				<span class="text-neutral-500 mr-2">$</span>
				{#if !tw.hasStarted}
					<span class="inline-block w-2.5 h-5 bg-red-400 align-middle animate-pulse"></span>
				{:else}
					<span>{tw.text}</span>
					{#if !tw.isDone}
						<span class="inline-block w-2.5 h-5 bg-red-400 ml-1.5 align-middle animate-pulse"
						></span>
					{/if}
				{/if}
			</div>

			<!-- Live Epicycle Stats HUD -->
			{#if timeProgress.current > 0 || tw.hasStarted}
				<div
					class="hidden sm:flex items-center gap-2.5 text-xs font-mono px-3.5 py-1.5 rounded-lg bg-neutral-900 border border-neutral-800 text-neutral-300"
				>
					<span
						class="inline-block w-2.5 h-2.5 rounded-full {timeProgress.current >= 1
							? 'bg-emerald-400 animate-ping'
							: 'bg-red-400 animate-pulse'}"
					></span>
					<span>harmonics: {Math.round(harmonics.current)}</span>
					<span class="text-neutral-600">•</span>
					<span>t: {(timeProgress.current * 100).toFixed(0)}%</span>
					<span class="text-neutral-600">•</span>
					<span class="text-rose-300">θ: {(timeProgress.current * 360).toFixed(0)}°</span>
				</div>
			{/if}
		</div>

		<!-- SVG Canvas with Rotating Epicycles and Traced Path -->
		<div class="bg-neutral-900/80 p-4 rounded-xl border border-neutral-800 overflow-hidden relative">
			<svg width="960" height="480" viewBox="0 0 960 480" class="w-full h-auto max-h-[58vh]">
				<defs>
					<!-- Subtle Background Grid Pattern -->
					<pattern id="fourier-grid-yt" width="30" height="30" patternUnits="userSpaceOnUse">
						<circle cx="15" cy="15" r="0.85" fill="#374151" opacity="0.35" />
					</pattern>

					<!-- Glow Filters for Epicycle Tip & Traced Path -->
					<filter id="yt-logo-glow" x="-30%" y="-30%" width="160%" height="160%">
						<feGaussianBlur stdDeviation="6" result="coloredBlur" />
						<feMerge>
							<feMergeNode in="coloredBlur" />
							<feMergeNode in="SourceGraphic" />
						</feMerge>
					</filter>

					<filter id="yt-tip-glow" x="-50%" y="-50%" width="200%" height="200%">
						<feGaussianBlur stdDeviation="4" result="coloredBlur" />
						<feMerge>
							<feMergeNode in="coloredBlur" />
							<feMergeNode in="SourceGraphic" />
						</feMerge>
					</filter>

					<!-- Radial Gradient for Background Center -->
					<radialGradient id="yt-center-glow" cx="50%" cy="50%" r="50%">
						<stop offset="0%" stop-color="#FF0000" stop-opacity="0.14" />
						<stop offset="100%" stop-color="#FF0000" stop-opacity="0" />
					</radialGradient>

					<!-- YouTube Brand Color Gradient -->
					<linearGradient id="youtube-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
						<stop offset="0%" stop-color="#FFFFFF" />
						<stop offset="35%" stop-color="#FF0033" />
						<stop offset="70%" stop-color="#FF1A4B" />
						<stop offset="100%" stop-color="#E50914" />
					</linearGradient>
				</defs>

				<!-- Grid Pattern Background -->
				<rect width="960" height="480" fill="url(#fourier-grid-yt)" />
				<circle cx="480" cy="240" r="220" fill="url(#yt-center-glow)" />

				<!-- Exact 1:1 Pixel-Aligned Reference Logo -->
				<image
					href="{base}/images/youtube_transparent.png"
					x={fourier.imageBounds.x}
					y={fourier.imageBounds.y}
					width={fourier.imageBounds.width}
					height={fourier.imageBounds.height}
					opacity={0.14 + logoGlow.current * 0.14}
				/>

				<!-- Epicycle Circles & Rotating Radius Arms -->
				<g opacity={circlesOpacity.current}>
					{#each evaluation.circles as circle (circle.index)}
						<!-- Render first 28 dominant circles for crisp performance and aesthetics -->
						{#if circle.index < 28 && circle.radius > 1.2}
							<!-- Circle Outline -->
							<circle
								cx={circle.x}
								cy={circle.y}
								r={circle.radius}
								fill="none"
								stroke={circle.index === 0
									? '#FF0033'
									: circle.index < 6
										? '#fb7185'
										: '#818cf8'}
								stroke-width={circle.index === 0 ? '1.5' : '1'}
								stroke-opacity={Math.max(0.12, 0.45 - circle.index * 0.014)}
								stroke-dasharray={circle.index > 3 ? '3 3' : undefined}
							/>

							<!-- Radius Vector Arm -->
							<line
								x1={circle.x}
								y1={circle.y}
								x2={circle.targetX}
								y2={circle.targetY}
								stroke={circle.index === 0 ? '#FFFFFF' : '#fecdd3'}
								stroke-width={circle.index === 0 ? '1.8' : '1.1'}
								stroke-opacity={Math.max(0.25, 0.7 - circle.index * 0.02)}
							/>

							<!-- Center Pivot Point -->
							{#if circle.index < 8}
								<circle
									cx={circle.x}
									cy={circle.y}
									r={circle.index === 0 ? 3.5 : 2}
									fill={circle.index === 0 ? '#FF0033' : '#fda4af'}
									opacity={0.8}
								/>
							{/if}
						{/if}
					{/each}
				</g>

				<!-- Traced Fourier Series Trail (Crisp YouTube Logo Drawing) -->
				{#if trailPath}
					<!-- Outer Glow Trail -->
					<path
						d={trailPath}
						fill="none"
						stroke="url(#youtube-gradient)"
						stroke-width="18"
						stroke-linecap="round"
						stroke-linejoin="round"
						filter="url(#yt-logo-glow)"
						opacity={0.6 * logoGlow.current}
					/>

					<!-- Main Crisp Trail -->
					<path
						d={trailPath}
						fill="none"
						stroke="url(#youtube-gradient)"
						stroke-width="14"
						stroke-linecap="round"
						stroke-linejoin="round"
					/>
				{/if}

				<!-- Active Pen Tip / Drawing Head -->
				{#if timeProgress.current > 0 && timeProgress.current < 1}
					<circle
						cx={evaluation.tip.x}
						cy={evaluation.tip.y}
						r="10"
						fill="#FF0033"
						opacity="0.3"
						class="animate-ping"
					/>

					<circle
						cx={evaluation.tip.x}
						cy={evaluation.tip.y}
						r="5"
						fill="#FFFFFF"
						stroke="#FF0033"
						stroke-width="2.5"
						filter="url(#yt-tip-glow)"
					/>
				{/if}
			</svg>

			<!-- Bottom Decorative Footer Badge -->
			<div
				class="mt-2.5 flex items-center justify-between text-xs font-mono text-neutral-500 border-t border-neutral-800/80 pt-2.5 px-2"
			>
				<div class="flex items-center gap-2">
					<span class="text-red-400 font-medium">⚡ discrete fourier transform</span>
					<span>•</span>
					<span>z(t) = ∑ cₙ e^(i 2π n t)</span>
				</div>
				<div>
					{#if circlesOpacity.current < 0.2}
						<span class="text-emerald-400 font-semibold animate-pulse"
							>✓ reconstructed youtube vector</span
						>
					{:else if timeProgress.current >= 1}
						<span class="text-rose-300 font-semibold"
							>100% traced • {Math.round(harmonics.current)} harmonics</span
						>
					{:else if timeProgress.current > 0}
						<span class="text-cyan-400">evaluating epicycles...</span>
					{:else}
						<span class="text-neutral-500">awaiting trigger</span>
					{/if}
				</div>
			</div>
		</div>
	</div>
</div>

