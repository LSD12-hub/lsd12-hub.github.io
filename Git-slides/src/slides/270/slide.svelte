<script lang="ts">
	import { Action, Notes } from '@animotion/core';
	import { fade, fly } from 'svelte/transition';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};
</script>

<Notes>
	Q: Why do first 2 characters of a hash make part of the path for an object in git?
	A: Instead of searching through 100 000 files in one folder, the computer looks inside one small subfolder containing only about 400 files. This keeps file lookups lightning fast.
</Notes>

<!-- Action 1: Split objects into 2-char prefix subfolders -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<div class="w-[1050px] h-[650px] text-left p-12 text-white relative select-none">
	<h2 class="text-5xl font-serif font-bold text-white mb-8">Objects</h2>

	<div class="relative min-h-[460px]">
		{#if step === 0}
			<!-- Flat Directory Tree -->
			<div
				in:fly={{ y: 10, duration: 400 }}
				out:fade={{ duration: 200 }}
				class="absolute inset-0 font-mono text-2xl leading-relaxed space-y-2"
			>
				<!-- .git -->
				<div class="flex items-center gap-3 font-bold text-white">
					<span class="text-amber-400">📁</span>
					<span>.git/</span>
				</div>

				<!-- objects -->
				<div class="pl-8 flex items-center gap-3 font-bold text-white">
					<span class="text-neutral-500 font-semibold">└──</span>
					<span class="text-teal-400">📁</span>
					<span>objects/</span>
				</div>

				<!-- List of objects -->
				<div class="pl-16 space-y-2 pt-1 text-neutral-200 text-xl">
					<div class="flex items-center gap-3">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-neutral-400">📄</span>
						<span class="font-medium">0155eb94a7c4acc32b94199cbb91fc1e23367541</span>
					</div>
					<div class="flex items-center gap-3">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-neutral-400">📄</span>
						<span class="font-medium">3c4e9c882b94199cbb91fc1e233675410155eb94</span>
					</div>
					<div class="flex items-center gap-3">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-neutral-400">📄</span>
						<span class="border-2 border-red-500 px-2.5 py-0.5 bg-red-950/60 text-red-200 rounded font-bold shadow-md">
							f0121e40a7c4acc32b94199cbb91fc1e23367541
						</span>
					</div>
					<div class="flex items-center gap-3">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-neutral-400">📄</span>
						<span class="font-medium">cac0ca77fc1e23367541f0121e40a7c4acc32b94</span>
					</div>
					<div class="flex items-center gap-3 text-neutral-400 italic font-medium">
						<span class="text-neutral-500 font-semibold">└──</span>
						<span>... (100,000 files in one folder)</span>
					</div>
				</div>
			</div>
		{:else}
			<!-- Prefixed Directory Tree -->
			<div
				in:fly={{ y: 10, duration: 400 }}
				out:fade={{ duration: 200 }}
				class="absolute inset-0 font-mono text-2xl leading-relaxed space-y-2"
			>
				<!-- .git -->
				<div class="flex items-center gap-3 font-bold text-white">
					<span class="text-amber-400">📁</span>
					<span>.git/</span>
				</div>

				<!-- objects -->
				<div class="pl-8 flex items-center gap-3 font-bold text-white">
					<span class="text-neutral-500 font-semibold">└──</span>
					<span class="text-teal-400">📁</span>
					<span>objects/</span>
				</div>

				<!-- Prefixes -->
				<div class="pl-16 space-y-2 pt-1 text-neutral-200 text-xl">
					<div class="flex items-center gap-3 text-neutral-200">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-amber-400">📁</span>
						<span class="font-bold">00/</span>
					</div>
					<div class="flex items-center gap-3 text-neutral-200">
						<span class="text-neutral-500 font-semibold">├──</span>
						<span class="text-amber-400">📁</span>
						<span class="font-bold">01/</span>
					</div>
					<div class="flex items-center gap-3 text-neutral-500 pl-8 text-lg font-bold">
						<span>⋮</span>
					</div>

					<!-- Highlighted f0/ -->
					<div>
						<div class="flex items-center gap-3 font-bold">
							<span class="text-neutral-500 font-semibold">├──</span>
							<span class="text-teal-400">📁</span>
							<span class="border-2 border-red-500 px-2.5 py-0.5 bg-red-950/60 text-red-200 rounded font-bold shadow-md">
								f0/
							</span>
						</div>

						<!-- Inside f0/ -->
						<div class="pl-10 pt-2 space-y-2 text-neutral-200">
							<div class="flex items-center gap-3">
								<span class="text-neutral-500 font-semibold">│ &nbsp; ├──</span>
								<span class="text-neutral-400">📄</span>
								<span class="border-2 border-red-500 px-2.5 py-0.5 bg-red-950/60 text-red-200 rounded font-bold shadow-md">
									121e40a7c4acc32b94199cbb91fc1e23367541
								</span>
							</div>
							<div class="flex items-center gap-3 text-neutral-400 italic font-medium">
								<span class="text-neutral-500 font-semibold">│ &nbsp; └──</span>
								<span>... (~400 files)</span>
							</div>
						</div>
					</div>

					<div class="flex items-center gap-3 text-neutral-500 pl-8 text-lg font-bold">
						<span>⋮</span>
					</div>
					<div class="flex items-center gap-3 text-neutral-200">
						<span class="text-neutral-500 font-semibold">└──</span>
						<span class="text-amber-400">📁</span>
						<span class="font-bold">ff/</span>
					</div>
				</div>
			</div>
		{/if}
	</div>
</div>
