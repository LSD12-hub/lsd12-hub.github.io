<script lang="ts">
	import { Action } from '@animotion/core';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};

	let isAll = $derived(step >= 10);

	// Blob
	let blobOpen = $derived((step >= 1 && step <= 3) || isAll);
	let blobHeaderOpen = $derived((step >= 2 && step <= 3) || isAll);
	let blobBodyOpen = $derived(step === 3 || isAll);

	// Tree
	let treeOpen = $derived((step >= 4 && step <= 6) || isAll);
	let treeHeaderOpen = $derived((step >= 5 && step <= 6) || isAll);
	let treeBodyOpen = $derived(step === 6 || isAll);

	// Commit
	let commitOpen = $derived(step >= 7);
	let commitHeaderOpen = $derived(step >= 8);
	let commitBodyOpen = $derived(step >= 9);
</script>

<!-- ========================================================================= -->
<!-- BLOB OBJECT ACTIONS                                                       -->
<!-- ========================================================================= -->
<!-- Action 1: Blob Title -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Blob Header -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<!-- Action 3: Blob Body (Schema) -->
<Action do={() => (step = 3)} undo={() => (step = 2)} />

<!-- ========================================================================= -->
<!-- TREE OBJECT ACTIONS                                                       -->
<!-- ========================================================================= -->
<!-- Action 4: Tree Title (Blob closes) -->
<Action do={() => (step = 4)} undo={() => (step = 3)} />

<!-- Action 5: Tree Header -->
<Action do={() => (step = 5)} undo={() => (step = 4)} />

<!-- Action 6: Tree Body (Schema) -->
<Action do={() => (step = 6)} undo={() => (step = 5)} />

<!-- ========================================================================= -->
<!-- COMMIT OBJECT ACTIONS                                                     -->
<!-- ========================================================================= -->
<!-- Action 7: Commit Title (Tree closes) -->
<Action do={() => (step = 7)} undo={() => (step = 6)} />

<!-- Action 8: Commit Header -->
<Action do={() => (step = 8)} undo={() => (step = 7)} />

<!-- Action 9: Commit Body (Schema) -->
<Action do={() => (step = 9)} undo={() => (step = 8)} />

<!-- ========================================================================= -->
<!-- FINAL STEP: SHOW EVERYTHING (CONCRETE EXAMPLES)                           -->
<!-- ========================================================================= -->
<!-- Action 10: Display All Concrete Examples -->
<Action do={() => (step = 10)} undo={() => (step = 9)} />

<div class="w-[1150px] h-[680px] p-6 text-white flex flex-col items-center justify-center">
	<div class="grid grid-cols-3 gap-6 w-full max-w-[1100px] items-center">
		<!-- Blob Box -->
		<div class="bg-neutral-900 border-2 border-neutral-700 rounded-xl shadow-2xl p-6 text-left transition-all duration-500 ease-out">
			<!-- Step 0 / Collapsed Placeholder -->
			<div
				class="grid transition-all duration-500 ease-out {!blobOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="py-1 text-center font-mono text-sm uppercase tracking-widest text-neutral-400 font-bold">
						Git Object
					</div>
				</div>
			</div>

			<!-- Title Section -->
			<div
				class="grid transition-all duration-500 ease-out {blobOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="border-b-2 border-neutral-700 pb-3 mb-4 flex items-center justify-between">
						<h3 class="text-3xl font-serif font-bold text-white">Blob</h3>
					</div>
				</div>
			</div>

			<!-- Object Header Section -->
			<div
				class="grid transition-all duration-500 ease-out {blobHeaderOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="mb-4 font-mono font-bold text-2xl text-white">
						{#if isAll}
							<span>Blob 11\0</span>
						{:else}
							<span>Blob &lt;size&gt;\0</span>
						{/if}
					</div>
				</div>
			</div>

			<!-- Body Section -->
			<div
				class="grid transition-all duration-500 ease-out {blobBodyOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="h-[210px] font-mono text-xl flex items-center justify-center">
						{#if isAll}
							<p class="text-emerald-400 font-bold">print("Hello World")</p>
						{:else}
							<p class="text-neutral-300 font-medium">&lt;content&gt;</p>
						{/if}
					</div>
				</div>
			</div>
		</div>

		<!-- Tree Box -->
		<div class="bg-neutral-900 border-2 border-neutral-700 rounded-xl shadow-2xl p-6 text-left transition-all duration-500 ease-out">
			<!-- Step 0 / Collapsed Placeholder -->
			<div
				class="grid transition-all duration-500 ease-out {!treeOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="py-1 text-center font-mono text-sm uppercase tracking-widest text-neutral-400 font-bold">
						Git Object
					</div>
				</div>
			</div>

			<!-- Title Section -->
			<div
				class="grid transition-all duration-500 ease-out {treeOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="border-b-2 border-neutral-700 pb-3 mb-4 flex items-center justify-between">
						<h3 class="text-3xl font-serif font-bold text-white">Tree</h3>
					</div>
				</div>
			</div>

			<!-- Object Header Section -->
			<div
				class="grid transition-all duration-500 ease-out {treeHeaderOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="mb-4 font-mono font-bold text-2xl text-white">
						{#if isAll}
							<span>Tree 56\0</span>
						{:else}
							<span>Tree &lt;size&gt;\0</span>
						{/if}
					</div>
				</div>
			</div>

			<!-- Body Section -->
			<div
				class="grid transition-all duration-500 ease-out {treeBodyOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="h-[210px] font-mono text-sm flex flex-col justify-center">
						{#if isAll}
							<div class="space-y-3">
								<div class="flex items-start gap-2">
									<span class="text-xs text-neutral-400">●</span>
									<div>
										<p class="font-bold text-white">100644</p>
										<p class="break-all text-xs text-neutral-300 font-medium">main.py\0e88f7a9.....209c97fa845fdbc</p>
									</div>
								</div>
								<div class="flex items-start gap-2 pt-2">
									<span class="text-xs text-neutral-400">●</span>
									<div>
										<p class="font-bold text-white">100644</p>
										<p class="break-all text-xs text-neutral-300 font-medium">test.py\04b890.....288fbee4904</p>
									</div>
								</div>
							</div>
						{:else}
							<div class="space-y-4 text-xl text-neutral-300 font-medium">
								<p>&lt;mode&gt; &lt;name&gt;\0&lt;20_byte_sha&gt;</p>
								<p>&lt;mode&gt; &lt;name&gt;\0&lt;20_byte_sha&gt;</p>
							</div>
						{/if}
					</div>
				</div>
			</div>
		</div>

		<!-- Commit Box -->
		<div class="bg-neutral-900 border-2 border-neutral-700 rounded-xl shadow-2xl p-6 text-left transition-all duration-500 ease-out">
			<!-- Step 0 / Collapsed Placeholder -->
			<div
				class="grid transition-all duration-500 ease-out {!commitOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="py-1 text-center font-mono text-sm uppercase tracking-widest text-neutral-400 font-bold">
						Git Object
					</div>
				</div>
			</div>

			<!-- Title Section -->
			<div
				class="grid transition-all duration-500 ease-out {commitOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="border-b-2 border-neutral-700 pb-3 mb-4 flex items-center justify-between">
						<h3 class="text-3xl font-serif font-bold text-white">Commit</h3>
					</div>
				</div>
			</div>

			<!-- Object Header Section -->
			<div
				class="grid transition-all duration-500 ease-out {commitHeaderOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="mb-4 font-mono font-bold text-2xl text-white">
						{#if isAll}
							<span>Commit 89\0</span>
						{:else}
							<span>Commit &lt;size&gt;\0</span>
						{/if}
					</div>
				</div>
			</div>

			<!-- Body Section -->
			<div
				class="grid transition-all duration-500 ease-out {commitBodyOpen
					? 'grid-rows-[1fr] opacity-100'
					: 'grid-rows-[0fr] opacity-0'}"
			>
				<div class="overflow-hidden">
					<div class="h-[210px] font-mono text-xs flex flex-col justify-center">
						{#if isAll}
							<div class="space-y-2 text-neutral-300">
								<p><span class="font-bold text-teal-400">Tree</span> 4b8a060e54b......69288fbee4904</p>
								<p><span class="font-bold text-teal-400">Parent</span> 69288fbee4904......8a060e54b</p>
								<p><span class="font-bold text-teal-400">author</span> Lesedi 21/10/2016+200</p>
								<p><span class="font-bold text-teal-400">committer</span> Lesedi 21/10/2026+200</p>
								<p class="pt-3 font-sans italic text-base font-medium text-white">Added stuff to function</p>
							</div>
						{:else}
							<div class="space-y-2 text-neutral-300 font-medium text-sm">
								<p>tree &lt;tree_sha&gt;</p>
								<p>parent &lt;parent_sha&gt;</p>
								<p>author &lt;name&gt; &lt;&lt;email&gt;&gt; &lt;timestamp&gt; &lt;timezone&gt;</p>
								<p>committer &lt;name&gt; &lt;&lt;email&gt;&gt; &lt;timestamp&gt; &lt;timezone&gt;</p>
								<p class="pt-4">&lt;commit message&gt;</p>
							</div>
						{/if}
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
