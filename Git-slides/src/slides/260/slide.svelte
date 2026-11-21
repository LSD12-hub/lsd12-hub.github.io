<script lang="ts">
	import { Action } from '@animotion/core';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};
</script>

<!-- Action 1: Example of hash (from slide 270) -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Live in .git/objects (from slide 280) -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<!-- Action 3: Path breakdown (from slide 290) -->
<Action do={() => (step = 3)} undo={() => (step = 2)} />

<div class="w-[1100px] h-[650px] text-left p-12 text-neutral-100">
	<h2 class="text-5xl font-serif font-bold text-white mb-12">Objects</h2>
	<ul class="text-3xl font-serif leading-loose space-y-6 list-disc list-inside text-neutral-100">
		<li>They are identified by a hash.</li>
		<li>A hash is normally 40 characters long.</li>

		{#if step === 1}
			<li class="flex items-center gap-3">
				<span>Example of hash:</span>
				<span class="font-mono text-2xl border-2 border-red-500 px-3 py-1 bg-red-950/60 text-red-200 font-bold rounded shadow-md">
					f0121e40a7c4acc32b94199cbb91fc1e23367541
				</span>
			</li>
		{:else if step >= 2}
			<li>
				Example of hash: <span class="font-mono text-2xl font-bold text-amber-300">f0121e40a7c4acc32b94199cbb91fc1e23367541</span>
			</li>
		{/if}

		{#if step === 2}
			<li class="flex items-center gap-3">
				<span>Live in</span>
				<span class="font-mono text-2xl border-2 border-red-500 px-3 py-1 bg-red-950/60 text-red-200 font-bold rounded shadow-md">
					.git/objects
				</span>
			</li>
		{:else if step >= 3}
			<li>Live in <span class="font-mono text-2xl font-bold text-teal-400">.git/objects</span></li>
		{/if}

		{#if step >= 3}
			<li class="flex items-center gap-2">
				<span class="font-mono text-2xl font-bold text-teal-400">.git/objects/</span>
				<span class="font-mono text-2xl border-2 border-red-500 px-2.5 py-0.5 bg-red-950/60 text-red-200 font-bold rounded">f0</span>
				<span class="font-mono text-2xl font-bold text-neutral-300">/</span>
				<span class="font-mono text-2xl border-2 border-red-500 px-2.5 py-0.5 bg-red-950/60 text-red-200 font-bold rounded">121e40a7c4acc32b94199cbb91fc1e23367541</span>
			</li>
		{/if}
	</ul>
</div>
