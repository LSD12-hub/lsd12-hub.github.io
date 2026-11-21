<script lang="ts">
	import { Presentation } from '@animotion/core';
	import Slides from '$lib/components/Slides.svelte';
</script>

<Presentation
	options={{ history: true, transition: 'slide', controls: true, progress: true }}
	plugins={{ notes: true }}
>
	<Slides center={true} />
</Presentation>
