<script lang="ts">
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
