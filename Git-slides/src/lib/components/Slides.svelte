<svelte:options runes />

<script lang="ts">
	import { Slide as AnimotionSlide } from '@animotion/core';
	import type { Component } from 'svelte';

	let { center = false } = $props();

	// Safe slide loader that excludes disabled folders starting with underscore (e.g. _060, _200)
	const slides = Object.entries(
		import.meta.glob<{
			default: Component;
			component?: Component;
			props?: any;
		}>(['/src/slides/**/slide.svelte', '!/src/slides/_*/**'], {
			eager: true
		})
	)
		.map(([filename, exports]) => {
			const matches = filename.match(/slides\/(\d+)\/slide\.svelte$/);
			if (!matches || !matches[1]) return null;
			return [+matches[1], exports] as const;
		})
		.filter((item): item is NonNullable<typeof item> => item !== null)
		.sort(([a], [b]) => a - b);
</script>

{#each slides as [_, Slide]}
	{@const Wrapper = Slide.component ?? AnimotionSlide}
	{@const props = {
		class: center ? 'h-full place-content-center place-items-center' : null,
		...(Slide.props ?? {})
	}}
	<Wrapper {...props}>
		<Slide.default></Slide.default>
	</Wrapper>
{/each}
