<script lang="ts">
	import { Action, Notes } from '@animotion/core';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};
</script>

<Notes>
	Q: What is bit masking and why do we need it in Java for Git?
	A:
	- Definition: A programming technique that uses a binary pattern (a "mask") and bitwise operators to inspect, set, clear, or toggle specific bits in a data value without changing the other bits.
	- Java 'byte' is signed (-128..127). Git raw bytes are unsigned (0..255).
	- Sign extension: Widening a negative byte to a 32-bit int copies '1' into all upper 24 bits (0xFFFFFF9A).
	- The 0xFF mask zeroes out the upper 24 sign bits while preserving the bottom 8 bits -> 0x0000009A (154).

	Q: Why use bitmask
	A: 
	- Because we are using Java
	- Java 'byte' is signed (-128..127). Git raw bytes are unsigned (0..255).
</Notes>

<!-- Action 1: Reveal the Sign-Extended Byte -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Introduce the 0xFF Mask -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<!-- Action 3: Resolve and Show Bitwise AND Result -->
<Action do={() => (step = 3)} undo={() => (step = 2)} />



<div class="w-[1040px] h-[620px] text-white select-none p-8 flex flex-col justify-between items-center">
	<!-- Centered Title, Concept Context & Definition (Step 0+) -->
	<div class="text-center max-w-3xl mx-auto space-y-4">
		<!-- Title & Concept Badges -->
		<div class="space-y-1.5">
			<h2 class="text-4xl font-serif font-bold text-white tracking-tight">
				Bit Masking
			</h2>
			<div class="font-mono text-xs text-neutral-400 space-x-2">
				<span>Java <span class="text-amber-300 font-semibold">byte</span> (-128..127)</span>
				<span class="text-neutral-600">•</span>
				<span>Git <span class="text-emerald-400 font-semibold">unsigned</span> (0..255)</span>
			</div>
		</div>

		<!-- Definition with Generous Spacing -->
		<p class="text-neutral-300 text-lg leading-relaxed font-sans pt-2">
			A programming technique that uses a binary pattern (a <span class="text-white font-semibold">"mask"</span>) and bitwise operators to <span class="text-sky-300 font-medium">inspect, set, clear, or toggle</span> specific bits in a data value without changing the other bits.
		</p>
	</div>

	<!-- Minimal Bitwise Alignment Diagram -->
	<div class="my-auto font-mono text-xl space-y-4 max-w-3xl mx-auto w-full">
		<!-- Line 1: Promoted Byte (Step 1+) -->
		<div
			class="flex items-center justify-between transition-all duration-500 ease-out"
			style="opacity: {step >= 1 ? 1 : 0}; transform: {step >= 1 ? 'translateY(0)' : 'translateY(8px)'};"
		>
			<div class="flex items-center gap-4">
				<span class="text-neutral-400 text-base w-20 text-right">b</span>
				<div class="flex gap-3 text-2xl tracking-widest">
					<span class="text-red-400 font-semibold">11111111</span>
					<span class="text-red-400 font-semibold">11111111</span>
					<span class="text-red-400 font-semibold">11111111</span>
					<span class="text-teal-300 font-bold">10011010</span>
				</div>
			</div>
			<div class="text-right">
				<span class="text-red-400 font-bold text-lg">0xFFFFFF9A</span>
				<span class="text-neutral-500 text-xs block">(-102 sign-extended)</span>
			</div>
		</div>

		<!-- Line 2: 0xFF Mask (Step 2+) -->
		<div
			class="flex items-center justify-between transition-all duration-500 ease-out"
			style="opacity: {step >= 2 ? 1 : 0}; transform: {step >= 2 ? 'translateY(0)' : 'translateY(8px)'};"
		>
			<div class="flex items-center gap-4">
				<span class="text-sky-400 font-bold text-base w-20 text-right">&amp; 0xFF</span>
				<div class="flex gap-3 text-2xl tracking-widest">
					<span class="text-neutral-600">00000000</span>
					<span class="text-neutral-600">00000000</span>
					<span class="text-neutral-600">00000000</span>
					<span class="text-sky-300 font-bold">11111111</span>
				</div>
			</div>
			<div class="text-right">
				<span class="text-sky-400 font-bold text-lg">0x000000FF</span>
				<span class="text-neutral-500 text-xs block">(255 mask)</span>
			</div>
		</div>

		<!-- Divider (Step 3+) -->
		<div
			class="border-t-2 border-neutral-700 my-2 transition-opacity duration-500"
			style="opacity: {step >= 3 ? 1 : 0};"
		></div>

		<!-- Line 3: Result (Step 3+) -->
		<div
			class="flex items-center justify-between transition-all duration-500 ease-out"
			style="opacity: {step >= 3 ? 1 : 0}; transform: {step >= 3 ? 'translateY(0)' : 'translateY(8px)'};"
		>
			<div class="flex items-center gap-4">
				<span class="text-emerald-400 font-bold text-base w-20 text-right">= result</span>
				<div class="flex gap-3 text-2xl tracking-widest">
					<span class="text-neutral-600">00000000</span>
					<span class="text-neutral-600">00000000</span>
					<span class="text-neutral-600">00000000</span>
					<span class="text-emerald-300 font-bold drop-shadow-[0_0_8px_rgba(52,211,153,0.5)]">10011010</span>
				</div>
			</div>
			<div class="text-right">
				<span class="text-emerald-400 font-bold text-lg">0x0000009A</span>
				<span class="text-emerald-400/70 text-xs block">(154 clean byte)</span>
			</div>
		</div>
	</div>

	<!-- Minimal Footer -->
	<div class="w-full font-mono text-xs text-neutral-500 flex items-center justify-between border-t border-neutral-800/80 pt-3">
		<span>Always mask raw bytes: <code class="text-sky-300 font-bold">b &amp; 0xFF</code></span>
		<span class="text-neutral-400">Step {step} of 3</span>
	</div>
</div>

