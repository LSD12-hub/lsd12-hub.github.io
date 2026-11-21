<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-sm text-gray-200">
		<div class="space-y-1">
			<p><span class="text-emerald-400">ByteArrayOutputStream</span> outputStream = <span class="text-pink-500">new</span> <span class="text-emerald-400">ByteArrayOutputStream</span>();</p>
			<p>outputStream.<span class="text-yellow-300">writeBytes</span>(headerBytes);</p>
			<p>outputStream.<span class="text-yellow-300">writeBytes</span>(content);</p>
			<p><span class="text-emerald-400">byte</span>[] fullContent = outputStream.<span class="text-yellow-300">toByteArray</span>();</p>
			<div class="pt-3 border-t border-neutral-800 space-y-1">
				<p><span class="text-emerald-400">MessageDigest</span> digest;</p>
				<p><span class="text-pink-500">try</span> {"{"}</p>
				<p class="pl-6">digest = <span class="text-emerald-400">MessageDigest</span>.<span class="text-yellow-300">getInstance</span>(<span class="text-amber-300">"SHA-1"</span>);</p>
				<p>{"}"} <span class="text-pink-500">catch</span> (<span class="text-emerald-400">NoSuchAlgorithmException</span> e) {"{"}</p>
				<p class="pl-6"><span class="text-pink-500">throw new</span> <span class="text-emerald-400">NoSuchAlgorithmException</span>(<span class="text-amber-300">"SHA-1 algorithm not found"</span>);</p>
				<p>{"}"}</p>
				<p class="pt-2"><span class="text-emerald-400">byte</span>[] hashBytes = digest.<span class="text-yellow-300">digest</span>(fullContent);</p>
			</div>
		</div>
	</div>
</div>
