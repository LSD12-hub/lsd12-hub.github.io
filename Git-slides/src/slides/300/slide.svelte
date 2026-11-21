<script lang="ts">
	import { Action } from '@animotion/core';
	import { createTypewriter } from '$lib';

	const twReading = createTypewriter('Reading', { speed: 45, delay: 50 });
	const twWriting = createTypewriter('Writing', { speed: 45, delay: 50 });

	export const props = {
		background: '#18181b',
		out: () => {
			twReading.reset();
			twWriting.reset();
		}
	};
</script>

<!-- Action 1: Type "Reading" on the left -->
<Action 
	do={
		() => {
			twReading.start()
			twWriting.start()
		}
	} 
	undo={
		() => {
			twReading.reset()
			twWriting.reset()
		}
	} 
/>

<div class="w-[1000px] h-[650px] flex items-center justify-center text-white select-none">
	<div class="grid grid-cols-2 w-full h-full relative items-center">
		<!-- Left Side: Reading -->
		<div class="flex items-center justify-center h-full">
			<h2 class="text-6xl font-serif font-bold text-white tracking-wide min-h-[80px] flex items-center justify-center">
				{#if !twReading.hasStarted}
					<span class="inline-block w-1.5 h-14 bg-white animate-pulse"></span>
				{:else}
					<span>{twReading.text}</span>
					{#if twReading.isTyping}
						<span class="inline-block w-1.5 h-14 bg-white ml-1.5 align-middle animate-pulse"></span>
					{/if}
				{/if}
			</h2>
		</div>

		<!-- Solid Line in the Middle -->
		<div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-[3px] h-[360px] bg-neutral-700 rounded-full"></div>

		<!-- Right Side: Writing -->
		<div class="flex items-center justify-center h-full">
			<h2 class="text-6xl font-serif font-bold text-white tracking-wide min-h-[80px] flex items-center justify-center">
				{#if !twWriting.hasStarted}
					<span class="inline-block w-1.5 h-14 bg-white animate-pulse"></span>
				{:else}
					<span>{twWriting.text}</span>
					{#if twWriting.isTyping}
						<span class="inline-block w-1.5 h-14 bg-white ml-1.5 align-middle animate-pulse"></span>
					{/if}
				{/if}
			</h2>
		</div>
	</div>
</div>
