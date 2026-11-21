<script lang="ts">
	import { createTypewriter } from './create-typewriter.svelte';

	type Props = {
		text: string | string[];
		speed?: number;
		delay?: number;
		lineDelay?: number;
		autostart?: boolean;
		cursorClass?: string;
		class?: string;
		onComplete?: () => void;
	};

	let {
		text,
		speed = 40,
		delay = 100,
		lineDelay = 180,
		autostart = false,
		cursorClass = 'bg-emerald-400',
		class: className = '',
		onComplete
	}: Props = $props();

	const tw = createTypewriter(() => text, {
		speed: () => speed,
		delay: () => delay,
		lineDelay: () => lineDelay,
		autostart: () => autostart,
		onComplete: () => onComplete?.()
	});

	// Expose methods for parent components / <Action>
	export function start() {
		tw.start();
	}

	export function reset() {
		tw.reset();
	}

	export function isDone() {
		return tw.isDone;
	}

	export function hasStarted() {
		return tw.hasStarted;
	}
</script>

<div class={className}>
	{#if Array.isArray(text)}
		{#each text as _, i}
			{#if i <= tw.currentLineIndex || tw.isDone}
				<div>
					<span>{tw.typedLines[i] ?? ''}</span>
					{#if (!tw.hasStarted && i === 0) || (tw.isTyping && tw.currentLineIndex === i)}
						<span class="inline-block w-2.5 h-[1.1em] ml-1 align-middle animate-pulse {cursorClass}"></span>
					{/if}
				</div>
			{/if}
		{/each}
	{:else}
		<span>{tw.text}</span>
		{#if !tw.hasStarted || tw.isTyping}
			<span class="inline-block w-2.5 h-[1.1em] ml-1 align-middle animate-pulse {cursorClass}"></span>
		{/if}
	{/if}
</div>
