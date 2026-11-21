<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[680px] p-4 flex items-center justify-center text-[#1a202c]">
	<div class="flex items-center gap-8">
		<!-- Commits Column -->
		<div class="border-2 border-teal-800 p-4 rounded-sm shadow-md bg-white flex flex-col gap-8 items-center">
			<!-- Second Commit -->
			<div class="bg-[#1e9a8e] text-white p-5 rounded w-52 text-left shadow">
				<p class="text-xs font-mono opacity-80">1bf34b</p>
				<p class="text-xl font-serif font-bold mt-1">Second commit lol</p>
			</div>

			<!-- Vertical Down Arrow -->
			<svg width="24" height="40" viewBox="0 0 24 40">
				<line x1="12" y1="0" x2="12" y2="30" stroke="#1e9a8e" stroke-width="2" />
				<polygon points="6,30 12,40 18,30" fill="#1e9a8e" />
			</svg>

			<!-- First Commit -->
			<div class="bg-[#1e9a8e] text-white p-5 rounded w-52 text-left shadow">
				<p class="text-xs font-mono opacity-80">fddf5c</p>
				<p class="text-xl font-serif font-bold mt-1">First commit</p>
			</div>
		</div>

		<!-- Tree & Blobs Column -->
		<div class="flex flex-col gap-12">
			<!-- Row 1: Second Commit Tree & Blobs -->
			<div class="flex items-center gap-6">
				<!-- Arrow -->
				<svg width="40" height="24" viewBox="0 0 40 24">
					<line x1="0" y1="12" x2="30" y2="12" stroke="#1e9a8e" stroke-width="2" />
					<polygon points="30,6 40,12 30,18" fill="#1e9a8e" />
				</svg>

				<!-- Tree 2 -->
				<div class="border-2 border-[#1e9a8e] bg-[#fff9e6] p-5 rounded w-48 text-left shadow">
					<p class="text-xs font-mono text-neutral-600">f7d80b</p>
					<p class="text-xl font-serif font-bold mt-1 text-neutral-900">Tree</p>
				</div>

				<!-- Fork Arrows -->
				<div class="flex flex-col justify-center">
					<svg width="50" height="120" viewBox="0 0 50 120">
						<!-- Arrow to test.py -->
						<line x1="0" y1="60" x2="40" y2="20" stroke="#1e9a8e" stroke-width="2" />
						<polygon points="35,14 48,18 42,28" fill="#1e9a8e" />
						<!-- Arrow to main.py -->
						<line x1="0" y1="60" x2="40" y2="100" stroke="#1e9a8e" stroke-width="2" />
						<polygon points="42,92 48,102 35,106" fill="#1e9a8e" />
					</svg>
				</div>

				<!-- Blob: test.py -->
				<div class="flex flex-col gap-8">
					<div class="bg-[#0d1117] text-white p-4 rounded w-44 text-left shadow">
						<p class="text-xs font-mono text-gray-400">17fb89</p>
						<p class="text-lg font-serif font-bold mt-1">test.py</p>
					</div>
				</div>
			</div>

			<!-- Row 2: First Commit Tree & Blob -->
			<div class="flex items-center gap-6">
				<!-- Arrow -->
				<svg width="40" height="24" viewBox="0 0 40 24">
					<line x1="0" y1="12" x2="30" y2="12" stroke="#1e9a8e" stroke-width="2" />
					<polygon points="30,6 40,12 30,18" fill="#1e9a8e" />
				</svg>

				<!-- Tree 1 -->
				<div class="border-2 border-[#1e9a8e] bg-[#fff9e6] p-5 rounded w-48 text-left shadow">
					<p class="text-xs font-mono text-neutral-600">kf6d60</p>
					<p class="text-xl font-serif font-bold mt-1 text-neutral-900">Tree</p>
				</div>

				<!-- Arrow -->
				<svg width="50" height="24" viewBox="0 0 50 24">
					<line x1="0" y1="12" x2="40" y2="12" stroke="#1e9a8e" stroke-width="2" />
					<polygon points="40,6 50,12 40,18" fill="#1e9a8e" />
				</svg>

				<!-- Blob: main.py -->
				<div class="bg-[#0d1117] text-white p-4 rounded w-44 text-left shadow">
					<p class="text-xs font-mono text-gray-400">bl08f5</p>
					<p class="text-lg font-serif font-bold mt-1">main.py</p>
				</div>
			</div>
		</div>
	</div>
</div>
