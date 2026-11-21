<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-sm text-gray-200">
		<div class="space-y-1">
			<p><span class="text-pink-500">try</span> (</p>
			<div class="pl-6 space-y-1">
				<p><span class="text-emerald-400">FileOutputStream</span> fos = <span class="text-pink-500">new</span> <span class="text-emerald-400">FileOutputStream</span>(filePath.<span class="text-yellow-300">toFile</span>());</p>
				<p><span class="text-emerald-400">DeflaterOutputStream</span> dos = <span class="text-pink-500">new</span> <span class="text-emerald-400">DeflaterOutputStream</span>(fos);</p>
			</div>
			<p>) {"{"}</p>
			<p class="pl-6">dos.<span class="text-yellow-300">write</span>(fullContent);</p>
			<p>{"}"} <span class="text-pink-500">catch</span> (<span class="text-emerald-400">IOException</span> e) {"{"}</p>
			<p class="pl-6"><span class="text-pink-500">throw new</span> <span class="text-emerald-400">IOException</span>(<span class="text-amber-300">"Error writing object: "</span> + e.<span class="text-yellow-300">getMessage</span>());</p>
			<p>{"}"}</p>
			<p class="text-pink-500 pt-2 font-semibold">return sha1;</p>
		</div>
	</div>
</div>
