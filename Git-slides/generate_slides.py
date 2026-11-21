import os

BASE_DIR = r"C:\Users\lavis\OneDrive\Documents\projects\git-slides\src\slides"
os.makedirs(BASE_DIR, exist_ok=True)

slides_data = {}

# Slide 010: Title with Clean Centered Layout & Typewriter on Next
slides_data["010"] = """<script lang="ts">
	import { Action } from '@animotion/core';
	import { createTypewriter } from '$lib';

	const tw = createTypewriter([
		'Learn programming the fun way',
		'by building git.'
	], { speed: 40, lineDelay: 180 });

	export const props = {
		out: () => tw.reset()
	};
</script>

<Action do={tw.start} undo={tw.reset} />

<div class="flex flex-col items-center justify-between h-[520px] w-full max-w-4xl text-center">
	<!-- Top Spacer to keep heading centered -->
	<div></div>

	<!-- Clean Heading with Typewriter -->
	<h1 class="text-6xl font-bold tracking-tight leading-tight min-h-[160px] flex flex-col items-center justify-center">
		{#if !tw.hasStarted}
			<span class="inline-block w-1 h-14 bg-emerald-400 animate-pulse"></span>
		{:else}
			<div>
				<span>{tw.typedLines[0]}</span>
				{#if tw.isTyping && tw.currentLineIndex === 0}
					<span class="inline-block w-1 h-12 bg-emerald-400 ml-1.5 align-middle animate-pulse"></span>
				{/if}
			</div>
			{#if tw.currentLineIndex >= 1 || tw.isDone}
				<div class="mt-2 text-emerald-400">
					<span>{tw.typedLines[1]}</span>
					{#if !tw.isDone}
						<span class="inline-block w-1 h-12 bg-white ml-1.5 align-middle animate-pulse"></span>
					{/if}
				</div>
			{/if}
		{/if}
	</h1>

	<!-- Name at Bottom -->
	<p class="text-2xl text-gray-400 font-medium tracking-wide transition-opacity duration-700 {tw.isDone ? 'opacity-100' : 'opacity-40'}">
		Lesedi Jonas
	</p>
</div>
"""

# Slide 020: Multi-Branch Side-Quest DAG Visual with Step Actions
slides_data["020"] = """<script lang="ts">
	import { Action } from '@animotion/core';
	import { tween } from '@animotion/motion';
	import { createTypewriter } from '$lib';

	const tw = createTypewriter('git checkout -b side-quest/build-git', { speed: 35 });

	// Animotion Tweens
	const branchProgress = tween(0, { duration: 550 });
	const commitScale = tween(0, { duration: 350 });

	const subBranchProgress = tween(0, { duration: 500 });
	const subCommitScale = tween(0, { duration: 350 });

	// Action 1: Type command & reveal primary side-quest branch
	async function step1() {
		await tw.start();
		await branchProgress.to(100);
		await commitScale.to(1);
	}

	function undoStep1() {
		tw.reset();
		branchProgress.reset();
		commitScale.reset();
	}

	// Action 2: Reveal sub-branches (Storage/Zlib and Merkle Trees/DAG)
	async function step2() {
		await subBranchProgress.to(100);
		await subCommitScale.to(1);
	}

	function undoStep2() {
		subBranchProgress.reset();
		subCommitScale.reset();
	}

	export const props = {
		out: () => {
			undoStep2();
			undoStep1();
		}
	};
</script>

<!-- Action 1: Command + Primary Branch -->
<Action do={step1} undo={undoStep1} />

<!-- Action 2: Sub-Branches (Cyan & Purple) -->
<Action do={step2} undo={undoStep2} />

<div class="flex flex-col items-center justify-center max-w-5xl w-full text-center px-4">
	<div class="w-full bg-neutral-950/90 border border-neutral-800 rounded-2xl p-7 shadow-2xl text-left">
		<div class="font-mono text-base bg-black/90 px-5 py-3 rounded-xl border border-emerald-500/40 text-emerald-400 shadow-inner mb-5 flex items-center min-h-[52px]">
			<span class="text-neutral-500 mr-2">$</span>
			{#if !tw.hasStarted}
				<span class="inline-block w-2.5 h-5 bg-emerald-400 align-middle animate-pulse"></span>
			{:else}
				<span>{tw.text}</span>
				{#if !tw.isDone}
					<span class="inline-block w-2.5 h-5 bg-emerald-400 ml-1.5 align-middle animate-pulse"></span>
				{/if}
			{/if}
		</div>

		<!-- Full-Width SVG Branch Diagram with Sub-branches -->
		<div class="bg-neutral-900/80 p-6 rounded-xl border border-neutral-800">
			<svg width="760" height="260" viewBox="0 0 760 260" class="w-full">
				<!-- Level 0: Main Branch (Top - Always Visible) -->
				<line x1="30" y1="35" x2="730" y2="35" stroke="#4b5563" stroke-width="4" stroke-dasharray="8 8" />
				<circle cx="70" cy="35" r="13" fill="#4b5563" />
				<text x="70" y="18" fill="#9ca3af" font-size="12" font-family="monospace" text-anchor="middle">main</text>
				
				<circle cx="270" cy="35" r="13" fill="#4b5563" />
				<text x="270" y="18" fill="#6b7280" font-size="12" font-family="monospace" text-anchor="middle">Jira-402</text>
				
				<circle cx="530" cy="35" r="13" fill="#4b5563" />
				<text x="530" y="18" fill="#6b7280" font-size="12" font-family="monospace" text-anchor="middle">Actual Work 🏢</text>

				<!-- Level 1: Primary Side Quest Branch (Emerald) -->
				{#if branchProgress.current > 0}
					<path
						d="M 70 35 Q 150 35 180 105 L 730 105"
						fill="transparent"
						stroke="#10b981"
						stroke-width="4"
						pathLength="100"
						stroke-dasharray="100"
						stroke-dashoffset={100 - branchProgress.current}
					/>
				{/if}

				<!-- Level 1 Commits -->
				{#if commitScale.current > 0}
					<g style:opacity={commitScale.current} style:transform="scale({commitScale.current})" style="transform-origin: 260px 105px; transform-box: fill-box;">
						<circle cx="260" cy="105" r="15" fill="#10b981" class="animate-pulse" />
						<text x="260" y="85" fill="#34d399" font-size="12" font-family="monospace" text-anchor="middle">hash-object</text>

						<circle cx="430" cy="105" r="15" fill="#10b981" />
						<text x="430" y="85" fill="#34d399" font-size="12" font-family="monospace" text-anchor="middle">cat-file</text>

						<circle cx="650" cy="105" r="15" fill="#10b981" />
						<text x="650" y="85" fill="#34d399" font-size="12" font-family="monospace" text-anchor="middle" font-weight="bold">side-quest ⚔️</text>
					</g>
				{/if}

				<!-- Level 2: Sub-branch 1 - Storage & Compression (Cyan) -->
				{#if subBranchProgress.current > 0}
					<path
						d="M 260 105 Q 310 105 340 175 L 730 175"
						fill="transparent"
						stroke="#06b6d4"
						stroke-width="3.5"
						pathLength="100"
						stroke-dasharray="100"
						stroke-dashoffset={100 - subBranchProgress.current}
					/>
				{/if}

				<!-- Level 2: Sub-branch 2 - Merkle Trees & DAGs (Purple - Extends off right edge) -->
				{#if subBranchProgress.current > 0}
					<path
						d="M 430 105 Q 470 105 500 235 L 760 235"
						fill="transparent"
						stroke="#a855f7"
						stroke-width="3.5"
						pathLength="100"
						stroke-dasharray="100"
						stroke-dashoffset={100 - subBranchProgress.current}
					/>
				{/if}

				<!-- Level 2 & 3 Sub-Branch Commits -->
				{#if subCommitScale.current > 0}
					<!-- Cyan Commits (Storage/Zlib) -->
					<g style:opacity={subCommitScale.current} style:transform="scale({subCommitScale.current})" style="transform-origin: 410px 175px; transform-box: fill-box;">
						<circle cx="410" cy="175" r="13" fill="#06b6d4" />
						<text x="410" y="157" fill="#67e8f9" font-size="11" font-family="monospace" text-anchor="middle">sha-1 & zlib</text>

						<circle cx="580" cy="175" r="13" fill="#06b6d4" />
						<text x="580" y="157" fill="#67e8f9" font-size="11" font-family="monospace" text-anchor="middle">internals 📦</text>
					</g>

					<!-- Purple Commits (Merkle Tree / DAG) with forward connector -->
					<g style:opacity={subCommitScale.current} style:transform="scale({subCommitScale.current})" style="transform-origin: 570px 235px; transform-box: fill-box;">
						<circle cx="570" cy="235" r="13" fill="#a855f7" />
						<text x="570" y="217" fill="#d8b4fe" font-size="11" font-family="monospace" text-anchor="middle">merkle-trees 🌳</text>

						<circle cx="670" cy="235" r="13" fill="#a855f7" />
						<text x="670" y="217" fill="#d8b4fe" font-size="11" font-family="monospace" text-anchor="middle" font-weight="bold">dag 🔀</text>

						<!-- Pulse arrow extending right to next slide -->
						<circle cx="750" cy="235" r="5" fill="#d8b4fe" class="animate-pulse" />
					</g>
				{/if}
			</svg>
		</div>
	</div>
</div>
"""

# Slide 030: LeetCode Connected Transition via Purple Branch Line
slides_data["030"] = """<script lang="ts">
	import { Action } from '@animotion/core';
	import { tween } from '@animotion/motion';

	// Animotion Tweens for incoming purple branch & logo reveal
	const lineProgress = tween(0, { duration: 650 });
	const logoScale = tween(0, { duration: 450 });
	const labelOpacity = tween(0, { duration: 400 });

	async function animate() {
		// 1. Purple branch line enters from the left edge and connects to the logo
		await lineProgress.to(100);
		// 2. Logo pops in on contact with the branch line
		await logoScale.to(1);
		// 3. Reveal title
		await labelOpacity.to(1);
	}

	function reset() {
		lineProgress.reset();
		logoScale.reset();
		labelOpacity.reset();
	}

	export const props = {
		out: reset
	};
</script>

<Action do={animate} undo={reset} />

<div class="relative flex flex-col items-center justify-center h-full w-full max-w-5xl mx-auto px-4">
	<!-- Purple Branch Line Incoming from Left Edge (viewBox 900x500) -->
	<svg class="absolute inset-0 w-full h-full pointer-events-none" viewBox="0 0 900 500">
		{#if lineProgress.current > 0}
			<!-- Incoming branch connection curve -->
			<path
				d="M 0 250 L 320 250"
				fill="transparent"
				stroke="#a855f7"
				stroke-width="5"
				pathLength="100"
				stroke-dasharray="100"
				stroke-dashoffset={100 - lineProgress.current}
			/>

			<!-- Commits along the incoming line -->
			<circle cx="60" cy="250" r="10" fill="#a855f7" />
			<text x="60" y="225" fill="#d8b4fe" font-size="13" font-family="monospace" text-anchor="middle">data-structures</text>

			<circle cx="200" cy="250" r="10" fill="#a855f7" />
			<text x="200" y="225" fill="#d8b4fe" font-size="13" font-family="monospace" text-anchor="middle">algorithms</text>

			<!-- Moving Energy Head Pulse -->
			{#if lineProgress.current < 99}
				<circle
					cx={320 * (lineProgress.current / 100)}
					cy="250"
					r="9"
					fill="#f3e8ff"
					class="animate-pulse"
				/>
			{/if}
		{/if}
	</svg>

	<!-- Centered Transparent LeetCode Logo & Header -->
	<div class="flex flex-col items-center justify-center z-10 ml-28">
		<div
			class="relative flex items-center justify-center p-4 transition-all"
			style:transform="scale({logoScale.current})"
			style:opacity={logoScale.current}
		>
			<!-- Ambient Glow Behind Logo -->
			{#if logoScale.current > 0}
				<div class="absolute inset-0 bg-gradient-to-r from-purple-500/25 to-amber-500/25 blur-3xl rounded-full"></div>
			{/if}

			<!-- Transparent LeetCode SVG -->
			<img
				src="/images/leetcode.svg"
				alt="LeetCode"
				class="w-64 h-64 object-contain drop-shadow-[0_0_40px_rgba(255,161,22,0.35)]"
			/>
		</div>

		<!-- Title Below -->
		<div
			class="mt-3 font-sans tracking-wide text-center transition-all duration-500"
			style:opacity={labelOpacity.current}
			style:transform="translateY({(1 - labelOpacity.current) * 12}px)"
		>
			<h2 class="text-4xl font-extrabold text-white tracking-wider flex items-center justify-center gap-1">
				<span>Leet</span><span class="text-[#FFA116]">Code</span>
			</h2>
		</div>
	</div>
</div>
"""

# Slide 040: LeetCode Profile
slides_data["040"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_04.png" alt="LeetCode Profile" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 050: Data Structures Grid
slides_data["050"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_05.png" alt="Data Structures" class="max-h-[85vh] max-w-full rounded-xl shadow-xl border border-neutral-300 bg-white" />
</div>
"""

# Slide 060: Data Structures Grid with Highlights
slides_data["060"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_06.png" alt="Data Structures with Highlights" class="max-h-[85vh] max-w-full rounded-xl shadow-xl border border-neutral-300 bg-white" />
</div>
"""

# Slide 070: On my pc right now Meme
slides_data["070"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_07.png" alt="On my pc right now" class="max-h-[82vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 080: YouTube Logo
slides_data["080"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_08.png" alt="YouTube" class="max-h-[80vh] max-w-full rounded-xl shadow-2xl" />
</div>
"""

# Slide 090: Make it look easy Meme
slides_data["090"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_09.png" alt="You make it look easy" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 100: Chair Tipping Comic
slides_data["100"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_10.png" alt="Chair Tipping Comic" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 110: Google Search: How to build git
slides_data["110"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_11.png" alt="How to build git" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-700" />
</div>
"""

# Slide 120: Books in Library
slides_data["120"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_12.png" alt="Books" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 130: Sandwich Comic - Thinking I can build git
slides_data["130"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_13.png" alt="Me thinking I can build git" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 140: Sandwich Comic - Understanding Git
slides_data["140"] = """<div class="flex items-center justify-center h-full">
	<img src="/images/slide_14.png" alt="Me understanding git" class="max-h-[85vh] max-w-full rounded-xl shadow-2xl border border-neutral-800" />
</div>
"""

# Slide 150: Section: Content-addressable filesystem
slides_data["150"] = """<script lang="ts">
	export const props = { background: '#1e9a8e' };
</script>

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide leading-tight">
		Content-addressable<br />filesystem
	</h1>
</div>
"""

# Slide 160: Key Value Pairs (1)
slides_data["160"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Key Value Pairs</h2>
	<div class="text-4xl font-serif leading-relaxed pl-4">
		<p class="font-mono">{"{"}</p>
		<p class="font-mono pl-12 py-4">Key: value</p>
		<p class="font-mono">{"}"}</p>
	</div>
</div>
"""

# Slide 170: WAIT !!! Is git not a graph?
slides_data["170"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="flex flex-col items-center justify-center h-full w-[1100px] text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-6 text-center w-full">WAIT !!! Is git not a graph?</h2>
	<img src="/images/slide_17.png" alt="Git Graph" class="max-h-[68vh] max-w-full rounded-lg shadow-2xl border border-neutral-300" />
</div>
"""

# Slide 180: Key Value Pairs (2 - Nested)
slides_data["180"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Key Value Pairs</h2>
	<div class="text-4xl font-serif leading-relaxed pl-4 font-mono">
		<p>{"{"}</p>
		<div class="pl-12 py-2">
			<p>Key: {"{"}</p>
			<p class="pl-12 py-2 text-[#1e9a8e] font-semibold">Key: Value</p>
			<p>{"}"}</p>
		</div>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 190: Key Value Pairs (3 - Nested deeper)
slides_data["190"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Key Value Pairs</h2>
	<div class="text-3xl font-serif leading-relaxed pl-4 font-mono">
		<p>{"{"}</p>
		<div class="pl-10 py-1">
			<p>Key: {"{"}</p>
			<div class="pl-10 py-1">
				<p>Key: {"{"}</p>
				<p class="pl-10 py-1 text-[#1e9a8e] font-semibold">Key: Value</p>
				<p>{"}"}</p>
			</div>
			<p>{"}"}</p>
		</div>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 200: Key Value Pairs + Tree Graph Visual
slides_data["200"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] text-left p-8 text-[#1a202c] flex items-center justify-between">
	<div class="w-1/2">
		<h2 class="text-5xl font-serif mb-10">Key Value Pairs</h2>
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
"""

# Slide 210: Objects Specification
slides_data["210"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1150px] h-[680px] p-6 text-[#1a202c] flex flex-col items-center">
	<h2 class="text-5xl font-serif mb-6 text-center">Objects</h2>

	<div class="grid grid-cols-3 gap-0 border-2 border-neutral-700 w-full bg-white rounded-md shadow-lg overflow-hidden text-left">
		<!-- Blob Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Blob</h3>
			<div class="font-mono text-xl space-y-4">
				<p class="font-bold text-2xl">Blob &lt;size&gt;\\0</p>
				<p class="text-neutral-700">&lt;content&gt;</p>
			</div>
		</div>

		<!-- Tree Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Tree</h3>
			<div class="font-mono text-xl space-y-4">
				<p class="font-bold text-2xl">Tree &lt;size&gt;\\0</p>
				<p class="text-neutral-700">&lt;mode&gt; &lt;name&gt;\\0&lt;20_byte_sha&gt;</p>
				<p class="text-neutral-700">&lt;mode&gt; &lt;name&gt;\\0&lt;20_byte_sha&gt;</p>
			</div>
		</div>

		<!-- Commit Column -->
		<div class="p-6">
			<h3 class="text-3xl font-serif mb-6">Commit</h3>
			<div class="font-mono text-sm space-y-2">
				<p class="font-bold text-2xl font-mono mb-3">Commit &lt;size&gt;\\0</p>
				<p class="text-neutral-700">tree &lt;tree_sha&gt;</p>
				<p class="text-neutral-700">parent &lt;parent_sha&gt;</p>
				<p class="text-neutral-700">author &lt;name&gt; &lt;&lt;email&gt;&gt; &lt;timestamp&gt; &lt;timezone&gt;</p>
				<p class="text-neutral-700">committer &lt;name&gt; &lt;&lt;email&gt;&gt; &lt;timestamp&gt; &lt;timezone&gt;</p>
				<p class="text-neutral-700 pt-4">&lt;commit message&gt;</p>
			</div>
		</div>
	</div>
</div>
"""

# Slide 220: Objects Concrete Example
slides_data["220"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1150px] h-[680px] p-6 text-[#1a202c] flex flex-col items-center">
	<h2 class="text-5xl font-serif mb-6 text-center">Objects</h2>

	<div class="grid grid-cols-3 gap-0 border-2 border-neutral-700 w-full bg-white rounded-md shadow-lg overflow-hidden text-left">
		<!-- Blob Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Blob</h3>
			<div class="font-mono text-xl space-y-4">
				<p class="font-bold text-2xl">Blob 11\\0</p>
				<p class="text-emerald-700 font-bold">print("Hello World")</p>
			</div>
		</div>

		<!-- Tree Column -->
		<div class="p-6 border-r-2 border-neutral-700">
			<h3 class="text-3xl font-serif mb-6">Tree</h3>
			<div class="font-mono text-sm space-y-3">
				<p class="font-bold text-2xl mb-4 font-mono">Tree 56\\0</p>
				<div class="flex items-start gap-2">
					<span class="text-xs">●</span>
					<div>
						<p class="font-semibold">100644</p>
						<p class="break-all text-xs text-neutral-600">main.py\\0e88f7a9.....209c97fa845fdbc</p>
					</div>
				</div>
				<div class="flex items-start gap-2 pt-2">
					<span class="text-xs">●</span>
					<div>
						<p class="font-semibold">100644</p>
						<p class="break-all text-xs text-neutral-600">test.py\\04b890.....288fbee4904</p>
					</div>
				</div>
			</div>
		</div>

		<!-- Commit Column -->
		<div class="p-6">
			<h3 class="text-3xl font-serif mb-6">Commit</h3>
			<div class="font-mono text-xs space-y-2">
				<p class="font-bold text-2xl font-mono mb-3">Commit 89\\0</p>
				<p><span class="font-semibold">Tree</span> 4b8a060e54b......69288fbee4904</p>
				<p><span class="font-semibold">Parent</span> 69288fbee4904......8a060e54b</p>
				<p><span class="font-semibold">author</span> Lesedi 21/10/2016+200</p>
				<p><span class="font-semibold">committer</span> Lesedi 21/10/2026+200</p>
				<p class="pt-3 font-sans italic text-base text-neutral-800">Added stuff to function</p>
			</div>
		</div>
	</div>
</div>
"""

# Slide 230: Diagram - First Commit
slides_data["230"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] p-8 flex items-center justify-center text-[#1a202c]">
	<div class="flex items-center gap-12">
		<!-- Commit Box in outer container -->
		<div class="border-2 border-teal-800 p-4 rounded-sm shadow-md bg-white">
			<div class="bg-[#1e9a8e] text-white p-6 rounded w-52 text-left shadow">
				<p class="text-sm font-mono opacity-80">fddf5c</p>
				<p class="text-2xl font-serif font-bold mt-2">First commit</p>
			</div>
		</div>

		<!-- Arrow -->
		<div class="flex items-center text-[#1e9a8e]">
			<svg width="60" height="24" viewBox="0 0 60 24">
				<line x1="0" y1="12" x2="50" y2="12" stroke="#1e9a8e" stroke-width="2" />
				<polygon points="50,6 60,12 50,18" fill="#1e9a8e" />
			</svg>
		</div>

		<!-- Tree Box -->
		<div class="border-2 border-[#1e9a8e] bg-[#fff9e6] p-6 rounded w-52 text-left shadow">
			<p class="text-sm font-mono text-neutral-600">kf6d60</p>
			<p class="text-2xl font-serif font-bold mt-2 text-neutral-900">Tree</p>
		</div>

		<!-- Arrow -->
		<div class="flex items-center text-[#1e9a8e]">
			<svg width="60" height="24" viewBox="0 0 60 24">
				<line x1="0" y1="12" x2="50" y2="12" stroke="#1e9a8e" stroke-width="2" />
				<polygon points="50,6 60,12 50,18" fill="#1e9a8e" />
			</svg>
		</div>

		<!-- Blob Box -->
		<div class="bg-[#0d1117] text-white p-6 rounded w-52 text-left shadow">
			<p class="text-sm font-mono text-gray-400">bl08f5</p>
			<p class="text-2xl font-serif font-bold mt-2">main.py</p>
		</div>
	</div>
</div>
"""

# Slide 240: Diagram - Second Commit
slides_data["240"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[680px] p-4 flex items-center justify-center text-[#1a202c]">
	<div class="flex items-center gap-8">
		<!-- Commits Column -->
		<div class="border-2 border-teal-800 p-4 rounded-sm shadow-md bg-white flex flex-col gap-8 items-center">
			<!-- Second Commit -->
			<div class="bg-[#1e9a8e] text-white p-5 rounded w-52 text-left shadow">
				<p class="text-xs font-mono opacity-80">1bf34b</p>
				<p class="text-xl font-serif font-bold mt-1">Second commit</p>
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
"""

# Slide 250: Diagram - Third Commit
slides_data["250"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1150px] h-[720px] p-2 flex items-center justify-center text-[#1a202c]">
	<img src="/images/slide_25.png" alt="Three commits DAG" class="max-h-[85vh] max-w-full rounded-lg shadow-xl border border-neutral-300" />
</div>
"""

# Slide 260: Objects - Hashes Intro
slides_data["260"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Objects</h2>
	<ul class="text-3xl font-serif leading-loose space-y-6 list-disc list-inside">
		<li>They are identified by a hash.</li>
		<li>A hash is normally 20 characters long.</li>
	</ul>
</div>
"""

# Slide 270: Objects - Example Hash
slides_data["270"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Objects</h2>
	<ul class="text-3xl font-serif leading-loose space-y-6 list-disc list-inside">
		<li>They are identified by a hash.</li>
		<li>A hash is normally 20 characters long.</li>
		<li class="flex items-center gap-3">
			<span>Example of hash:</span>
			<span class="font-mono text-2xl border-2 border-red-600 px-3 py-1 bg-red-50 text-neutral-900 rounded">
				f0121e40a7c4acc32b94199cbb91fc1e23367541
			</span>
		</li>
	</ul>
</div>
"""

# Slide 280: Objects - Live in .git/objects
slides_data["280"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Objects</h2>
	<ul class="text-3xl font-serif leading-loose space-y-6 list-disc list-inside">
		<li>They are identified by a hash.</li>
		<li>A hash is normally 20 characters long.</li>
		<li>Example of hash: <span class="font-mono text-2xl">f0121e40a7c4acc32b94199cbb91fc1e23367541</span></li>
		<li class="flex items-center gap-3">
			<span>Live in</span>
			<span class="font-mono text-2xl border-2 border-red-600 px-3 py-1 bg-red-50 text-neutral-900 rounded">
				.git/objects
			</span>
		</li>
	</ul>
</div>
"""

# Slide 290: Objects - Hash prefix directory
slides_data["290"] = """<script lang="ts">
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
"""

# Slide 300: Interacting with Objects
slides_data["300"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Interacting with Objects</h2>
	<ul class="text-4xl font-serif leading-loose space-y-4 list-disc list-inside">
		<li>Reading</li>
		<li>Writing</li>
	</ul>
</div>
"""

# Slide 310: Before reading and writing...
slides_data["310"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="flex items-center justify-center h-[650px] w-[1000px] text-[#1a202c]">
	<h2 class="text-4xl font-serif text-center leading-relaxed">
		Before reading and writing we need to explain masking.
	</h2>
</div>
"""

# Slide 320: catFile (Step 1 - Signature)
slides_data["320"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] p-6 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-xl text-gray-200">
		<p><span class="text-pink-500 font-semibold">public static</span> <span class="text-emerald-400">String</span> <span class="text-yellow-300">catFile</span>(<span class="text-emerald-400">String</span> <span class="text-cyan-300">sha1</span>) <span class="text-pink-500">throws</span> <span class="text-emerald-400">IOException</span> {"{"}</p>
		<p class="text-gray-500 py-4 pl-8">// ...</p>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 330: catFile (Step 2 - Paths)
slides_data["330"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] p-6 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-lg text-gray-200">
		<p><span class="text-pink-500 font-semibold">public static</span> <span class="text-emerald-400">String</span> <span class="text-yellow-300">catFile</span>(<span class="text-emerald-400">String</span> <span class="text-cyan-300">sha1</span>) <span class="text-pink-500">throws</span> <span class="text-emerald-400">IOException</span> {"{"}</p>
		<div class="pl-8 py-3 space-y-1">
			<p><span class="text-emerald-400">String</span> dirName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">0</span>, <span class="text-purple-400">2</span>);</p>
			<p><span class="text-emerald-400">String</span> fileName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">2</span>);</p>
			<p><span class="text-emerald-400">Path</span> filePath = <span class="text-emerald-400">Path</span>.<span class="text-yellow-300">of</span>(<span class="text-amber-300">".git"</span>, <span class="text-amber-300">"objects"</span>, dirName, fileName);</p>
		</div>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 340: catFile (Step 3 - Decompression)
slides_data["340"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-base text-gray-200 overflow-hidden">
		<p><span class="text-pink-500 font-semibold">public static</span> <span class="text-emerald-400">String</span> <span class="text-yellow-300">catFile</span>(<span class="text-emerald-400">String</span> <span class="text-cyan-300">sha1</span>) <span class="text-pink-500">throws</span> <span class="text-emerald-400">IOException</span> {"{"}</p>
		<div class="pl-6 py-2 space-y-1">
			<p><span class="text-emerald-400">String</span> dirName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">0</span>, <span class="text-purple-400">2</span>);</p>
			<p><span class="text-emerald-400">String</span> fileName = sha1.<span class="text-yellow-300">substring</span>(<span class="text-purple-400">2</span>);</p>
			<p><span class="text-emerald-400">Path</span> filePath = <span class="text-emerald-400">Path</span>.<span class="text-yellow-300">of</span>(<span class="text-amber-300">".git"</span>, <span class="text-amber-300">"objects"</span>, dirName, fileName);</p>
			<div class="pt-2 border-t border-neutral-800">
				<p><span class="text-emerald-400">ByteArrayOutputStream</span> decompressedStream = <span class="text-pink-500">new</span> <span class="text-emerald-400">ByteArrayOutputStream</span>();</p>
				<p><span class="text-pink-500">try</span> (<span class="text-emerald-400">FileInputStream</span> fis = <span class="text-pink-500">new</span> <span class="text-emerald-400">FileInputStream</span>(filePath.<span class="text-yellow-300">toFile</span>())) {"{"}</p>
				<p class="pl-6"><span class="text-emerald-400">InflaterInputStream</span> iis = <span class="text-pink-500">new</span> <span class="text-emerald-400">InflaterInputStream</span>(fis);</p>
				<p class="pl-6">decompressedStream.<span class="text-yellow-300">write</span>(iis.<span class="text-yellow-300">readAllBytes</span>());</p>
				<p>{"}"} <span class="text-pink-500">catch</span> (<span class="text-emerald-400">IOException</span> e) {"{"}</p>
				<p class="pl-6"><span class="text-pink-500">throw new</span> <span class="text-emerald-400">IOException</span>(<span class="text-amber-300">"Error reading object: "</span> + e.<span class="text-yellow-300">getMessage</span>());</p>
				<p>{"}"}</p>
				<p class="pt-2"><span class="text-emerald-400">byte</span>[] decompressedData = decompressedStream.<span class="text-yellow-300">toByteArray</span>();</p>
			</div>
		</div>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 350: catFile (Step 4 - Output & return)
slides_data["350"] = """<script lang="ts">
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
				<p class="text-gray-500">// System.out.print(header + "\\n");</p>
				<p class="text-gray-500">// System.out.print(content);</p>
				<p class="text-pink-500 pt-2"><span class="font-semibold">return</span> content;</p>
			</div>
		</div>
	</div>
</div>
"""

# Slide 360: hashObject (Step 1 - Signature)
slides_data["360"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[650px] p-6 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-lg text-gray-200">
		<p><span class="text-pink-500 font-semibold">public static</span> <span class="text-emerald-400">String</span> <span class="text-yellow-300">hashObject</span>(<span class="text-emerald-400">byte</span>[] <span class="text-cyan-300">content</span>, <span class="text-emerald-400">String</span> <span class="text-cyan-300">type</span>, <span class="text-emerald-400">boolean</span> <span class="text-cyan-300">write</span>)</p>
		<p class="pl-8"><span class="text-pink-500">throws</span> <span class="text-emerald-400">IOException</span>, <span class="text-emerald-400">NoSuchAlgorithmException</span> {"{"}</p>
		<p class="text-gray-500 py-4 pl-8">// ...</p>
		<p>{"}"}</p>
	</div>
</div>
"""

# Slide 370: hashObject (Step 2 - Byte Assembly)
slides_data["370"] = """<script lang="ts">
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
"""

# Slide 380: hashObject (Step 3 - SHA-1 Digest)
slides_data["380"] = """<script lang="ts">
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
"""

# Slide 390: hashObject (Step 4 - If Write)
slides_data["390"] = """<script lang="ts">
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
"""

# Slide 400: hashObject (Step 5 - Directory Creation)
slides_data["400"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1050px] h-[680px] p-4 flex flex-col justify-center">
	<div class="bg-[#1e1e1e] p-6 rounded-xl shadow-2xl text-left border border-neutral-700 font-mono text-sm text-gray-200">
		<div class="space-y-1">
			<p><span class="text-pink-500 font-semibold">if</span> (!<span class="text-emerald-400">Files</span>.<span class="text-yellow-300">exists</span>(dirPath)) {"{"}</p>
			<div class="pl-6 space-y-1">
				<p><span class="text-pink-500">try</span> {"{"}</p>
				<p class="pl-6"><span class="text-emerald-400">Files</span>.<span class="text-yellow-300">createDirectories</span>(dirPath);</p>
				<p>{"}"} <span class="text-pink-500">catch</span> (<span class="text-emerald-400">IOException</span> e) {"{"}</p>
				<p class="pl-6"><span class="text-pink-500">throw new</span> <span class="text-emerald-400">IOException</span>(<span class="text-amber-300">"Error creating directories: "</span> + e.<span class="text-yellow-300">getMessage</span>());</p>
				<p>{"}"}</p>
			</div>
			<p>{"}"}</p>
		</div>
	</div>
</div>
"""

# Slide 410: hashObject (Step 6 - DeflaterOutputStream Write)
slides_data["410"] = """<script lang="ts">
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
"""

# Slide 420: Section: What's next?
slides_data["420"] = """<script lang="ts">
	export const props = { background: '#1e9a8e' };
</script>

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide leading-tight">
		What’s next?
	</h1>
</div>
"""

# Slide 430: Text: Need to create a diagram of git file system
slides_data["430"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1000px] h-[650px] text-left p-12 text-[#1a202c] flex flex-col justify-center">
	<p class="text-3xl font-serif leading-relaxed mb-6">
		Need to create a diagram of git file system.
	</p>
	<p class="text-3xl font-serif leading-relaxed">
		Explain how each command interacts with the diagram.
	</p>
</div>
"""

# Slide 440: Types of commands (Headers)
slides_data["440"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-16">Types of commands</h2>
	<div class="grid grid-cols-2 gap-12">
		<h3 class="text-3xl font-serif text-neutral-800">Plumbing commands</h3>
		<h3 class="text-3xl font-serif text-neutral-800">Porcelain commands</h3>
	</div>
</div>
"""

# Slide 450: Types of commands (Complete list)
slides_data["450"] = """<script lang="ts">
	export const props = { background: '#faf7f2' };
</script>

<div class="w-[1100px] h-[650px] text-left p-12 text-[#1a202c]">
	<h2 class="text-5xl font-serif mb-12">Types of commands</h2>
	<div class="grid grid-cols-2 gap-12">
		<!-- Plumbing Commands -->
		<div>
			<h3 class="text-3xl font-serif text-neutral-800 mb-6">Plumbing commands</h3>
			<ul class="text-2xl font-mono leading-loose space-y-2 list-disc list-inside text-neutral-700">
				<li>git hash-object</li>
				<li>git cat-file</li>
				<li>git update-index</li>
				<li>git write-tree</li>
				<li>git commit-tree</li>
				<li>git rev-parse</li>
			</ul>
		</div>

		<!-- Porcelain Commands -->
		<div>
			<h3 class="text-3xl font-serif text-neutral-800 mb-6">Porcelain commands</h3>
			<ul class="text-2xl font-mono leading-loose space-y-2 list-disc list-inside text-neutral-700">
				<li>git add</li>
				<li>git commit</li>
				<li>git push / git pull</li>
				<li>git status</li>
				<li>git branch</li>
				<li>git log</li>
			</ul>
		</div>
	</div>
</div>
"""

# Slide 460: Demo Section
slides_data["460"] = """<script lang="ts">
	export const props = { background: '#1e9a8e' };
</script>

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide">
		Demo
	</h1>
</div>
"""

# Slide 470: What is the point?
slides_data["470"] = """<script lang="ts">
	export const props = { background: '#1e9a8e' };
</script>

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide">
		What is the point?
	</h1>
</div>
"""

# Slide 480: Questions?
slides_data["480"] = """<script lang="ts">
	export const props = { background: '#1e9a8e' };
</script>

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide">
		Questions?
	</h1>
</div>
"""

for folder, content in slides_data.items():
    slide_dir = os.path.join(BASE_DIR, folder)
    os.makedirs(slide_dir, exist_ok=True)
    with open(os.path.join(slide_dir, "slide.svelte"), "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully generated {len(slides_data)} slides in {BASE_DIR}")
