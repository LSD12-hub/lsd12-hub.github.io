<script lang="ts">
	import { Action, Code, Notes } from '@animotion/core';

	let codeRef: ReturnType<typeof Code> | undefined = $state();
	let step = $state(0);

	function highlightStep(s: number) {
		step = s;
		if (!codeRef) return;
		switch (s) {
			case 0:
				codeRef.selectLines`*`;
				break;
			case 1:
				codeRef.select`digest.digest(fullContent)`;
				break;
			case 2:
				codeRef.select`Integer.toHexString(0xff & b)`;
				break;
			case 3:
				codeRef.select`hexString.toString()`;
				break;
		}
	}

	export const props = {
		background: '#18181b',
		out: () => {
			highlightStep(0);
		}
	};

	const code = `byte[] hashBytes = digest.digest(fullContent);

StringBuilder hexString = new StringBuilder();
for (byte b : hashBytes) {
    String hex = Integer.toHexString(0xff & b);
    if (hex.length() == 1) {
        hexString.append('0');
    }
    hexString.append(hex);
}
String sha1 = hexString.toString();`;
</script>

<Notes>
	- Step 1: Compute 20-byte SHA-1 digest from content.
	- Step 2: Mask with 0xFF & b to strip Java's sign extension (unsigned 0..255).
	- Step 3: Assemble the 20 byte pairs into the 40-character SHA-1 hash.
</Notes>

<!-- Action 1: Highlight SHA-1 digest generation -->
<Action do={() => highlightStep(1)} undo={() => highlightStep(0)} />

<!-- Action 2: Highlight Bitmasking (0xff & b) -->
<Action do={() => highlightStep(2)} undo={() => highlightStep(1)} />

<!-- Action 3: Highlight Final 40-character SHA-1 string assembly -->
<Action do={() => highlightStep(3)} undo={() => highlightStep(2)} />

<div class="w-[1050px] h-[650px] flex flex-col justify-between items-center select-none text-white p-6">
	<!-- Centered Large Code Snippet with Transparent Background -->
	<!-- <div class="my-auto w-full max-w-4xl flex justify-start pl-8"> -->
		<Code
			bind:this={codeRef}
			lang="java"
			theme="dracula"
			{code}
			autoIndent={false}
			options={{ lineNumbers: true }}
			// class="!bg-transparent text-2xl font-mono leading-[1.65] tracking-wide"
		/>
	<!-- </div> -->

	<!-- Step description footer -->
	<div class="w-full max-w-4xl font-mono text-xs text-neutral-400 flex items-center justify-between border-t border-neutral-800/80 pt-3">
		<span>
			{#if step === 1}
				<span class="text-emerald-400 font-semibold">Step 1:</span> Generate 20-byte SHA-1 digest from content
			{:else if step === 2}
				<span class="text-sky-400 font-semibold">Step 2:</span> Apply <code class="text-sky-300 font-bold">0xff &amp; b</code> to strip sign extension
			{:else if step === 3}
				<span class="text-purple-400 font-semibold">Step 3:</span> Assemble 40-character hexadecimal SHA-1 string
			{:else}
				<span>Converting binary digest to 40-character hex string</span>
			{/if}
		</span>
		<span class="text-neutral-500">Step {step} of 3</span>
	</div>
</div>

<style>
	:global(.shiki-magic-move-container) {
		background-color: transparent !important;
	}
</style>
