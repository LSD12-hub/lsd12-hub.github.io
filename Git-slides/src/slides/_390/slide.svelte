<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-sm text-gray-200">
		<div class="space-y-1">
			<p><span class="text-emerald-400">byte</span>[] hashBytes = digest.<span class="text-yellow-300">digest</span>(fullContent);</p>
			<div class="pt-3 border-t border-neutral-800 space-y-1">
				<p><span class="text-pink-500 font-semibold">if</span> (write) {"{"}</p>
				<div class="pl-6 space-y-1">
					<p><span class="text-emerald-400">String</span> dirName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">0</span>, <span class="text-purple-400">2</span>);</p>
					<p><span class="text-emerald-400">String</span> fileName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">2</span>);</p>
					<p><span class="text-emerald-400">Path</span> dirPath = <span class="text-emerald-400">Path</span>.<span class="text-yellow-300">of</span>(<span class="text-amber-300">".git"</span>, <span class="text-amber-300">"objects"</span>, dirName);</p>
					<p><span class="text-emerald-400">Path</span> filePath = dirPath.<span class="text-yellow-300">resolve</span>(fileName);</p>
				</div>
				<p>{"}"}</p>
			</div>
		</div>
	</div>
</div>
