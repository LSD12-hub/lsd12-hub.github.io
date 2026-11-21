<script lang="ts">
	import { Action, Code, Notes } from '@animotion/core';

	let codeRef: ReturnType<typeof Code> | undefined = $state();
	let step = $state(0);

	const code = `public static String hashObject(byte[] content, String type, boolean write)
    throws IOException, NoSuchAlgorithmException {
    byte[] header = (type + " " + content.length + '\0').getBytes();
    byte[] fullContent = concat(header, content);

    String sha1 = sha1Hex(fullContent);

    if (write) {
        Path path = Path.of(".git", "objects",
            sha1.substring(0, 2), sha1.substring(2));
        Files.createDirectories(path.getParent());
        compress(fullContent, path);
    }
    return sha1;
}`;

	function highlightStep(s: number) {
		step = s;
		if (!codeRef) return;
		switch (s) {
			case 0:
				codeRef.selectLines`*`;
				break;
			case 1:
				codeRef.select`(type + " " + content.length + '\0').getBytes()`;
				break;
			case 2:
				codeRef.select`sha1Hex(fullContent)`;
				break;
			case 3:
				codeRef.select`sha1.substring(0, 2), sha1.substring(2)`;
				break;
			case 4:
				codeRef.select`compress(fullContent, path)`;
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
	- Step 1: Build the Git loose object header "type size\0" encoded as raw bytes.
	- Step 2: Compute SHA-1 hex over the combined header + content payload.
	- Step 3: Shard SHA-1 into 2-char dir prefix and 38-char filename → .git/objects/xx/yyyy...
	- Step 4: Compress with zlib (Deflater) and write the object file to disk.
</Notes>

<!-- Action 1: Build header bytes -->
<Action do={() => highlightStep(1)} undo={() => highlightStep(0)} />

<!-- Action 2: Compute SHA-1 hash -->
<Action do={() => highlightStep(2)} undo={() => highlightStep(1)} />

<!-- Action 3: Shard SHA-1 into path -->
<Action do={() => highlightStep(3)} undo={() => highlightStep(2)} />

<!-- Action 4: Compress and write to disk -->
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
				<span class="text-emerald-400 font-semibold">Step 1:</span> Build header <code class="text-emerald-300 font-bold">"type size\0"</code> as raw bytes
			{:else if step === 2}
				<span class="text-sky-400 font-semibold">Step 2:</span> Compute SHA-1 hex over header + content
			{:else if step === 3}
				<span class="text-indigo-400 font-semibold">Step 3:</span> Shard SHA-1 → <code class="text-indigo-300 font-bold">.git/objects/xx/yyyy...</code>
			{:else if step === 4}
				<span class="text-pink-400 font-semibold">Step 4:</span> Compress with zlib and write object to disk
			{:else}
				<span>Creating and writing objects to <code class="text-neutral-300 font-bold">.git/objects</code></span>
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

