<svelte:options runes />

<script lang="ts">
	type Props = {
		/** Value from 0–1 representing how full the bar is */
		value: number;
		/** Colour of the filled portion – any Tailwind bg-* class */
		color?: string;
		/** Label shown on the left */
		label?: string;
		/** Sub-label shown beneath the label */
		sublabel?: string;
		/** Annotation shown inside / at the end of the bar */
		annotation?: string;
	};

	let {
		value,
		color = 'bg-teal-400',
		label = '',
		sublabel = '',
		annotation = ''
	}: Props = $props();

	// Clamp to [0, 1]
	const pct = $derived(Math.min(1, Math.max(0, value)) * 100);
</script>

<div class="flex flex-col gap-1 w-full">
	{#if label}
		<div class="flex items-baseline justify-between font-mono">
			<span class="text-base font-bold text-white">{label}</span>
			{#if sublabel}
				<span class="text-xs text-neutral-500">{sublabel}</span>
			{/if}
		</div>
	{/if}

	<div class="relative h-9 w-full rounded bg-neutral-800 overflow-hidden">
		<!-- Filled portion -->
		<div
			class="h-full rounded transition-all duration-700 ease-out {color}"
			style="width: {pct}%;"
		></div>

		<!-- Annotation inside bar -->
		{#if annotation}
			<span
				class="absolute inset-0 flex items-center px-3 text-xs font-mono font-semibold text-white/80 select-none"
			>
				{annotation}
			</span>
		{/if}
	</div>
</div>
