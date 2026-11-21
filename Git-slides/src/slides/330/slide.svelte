<script lang="ts">
	import { Action, Code, Notes } from '@animotion/core';

	let codeRef: ReturnType<typeof Code> | undefined = $state();
	let step = $state(0);

	const code = `public static String catFile(String sha1) throws IOException {
    Path path = Path.of(".git", "objects",
        sha1.substring(0, 2), sha1.substring(2));

    byte[] raw = new InflaterInputStream(
        new FileInputStream(path.toFile())
    ).readAllBytes();

    int nullIndex = indexOf(raw, (byte) 0);

    return new String(raw, nullIndex + 1,
        raw.length - nullIndex - 1, "UTF-8");
}`;

	function highlightStep(s: number) {
		step = s;
		if (!codeRef) return;
		switch (s) {
			case 0:
				codeRef.selectLines`*`;
				break;
			case 1:
				codeRef.select`sha1.substring(0, 2), sha1.substring(2)`;
				break;
			case 2:
				codeRef.select`new InflaterInputStream(
        new FileInputStream(path.toFile())
    ).readAllBytes()`;
				break;
			case 3:
				codeRef.select`indexOf(raw, (byte) 0)`;
				break;
			case 4:
				codeRef.select`return new String(raw, nullIndex + 1,
        raw.length - nullIndex - 1, "UTF-8")`;
				break;
		}
	}

	export const props = {
		background: '#18181b',
		out: () => {
			highlightStep(0);
		}
	};
</script>

<Notes>
	- Step 1: Split 40-char SHA-1 into 2-char dir prefix and 38-char filename — maps to .git/objects/xx/yyyy...
	- Step 2: Open the file and decompress via zlib (InflaterInputStream), reading all bytes at once.
	- Step 3: Git objects start with a header ("type size\0"). Scan for the null byte to find where content starts.
	- Step 4: Slice past the null byte and decode the remaining bytes as UTF-8 to get the file content.
</Notes>

<!-- Action 1: Derive path from SHA-1 -->
<Action do={() => highlightStep(1)} undo={() => highlightStep(0)} />

<!-- Action 2: Read & decompress from disk -->
<Action do={() => highlightStep(2)} undo={() => highlightStep(1)} />

<!-- Action 3: Find null byte header separator -->
<Action do={() => highlightStep(3)} undo={() => highlightStep(2)} />

<!-- Action 4: Decode content past header -->
<Action do={() => highlightStep(4)} undo={() => highlightStep(3)} />

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
				<span class="text-emerald-400 font-semibold">Step 1:</span> Shard SHA-1 → <code class="text-emerald-300 font-bold">.git/objects/xx/yyyy...</code>
			{:else if step === 2}
				<span class="text-sky-400 font-semibold">Step 2:</span> Decompress zlib stream and read all bytes
			{:else if step === 3}
				<span class="text-indigo-400 font-semibold">Step 3:</span> Find null byte (<code class="text-indigo-300 font-bold">0x00</code>) separating header from content
			{:else if step === 4}
				<span class="text-pink-400 font-semibold">Step 4:</span> Decode content bytes to UTF-8 string
			{:else}
				<span>Reading and decompressing objects from <code class="text-neutral-300 font-bold">.git/objects</code></span>
			{/if}
		</span>
		<span class="text-neutral-500">Step {step} of 4</span>
	</div>
</div>

<style>
	:global(.shiki-magic-move-container) {
		background-color: transparent !important;
	}
</style>
