export type TypewriterOptions = {
	speed?: number | (() => number);
	delay?: number | (() => number);
	lineDelay?: number | (() => number);
	autostart?: boolean | (() => boolean);
	onComplete?: () => void;
};

export function createTypewriter(
	textInput: string | string[] | (() => string | string[]),
	options: TypewriterOptions = {}
) {
	const getLines = () => {
		const val = typeof textInput === 'function' ? textInput() : textInput;
		return Array.isArray(val) ? val : [val];
	};

	const getAutostart = () => {
		return typeof options.autostart === 'function' ? options.autostart() : (options.autostart ?? false);
	};

	let typedLines = $state<string[]>(getLines().map(() => ''));
	let currentLineIndex = $state(0);
	let hasStarted = $state(getAutostart());
	let isDone = $state(false);
	let isTyping = $state(false);

	let timeoutId: number | ReturnType<typeof setTimeout> | undefined;
	let resolveDone: (() => void) | null = null;

	function reset() {
		if (timeoutId) clearTimeout(timeoutId);
		typedLines = getLines().map(() => '');
		currentLineIndex = 0;
		hasStarted = false;
		isDone = false;
		isTyping = false;
		resolveDone = null;
	}

	function start(): Promise<void> {
		reset();
		hasStarted = true;
		isTyping = true;

		const currentLines = getLines();
		const speed = typeof options.speed === 'function' ? options.speed() : (options.speed ?? 40);
		const delay = typeof options.delay === 'function' ? options.delay() : (options.delay ?? 100);
		const lineDelay = typeof options.lineDelay === 'function' ? options.lineDelay() : (options.lineDelay ?? 180);

		let lineIdx = 0;
		let charIdx = 0;

		return new Promise<void>((resolve) => {
			resolveDone = resolve;

			function step() {
				if (lineIdx < currentLines.length) {
					const currentFullLine = currentLines[lineIdx];
					if (charIdx < currentFullLine.length) {
						typedLines[lineIdx] = currentFullLine.slice(0, charIdx + 1);
						charIdx++;
						timeoutId = setTimeout(step, speed);
					} else {
						lineIdx++;
						charIdx = 0;
						currentLineIndex = lineIdx;
						if (lineIdx < currentLines.length) {
							timeoutId = setTimeout(step, lineDelay);
						} else {
							isTyping = false;
							isDone = true;
							options.onComplete?.();
							resolveDone?.();
						}
					}
				}
			}

			timeoutId = setTimeout(step, delay);
		});
	}

	if (getAutostart()) {
		start();
	}

	return {
		get typedLines() {
			return typedLines;
		},
		get text() {
			return typedLines.join('\n');
		},
		get line() {
			return typedLines[0] ?? '';
		},
		get currentLineIndex() {
			return currentLineIndex;
		},
		get hasStarted() {
			return hasStarted;
		},
		get isDone() {
			return isDone;
		},
		get isTyping() {
			return isTyping;
		},
		start,
		reset
	};
}
