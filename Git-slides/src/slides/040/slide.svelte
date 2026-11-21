<script lang="ts">
	import { tween, all } from '@animotion/motion';
	import { Action, Notes } from '@animotion/core';

	// Animotion tweens for numbers
	const solvedTween = tween(0, { duration: 1400 });
	const easyTween = tween(0, { duration: 1100 });
	const medTween = tween(0, { duration: 1200 });
	const hardTween = tween(0, { duration: 1400 });
	const donutProgress = tween(0, { duration: 1400 });

	// Donut chart geometry
	const radius = 54;
	const circumference = 2 * Math.PI * radius; // ~339.29

	// Proportions: 209 Easy (41.7%), 262 Med (52.3%), 30 Hard (6.0%) of 501
	const easyShare = 209 / 501;
	const medShare = 262 / 501;
	const hardShare = 30 / 501;

	let easyLength = $derived(circumference * easyShare * donutProgress.current);
	let medLength = $derived(circumference * medShare * donutProgress.current);
	let hardLength = $derived(circumference * hardShare * donutProgress.current);

	let easyOffset = $derived(0);
	let medOffset = $derived(-easyLength);
	let hardOffset = $derived(-(easyLength + medLength));

	async function playAnimation() {
		await all(
			solvedTween.to(501, { duration: 1400 }),
			easyTween.to(209, { duration: 1100 }),
			medTween.to(262, { duration: 1200 }),
			hardTween.to(30, { duration: 1400 }),
			donutProgress.to(1, { duration: 1400 })
		);
	}

	function resetAnimation() {
		solvedTween.reset();
		easyTween.reset();
		medTween.reset();
		hardTween.reset();
		donutProgress.reset();
	}

	export const props = {
		out: () => {
			resetAnimation();
		}
	};
</script>

<Notes>
	- 501 questions solved on LeetCode <br />
	- 209 Easy, 262 Medium, 30 Hard <br />
	- A milestone worth celebrating.
</Notes>

<!-- Trigger the counting animation on first step into this slide -->
<Action do={playAnimation} undo={resetAnimation} />

<!-- Slide 040: 501 LeetCode Questions Highlight -->
<div class="flex flex-col items-center justify-center h-full w-full gap-10">

	<!-- Big headline number -->
	<div class="flex flex-col items-center gap-3">
		<span class="text-[120px] font-black leading-none text-white font-mono tracking-tight tabular-nums drop-shadow-[0_0_40px_rgba(251,191,36,0.35)]">
			{Math.round(solvedTween.current)}
		</span>
		<span class="text-2xl font-semibold text-neutral-400 tracking-widest uppercase">
			LeetCode Questions Solved
		</span>
	</div>

	<!-- Donut + breakdown row -->
	<div class="flex items-center gap-14">

		<!-- Donut Chart -->
		<div class="relative w-36 h-36 flex items-center justify-center">
			<svg class="w-36 h-36 transform -rotate-90" viewBox="0 0 130 130">
				<!-- Track -->
				<circle cx="65" cy="65" r={radius} stroke="#2a2a2a" stroke-width="13" fill="transparent" />
				<!-- Easy (teal) -->
				<circle
					cx="65" cy="65" r={radius}
					stroke="#00b8a3" stroke-width="13" fill="transparent"
					stroke-linecap="round"
					stroke-dasharray="{easyLength} {circumference}"
					stroke-dashoffset={easyOffset}
				/>
				<!-- Medium (yellow) -->
				<circle
					cx="65" cy="65" r={radius}
					stroke="#ffc01e" stroke-width="13" fill="transparent"
					stroke-linecap="round"
					stroke-dasharray="{medLength} {circumference}"
					stroke-dashoffset={medOffset}
				/>
				<!-- Hard (red) -->
				<circle
					cx="65" cy="65" r={radius}
					stroke="#ef4444" stroke-width="13" fill="transparent"
					stroke-linecap="round"
					stroke-dasharray="{hardLength} {circumference}"
					stroke-dashoffset={hardOffset}
				/>
			</svg>
			<div class="absolute inset-0 flex flex-col items-center justify-center text-center pointer-events-none">
				<span class="text-2xl font-black text-white font-mono leading-none">
					{Math.round(solvedTween.current)}
				</span>
				<span class="text-[11px] text-neutral-400 font-mono mt-0.5">solved</span>
			</div>
		</div>

		<!-- Difficulty Breakdown -->
		<div class="flex flex-col gap-4 min-w-[220px]">
			<!-- Easy -->
			<div>
				<div class="flex justify-between text-sm mb-1.5">
					<span class="text-[#00b8a3] font-semibold">Easy</span>
					<span class="font-mono font-bold text-white">{Math.round(easyTween.current)}</span>
				</div>
				<div class="w-full bg-neutral-800 h-2 rounded-full overflow-hidden">
					<div
						class="bg-[#00b8a3] h-full rounded-full"
						style="width: {(easyTween.current / 501) * 100}%;"
					></div>
				</div>
			</div>

			<!-- Medium -->
			<div>
				<div class="flex justify-between text-sm mb-1.5">
					<span class="text-[#ffc01e] font-semibold">Medium</span>
					<span class="font-mono font-bold text-white">{Math.round(medTween.current)}</span>
				</div>
				<div class="w-full bg-neutral-800 h-2 rounded-full overflow-hidden">
					<div
						class="bg-[#ffc01e] h-full rounded-full"
						style="width: {(medTween.current / 501) * 100}%;"
					></div>
				</div>
			</div>

			<!-- Hard -->
			<div>
				<div class="flex justify-between text-sm mb-1.5">
					<span class="text-[#ef4444] font-semibold">Hard</span>
					<span class="font-mono font-bold text-white">{Math.round(hardTween.current)}</span>
				</div>
				<div class="w-full bg-neutral-800 h-2 rounded-full overflow-hidden">
					<div
						class="bg-[#ef4444] h-full rounded-full"
						style="width: {(hardTween.current / 501) * 100}%;"
					></div>
				</div>
			</div>
		</div>

	</div>

	<!-- Subtle footer -->
	<span class="text-sm text-neutral-600 font-mono tracking-widest">
		leetcode.com/u/lsd12
	</span>

</div>
