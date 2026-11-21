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
	Plumbing commands: Low-level commands that manipulate objects, the index, and trees directly (represented by the pipe network).
	Porcelain commands: High-level, user-friendly commands used in everyday Git workflows (represented by the porcelain sink fixture).
</Notes>

<!-- Action 1: Reveal Plumbing Commands & Picture -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Reveal Porcelain Commands & Picture -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<div class="w-[1100px] h-[650px] text-left p-8 text-white flex flex-col justify-between select-none">
	<div class="flex items-center justify-between mb-4">
		<h2 class="text-4xl font-serif font-bold text-white tracking-tight">Types of commands</h2>
	</div>

	<!-- Split Screen: 50 / 50 Cards -->
	<div class="grid grid-cols-2 gap-8 relative flex-1 items-stretch">
		<!-- Left Side: Plumbing -->
		<div
			class="flex flex-col bg-neutral-900/70 border border-neutral-800/90 rounded-2xl p-6 relative overflow-hidden transition-all duration-500 ease-out {step >= 1
				? 'opacity-100 translate-y-0 shadow-2xl'
				: 'opacity-20 translate-y-2'}"
		>
			<div class="flex items-center gap-4 mb-5 pb-4 border-b border-neutral-800">
				<img
					src="/images/plumbing.jpg"
					alt="Plumbing Pipes"
					class="w-20 h-20 rounded-xl object-cover border border-neutral-700/80 shadow-md transition-transform duration-500 {step >= 1 ? 'scale-100' : 'scale-95'}"
				/>
				<div>
					<span class="text-xs font-mono uppercase tracking-wider text-sky-400 font-semibold block">Under the Hood</span>
					<h3 class="text-2xl font-serif font-bold text-white">Plumbing</h3>
				</div>
			</div>

			<ul
				class="space-y-3 font-mono text-xl transition-all duration-500 ease-out {step >= 1
					? 'opacity-100 translate-y-0'
					: 'opacity-0 translate-y-2 pointer-events-none'}"
			>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git hash-object</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git cat-file</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git update-index</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git write-tree</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git commit-tree</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git rev-parse</span>
				</li>
			</ul>
		</div>

		<!-- Right Side: Porcelain -->
		<div
			class="flex flex-col bg-neutral-900/70 border border-neutral-800/90 rounded-2xl p-6 relative overflow-hidden transition-all duration-500 ease-out {step >= 2
				? 'opacity-100 translate-y-0 shadow-2xl'
				: 'opacity-20 translate-y-2'}"
		>
			<div class="flex items-center gap-4 mb-5 pb-4 border-b border-neutral-800">
				<img
					src="/images/porcelain.jpg"
					alt="Porcelain Fixture"
					class="w-20 h-20 rounded-xl object-cover border border-neutral-700/80 shadow-md transition-transform duration-500 {step >= 2 ? 'scale-100' : 'scale-95'}"
				/>
				<div>
					<span class="text-xs font-mono uppercase tracking-wider text-amber-400 font-semibold block">User Facing</span>
					<h3 class="text-2xl font-serif font-bold text-white">Porcelain</h3>
				</div>
			</div>

			<ul
				class="space-y-3 font-mono text-xl transition-all duration-500 ease-out {step >= 2
					? 'opacity-100 translate-y-0'
					: 'opacity-0 translate-y-2 pointer-events-none'}"
			>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git add</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git commit</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git push / git pull</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git status</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git branch</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-200">
					<span class="text-neutral-500 text-base select-none font-mono">$</span>
					<span>git log</span>
				</li>
			</ul>
		</div>
	</div>
</div>
