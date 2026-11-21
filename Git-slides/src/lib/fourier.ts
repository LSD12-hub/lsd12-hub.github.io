/**
 * Fourier Series & Epicycles Utility
 *
 * Computes Discrete Fourier Transform (DFT) for 2D complex curves
 * and evaluates rotating epicycles for animated SVG drawings.
 *
 * Mathematically aligned 1:1 with static/images/leetcode_transparent.png.
 */

export interface Point {
	x: number;
	y: number;
}

export interface FourierCoefficient {
	freq: number;
	amp: number;
	phase: number;
	re: number;
	im: number;
}

export interface EpicycleCircle {
	index: number;
	x: number;
	y: number;
	radius: number;
	angle: number;
	targetX: number;
	targetY: number;
	freq: number;
}

export interface FourierEvaluation {
	circles: EpicycleCircle[];
	tip: Point;
}

export interface FourierOptions {
	scale?: number;
	offsetX?: number;
	offsetY?: number;
	samplesPerStroke?: number;
}

function sampleLine(p0: Point, p1: Point, steps: number): Point[] {
	const pts: Point[] = [];
	for (let i = 0; i <= steps; i++) {
		const t = i / steps;
		pts.push({
			x: p0.x + (p1.x - p0.x) * t,
			y: p0.y + (p1.y - p0.y) * t
		});
	}
	return pts;
}

function sampleQuad(p0: Point, pc: Point, p1: Point, steps: number): Point[] {
	const pts: Point[] = [];
	for (let i = 0; i <= steps; i++) {
		const t = i / steps;
		const u = 1 - t;
		pts.push({
			x: u * u * p0.x + 2 * u * t * pc.x + t * t * p1.x,
			y: u * u * p0.y + 2 * u * t * pc.y + t * t * p1.y
		});
	}
	return pts;
}

function sampleCubic(p0: Point, pc1: Point, pc2: Point, p1: Point, steps: number): Point[] {
	const pts: Point[] = [];
	for (let i = 0; i <= steps; i++) {
		const t = i / steps;
		const u = 1 - t;
		pts.push({
			x: u * u * u * p0.x + 3 * u * u * t * pc1.x + 3 * u * t * t * pc2.x + t * t * t * p1.x,
			y: u * u * u * p0.y + 3 * u * u * t * pc1.y + 3 * u * t * t * pc2.y + t * t * t * p1.y
		});
	}
	return pts;
}

/**
 * Normalized 2D contour coordinates for the full LeetCode logo outline (900x508 space),
 * capturing the exact outer/inner boundaries of the curved hook bracket and horizontal bar,
 * bridged cleanly without artificial cross-logo jumps.
 */
const BASE_LEETCODE_OUTLINE: [number, number][] = [
	[491.2, 44.0], [496.4, 44.2], [501.4, 45.6], [506.0, 48.0], [510.1, 51.4], [513.3, 55.5],
	[515.4, 60.2], [516.6, 65.3], [516.8, 70.5], [515.7, 75.6], [513.8, 80.4], [510.9, 84.8],
	[507.4, 88.6], [503.7, 92.3], [500.0, 96.0], [496.3, 99.7], [492.6, 103.4], [488.9, 107.1],
	[485.2, 110.8], [481.5, 114.5], [477.8, 118.2], [474.1, 121.9], [470.5, 125.7], [472.0, 129.4],
	[476.9, 131.0], [481.8, 133.0], [486.6, 135.1], [491.2, 137.5], [495.7, 140.2], [500.0, 143.1],
	[504.2, 146.3], [508.3, 149.5], [512.1, 153.1], [515.8, 156.8], [519.5, 160.5], [523.2, 164.2],
	[526.9, 167.9], [530.6, 171.6], [534.3, 175.3], [538.0, 179.0], [541.7, 182.7], [545.4, 186.4],
	[549.1, 190.1], [552.8, 193.8], [556.3, 197.6], [559.4, 201.8], [561.4, 206.6], [562.4, 211.7],
	[562.3, 216.9], [561.3, 222.0], [559.1, 226.8], [555.9, 230.9], [552.0, 234.3], [547.4, 236.8],
	[542.4, 238.3], [537.2, 239.0], [532.1, 238.3], [527.1, 236.6], [522.6, 234.0], [518.6, 230.6],
	[515.2, 226.7], [511.8, 222.8], [507.9, 219.3], [503.9, 215.9], [500.4, 212.0], [497.0, 208.0],
	[493.3, 204.3], [489.4, 200.9], [485.4, 197.4], [482.0, 193.5], [478.4, 189.8], [474.4, 186.4],
	[470.2, 183.3], [465.7, 180.7], [460.9, 178.7], [455.9, 177.0], [450.8, 175.8], [445.6, 175.1],
	[440.4, 175.0], [435.2, 175.7], [430.1, 176.7], [425.1, 178.2], [420.3, 180.2], [415.7, 182.6],
	[411.4, 185.7], [407.4, 189.0], [403.5, 192.5], [399.8, 196.2], [396.1, 199.9], [392.4, 203.6],
	[388.7, 207.3], [385.0, 211.0], [381.3, 214.7], [377.6, 218.4], [373.9, 222.1], [370.2, 225.8],
	[366.6, 229.4], [362.9, 233.1], [359.2, 236.8], [355.5, 240.5], [351.8, 244.2], [348.1, 247.9],
	[344.4, 251.6], [340.7, 255.3], [337.1, 259.2], [333.8, 263.2], [330.7, 267.4], [328.3, 272.0],
	[326.1, 276.8], [324.5, 281.8], [323.4, 286.9], [323.0, 292.1], [323.0, 297.3], [323.5, 302.5],
	[324.6, 307.6], [326.2, 312.6], [328.0, 317.4], [330.7, 321.9], [333.6, 326.2], [337.1, 330.1],
	[340.8, 333.8], [344.4, 337.6], [348.0, 341.4], [351.8, 345.0], [355.2, 348.9], [359.0, 352.6],
	[363.0, 356.0], [366.4, 359.9], [369.8, 363.8], [373.5, 367.5], [377.3, 371.1], [381.3, 374.5],
	[384.9, 378.3], [388.3, 382.2], [392.0, 386.0], [395.7, 389.7], [399.4, 393.4], [403.1, 397.1],
	[407.0, 400.5], [411.1, 403.8], [415.3, 406.8], [419.9, 409.3], [424.7, 411.3], [429.7, 412.8],
	[434.8, 413.8], [440.0, 414.3], [445.3, 414.2], [450.5, 413.8], [455.6, 412.7], [460.5, 411.1],
	[465.3, 409.1], [469.8, 406.4], [474.1, 403.5], [478.0, 400.0], [481.7, 396.3], [485.4, 392.6],
	[489.1, 388.9], [492.8, 385.2], [496.5, 381.5], [500.2, 377.8], [503.9, 374.1], [507.6, 370.4],
	[511.3, 366.7], [515.0, 363.0], [518.7, 359.3], [522.7, 355.9], [527.1, 353.2], [532.0, 351.4],
	[537.2, 351.0], [542.4, 351.3], [542.5, 348.2], [542.7, 345.0], [542.9, 341.9], [543.0, 338.8],
	[543.1, 335.6], [543.3, 332.5], [543.4, 329.4], [543.6, 326.3], [543.8, 323.1], [543.9, 320.0],
	[539.8, 319.6], [535.7, 319.0], [531.5, 319.0], [527.3, 319.0], [523.1, 319.0], [519.0, 319.6],
	[514.9, 320.0], [510.7, 320.0], [506.5, 320.0], [502.4, 320.0], [498.3, 319.3], [494.1, 319.0],
	[489.9, 319.0], [485.8, 319.0], [481.6, 319.1], [477.5, 319.9], [473.3, 320.0], [469.1, 320.0],
	[465.0, 320.0], [460.8, 319.8], [456.7, 319.0], [452.5, 319.0], [448.4, 319.0], [444.2, 319.0],
	[440.0, 319.4], [435.9, 320.0], [431.8, 320.0], [427.6, 319.9], [423.5, 319.0], [419.5, 317.8],
	[415.8, 316.1], [412.5, 313.5], [409.7, 310.4], [407.4, 306.9], [405.7, 303.1], [404.8, 299.0],
	[404.0, 294.9], [404.9, 290.9], [406.1, 286.9], [407.8, 283.1], [410.0, 279.5], [412.7, 276.4],
	[416.2, 274.1], [419.9, 272.2], [424.0, 271.4], [428.1, 271.0], [432.3, 271.0], [436.5, 271.0],
	[440.7, 271.0], [444.8, 271.0], [449.0, 271.0], [453.2, 271.0], [457.4, 271.0], [461.5, 271.0],
	[465.7, 271.0], [469.9, 271.0], [474.1, 271.0], [478.3, 271.0], [482.4, 271.0], [486.6, 271.0],
	[490.8, 271.0], [495.0, 271.0], [499.1, 271.0], [503.3, 271.0], [507.5, 271.0], [511.7, 271.0],
	[515.8, 271.0], [520.0, 271.0], [524.2, 271.0], [528.4, 271.0], [532.6, 271.0], [536.7, 271.0],
	[540.9, 271.0], [545.1, 271.0], [549.3, 271.0], [553.4, 271.0], [557.6, 271.0], [561.8, 271.0],
	[566.0, 271.0], [570.1, 271.0], [574.3, 271.0], [578.5, 271.0], [582.7, 271.0], [586.8, 271.0],
	[591.0, 271.0], [595.2, 271.0], [599.4, 271.0], [603.6, 271.0], [607.7, 271.3], [611.6, 272.7],
	[615.3, 274.6], [618.6, 277.2], [621.3, 280.4], [623.7, 283.8], [625.3, 287.6], [626.0, 291.7],
	[626.4, 295.9], [625.8, 300.0], [624.6, 304.0], [622.8, 307.7], [620.5, 311.2], [617.6, 314.1],
	[614.1, 316.5], [610.4, 318.3], [606.3, 319.0], [602.1, 319.0], [598.0, 319.8], [593.8, 320.0],
	[589.7, 320.0], [585.5, 320.0], [581.3, 319.9], [577.2, 319.0], [573.1, 319.0], [568.9, 319.0],
	[564.7, 319.0], [560.6, 319.3], [556.5, 320.0], [552.3, 320.0], [548.1, 320.0], [543.8, 323.1],
	[543.6, 326.3], [543.4, 329.4], [543.3, 332.5], [543.1, 335.6], [543.0, 338.8], [542.9, 341.9],
	[542.7, 345.0], [542.5, 348.2], [547.4, 353.0], [551.9, 355.5], [555.9, 358.9], [559.2, 363.0],
	[561.2, 367.8], [562.3, 372.9], [562.3, 378.1], [561.5, 383.3], [559.4, 388.1], [556.3, 392.3],
	[552.8, 396.2], [549.1, 399.9], [545.4, 403.6], [541.7, 407.3], [538.0, 411.0], [534.3, 414.7],
	[530.6, 418.4], [527.0, 422.0], [523.3, 425.7], [519.6, 429.4], [515.9, 433.1], [512.2, 436.8],
	[508.3, 440.3], [504.2, 443.6], [500.0, 446.7], [495.6, 449.6], [491.1, 452.2], [486.4, 454.5],
	[481.7, 456.7], [476.8, 458.6], [471.9, 460.2], [466.8, 461.6], [461.7, 462.7], [456.6, 463.8],
	[451.4, 464.1], [446.2, 464.8], [441.0, 464.7], [435.9, 464.0], [430.6, 463.9], [425.5, 463.2],
	[420.3, 462.2], [415.3, 460.9], [410.3, 459.4], [405.4, 457.6], [400.6, 455.5], [395.9, 453.2],
	[391.3, 450.8], [386.9, 448.0], [382.6, 445.1], [378.5, 441.8], [374.5, 438.4], [370.8, 434.8],
	[367.1, 431.1], [363.4, 427.4], [359.7, 423.7], [356.0, 420.0], [352.3, 416.3], [348.6, 412.6],
	[344.9, 408.9], [341.2, 405.2], [337.5, 401.5], [333.8, 397.8], [330.1, 394.1], [326.4, 390.4],
	[322.7, 386.7], [319.0, 383.0], [315.3, 379.3], [311.6, 375.6], [307.9, 371.9], [304.2, 368.2],
	[300.6, 364.4], [297.2, 360.4], [293.8, 356.5], [290.8, 352.2], [288.0, 347.8], [285.4, 343.3],
	[283.1, 338.6], [280.9, 333.8], [279.0, 329.0], [277.4, 324.0], [276.3, 318.9], [275.2, 313.8],
	[274.2, 308.7], [273.8, 303.5], [273.0, 298.3], [273.0, 293.1], [273.6, 287.9], [274.0, 282.7],
	[274.8, 277.5], [275.7, 272.4], [277.0, 267.3], [278.6, 262.3], [280.4, 257.4], [282.4, 252.6],
	[284.7, 248.0], [287.2, 243.4], [289.9, 238.9], [292.9, 234.6], [296.1, 230.4], [299.5, 226.5],
	[303.2, 222.8], [306.9, 219.1], [310.6, 215.4], [314.3, 211.7], [318.0, 208.0], [321.7, 204.3],
	[325.4, 200.6], [329.1, 196.9], [332.8, 193.2], [336.5, 189.5], [340.2, 185.8], [343.9, 182.1],
	[347.6, 178.4], [351.2, 174.7], [354.6, 170.8], [358.3, 167.0], [362.3, 163.6], [365.9, 159.9],
	[369.6, 156.2], [373.3, 152.6], [377.1, 148.9], [380.8, 145.2], [384.5, 141.5], [388.2, 137.8],
	[391.9, 134.1], [395.6, 130.4], [399.3, 126.7], [403.0, 123.0], [406.7, 119.3], [410.4, 115.6],
	[414.1, 111.9], [417.7, 108.2], [421.4, 104.5], [425.0, 100.7], [428.6, 97.0], [432.5, 93.5],
	[436.1, 89.7], [439.8, 86.0], [443.6, 82.4], [447.3, 78.7], [450.7, 74.7], [454.2, 70.8],
	[458.0, 67.3], [461.7, 63.6], [465.4, 59.9], [469.0, 56.1], [472.7, 52.4], [476.7, 49.1],
	[481.1, 46.2], [486.0, 44.4]
];

/**
 * Generates continuous path points for the complete LeetCode logo outline,
 * precisely matching the proportions and contours in leetcode_transparent.png (900x508).
 */
export function generateLeetCodePoints(options: FourierOptions = {}): Point[] {
	const {
		scale = 0.88,
		offsetX = (960 - 900 * 0.88) / 2,
		offsetY = (480 - 508 * 0.88) / 2
	} = options;

	return BASE_LEETCODE_OUTLINE.map(([x, y]) => ({
		x: Number((x * scale + offsetX).toFixed(1)),
		y: Number((y * scale + offsetY).toFixed(1))
	}));
}

export function computeDFT(points: Point[]): FourierCoefficient[] {
	const N = points.length;
	if (N === 0) return [];

	const X: FourierCoefficient[] = [];

	for (let k = 0; k < N; k++) {
		const freq = k <= N / 2 ? k : k - N;
		let re = 0;
		let im = 0;

		for (let n = 0; n < N; n++) {
			const phi = (2 * Math.PI * freq * n) / N;
			re += points[n].x * Math.cos(phi) + points[n].y * Math.sin(phi);
			im += -points[n].x * Math.sin(phi) + points[n].y * Math.cos(phi);
		}

		re /= N;
		im /= N;

		const amp = Math.sqrt(re * re + im * im);
		const phase = Math.atan2(im, re);

		X.push({ freq, amp, phase, re, im });
	}

	X.sort((a, b) => b.amp - a.amp);
	return X;
}

/**
 * Evaluates epicycle chain at parameter t ∈ [0, 1].
 */
export function evaluateEpicycles(
	coefficients: FourierCoefficient[],
	t: number,
	maxEpicycles?: number,
	origin: Point = { x: 0, y: 0 }
): FourierEvaluation {
	const limit = Math.min(coefficients.length, maxEpicycles ?? coefficients.length);
	let currentX = origin.x;
	let currentY = origin.y;
	const circles: EpicycleCircle[] = [];

	for (let i = 0; i < limit; i++) {
		const c = coefficients[i];
		const prevX = currentX;
		const prevY = currentY;
		const angle = c.freq * (2 * Math.PI * t) + c.phase;

		currentX += c.amp * Math.cos(angle);
		currentY += c.amp * Math.sin(angle);

		circles.push({
			index: i,
			x: prevX,
			y: prevY,
			radius: c.amp,
			angle,
			targetX: currentX,
			targetY: currentY,
			freq: c.freq
		});
	}

	return {
		circles,
		tip: { x: currentX, y: currentY }
	};
}

/**
 * Creates the high-fidelity Fourier model for the LeetCode logo.
 */
export function createLeetCodeFourier(options: FourierOptions = {}): {
	points: Point[];
	coefficients: FourierCoefficient[];
	imageBounds: { x: number; y: number; width: number; height: number };
} {
	const scale = options.scale ?? 0.88;
	const offsetX = options.offsetX ?? (960 - 900 * scale) / 2;
	const offsetY = options.offsetY ?? (480 - 508 * scale) / 2;

	const points = generateLeetCodePoints({ scale, offsetX, offsetY, samplesPerStroke: 50 });
	const coefficients = computeDFT(points);

	return {
		points,
		coefficients,
		imageBounds: {
			x: offsetX,
			y: offsetY,
			width: 900 * scale,
			height: 508 * scale
		}
	};
}

/**
 * Generates continuous path points for the complete YouTube logo outline,
 * capturing the iconic curved squircle badge and the central play button triangle.
 * Coordinates are mapped from standard 800x560 space.
 */
export function generateYouTubePoints(options: FourierOptions = {}): Point[] {
	const {
		scale = 0.72,
		offsetX = (960 - 800 * 0.72) / 2,
		offsetY = (480 - 560 * 0.72) / 2,
		samplesPerStroke = 40
	} = options;

	// In 800x560 coordinate space
	const rawPoints: Point[] = [
		// 1. Top edge: center (400, 0) to top-right start (680, 18)
		...sampleCubic({ x: 400, y: 0 }, { x: 520, y: 0 }, { x: 620, y: 6 }, { x: 680, y: 18 }, samplesPerStroke),
		// 2. Top-right corner: (680, 18) to (795, 150) to (800, 280)
		...sampleCubic({ x: 680, y: 18 }, { x: 745, y: 35 }, { x: 785, y: 80 }, { x: 795, y: 150 }, samplesPerStroke),
		...sampleCubic({ x: 795, y: 150 }, { x: 800, y: 200 }, { x: 800, y: 250 }, { x: 800, y: 280 }, Math.round(samplesPerStroke * 0.7)),
		// 3. Bottom-right edge & corner: (800, 280) to (795, 410) to (680, 542)
		...sampleCubic({ x: 800, y: 280 }, { x: 800, y: 310 }, { x: 800, y: 360 }, { x: 795, y: 410 }, Math.round(samplesPerStroke * 0.7)),
		...sampleCubic({ x: 795, y: 410 }, { x: 785, y: 480 }, { x: 745, y: 525 }, { x: 680, y: 542 }, samplesPerStroke),
		// 4. Bottom edge: (680, 542) to center (400, 560) to (120, 542)
		...sampleCubic({ x: 680, y: 542 }, { x: 620, y: 554 }, { x: 520, y: 560 }, { x: 400, y: 560 }, samplesPerStroke),
		...sampleCubic({ x: 400, y: 560 }, { x: 280, y: 560 }, { x: 180, y: 554 }, { x: 120, y: 542 }, samplesPerStroke),
		// 5. Bottom-left corner & edge: (120, 542) to (5, 410) to (0, 280)
		...sampleCubic({ x: 120, y: 542 }, { x: 55, y: 525 }, { x: 15, y: 480 }, { x: 5, y: 410 }, samplesPerStroke),
		...sampleCubic({ x: 5, y: 410 }, { x: 0, y: 360 }, { x: 0, y: 310 }, { x: 0, y: 280 }, Math.round(samplesPerStroke * 0.7)),
		// 6. Top-left edge & corner: (0, 280) to (5, 150) to (120, 18)
		...sampleCubic({ x: 0, y: 280 }, { x: 0, y: 250 }, { x: 0, y: 200 }, { x: 5, y: 150 }, Math.round(samplesPerStroke * 0.7)),
		...sampleCubic({ x: 5, y: 150 }, { x: 15, y: 80 }, { x: 55, y: 35 }, { x: 120, y: 18 }, samplesPerStroke),
		// 7. Top edge return to center: (120, 18) to (400, 0)
		...sampleCubic({ x: 120, y: 18 }, { x: 180, y: 6 }, { x: 280, y: 0 }, { x: 400, y: 0 }, samplesPerStroke),
		// 8. Bridge into inner play button triangle: (400, 0) -> (321, 162)
		...sampleLine({ x: 400, y: 0 }, { x: 321, y: 162 }, Math.round(samplesPerStroke * 0.6)),
		// 9. Play button: Left vertical edge (321, 162) -> (321, 398)
		...sampleLine({ x: 321, y: 162 }, { x: 321, y: 398 }, samplesPerStroke),
		// 10. Play button: Lower diagonal edge (321, 398) -> (526, 280)
		...sampleLine({ x: 321, y: 398 }, { x: 526, y: 280 }, samplesPerStroke),
		// 11. Play button: Upper diagonal edge (526, 280) -> (321, 162)
		...sampleLine({ x: 526, y: 280 }, { x: 321, y: 162 }, samplesPerStroke),
		// 12. Bridge back to top center: (321, 162) -> (400, 0)
		...sampleLine({ x: 321, y: 162 }, { x: 400, y: 0 }, Math.round(samplesPerStroke * 0.6))
	];

	return rawPoints.map((p) => ({
		x: Number((p.x * scale + offsetX).toFixed(1)),
		y: Number((p.y * scale + offsetY).toFixed(1))
	}));
}

/**
 * Creates the high-fidelity Fourier model for the YouTube logo.
 */
export function createYouTubeFourier(options: FourierOptions = {}): {
	points: Point[];
	coefficients: FourierCoefficient[];
	imageBounds: { x: number; y: number; width: number; height: number };
} {
	const scale = options.scale ?? 0.72;
	const offsetX = options.offsetX ?? (960 - 800 * scale) / 2;
	const offsetY = options.offsetY ?? (480 - 560 * scale) / 2;

	const points = generateYouTubePoints({
		scale,
		offsetX,
		offsetY,
		samplesPerStroke: options.samplesPerStroke ?? 40
	});
	const coefficients = computeDFT(points);

	return {
		points,
		coefficients,
		imageBounds: {
			x: offsetX,
			y: offsetY,
			width: 800 * scale,
			height: 560 * scale
		}
	};
}
