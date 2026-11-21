<script lang="ts">
	export const props = { background: '#18181b' };
</script>

<div class="w-[1100px] h-[650px] text-left p-10 text-white flex flex-col justify-between select-none">
	<h2 class="text-5xl font-serif font-bold text-white tracking-tight mb-6">Types of commands</h2>

	<div class="grid grid-cols-2 gap-8 relative flex-1 items-stretch">
		<!-- Plumbing (Low-level Pipes) -->
		<div class="flex flex-col bg-neutral-900/70 border border-neutral-800 rounded-2xl p-6 relative overflow-hidden shadow-xl">
			<div class="flex items-center gap-4 mb-5">
				<img
					src="/images/plumbing.jpg"
					alt="Plumbing"
					class="w-20 h-20 rounded-xl object-cover border border-neutral-700 shadow-md"
				/>
				<div>
					<span class="text-xs font-mono uppercase tracking-widest text-sky-400 font-bold block">Low-Level</span>
					<h3 class="text-2xl font-serif font-bold text-white">Plumbing</h3>
				</div>
			</div>

			<ul class="space-y-3.5 font-mono text-xl text-neutral-200">
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git hash-object</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git cat-file</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git update-index</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git write-tree</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git commit-tree</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git rev-parse</span>
				</li>
			</ul>
		</div>

		<!-- Porcelain (User-facing Ceramic Fixtures) -->
		<div class="flex flex-col bg-neutral-900/70 border border-neutral-800 rounded-2xl p-6 relative overflow-hidden shadow-xl">
			<div class="flex items-center gap-4 mb-5">
				<img
					src="/images/porcelain.jpg"
					alt="Porcelain"
					class="w-20 h-20 rounded-xl object-cover border border-neutral-700 shadow-md"
				/>
				<div>
					<span class="text-xs font-mono uppercase tracking-widest text-amber-400 font-bold block">User-Facing</span>
					<h3 class="text-2xl font-serif font-bold text-white">Porcelain</h3>
				</div>
			</div>

			<ul class="space-y-3.5 font-mono text-xl text-neutral-200">
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git add</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git commit</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git push / git pull</span>
				</li>
				<li class="flex items-center gap-3">
					<span class="text-neutral-500 text-base font-mono">$</span>
					<span>git status</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-100">
					<span class="text-neutral-500 text-lg select-none font-mono">$</span>
					<span>git branch</span>
				</li>
				<li class="flex items-center gap-3 text-neutral-100">
					<span class="text-neutral-500 text-lg select-none font-mono">$</span>
					<span>git log</span>
				</li>
			</ul>
		</div>
	</div>
</div>

