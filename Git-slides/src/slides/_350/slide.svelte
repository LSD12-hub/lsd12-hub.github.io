<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-sm text-gray-200">
		<div class="space-y-1">
			<p><span class="text-emerald-400">ByteArrayOutputStream</span> decompressedStream = <span class="text-pink-500">new</span> <span class="text-emerald-400">ByteArrayOutputStream</span>();</p>
			<p><span class="text-pink-500">try</span> (<span class="text-emerald-400">FileInputStream</span> fis = <span class="text-pink-500">new</span> <span class="text-emerald-400">FileInputStream</span>(filePath.<span class="text-yellow-300">toFile</span>())) {"{"}</p>
			<p class="pl-6"><span class="text-emerald-400">InflaterInputStream</span> iis = <span class="text-pink-500">new</span> <span class="text-emerald-400">InflaterInputStream</span>(fis);</p>
			<p class="pl-6">decompressedStream.<span class="text-yellow-300">write</span>(iis.<span class="text-yellow-300">readAllBytes</span>());</p>
			<p>{"}"} <span class="text-pink-500">catch</span> (<span class="text-emerald-400">IOException</span> e) {"{"}</p>
			<p class="pl-6"><span class="text-pink-500">throw new</span> <span class="text-emerald-400">IOException</span>(<span class="text-amber-300">"Error reading object: "</span> + e.<span class="text-yellow-300">getMessage</span>());</p>
			<p>{"}"}</p>
			<p class="pt-2"><span class="text-emerald-400">byte</span>[] decompressedData = decompressedStream.<span class="text-yellow-300">toByteArray</span>();</p>
			<div class="pt-3 border-t border-neutral-800 space-y-1">
				<p><span class="text-emerald-400">String</span> content = <span class="text-pink-500">new</span> <span class="text-emerald-400">String</span>(decompressedData, nullIndex + <span class="text-purple-400">1</span>, decompressedData.length - nullIndex - <span class="text-purple-400">1</span>, <span class="text-amber-300">"UTF-8"</span>);</p>
				<p class="text-gray-500">// System.out.print(header + "\n");</p>
				<p class="text-gray-500">// System.out.print(content);</p>
				<p class="text-pink-500 pt-2"><span class="font-semibold">return</span> content;</p>
			</div>
		</div>
	</div>
</div>
