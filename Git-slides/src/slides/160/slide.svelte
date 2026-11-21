<script lang="ts">
	import { Action } from '@animotion/core';
	import { createTypewriter } from '$lib';

	let activeLevel = $state(0);

	const twKey1 = createTypewriter('Key', { speed: 55 });
	const twVal1 = createTypewriter('Value', { speed: 55 });

	const twKey2 = createTypewriter('Key', { speed: 55 });
	const twVal2 = createTypewriter('Value', { speed: 55 });

	const twKey3 = createTypewriter('Key', { speed: 55 });
	const twVal3 = createTypewriter('Value', { speed: 55 });

	const twKey4 = createTypewriter('Key', { speed: 55 });
	const twVal4 = createTypewriter('Value', { speed: 55 });

	const twKey5 = createTypewriter('Key', { speed: 55 });
	const twVal5 = createTypewriter('Value', { speed: 55 });

	function getFontSize(level: number): string {
		if (activeLevel <= 1) return 'text-7xl';
		if (activeLevel === 2) return 'text-5xl';
		if (activeLevel === 3) return level <= 2 ? 'text-4xl' : 'text-3xl';
		if (activeLevel === 4) return level <= 2 ? 'text-3xl' : 'text-2xl';
		return level <= 2 ? 'text-2xl' : 'text-xl';
	}

	async function step1() {
		activeLevel = 1;
		await Promise.all([twKey1.start(), twVal1.start()]);
	}

	function undoStep1() {
		activeLevel = 0;
		twKey1.reset();
		twVal1.reset();
	}

	async function step2() {
		activeLevel = 2;
		await Promise.all([twKey2.start(), twVal2.start()]);
	}

	function undoStep2() {
		activeLevel = 1;
		twKey2.reset();
		twVal2.reset();
	}

	async function step3() {
		activeLevel = 3;
		await Promise.all([twKey3.start(), twVal3.start()]);
	}

	function undoStep3() {
		activeLevel = 2;
		twKey3.reset();
		twVal3.reset();
	}

	async function step4() {
		activeLevel = 4;
		await Promise.all([twKey4.start(), twVal4.start()]);
	}

	function undoStep4() {
		activeLevel = 3;
		twKey4.reset();
		twVal4.reset();
	}

	async function step5() {
		activeLevel = 5;
		await Promise.all([twKey5.start(), twVal5.start()]);
	}

	function undoStep5() {
		activeLevel = 4;
		twKey5.reset();
		twVal5.reset();
	}

	function resetAll() {
		activeLevel = 0;
		twKey1.reset();
		twVal1.reset();
		twKey2.reset();
		twVal2.reset();
		twKey3.reset();
		twVal3.reset();
		twKey4.reset();
		twVal4.reset();
		twKey5.reset();
		twVal5.reset();
	}

	export const props = {
		background: '#18181b',
		out: () => {
			resetAll();
		}
	};
</script>

<!-- Action 1: Initial Key-Value Pair -->
<Action do={step1} undo={undoStep1} />

<!-- Action 2: Split 1 (Value -> Key-Value) -->
<Action do={step2} undo={undoStep2} />

<!-- Action 3: Split 2 (Value -> Key-Value) -->
<Action do={step3} undo={undoStep3} />

<!-- Action 4: Split 3 (Value -> Key-Value) -->
<Action do={step4} undo={undoStep4} />

<!-- Action 5: Split 4 (Value -> Key-Value) -->
<Action do={step5} undo={undoStep5} />

<div class="w-[1060px] h-[660px] flex flex-col justify-between p-8 text-white">
	<!-- Header / Title -->
	<div class="flex items-center justify-between border-b border-neutral-800 pb-3">
		<div class="flex items-center gap-3">
			<h2 class="text-3xl font-serif font-bold tracking-tight text-white">Key Value Pairs</h2>
			<span class="text-xs font-mono px-2.5 py-0.5 rounded-full bg-neutral-800 text-neutral-300 border border-neutral-700 font-semibold">
				Git Storage Primitive
			</span>
		</div>
		<div>
			{#if activeLevel <= 1}
				<span class="text-xs font-mono uppercase tracking-wider text-neutral-400 font-semibold">Step 1: Simple Store</span>
			{:else if activeLevel === 2}
				<span class="text-xs font-mono uppercase tracking-wider text-teal-400 font-bold">Split 1: Value is a Pair</span>
			{:else if activeLevel === 3}
				<span class="text-xs font-mono uppercase tracking-wider text-teal-400 font-bold">Split 2: Nested Subtree</span>
			{:else if activeLevel === 4}
				<span class="text-xs font-mono uppercase tracking-wider text-teal-400 font-bold">Split 3: Deep Hierarchy</span>
			{:else}
				<span class="text-xs font-mono uppercase tracking-wider text-emerald-400 font-bold">Split 4: Key-Value is a Graph</span>
			{/if}
		</div>
	</div>

	<!-- Main Clean Split Container -->
	<div class="flex items-center justify-center my-auto w-full h-[360px]">
		<!-- Level 1 Outer Split -->
		<div
			class="flex items-center justify-between w-full h-full border-2 border-neutral-700 rounded-2xl bg-neutral-900/90 p-4 shadow-2xl transition-all duration-500 overflow-hidden"
		>
			<!-- Level 1: Left Key -->
			<div class="flex-1 flex items-center justify-center font-mono font-bold text-teal-400 {getFontSize(1)} transition-all duration-500">
				{#if !twKey1.hasStarted}
					<span class="inline-block w-2 h-14 bg-teal-400 animate-pulse"></span>
				{:else}
					<span>{twKey1.text}</span>
					{#if !twKey1.isDone}
						<span class="inline-block w-2 h-14 bg-teal-400 ml-2 animate-pulse"></span>
					{/if}
				{/if}
			</div>

			<!-- Divider 1 -->
			<div class="h-4/5 w-[2.5px] bg-neutral-700 mx-3 shrink-0"></div>

			<!-- Level 1 Right: Value 1 or Level 2 Container -->
			{#if activeLevel <= 1}
				<div class="flex-1 flex items-center justify-center font-mono font-bold text-white {getFontSize(1)} transition-all duration-500">
					{#if !twVal1.hasStarted}
						<span class="inline-block w-2 h-14 bg-white animate-pulse"></span>
					{:else}
						<span>{twVal1.text}</span>
						{#if !twVal1.isDone}
							<span class="inline-block w-2 h-14 bg-white ml-2 animate-pulse"></span>
						{/if}
					{/if}
				</div>
			{:else}
				<!-- Level 2 Nested Container (Value becomes a Key-Value pair) -->
				<div
					class="flex-[1.2] h-full flex items-center justify-between border-2 border-dashed border-teal-500/50 rounded-xl bg-teal-950/20 p-3 transition-all duration-500 overflow-hidden"
				>
					<!-- Level 2: Left Key -->
					<div class="flex-1 flex items-center justify-center font-mono font-bold text-teal-400 {getFontSize(2)} transition-all duration-500">
						{#if !twKey2.hasStarted}
							<span class="inline-block w-2 h-10 bg-teal-400 animate-pulse"></span>
						{:else}
							<span>{twKey2.text}</span>
							{#if !twKey2.isDone}
								<span class="inline-block w-2 h-10 bg-teal-400 ml-1.5 animate-pulse"></span>
							{/if}
						{/if}
					</div>

					<!-- Divider 2 -->
					<div class="h-4/5 w-[2px] bg-neutral-700 mx-2.5 shrink-0"></div>

					<!-- Level 2 Right: Value 2 or Level 3 Container -->
					{#if activeLevel === 2}
						<div class="flex-1 flex items-center justify-center font-mono font-bold text-white {getFontSize(2)} transition-all duration-500">
							{#if !twVal2.hasStarted}
								<span class="inline-block w-2 h-10 bg-white animate-pulse"></span>
							{:else}
								<span>{twVal2.text}</span>
								{#if !twVal2.isDone}
									<span class="inline-block w-2 h-10 bg-white ml-1.5 animate-pulse"></span>
								{/if}
							{/if}
						</div>
					{:else}
						<!-- Level 3 Nested Container -->
						<div
							class="flex-[1.3] h-full flex items-center justify-between border-2 border-dashed border-teal-500/60 rounded-lg bg-teal-950/30 p-2.5 transition-all duration-500 overflow-hidden"
						>
							<!-- Level 3: Left Key -->
							<div class="flex-1 flex items-center justify-center font-mono font-bold text-teal-400 {getFontSize(3)} transition-all duration-500">
								{#if !twKey3.hasStarted}
									<span class="inline-block w-1.5 h-8 bg-teal-400 animate-pulse"></span>
								{:else}
									<span>{twKey3.text}</span>
									{#if !twKey3.isDone}
										<span class="inline-block w-1.5 h-8 bg-teal-400 ml-1 animate-pulse"></span>
									{/if}
								{/if}
							</div>

							<!-- Divider 3 -->
							<div class="h-4/5 w-[2px] bg-neutral-700 mx-2 shrink-0"></div>

							<!-- Level 3 Right: Value 3 or Level 4 Container -->
							{#if activeLevel === 3}
								<div class="flex-1 flex items-center justify-center font-mono font-bold text-white {getFontSize(3)} transition-all duration-500">
									{#if !twVal3.hasStarted}
										<span class="inline-block w-1.5 h-8 bg-white animate-pulse"></span>
									{:else}
										<span>{twVal3.text}</span>
										{#if !twVal3.isDone}
											<span class="inline-block w-1.5 h-8 bg-white ml-1 animate-pulse"></span>
										{/if}
									{/if}
								</div>
							{:else}
								<!-- Level 4 Nested Container -->
								<div
									class="flex-[1.4] h-full flex items-center justify-between border-2 border-dashed border-teal-500/70 rounded-md bg-teal-950/40 p-2 transition-all duration-500 overflow-hidden"
								>
									<!-- Level 4: Left Key -->
									<div class="flex-1 flex items-center justify-center font-mono font-bold text-teal-400 {getFontSize(4)} transition-all duration-500">
										{#if !twKey4.hasStarted}
											<span class="inline-block w-1.5 h-6 bg-teal-400 animate-pulse"></span>
										{:else}
											<span>{twKey4.text}</span>
											{#if !twKey4.isDone}
												<span class="inline-block w-1.5 h-6 bg-teal-400 ml-1 animate-pulse"></span>
											{/if}
										{/if}
									</div>

									<!-- Divider 4 -->
									<div class="h-4/5 w-[2px] bg-neutral-700 mx-1.5 shrink-0"></div>

									<!-- Level 4 Right: Value 4 or Level 5 Container -->
									{#if activeLevel === 4}
										<div class="flex-1 flex items-center justify-center font-mono font-bold text-white {getFontSize(4)} transition-all duration-500">
											{#if !twVal4.hasStarted}
												<span class="inline-block w-1.5 h-6 bg-white animate-pulse"></span>
											{:else}
												<span>{twVal4.text}</span>
												{#if !twVal4.isDone}
													<span class="inline-block w-1.5 h-6 bg-white ml-1 animate-pulse"></span>
												{/if}
											{/if}
										</div>
									{:else}
										<!-- Level 5 Nested Container (Final Split) -->
										<div
											class="flex-[1.5] h-full flex items-center justify-between border-2 border-dashed border-teal-500/80 rounded bg-teal-950/50 p-1.5 transition-all duration-500 overflow-hidden"
										>
											<!-- Level 5: Left Key -->
											<div class="flex-1 flex items-center justify-center font-mono font-bold text-teal-400 {getFontSize(5)} transition-all duration-500">
												{#if !twKey5.hasStarted}
													<span class="inline-block w-1 h-5 bg-teal-400 animate-pulse"></span>
												{:else}
													<span>{twKey5.text}</span>
													{#if !twKey5.isDone}
														<span class="inline-block w-1 h-5 bg-teal-400 ml-0.5 animate-pulse"></span>
													{/if}
												{/if}
											</div>

											<!-- Divider 5 -->
											<div class="h-4/5 w-[2px] bg-neutral-700 mx-1 shrink-0"></div>

											<!-- Level 5: Right Value -->
											<div class="flex-1 flex items-center justify-center font-mono font-bold text-white {getFontSize(5)} transition-all duration-500">
												{#if !twVal5.hasStarted}
													<span class="inline-block w-1 h-5 bg-white animate-pulse"></span>
												{:else}
													<span>{twVal5.text}</span>
													{#if !twVal5.isDone}
														<span class="inline-block w-1 h-5 bg-white ml-0.5 animate-pulse"></span>
													{/if}
												{/if}
											</div>
										</div>
									{/if}
								</div>
							{/if}
						</div>
					{/if}
				</div>
			{/if}
		</div>
	</div>

	<!-- Bottom Structure & Code Representation -->
	<div class="h-[80px] flex items-center justify-between font-mono bg-neutral-900 border-2 border-neutral-800 rounded-xl px-6 py-2.5 shadow-lg transition-all duration-300">
		{#if activeLevel === 0}
			<span class="text-sm text-neutral-400 font-medium italic">Press next to type initial key-value pair...</span>
		{:else if activeLevel === 1}
			<div class="text-xl space-x-1">
				<span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-white font-bold">Value</span>
				<span class="text-neutral-400 font-bold">&#125;</span>
			</div>
			<span class="text-xs font-mono text-neutral-400 font-semibold">1 depth</span>
		{:else if activeLevel === 2}
			<div class="text-lg space-x-1">
				<span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-white font-bold">Value</span>
				<span class="text-neutral-400 font-bold">&#125;</span>
				<span class="text-neutral-400 font-bold">&#125;</span>
			</div>
			<span class="text-xs font-mono text-teal-400 font-bold">2 depths</span>
		{:else if activeLevel === 3}
			<div class="text-base space-x-1">
				<span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-white font-bold">Value</span>
				<span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span>
			</div>
			<span class="text-xs font-mono text-teal-400 font-bold">3 depths</span>
		{:else if activeLevel === 4}
			<div class="text-sm space-x-1">
				<span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-white font-bold">Value</span>
				<span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span>
			</div>
			<span class="text-xs font-mono text-teal-400 font-bold">4 depths</span>
		{:else}
			<div class="text-xs space-x-0.5 tracking-tight">
				<span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-neutral-400 font-bold">&#123;</span>
				<span class="text-teal-400 font-bold">Key</span>: <span class="text-white font-bold">Value</span>
				<span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span> <span class="text-neutral-400 font-bold">&#125;</span>
			</div>
			<div class="flex items-center gap-2">
				<span class="text-xs font-mono bg-emerald-950 text-emerald-300 px-3 py-1 rounded-full font-bold border border-emerald-600">
					Tree / Graph (DAG) Structure
				</span>
			</div>
		{/if}
	</div>
</div>
