<script lang="ts">
	import { Action, Notes } from '@animotion/core';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};

	const commandList = [
		{ id: 1, group: 'plumbing', name: 'git init' },
		{ id: 2, group: 'plumbing', name: 'git symbolic-ref' },
		{ id: 3, group: 'plumbing', name: 'git commit-tree' },
		{ id: 4, group: 'plumbing', name: 'git update-ref' },
		{ id: 5, group: 'plumbing', name: 'git rev-parse' },
		{ id: 6, group: 'porcelain', name: 'git commit' },
		{ id: 7, group: 'porcelain', name: 'git branch' },
		{ id: 8, group: 'porcelain', name: 'git checkout' },
		{ id: 9, group: 'porcelain', name: 'git commit (feat)' }
	];

	const steps = [
		{
			cmd: 'Filesystem Graph & Commands',
			badge: 'OVERVIEW',
			desc: 'HEAD is a file; branch refs are files; commits are loose objects in .git/objects/.'
		},
		{
			cmd: '$ git init',
			badge: 'PLUMBING',
			desc: 'Creates .git/ filesystem structure: objects/, refs/heads/, and empty repository files.'
		},
		{
			cmd: '$ git symbolic-ref HEAD refs/heads/main',
			badge: 'PLUMBING',
			desc: 'Reads or writes the symbolic reference inside .git/HEAD -> "ref: refs/heads/main".'
		},
		{
			cmd: '$ git commit-tree d8329f -m "first commit"',
			badge: 'PLUMBING',
			desc: 'Writes commit object file .git/objects/fd/f4fc... Refs are not yet connected!'
		},
		{
			cmd: '$ git update-ref refs/heads/main fdf4fc',
			badge: 'PLUMBING',
			desc: 'Writes commit SHA "fdf4fc" into file .git/refs/heads/main. HEAD resolves to this commit.'
		},
		{
			cmd: '$ git rev-parse HEAD',
			badge: 'PLUMBING',
			desc: 'Dereferences .git/HEAD -> reads .git/refs/heads/main -> resolves commit SHA fdf4fc.'
		},
		{
			cmd: '$ git commit -am "second commit"',
			badge: 'PORCELAIN',
			desc: 'Composite: writes commit (cac0ca) at top, pushes (fdf4fc) down, and advances main.'
		},
		{
			cmd: '$ git branch feature',
			badge: 'PORCELAIN',
			desc: 'Creates new branch file .git/refs/heads/feature containing "cac0ca".'
		},
		{
			cmd: '$ git checkout feature',
			badge: 'PORCELAIN',
			desc: 'Updates .git/HEAD file content to "ref: refs/heads/feature". Active branch switches.'
		},
		{
			cmd: '$ git commit -m "feat: login"',
			badge: 'PORCELAIN',
			desc: 'Creates feature commit (1a410e) with parent (cac0ca); advances feature ref file.'
		}
	];

	let cur = $derived(steps[step] ?? steps[0]);

	// Dynamic Y-position: First commit starts at top (215) and pushes down to (345) when second commit arrives at step 6
	let commit1Y = $derived(step < 6 ? 215 : 345);
</script>

<Notes>
	Step 0: Overview - Plumbing vs Porcelain commands interacting with the .git filesystem graph.
	Step 1 (git init): Initializes .git directory on disk, creating HEAD, refs/heads/, and objects/.
	Step 2 (git symbolic-ref): Manages the symbolic link inside .git/HEAD pointing to refs/heads/main.
	Step 3 (git commit-tree): Creates commit object file fdf4fc in .git/objects/ (isolated, not yet referenced by main).
	Step 4 (git update-ref): Writes the 40-char SHA fdf4fc into .git/refs/heads/main, connecting the branch to the commit.
	Step 5 (git rev-parse): Resolves HEAD through the branch ref file to output the commit SHA fdf4fc.
	Step 6 (git commit): Porcelain wrapper: creates commit object cac0ca at top, pushes fdf4fc down, and updates main.
	Step 7 (git branch feature): Creates file .git/refs/heads/feature storing "cac0ca".
	Step 8 (git checkout feature): Updates .git/HEAD to "ref: refs/heads/feature".
	Step 9 (git commit on feature): Creates commit 1a410e under feature with parent link back to cac0ca.
</Notes>

<!-- Action triggers for all 9 steps -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />
<Action do={() => (step = 2)} undo={() => (step = 1)} />
<Action do={() => (step = 3)} undo={() => (step = 2)} />
<Action do={() => (step = 4)} undo={() => (step = 3)} />
<Action do={() => (step = 5)} undo={() => (step = 4)} />
<Action do={() => (step = 6)} undo={() => (step = 5)} />
<Action do={() => (step = 7)} undo={() => (step = 6)} />
<Action do={() => (step = 8)} undo={() => (step = 7)} />
<Action do={() => (step = 9)} undo={() => (step = 8)} />

<div class="w-[1120px] h-[660px] flex flex-col justify-between items-center select-none text-white p-4">
	<!-- Minimal Command Header -->
	<div class="w-full flex items-baseline justify-between border-b border-neutral-800 pb-3">
		<div class="flex items-baseline gap-4">
			<h2 class="text-2xl font-mono font-bold tracking-tight text-white">
				{cur.cmd}
			</h2>
			<span class="px-2 py-0.5 rounded text-[11px] font-mono font-bold tracking-wider border {cur.badge === 'PLUMBING' ? 'bg-sky-950/80 text-sky-400 border-sky-600/50' : cur.badge === 'PORCELAIN' ? 'bg-amber-950/80 text-amber-400 border-amber-600/50' : 'bg-neutral-800 text-neutral-300 border-neutral-700'}">
				{cur.badge}
			</span>
			<p class="text-sm font-sans text-neutral-400">
				{cur.desc}
			</p>
		</div>
		<span class="text-xs font-mono text-neutral-500">
			{step} / 9
		</span>
	</div>

	<!-- Main Body: Sidebar (Left) + Graph (Right) -->
	<div class="w-full h-[535px] flex items-center gap-4">
		<!-- Left: Minimal Command Sidebar -->
		<div class="w-[230px] h-full bg-neutral-900/60 border border-neutral-800 rounded-xl p-3.5 flex flex-col justify-between text-xs font-mono">
			<!-- Plumbing Section -->
			<div>
				<div class="flex items-center justify-between text-[11px] font-bold tracking-wider text-sky-400 uppercase mb-2">
					<span>Plumbing</span>
					<span class="text-[9px] text-neutral-500 font-sans">low-level</span>
				</div>
				<div class="space-y-1">
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 1 ? 'bg-neutral-800 text-sky-300 font-bold border border-sky-500/40' : 'text-neutral-400'}">
						<span>$ git init</span>
						{#if step === 1}<span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 2 ? 'bg-neutral-800 text-sky-300 font-bold border border-sky-500/40' : 'text-neutral-400'}">
						<span>$ symbolic-ref</span>
						{#if step === 2}<span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 3 ? 'bg-neutral-800 text-sky-300 font-bold border border-sky-500/40' : 'text-neutral-400'}">
						<span>$ commit-tree</span>
						{#if step === 3}<span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 4 ? 'bg-neutral-800 text-sky-300 font-bold border border-sky-500/40' : 'text-neutral-400'}">
						<span>$ update-ref</span>
						{#if step === 4}<span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 5 ? 'bg-neutral-800 text-sky-300 font-bold border border-sky-500/40' : 'text-neutral-400'}">
						<span>$ rev-parse</span>
						{#if step === 5}<span class="w-1.5 h-1.5 rounded-full bg-sky-400"></span>{/if}
					</div>
				</div>
			</div>

			<!-- Porcelain Section -->
			<div class="border-t border-neutral-800/80 pt-2">
				<div class="flex items-center justify-between text-[11px] font-bold tracking-wider text-amber-400 uppercase mb-2">
					<span>Porcelain</span>
					<span class="text-[9px] text-neutral-500 font-sans">high-level</span>
				</div>
				<div class="space-y-1">
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 6 ? 'bg-neutral-800 text-amber-300 font-bold border border-amber-500/40' : 'text-neutral-400'}">
						<span>$ git commit</span>
						{#if step === 6}<span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 7 ? 'bg-neutral-800 text-amber-300 font-bold border border-amber-500/40' : 'text-neutral-400'}">
						<span>$ git branch</span>
						{#if step === 7}<span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 8 ? 'bg-neutral-800 text-amber-300 font-bold border border-amber-500/40' : 'text-neutral-400'}">
						<span>$ git checkout</span>
						{#if step === 8}<span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>{/if}
					</div>
					<div class="px-2.5 py-1 rounded transition-all flex items-center justify-between {step === 9 ? 'bg-neutral-800 text-amber-300 font-bold border border-amber-500/40' : 'text-neutral-400'}">
						<span>$ git commit (feat)</span>
						{#if step === 9}<span class="w-1.5 h-1.5 rounded-full bg-amber-400"></span>{/if}
					</div>
				</div>
			</div>
		</div>

		<!-- Right: Minimal Filesystem Graph Canvas -->
		<div class="flex-1 h-full bg-neutral-950/70 border border-neutral-800/80 rounded-xl p-3 flex items-center justify-center relative overflow-hidden">
			<svg viewBox="0 0 740 480" class="w-full h-full">
				<defs>
					<!-- Clean Minimal Arrow Markers -->
					<marker
						id="arr"
						viewBox="0 0 10 10"
						refX="7"
						refY="5"
						markerWidth="6"
						markerHeight="6"
						orient="auto-start-reverse"
					>
						<polygon points="0,2 7,5 0,8" fill="#d4d4d8" />
					</marker>
					<marker
						id="arr-muted"
						viewBox="0 0 10 10"
						refX="7"
						refY="5"
						markerWidth="6"
						markerHeight="6"
						orient="auto-start-reverse"
					>
						<polygon points="0,2 7,5 0,8" fill="#71717a" />
					</marker>
				</defs>

				<!-- ========================================================================= -->
				<!-- 1. HEAD FILE (.git/HEAD)                                                  -->
				<!-- ========================================================================= -->
				<g
					class="transition-opacity duration-300"
					style="opacity: {step >= 1 ? 1 : 0.25};"
				>
					<!-- .git/HEAD File Box -->
					<g transform="translate(280, 15)">
						<rect
							width="180"
							height="44"
							rx="6"
							fill="#27272a"
							stroke={step === 2 || step === 5 || step === 8 ? '#e4e4e7' : '#71717a'}
							stroke-width={step === 2 || step === 5 || step === 8 ? '2' : '1.5'}
						/>
						<text x="12" y="19" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
							📄 .git/HEAD
						</text>
						<text x="12" y="36" font-size="11.5" font-weight="600" fill="#ffffff" font-family="'Monaspace Neon', monospace">
							{step >= 8 ? 'ref: refs/heads/feature' : 'ref: refs/heads/main'}
						</text>
					</g>

					<!-- Pointer from HEAD file to active branch file in refs/heads/ -->
					{#if step >= 2 && step < 8}
						<!-- HEAD -> main -->
						<line
							x1="330"
							y1="59"
							x2="240"
							y2="118"
							stroke="#d4d4d8"
							stroke-width="2"
							marker-end="url(#arr)"
						/>
					{:else if step >= 8}
						<!-- HEAD -> feature (checkout) -->
						<line
							x1="410"
							y1="59"
							x2="500"
							y2="118"
							stroke="#d4d4d8"
							stroke-width="2"
							marker-end="url(#arr)"
						/>
					{/if}
				</g>

				<!-- ========================================================================= -->
				<!-- 2. REFS DIRECTORY DIVIDER (.git/refs/heads/)                              -->
				<!-- ========================================================================= -->
				<g
					class="transition-opacity duration-300"
					style="opacity: {step >= 1 ? 1 : 0.25};"
				>
					<!-- Folder Label -->
					<text
						x="40"
						y="102"
						font-size="12"
						font-weight="700"
						fill="#a1a1aa"
						font-family="'Monaspace Neon', monospace"
					>
						📁 .git/refs/heads/
					</text>

					<!-- Solid Horizontal Divider -->
					<line
						x1="40"
						y1="112"
						x2="700"
						y2="112"
						stroke="#52525b"
						stroke-width="2.5"
						stroke-linecap="round"
					/>
				</g>

				<!-- ========================================================================= -->
				<!-- 3. BRANCH FILES IN .git/refs/heads/                                       -->
				<!-- ========================================================================= -->

				<!-- Branch File: .git/refs/heads/main -->
				<g
					transform="translate(170, 126)"
					class="transition-opacity duration-300"
					style="opacity: {step >= 1 ? 1 : 0.2};"
				>
					<rect
						width="140"
						height="46"
						rx="6"
						fill="#27272a"
						stroke={step === 4 || step === 5 || step === 6 ? '#e4e4e7' : '#71717a'}
						stroke-width={step === 4 || step === 5 || step === 6 ? '2' : '1.5'}
					/>
					<text x="12" y="19" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
						📄 main
					</text>
					<text x="12" y="36" font-size="11.5" font-weight="600" fill="#ffffff" font-family="'Monaspace Neon', monospace">
						{step >= 6 ? 'cac0ca...' : step >= 4 ? 'fdf4fc...' : '(empty)'}
					</text>
				</g>

				<!-- Branch File: .git/refs/heads/feature -->
				<g
					transform="translate(430, 126)"
					class="transition-opacity duration-300"
					style="opacity: {step >= 7 ? 1 : 0.15};"
				>
					<rect
						width="140"
						height="46"
						rx="6"
						fill="#27272a"
						stroke={step === 7 || step === 9 ? '#e4e4e7' : '#71717a'}
						stroke-width={step === 7 || step === 9 ? '2' : '1.5'}
					/>
					<text x="12" y="19" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
						📄 feature
					</text>
					<text x="12" y="36" font-size="11.5" font-weight="600" fill="#ffffff" font-family="'Monaspace Neon', monospace">
						{step >= 9 ? '1a410e...' : step >= 7 ? 'cac0ca...' : '(empty)'}
					</text>
				</g>

				<!-- ========================================================================= -->
				<!-- 4. OBJECT STORE SECTION (.git/objects/)                                   -->
				<!-- ========================================================================= -->
				<g
					class="transition-opacity duration-300"
					style="opacity: {step >= 1 ? 1 : 0.2};"
				>
					<!-- Objects Directory Label -->
					<text
						x="40"
						y="198"
						font-size="12"
						font-weight="700"
						fill="#a1a1aa"
						font-family="'Monaspace Neon', monospace"
					>
						📁 .git/objects/
					</text>
				</g>

				<!-- ========================================================================= -->
				<!-- 5. COMMITS UNDER MAIN (IN .git/objects/)                                  -->
				<!-- ========================================================================= -->

				<!-- Pointer: main file -> Top Commit in objects/ (step 4+) -->
				{#if step >= 4}
					<line
						x1="240"
						y1="172"
						x2="240"
						y2="213"
						stroke="#d4d4d8"
						stroke-width="2"
						marker-end="url(#arr)"
					/>
				{/if}

				<!-- Commit Object File: cac0ca (Second Commit) - Appears at top (Y: 215) in Step 6+ -->
				<g
					transform="translate(170, 215)"
					class="transition-opacity duration-500 ease-out"
					style="opacity: {step >= 6 ? 1 : 0};"
				>
					<rect
						width="140"
						height="72"
						rx="6"
						fill="#27272a"
						stroke={step === 6 ? '#e4e4e7' : '#71717a'}
						stroke-width={step === 6 ? '2' : '1.5'}
					/>
					<text x="12" y="20" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
						📄 ca/c0ca...
					</text>
					<text x="12" y="42" font-size="12.5" font-weight="600" fill="#ffffff" font-family="sans-serif">
						second commit
					</text>
					<text x="12" y="60" font-size="10" fill="#71717a" font-family="'Monaspace Neon', monospace">
						parent: fdf4fc...
					</text>
				</g>

				<!-- Downward Pointer from Commit 2 (215) -> Commit 1 (345) -->
				{#if step >= 6}
					<line
						x1="240"
						y1="287"
						x2="240"
						y2="343"
						stroke="#71717a"
						stroke-width="2"
						marker-end="url(#arr-muted)"
					/>
				{/if}

				<!-- Commit Object File: fdf4fc (First Commit) - Created by commit-tree at Step 3 (Y: 215), pushes down to (Y: 345) at Step 6+ -->
				<g
					transform="translate(170, {commit1Y})"
					class="transition-all duration-500 ease-out"
					style="opacity: {step >= 3 ? 1 : 0};"
				>
					<rect
						width="140"
						height="72"
						rx="6"
						fill="#27272a"
						stroke={step === 3 || step === 4 ? '#e4e4e7' : '#71717a'}
						stroke-width={step === 3 || step === 4 ? '2' : '1.5'}
					/>
					<text x="12" y="20" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
						📄 fd/f4fc...
					</text>
					<text x="12" y="42" font-size="12.5" font-weight="600" fill="#ffffff" font-family="sans-serif">
						first commit
					</text>
					<text x="12" y="60" font-size="10" fill="#71717a" font-family="'Monaspace Neon', monospace">
						parent: (root)
					</text>
				</g>

				<!-- ========================================================================= -->
				<!-- 6. COMMITS UNDER FEATURE (IN .git/objects/)                                -->
				<!-- ========================================================================= -->

				<!-- Pointer: feature file -> cac0ca (Step 7/8) OR feature commit (Step 9) -->
				{#if step === 7 || step === 8}
					<!-- Initial branch creation pointing to cac0ca on main -->
					<path
						d="M 450,172 L 410,195 L 312,235"
						fill="none"
						stroke="#71717a"
						stroke-width="2"
						stroke-dasharray="4 3"
						marker-end="url(#arr-muted)"
					/>
				{:else if step >= 9}
					<!-- feature file points to top commit in objects/ -->
					<line
						x1="500"
						y1="172"
						x2="500"
						y2="213"
						stroke="#d4d4d8"
						stroke-width="2"
						marker-end="url(#arr)"
					/>
				{/if}

				<!-- Feature Commit Object File: 1a410e (feat: login) - Step 9 -->
				<g
					transform="translate(430, 215)"
					class="transition-opacity duration-500 ease-out"
					style="opacity: {step >= 9 ? 1 : 0};"
				>
					<rect
						width="140"
						height="72"
						rx="6"
						fill="#27272a"
						stroke={step === 9 ? '#e4e4e7' : '#71717a'}
						stroke-width={step === 9 ? '2' : '1.5'}
					/>
					<text x="12" y="20" font-size="10.5" font-weight="700" fill="#a1a1aa" font-family="'Monaspace Neon', monospace">
						📄 1a/410e...
					</text>
					<text x="12" y="42" font-size="12.5" font-weight="600" fill="#ffffff" font-family="sans-serif">
						feat: login
					</text>
					<text x="12" y="60" font-size="10" fill="#71717a" font-family="'Monaspace Neon', monospace">
						parent: cac0ca...
					</text>
				</g>

				<!-- Connector from 1a410e back to parent cac0ca on main with Rotation Icon -->
				{#if step >= 9}
					<g class="transition-opacity duration-400">
						<!-- Curved parent line -->
						<path
							d="M 430,251 C 390,251 350,251 312,251"
							fill="none"
							stroke="#71717a"
							stroke-width="2"
							marker-end="url(#arr-muted)"
						/>
						<!-- Minimal Rotation Fork Icon (Circle + Arrow) -->
						<g transform="translate(370, 251)">
							<circle cx="0" cy="0" r="13" fill="#18181b" stroke="#71717a" stroke-width="1.5" />
							<path
								d="M -4,-2 A 5.5 5.5 0 1 1 -2,4.5"
								fill="none"
								stroke="#d4d4d8"
								stroke-width="1.6"
								stroke-linecap="round"
							/>
							<polygon points="-4,-4.5 -4,0 0,-2" fill="#d4d4d8" />
						</g>
					</g>
				{/if}

				<!-- Step 5 rev-parse Dereferencing Inspection Beam -->
				{#if step === 5}
					<g class="transition-opacity duration-300" transform="translate(480, 20)">
						<rect width="210" height="40" rx="6" fill="#1c1917" stroke="#e4e4e7" stroke-width="1.5" />
						<text x="12" y="24" font-size="11" font-weight="700" fill="#ffffff" font-family="'Monaspace Neon', monospace">
							stdout: fdf4fc...
						</text>
					</g>
				{/if}
			</svg>
		</div>
	</div>

	<!-- Minimal Footer Navigation Hint -->
	<div class="w-full text-xs font-mono text-neutral-500 flex justify-between items-center pt-1 border-t border-neutral-800/80">
		<span class="text-neutral-400">Plumbing &amp; Porcelain Commands</span>
		<div>
			Use <span class="text-neutral-300 font-semibold">Space</span> or <span class="text-neutral-300 font-semibold">→</span> to step
		</div>
	</div>
</div>
