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
				codeRef.select`int nullIndex = -1;`;
				break;
			case 2:
				codeRef.select`decompressedData[i] == 0`;
				break;
			case 3:
				codeRef.select`nullIndex = i;
        break;`;
				break;
			case 4:
				codeRef.select`nullIndex + 1`;
				break;
			case 5:
				codeRef.select`return content;`;
				break;
		}
	}

	export const props = {
		background: '#18181b',
		out: () => {
			highlightStep(0);
		}
	};

	const code = `byte[] decompressedData = decompressedStream.toByteArray();

int nullIndex = -1;
for (int i = 0; i < decompressedData.length; i++) {
    if (decompressedData[i] == 0) {
        nullIndex = i;
        break;
    }
}

String content = new String(decompressedData, nullIndex + 1, 
    decompressedData.length - nullIndex - 1, "UTF-8");
return content;`;
</script>

<Notes>
	- Step 1: Git loose objects format is header ("type size\0") followed by content. We need to find the null byte separator.
	- Step 2: Iterate over raw bytes to scan for 0x00 (null byte delimiter).
	- Step 3: Record the index where the header ends and break out of loop.
	- Step 4: Slice the byte array starting past the null byte (nullIndex + 1) and decode to UTF-8 String.
	- Step 5: Return the reconstructed file content.
</Notes>

<!-- Action 1: Initialize null byte pointer -->
<Action do={() => highlightStep(1)} undo={() => highlightStep(0)} />

<!-- Action 2: Scan for null byte separator -->
<Action do={() => highlightStep(2)} undo={() => highlightStep(1)} />

<!-- Action 3: Save null index and break -->
<Action do={() => highlightStep(3)} undo={() => highlightStep(2)} />

<!-- Action 4: Slice payload past null byte and decode to UTF-8 String -->
<Action do={() => highlightStep(4)} undo={() => highlightStep(3)} />

<!-- Action 5: Return content -->
<Action do={() => highlightStep(5)} undo={() => highlightStep(4)} />

<div class="w-[1000px] h-[580px] flex flex-col justify-between items-center select-none text-white p-4">
	<div class="my-auto">
		<Code
			bind:this={codeRef}
			lang="java"
			theme="dracula"
			{code}
			autoIndent={false}
			options={{ lineNumbers: true }}
		/>
	</div>

	<!-- Step description footer -->
	<div class="w-full max-w-3xl font-mono text-xs text-neutral-400 flex items-center justify-between border-t border-neutral-800/80 pt-3">
		<span>
			{#if step === 1}
				<span class="text-emerald-400 font-semibold">Step 1:</span> Initialize index to locate the header's null byte (<code class="text-emerald-300 font-bold">0x00</code>) delimiter
			{:else if step === 2}
				<span class="text-sky-400 font-semibold">Step 2:</span> Scan decompressed bytes for header end (<code class="text-sky-300 font-bold">'\0'</code>)
			{:else if step === 3}
				<span class="text-indigo-400 font-semibold">Step 3:</span> Record null byte index boundary and exit loop
			{:else if step === 4}
				<span class="text-pink-400 font-semibold">Step 4:</span> Slice payload slice past header &amp; decode UTF-8 string (<code class="text-pink-300 font-bold">nullIndex + 1</code>)
			{:else if step === 5}
				<span class="text-purple-400 font-semibold">Step 5:</span> Return reconstructed file content
			{:else}
				<span>Parsing Git object header and extracting file content (Part 2)</span>
			{/if}
		</span>
		<span class="text-neutral-500">Step {step} of 5</span>
	</div>
</div>

<style>
	:global(.shiki-magic-move-container) {
		background-color: transparent !important;
	}
</style>
