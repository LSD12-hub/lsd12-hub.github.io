<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1150px] h-[680px] p-6 text-[#1a202c] flex flex-col items-center">
	<h2 class="text-5xl font-serif mb-6 text-center">Objects</h2>

	<div class="grid grid-cols-3 gap-0 border-2 border-neutral-700 w-full bg-white rounded-md shadow-lg overflow-hidden text-left">
		<!-- Blob Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Blob elol</h3>
			<div class="font-mono text-xl space-y-4">
				<p class="font-bold text-2xl">Blob 11\0</p>
				<p class="text-emerald-700 font-bold">print("Hello World")</p>
			</div>
		</div>

		<!-- Tree Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Tree</h3>
			<div class="font-mono text-sm space-y-3">
				<p class="font-bold text-2xl mb-4 font-mono">Tree 56\0</p>
				<div class="flex items-start gap-2">
					<span class="text-xs">●</span>
					<div>
						<p class="font-semibold">100644</p>
						<p class="break-all text-xs text-neutral-600">main.py\0e88f7a9.....209c97fa845fdbc</p>
					</div>
				</div>
				<div class="flex items-start gap-2 pt-2">
					<span class="text-xs">●</span>
					<div>
						<p class="font-semibold">100644</p>
						<p class="break-all text-xs text-neutral-600">test.py\04b890.....288fbee4904</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Commit Column -->
		<div class="p-6">
			<h3 class="text-3xl font-serif mb-6">Commit</h3>
			<div class="font-mono text-xs space-y-2">
				<p class="font-bold text-2xl font-mono mb-3">Commit 89\0</p>
				<p><span class="font-semibold">Tree</span> 4b8a060e54b......69288fbee4904</p>
				<p><span class="font-semibold">Parent</span> 69288fbee4904......8a060e54b</p>
				<p><span class="font-semibold">author</span> Lesedi 21/10/2016+200</p>
				<p><span class="font-semibold">committer</span> Lesedi 21/10/2026+200</p>
				<p class="pt-3 font-sans italic text-base text-neutral-800">Added stuff to function</p>
			</div>
		</div>
	</div>
</div>
