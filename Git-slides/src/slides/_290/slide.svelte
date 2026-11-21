<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Objects</h2>
	<ul class="text-3xl font-serif leading-loose space-y-6 list-disc list-inside">
		<li>They are identified by a hash.</li>
		<li>A hash is normally 20 characters long.</li>
		<li>Example of hash: <span class="font-mono text-2xl">f0121e40a7c4acc32b94199cbb91fc1e23367541</span></li>
		<li>Live in .git/objects</li>
		<li class="flex items-center gap-2">
			<span class="font-mono text-2xl">.git/objects/</span>
			<span class="font-mono text-2xl border-2 border-red-600 px-2 py-0.5 bg-red-50 rounded">f0</span>
			<span class="font-mono text-2xl">/</span>
			<span class="font-mono text-2xl border-2 border-red-600 px-2 py-0.5 bg-red-50 rounded">121e40a7c4acc32b94199cbb91fc1e23367541</span>
		</li>
	</ul>
</div>
