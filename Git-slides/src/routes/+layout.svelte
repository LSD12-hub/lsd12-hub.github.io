<script lang="ts">
	import '../styles/app.css';

	let { children } = $props();
</script>

<svelte:head>
	<title>Learn programming the fun way by building git</title>
</svelte:head>

{@render children()}
