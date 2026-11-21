<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] text-left p-8 text-[#1a202c] flex items-center justify-between">
	<div class="w-1/2">
		<div class="text-2xl font-serif leading-relaxed pl-4 font-mono">
			<p>{"{"}</p>
			<div class="pl-8 py-1">
				<p>Key: {"{"}</p>
				<div class="pl-8 py-1">
					<p>Key: {"{"}</p>
					<p class="pl-8 py-1 text-[#1e9a8e] font-semibold">Key: Value</p>
					<p>{"}"}</p>
				</div>
				<p>{"}"}</p>
			</div>
			<p>{"}"}</p>
		</div>
	</div>

	<!-- Connected Tree Nodes -->
	<div class="w-1/2 flex items-center justify-center">
		<svg width="400" height="480" viewBox="0 0 400 480" class="drop-shadow-lg">
			<!-- Connecting lines -->
			<line x1="200" y1="110" x2="200" y2="190" stroke="#1e9a8e" stroke-width="3" />
			<line x1="200" y1="190" x2="200" y2="280" stroke="#1e9a8e" stroke-width="3" />
			<line x1="200" y1="280" x2="200" y2="380" stroke="#1e9a8e" stroke-width="3" />
			
			<line x1="120" y1="150" x2="200" y2="190" stroke="#1e9a8e" stroke-width="3" />
			<line x1="260" y1="170" x2="260" y2="240" stroke="#1e9a8e" stroke-width="3" />
			<line x1="200" y1="280" x2="260" y2="240" stroke="#1e9a8e" stroke-width="3" />

			<!-- Node circles -->
			<circle cx="200" cy="110" r="32" fill="#1e9a8e" />
			<circle cx="120" cy="150" r="32" fill="#1e9a8e" />
			<circle cx="200" cy="190" r="32" fill="#1e9a8e" />
			<circle cx="260" cy="170" r="32" fill="#1e9a8e" />
			<circle cx="260" cy="240" r="32" fill="#1e9a8e" />
			<circle cx="200" cy="280" r="32" fill="#1e9a8e" />
			<circle cx="200" cy="380" r="32" fill="#1e9a8e" />
		</svg>
	</div>
</div>
