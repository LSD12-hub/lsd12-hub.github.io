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
	Q: How does bit masking look in actual Java code?
	A:
	- byte b = (byte) 0xAB stores -85 due to Java signed byte type.
	- Integer.toHexString(b) sign-extends to "ffffffab" — WRONG.
	- Integer.toHexString(0xff & b) masks the upper bits, giving "ab" — CORRECT.
</Notes>

<!-- Action 1: Show byte declaration + wrong conversion -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Show correct masked conversion -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<div class="w-[1040px] h-[620px] text-white select-none p-8 flex flex-col justify-between items-center">
	<!-- Title -->
	<div class="text-center max-w-3xl mx-auto space-y-4">
		<div class="space-y-1.5">
			<h2 class="text-4xl font-serif font-bold text-white tracking-tight">
				Bit Masking in Code
			</h2>
			<div class="font-mono text-xs text-neutral-400 space-x-2">
				<span>Java <span class="text-amber-300 font-semibold">byte</span> (-128..127)</span>
				<span class="text-neutral-600">•</span>
				<span>Git <span class="text-emerald-400 font-semibold">unsigned</span> (0..255)</span>
			</div>
		</div>

		<!-- <p class="text-neutral-300 text-lg leading-relaxed font-sans pt-2">
			Without the mask, Java <span class="text-white font-semibold">sign-extends</span> the byte —
			corrupting every SHA-1 byte above <span class="text-sky-300 font-medium">0x7F</span>.
		</p> -->
	</div>

	<!-- Code Lines -->
	<div class="my-auto font-mono text-xl space-y-4 max-w-3xl mx-auto w-full">

		<!-- Line 1: byte declaration + wrong call (Step 1+) -->
		<div
			class="flex flex-col gap-2 transition-all duration-500 ease-out"
			style="opacity: {step >= 1 ? 1 : 0}; transform: {step >= 1 ? 'translateY(0)' : 'translateY(8px)'};"
		>
			<div class="flex items-center justify-between">
				<span class="text-neutral-300">
					<span class="text-amber-300">byte</span> b = (<span class="text-amber-300">byte</span>) <span class="text-purple-300">0xAB</span>;
				</span>
				<span class="text-neutral-500 text-sm">// stored as -85</span>
			</div>
			<div class="flex items-center justify-between">
				<span class="text-neutral-300">Integer.<span class="text-sky-300">toHexString</span>(b)</span>
				<div class="text-right">
					<span class="text-red-400 font-bold">"ffffffab"</span>
					<span class="text-neutral-500 text-xs block">❌ sign-extended</span>
				</div>
			</div>
		</div>

		<!-- Divider (Step 2+) -->
		<div
			class="border-t-2 border-neutral-700 my-2 transition-opacity duration-500"
			style="opacity: {step >= 2 ? 1 : 0};"
		></div>

		<!-- Line 2: masked call (Step 2+) -->
		<div
			class="flex items-center justify-between transition-all duration-500 ease-out"
			style="opacity: {step >= 2 ? 1 : 0}; transform: {step >= 2 ? 'translateY(0)' : 'translateY(8px)'};"
		>
			<span class="text-neutral-300">Integer.<span class="text-sky-300">toHexString</span>(<span class="text-sky-400 font-bold">0xff &amp; b</span>)</span>
			<div class="text-right">
				<span class="text-emerald-400 font-bold drop-shadow-[0_0_8px_rgba(52,211,153,0.5)]">"ab"</span>
				<span class="text-emerald-400/70 text-xs block">✅ clean byte</span>
			</div>
		</div>

	</div>

	<!-- Minimal Footer -->
	<div class="w-full font-mono text-xs text-neutral-500 flex items-center justify-between border-t border-neutral-800/80 pt-3">
		<span>Always mask raw bytes: <code class="text-sky-300 font-bold">b &amp; 0xFF</code></span>
		<span class="text-neutral-400">Step {step} of 2</span>
	</div>
</div>
