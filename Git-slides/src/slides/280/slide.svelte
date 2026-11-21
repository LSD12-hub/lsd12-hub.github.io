<script lang="ts">
	import { Action, Notes } from '@animotion/core';
	import { tween } from '@animotion/motion';
	import Progress from '$lib/components/Progress.svelte';

	let step = $state(0);

	// Counting tweens for the realistic scenario numbers
	const count1 = tween(0, { duration: 1000 }); // 0 → 1,000,000
	const count2 = tween(0, { duration: 900 });  // 0 → 3,906

	// Progress-bar fill tweens (0→target fraction)
	const barAmber = tween(0, { duration: 1000 }); // fills to 1
	const barTeal  = tween(0, { duration: 900 });  // fills to 1/256

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
			count1.reset();
			count2.reset();
			barAmber.reset();
			barTeal.reset();
		}
	};
</script>

<Notes>
	Q: Why do we need the 2-character prefix?
	A: 2 hexadecimal characters give 16² = 256 possible subfolders (00 through ff).
	1) In a 1,000,000 object repository without prefixes, we search 1,000,000 files in 1 folder.
	2) With prefixes, it's 1,000,000 / 256 ≈ 3,906 files per folder.
	3) At the theoretical SHA-1 limit (2¹⁶⁰), without prefix is 1.4615 × 10⁴⁸ files in 1 folder.
	4) With prefix, 1.4615 × 10⁴⁸ / 256 = 2¹⁵² ≈ 5.709 × 10⁴⁵ files per folder.
</Notes>

<!-- Action 1: Show "without prefix" column and count up to 1,000,000 -->
<Action
	do={async () => { step = 1; await count1.to(1_000_000, { duration: 1000 }); }}
	undo={() => { step = 0; count1.reset(); }}
/>

<!-- Action 2: Show "with prefix" column and count up to 3,906 -->
<Action
	do={async () => { step = 2; await count2.to(3906, { duration: 900 }); }}
	undo={() => { step = 1; count2.reset(); }}
/>

<!-- Action 3: Reveal theoretical limit section, fill amber bar left→right -->
<Action
	do={async () => { step = 3; await barAmber.to(1, { duration: 1000 }); }}
	undo={() => { step = 2; barAmber.reset(); }}
/>

<!-- Action 4: Reveal "with prefix" bar and fill teal bar left→right -->
<Action
	do={async () => { step = 4; await barTeal.to(1 / 256, { duration: 900 }); }}
	undo={() => { step = 3; barTeal.reset(); }}
/>

<div class="w-[1050px] h-[650px] text-left p-12 text-white relative select-none flex flex-col justify-between">
	<div>
		<!-- Title & Subfolder Formula -->
		<h2 class="text-5xl font-serif font-bold text-white mb-3">Objects</h2>
		<p class="text-xl font-mono text-neutral-400 mb-10">
			2 hex characters &nbsp;=&nbsp; 16² &nbsp;=&nbsp;
			<span class="text-teal-400 font-bold">256 subfolders</span>
			<span class="text-neutral-500 text-lg">(00 → ff)</span>
		</p>

		<!-- Comparison Rows -->
		<div class="space-y-8">
			<!-- Scenario 1: Realistic Scale -->
			<div
				class="transition-opacity duration-500"
				style="opacity: {step >= 1 ? '1' : '0.2'};"
			>
				<div class="text-xs font-mono uppercase tracking-widest text-neutral-400 mb-3 flex items-center justify-between">
					<span class="font-semibold text-neutral-300">Realistic Repository</span>
					<span>1,000,000 objects</span>
				</div>

				<div class="grid grid-cols-2 gap-12 font-mono">
					<!-- Without Prefix -->
					<div
						class="transition-all duration-500 ease-out"
						style="opacity: {step >= 1 ? '1' : '0'}; transform: {step >= 1 ? 'translateX(0)' : 'translateX(-24px)'};"
					>
						<div class="text-xs uppercase tracking-wider text-neutral-500 mb-1">Without Prefix</div>
						<div class="text-4xl font-bold text-red-400 tracking-tight mb-1">
							{Math.round(count1.current).toLocaleString('en-US')}
						</div>
						<div class="text-sm text-neutral-400 font-sans">
							files in <span class="text-neutral-200">1 single folder</span>
						</div>
					</div>

					<!-- With Prefix -->
					<div
						class="transition-all duration-500 ease-out"
						style="opacity: {step >= 2 ? '1' : '0'}; transform: {step >= 2 ? 'translateX(0)' : 'translateX(-24px)'};"
					>
						<div class="text-xs uppercase tracking-wider text-neutral-500 mb-1">With Prefix (256 folders)</div>
						<div class="flex items-baseline gap-2 mb-1">
							<span class="text-4xl font-bold text-teal-400 tracking-tight">~{Math.round(count2.current).toLocaleString('en-US')}</span>
							<span class="text-sm text-neutral-500">(1,000,000 / 256)</span>
						</div>
						<div class="text-sm text-neutral-400 font-sans">
							files per <span class="text-teal-300 font-medium">subfolder</span>
						</div>
					</div>
				</div>
			</div>

			<!-- Divider -->
			<div
				class="border-t border-neutral-800/80 transition-opacity duration-500"
				style="opacity: {step >= 3 ? '1' : '0.2'};"
			></div>

			<!-- Scenario 2: Theoretical Limit with Progress bars -->
			<div
				class="transition-opacity duration-500"
				style="opacity: {step >= 3 ? '1' : '0.2'};"
			>
				<div class="text-xs font-mono uppercase tracking-widest text-neutral-400 mb-4 flex items-center justify-between">
					<span class="font-semibold text-neutral-300">Theoretical Limit</span>
					<span>2¹⁶⁰ SHA-1 combinations</span>
				</div>

				<div class="space-y-4">
					<!-- Without Prefix bar — 100% reference -->
					<div
						class="transition-all duration-500 ease-out"
						style="opacity: {step >= 3 ? '1' : '0'}; transform: {step >= 3 ? 'translateX(0)' : 'translateX(-24px)'};"
					>
						<Progress
							value={barAmber.current}
							color="bg-amber-400"
							label="1.4615 × 10⁴⁸"
							sublabel="Without Prefix — all files in 1 folder"
							annotation="the full SHA-1 space"
						/>
					</div>

					<!-- With Prefix bar — exactly 1/256 ≈ 0.39% of the above -->
					<div
						class="transition-all duration-500 ease-out"
						style="opacity: {step >= 4 ? '1' : '0'}; transform: {step >= 4 ? 'translateX(0)' : 'translateX(-24px)'};"
					>
						<Progress
							value={barTeal.current}
							color="bg-teal-400"
							label="5.709 × 10⁴⁵"
							sublabel="With Prefix (256 folders) — 2¹⁶⁰ ÷ 256 = 2¹⁵²"
							annotation="÷ 256 per subfolder"
						/>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
