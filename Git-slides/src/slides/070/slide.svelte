<script>
	import { Notes } from '@animotion/core';
</script>

<Notes>
	- infinate wisedom <br />
	- What things can I use it for <br />
</Notes>

<div class="flex items-center justify-center h-full">
	<div class="relative inline-block max-h-[95vh] max-w-full">
		<img
			src="https://fbi.cults3d.com/uploaders/13729991/illustration-file/0e301d80-9c63-439d-8e9c-80aadd918453/ThinkingMeme.png"
			alt="I am thinking"
			class="max-h-[60vh] max-w-full rounded-xl shadow-2xl border border-neutral-800 block"
		/>

		<!-- Arrow and Marker-style "Me" Annotation -->
		<svg
			viewBox="0 0 498 310"
			class="absolute inset-0 w-full h-full pointer-events-none select-none arrow-me-group"
		>
			<defs>
				<filter id="shadow-me" x="-20%" y="-20%" width="150%" height="150%">
					<feDropShadow dx="2" dy="3" stdDeviation="3" flood-color="#000000" flood-opacity="0.65" />
				</filter>
				<marker
					id="arrow-me-head"
					viewBox="0 0 10 10"
					refX="5"
					refY="5"
					markerWidth="4.5"
					markerHeight="4.5"
					orient="auto-start-reverse"
				>
					<path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#ef4444" />
				</marker>
			</defs>

			<!-- Marker Style "Me" Text -->
			<text
				x="415"
				y="136"
				text-anchor="middle"
				fill="#ef4444"
				font-family="'Permanent Marker', 'Caveat', 'Comic Sans MS', cursive, sans-serif"
				font-size="58"
				letter-spacing="0.02em"
				filter="url(#shadow-me)"
			>
				Me
			</text>

			<!-- Hand-drawn curved red marker arrow pointing to character -->
			<path
				d="M 390 148 C 362 154, 346 166, 332 176"
				fill="none"
				stroke="#ef4444"
				stroke-width="7.5"
				stroke-linecap="round"
				stroke-linejoin="round"
				marker-end="url(#arrow-me-head)"
				filter="url(#shadow-me)"
			/>
		</svg>
	</div>
</div>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

	@keyframes point-bounce {
		0%,
		100% {
			transform: translate(0, 0);
		}
		50% {
			transform: translate(-4px, 3px);
		}
	}

	.arrow-me-group {
		animation: point-bounce 2.2s ease-in-out infinite;
	}
</style>