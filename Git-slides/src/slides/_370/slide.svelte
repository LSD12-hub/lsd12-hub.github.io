<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] p-6 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-base text-gray-200">
		<p><span class="text-pink-500 font-semibold">public static</span> <span class="text-emerald-400">String</span> <span class="text-yellow-300">hashObject</span>(<span class="text-emerald-400">byte</span>[] <span class="text-cyan-300">content</span>, <span class="text-emerald-400">String</span> <span class="text-cyan-300">type</span>, <span class="text-emerald-400">boolean</span> <span class="text-cyan-300">write</span>)</p>
		<p class="pl-8"><span class="text-pink-500">throws</span> <span class="text-emerald-400">IOException</span>, <span class="text-emerald-400">NoSuchAlgorithmException</span> {"{"}</p>
		<div class="pl-8 py-3 space-y-1">
			<p><span class="text-emerald-400">ByteArrayOutputStream</span> outputStream = <span class="text-pink-500">new</span> <span class="text-emerald-400">ByteArrayOutputStream</span>();</p>
			<p>outputStream.<span class="text-yellow-300">writeBytes</span>(headerBytes);</p>
			<p>outputStream.<span class="text-yellow-300">writeBytes</span>(content);</p>
			<p><span class="text-emerald-400">byte</span>[] fullContent = outputStream.<span class="text-yellow-300">toByteArray</span>();</p>
		</div>
		<p>{"}"}</p>
	</div>
</div>
