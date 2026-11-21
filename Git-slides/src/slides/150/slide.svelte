<script lang="ts">
	import { Action, Notes } from '@animotion/core';
	import { createTypewriter } from '$lib';

	const tw = createTypewriter(
		['Content-addressable', 'filesystem'],
		{ speed: 45, lineDelay: 200 }
	);

	export const props = {
		background: '#1e9a8e',
		out: () => tw.reset()
	};
</script>

<Notes>
	- Before you build
	- What are we building (on screen)
	- Key value pairs
</Notes>

<Action do={tw.start} undo={tw.reset} />

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide leading-tight min-h-[180px] flex flex-col items-center justify-center">
		{#if !tw.hasStarted}
			<span class="inline-block w-1.5 h-16 bg-white animate-pulse"></span>
		{:else}
			<div>
				<span>{tw.typedLines[0]}</span>
				{#if tw.isTyping && tw.currentLineIndex === 0}
					<span class="inline-block w-1.5 h-16 bg-white ml-2 align-middle animate-pulse"></span>
				{/if}
			</div>
			{#if tw.currentLineIndex >= 1 || tw.isDone}
				<div>
					<span>{tw.typedLines[1]}</span>
					{#if !tw.isDone}
						<span class="inline-block w-1.5 h-16 bg-white ml-2 align-middle animate-pulse"></span>
					{/if}
				</div>
			{/if}
		{/if}
	</h1>
</div>
