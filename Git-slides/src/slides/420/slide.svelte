<script lang="ts">
	import { Action } from '@animotion/core';
	import { createTypewriter } from '$lib';

	const tw = createTypewriter('What’s next?', { speed: 45 });

	export const props = {
		background: '#1e9a8e',
		out: () => tw.reset()
	};
</script>

<Action do={tw.start} undo={tw.reset} />

<div class="flex items-center justify-center h-[750px] w-full text-center">
	<h1 class="text-7xl font-serif text-white font-normal tracking-wide leading-tight min-h-[100px] flex items-center justify-center">
		{#if !tw.hasStarted}
			<span class="inline-block w-1.5 h-16 bg-white animate-pulse"></span>
		{:else}
			<span>{tw.text}</span>
			{#if tw.isTyping}
				<span class="inline-block w-1.5 h-16 bg-white ml-2 align-middle animate-pulse"></span>
			{/if}
		{/if}
	</h1>
</div>
