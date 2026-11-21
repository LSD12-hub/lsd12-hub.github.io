<script lang="ts">
	import { Action } from '@animotion/core';

	let step = $state(0);

	export const props = {
		background: '#18181b',
		out: () => {
			step = 0;
		}
	};
</script>

<!-- Action 1: First commit -->
<Action do={() => (step = 1)} undo={() => (step = 0)} />

<!-- Action 2: Second commit -->
<Action do={() => (step = 2)} undo={() => (step = 1)} />

<!-- Action 3: Third commit -->
<Action do={() => (step = 3)} undo={() => (step = 2)} />

<!-- Action 4: Highlight hashes in red -->
<Action do={() => (step = 4)} undo={() => (step = 3)} />

<div class="w-[1100px] h-[660px] flex items-center justify-center select-none">
	<svg
		viewBox="0 0 940 590"
		class="w-full h-full max-h-[88vh]"
		style="font-family: 'Monaspace Neon', monospace;"
	>
		<defs>
			<!-- Arrowhead marker -->
			<marker
				id="arrow"
				viewBox="0 0 10 10"
				refX="7"
				refY="5"
				markerWidth="7"
				markerHeight="7"
				orient="auto-start-reverse"
			>
				<polygon points="0,1.5 8,5 0,8.5" fill="#94a3b8" />
			</marker>
		</defs>

		<!-- ========================================================================= -->
		<!-- STEP 1: FIRST COMMIT                                                      -->
		<!-- ========================================================================= -->
		<g class="transition-opacity duration-500 ease-out" style="opacity: {step >= 1 ? 1 : 0};">
			<!-- Commit 3 (First Commit) -> Tree 3 Arrow -->
			<line x1="220" y1="467" x2="318" y2="467" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Tree 3 -> Blob 3 (version 1) Arrow -->
			<line x1="455" y1="467" x2="643" y2="467" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Badge: bottom test.java -->
			<g transform="translate(565, 467)">
				<rect x="-62" y="-12" width="124" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
				<text text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="800" fill="#0f172a">
					test.java
				</text>
			</g>

			<!-- Commit Box: First Commit -->
			<g transform="translate(40, 425)">
				<rect width="180" height="84" rx="16" fill="#78350f" stroke="#d97706" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#fef3c7'}
				>
					fdf4fc
				</text>
				<text x="24" y="58" font-size="18" font-weight="800" fill="#ffffff">first commit</text>
			</g>

			<!-- Tree Box: Tree 3 -->
			<g transform="translate(320, 425)">
				<rect width="135" height="84" rx="16" fill="#0f766e" stroke="#14b8a6" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#ccfbf1'}
				>
					d8329f
				</text>
				<text x="48" y="58" font-size="18" font-weight="800" fill="#ffffff">tree</text>
			</g>

			<!-- Blob Box: "version 1" -->
			<g transform="translate(645, 425)">
				<rect width="150" height="84" rx="16" fill="#1e293b" stroke="#475569" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight="800"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#e2e8f0'}
				>
					83baae
				</text>
				<text x="16" y="58" font-size="18" font-weight="800" fill="#ffffff">"version 1"</text>
			</g>
		</g>

		<!-- ========================================================================= -->
		<!-- STEP 2: SECOND COMMIT                                                     -->
		<!-- ========================================================================= -->
		<g class="transition-opacity duration-500 ease-out" style="opacity: {step >= 2 ? 1 : 0};">
			<!-- Commit 2 -> Commit 3 Downward Arrow -->
			<line x1="130" y1="334" x2="130" y2="423" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Commit 2 -> Tree 2 Arrow -->
			<line x1="220" y1="292" x2="318" y2="292" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Tree 2 -> Blob 1 ("version 2") via "test.java" -->
			<path d="M 455,270 L 610,270 L 643,252" fill="none" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Tree 2 -> Blob 2 ("new file") via "new.java" -->
			<path d="M 455,315 L 515,338 L 643,355" fill="none" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Badge: middle test.java -->
			<g transform="translate(565, 270)">
				<rect x="-62" y="-12" width="124" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
				<text text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="800" fill="#0f172a">
					test.java
				</text>
			</g>

			<!-- Badge: middle new.java -->
			<g transform="translate(565, 338)">
				<rect x="-58" y="-12" width="116" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
				<text text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="800" fill="#0f172a">
					new.java
				</text>
			</g>

			<!-- Commit Box: Second Commit -->
			<g transform="translate(40, 250)">
				<rect width="180" height="84" rx="16" fill="#78350f" stroke="#d97706" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#fef3c7'}
				>
					cac0ca
				</text>
				<text x="19" y="58" font-size="18" font-weight="800" fill="#ffffff">second commit</text>
			</g>

			<!-- Tree Box: Tree 2 -->
			<g transform="translate(320, 250)">
				<rect width="135" height="84" rx="16" fill="#0f766e" stroke="#14b8a6" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#ccfbf1'}
				>
					0155eb
				</text>
				<text x="48" y="58" font-size="18" font-weight="800" fill="#ffffff">tree</text>
			</g>

			<!-- Blob Box: "version 2" -->
			<g transform="translate(645, 190)">
				<rect width="150" height="84" rx="16" fill="#1e293b" stroke="#475569" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight="800"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#e2e8f0'}
				>
					1f7a7a
				</text>
				<text x="16" y="58" font-size="18" font-weight="800" fill="#ffffff">"version 2"</text>
			</g>

			<!-- Blob Box: "new file" -->
			<g transform="translate(645, 330)">
				<rect width="150" height="84" rx="16" fill="#1e293b" stroke="#475569" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight="800"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#e2e8f0'}
				>
					fa49b0
				</text>
				<text x="21" y="58" font-size="18" font-weight="800" fill="#ffffff">"new file"</text>
			</g>
		</g>

		<!-- ========================================================================= -->
		<!-- STEP 3: THIRD COMMIT                                                      -->
		<!-- ========================================================================= -->
		<g class="transition-opacity duration-500 ease-out" style="opacity: {step >= 3 ? 1 : 0};">
			<!-- Commit 1 -> Commit 2 Downward Arrow -->
			<line x1="130" y1="159" x2="130" y2="248" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Commit 1 -> Tree 1 Arrow -->
			<line x1="220" y1="117" x2="318" y2="117" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Tree 1 -> Blob 4 ("version 3") via "new.java" -->
			<line x1="455" y1="117" x2="643" y2="117" stroke="#94a3b8" stroke-width="2.5" marker-end="url(#arrow)" />

			<!-- Tree 1 -> Blob 1 via "test.java" -->
			<path
				d="M 455,145 L 515,165 L 643,205"
				fill="none"
				stroke="#94a3b8"
				stroke-width="2.5"
				marker-end="url(#arrow)"
			/>

			<!-- Badge: top new.java -->
			<g transform="translate(565, 117)">
				<rect x="-58" y="-12" width="116" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
				<text text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="800" fill="#0f172a">
					new.java
				</text>
			</g>

			<!-- Badge: top test.java -->
			<g transform="translate(565, 165)">
				<rect x="-62" y="-12" width="124" height="24" rx="4" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
				<text text-anchor="middle" dominant-baseline="central" font-size="15" font-weight="800" fill="#0f172a">
					test.java
				</text>
			</g>

			<!-- Commit Box: Third Commit -->
			<g transform="translate(40, 75)">
				<rect width="180" height="84" rx="16" fill="#78350f" stroke="#d97706" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#fef3c7'}
				>
					1a410e
				</text>
				<text x="24" y="58" font-size="18" font-weight="800" fill="#ffffff">third commit</text>
			</g>

			<!-- Tree Box: Tree 1 -->
			<g transform="translate(320, 75)">
				<rect width="135" height="84" rx="16" fill="#0f766e" stroke="#14b8a6" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight={step >= 4 ? '800' : '700'}
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#ccfbf1'}
				>
					3c4e9c
				</text>
				<text x="48" y="58" font-size="18" font-weight="800" fill="#ffffff">tree</text>
			</g>

			<!-- Blob Box: "version 3" -->
			<g transform="translate(645, 75)">
				<rect width="150" height="84" rx="16" fill="#1e293b" stroke="#475569" stroke-width="2" />
				<!-- Hash Highlight Pill (Red) -->
				<rect
					x="10"
					y="10"
					width="76"
					height="22"
					rx="5"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#dc2626' : 'transparent'}
					stroke={step >= 4 ? '#ef4444' : 'transparent'}
					stroke-width="1.5"
					style="filter: {step >= 4 ? 'drop-shadow(0 0 10px rgba(239, 68, 68, 0.9))' : 'none'};"
				/>
				<text
					x="48"
					y="21"
					text-anchor="middle"
					dominant-baseline="central"
					font-size="14"
					font-weight="800"
					class="transition-all duration-500 ease-out"
					fill={step >= 4 ? '#ffffff' : '#e2e8f0'}
				>
					7170a5
				</text>
				<text x="16" y="58" font-size="18" font-weight="800" fill="#ffffff">"version 3"</text>
			</g>
		</g>
	</svg>
</div>
