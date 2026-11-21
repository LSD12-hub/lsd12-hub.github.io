export interface Branch {
	id: string;
	depth: number;
	x1: number;
	y1: number;
	x2: number;
	y2: number;
	color: string;
	width: number;
	branchName?: string;
}

export interface Leaf {
	id: string;
	x: number;
	y: number;
	r: number;
	color: string;
	opacity: number;
	tag?: string;
	branchName?: string;
}

export interface GitCommitNode {
	id: string;
	hash: string;
	message: string;
	author: string;
	date: string;
	branchName: string;
	x: number;
	y: number;
	depth: number;
	color: string;
	isHead?: boolean;
	isMerge?: boolean;
	tag?: string;
	parents: string[];
	opacity: number;
}

export interface GitMergeConnection {
	id: string;
	fromX: number;
	fromY: number;
	toX: number;
	toY: number;
	color: string;
	pathD: string;
	sourceBranch: string;
	targetBranch: string;
	hash: string;
	message: string;
	opacity: number;
}

export interface FractalTreeOptions {
	startX?: number;
	startY?: number;
	initialLength?: number;
	initialAngle?: number;
	maxDepth?: number;
	growth?: number;
	spread?: number;
	lengthRatio?: number;
	depthColors?: string[];
	baseStrokeWidth?: number;
	widthDecay?: number;
	gitMode?: boolean;
	showMerges?: boolean;
}

export interface GitFractalGraphResult {
	branches: Branch[];
	leaves: Leaf[];
	commits: GitCommitNode[];
	merges: GitMergeConnection[];
	stats: {
		totalCommits: number;
		branchCount: number;
		mergeCount: number;
		maxDepth: number;
	};
}

export const DEFAULT_DEPTH_COLORS = [
	'#10b981', // 0: Trunk / Main (Emerald)
	'#10b981', // 1: Emerald
	'#14b8a6', // 2: Teal
	'#06b6d4', // 3: Cyan (develop)
	'#38bdf8', // 4: Sky Blue (features)
	'#818cf8', // 5: Indigo (sub-features)
	'#a855f7', // 6: Purple (hotfixes)
	'#c084fc', // 7: Fuchsia
	'#f472b6' // 8: Blossom Pink
];

// Curated realistic commit metadata mapped by path hierarchy
const GIT_COMMIT_CATALOG: Record<
	string,
	{
		hash: string;
		branch: string;
		message: string;
		author: string;
		date: string;
		tag?: string;
		isMerge?: boolean;
	}
> = {
	'R-0': {
		hash: '3fcf8b2',
		branch: 'main',
		message: 'Initial commit: key-value storage engine',
		author: 'Lesedi',
		date: '1 year ago',
		tag: 'v0.1.0'
	},
	'R-1': {
		hash: '8ebb58c',
		branch: 'main',
		message: 'Create .git/objects loose object store',
		author: 'Lesedi',
		date: '11 months ago'
	},
	'RL-1': {
		hash: 'aedea34',
		branch: 'develop',
		message: 'Initialize develop branch workflow',
		author: 'German',
		date: '10 months ago',
		tag: 'develop'
	},
	'RR-1': {
		hash: '3b06317',
		branch: 'main',
		message: 'Release candidate v0.9 baseline',
		author: 'Lesedi',
		date: '9 months ago',
		tag: 'v0.9.0'
	},
	'RLL-2': {
		hash: '459d238',
		branch: 'feat/tree-walker',
		message: 'Recursive tree object traversal & hashing',
		author: 'Julien',
		date: '8 months ago'
	},
	'RLR-2': {
		hash: 'e9898eb',
		branch: 'feat/packfile',
		message: 'Delta compression packfile indexing',
		author: 'David',
		date: '7 months ago'
	},
	'RRL-2': {
		hash: '3ec6862',
		branch: 'hotfix/lock',
		message: 'Fix index concurrency lock in .git/index',
		author: 'Lesedi',
		date: '6 months ago'
	},
	'RRR-2': {
		hash: '525a852',
		branch: 'main',
		message: 'Merge pull request #169 into main',
		author: 'German',
		date: '5 months ago',
		isMerge: true,
		tag: 'v1.0.0'
	},
	'RLLL-3': {
		hash: '5fd6701',
		branch: 'feat/tree-walker',
		message: 'Add SHA-1 integrity check for tree entries',
		author: 'Julien',
		date: '4 months ago'
	},
	'RLLR-3': {
		hash: '78a0042',
		branch: 'feat/dag-cycle',
		message: 'DAG cycle detection & topological sort',
		author: 'Lesedi',
		date: '4 months ago'
	},
	'RLRL-3': {
		hash: '687e6a4',
		branch: 'feat/diff-engine',
		message: 'Myers sliding window diff implementation',
		author: 'David',
		date: '3 months ago'
	},
	'RLRR-3': {
		hash: '9a8b8f0',
		branch: 'feat/3way-merge',
		message: '3-way merge lowest common ancestor finder',
		author: 'German',
		date: '3 months ago'
	},
	'RRLL-3': {
		hash: '637b096',
		branch: 'hotfix/lock',
		message: 'Atomic lock replacement on cache flush',
		author: 'Lesedi',
		date: '2 months ago'
	},
	'RRLR-3': {
		hash: '7fafdb8',
		branch: 'hotfix/zlib',
		message: 'Zlib inflate streaming window fix',
		author: 'Julien',
		date: '2 months ago'
	},
	'RRRL-3': {
		hash: '5958f5b',
		branch: 'release/v1.1',
		message: 'Prepare release v1.1.0 build metadata',
		author: 'David',
		date: '1 month ago',
		tag: 'v1.1.0'
	},
	'RRRR-3': {
		hash: '30360af',
		branch: 'main',
		message: 'Merge branch develop into main',
		author: 'German',
		date: '2 weeks ago',
		isMerge: true,
		tag: 'HEAD -> main'
	}
};

function getBranchNameForPath(path: string): string {
	if (path === 'R' || path === 'RR' || path === 'RRR' || path === 'RRRR') return 'main';
	if (path === 'RL' || path === 'RLR') return 'develop';
	if (path.startsWith('RLL')) return 'feat/tree-walker';
	if (path.startsWith('RLR')) return 'feat/packfile';
	if (path.startsWith('RRL')) return 'hotfix/lock';
	if (path.startsWith('RRR')) return 'release/v1.1';
	return `feat/subtask-${path.slice(-2)}`;
}

function getCommitInfo(path: string, depth: number) {
	const key = `${path}-${depth}`;
	if (GIT_COMMIT_CATALOG[key]) {
		return GIT_COMMIT_CATALOG[key];
	}

	// Deterministic fallback for deeper levels
	let hashNum = 0;
	for (let i = 0; i < path.length; i++) {
		hashNum = (hashNum * 31 + path.charCodeAt(i) + depth * 17) % 0xffffff;
	}
	const hex = hashNum.toString(16).padStart(6, '0');
	const branch = getBranchNameForPath(path);

	const messages = [
		'Refactor commit parent graph',
		'Optimize object pack lookup',
		'Add index binary search',
		'Verify Merkle root integrity',
		'Fast-forward ref pointer',
		'Update HEAD reference log'
	];
	const message = messages[hashNum % messages.length];

	return {
		hash: `${hex}a`,
		branch,
		message,
		author: hashNum % 2 === 0 ? 'Lesedi' : 'German',
		date: `${Math.max(1, 10 - depth)} days ago`,
		tag: depth >= 4 && path.endsWith('R') ? `${branch}` : undefined,
		isMerge: path.endsWith('RL') && depth >= 3
	};
}

function buildBranches(
	x: number,
	y: number,
	length: number,
	angle: number,
	depth: number,
	maxDepth: number,
	growth: number,
	spread: number,
	lengthRatio: number,
	colors: string[],
	baseStrokeWidth: number,
	widthDecay: number,
	branches: Branch[],
	leaves: Leaf[],
	commits: GitCommitNode[],
	path = 'R',
	parentId?: string,
	nodePositions: Map<string, { x: number; y: number; branch: string; hash: string }> = new Map()
) {
	if (depth > maxDepth || growth <= depth) return;

	const branchGrowth = Math.min(1, Math.max(0, growth - depth));
	if (branchGrowth <= 0) return;

	const curLen = length * branchGrowth;
	const x2 = x + curLen * Math.cos(angle);
	const y2 = y + curLen * Math.sin(angle);

	const color = colors[Math.min(depth, colors.length - 1)];
	const width = Math.max(1, baseStrokeWidth - depth * widthDecay);
	const branchName = getBranchNameForPath(path);
	const branchId = `${path}-${depth}`;

	branches.push({
		id: branchId,
		depth,
		x1: x,
		y1: y,
		x2,
		y2,
		color,
		width,
		branchName
	});

	// Register commit node for this branch tip
	const commitMeta = getCommitInfo(path, depth);
	const isHead = depth === maxDepth || (growth <= depth + 1 && branchGrowth >= 0.85);

	commits.push({
		id: `commit-${branchId}`,
		hash: commitMeta.hash,
		message: commitMeta.message,
		author: commitMeta.author,
		date: commitMeta.date,
		branchName: commitMeta.branch,
		x: x2,
		y: y2,
		depth,
		color,
		isHead: isHead && Boolean(commitMeta.tag),
		isMerge: commitMeta.isMerge,
		tag: commitMeta.tag,
		parents: parentId ? [parentId] : [],
		opacity: Math.min(1, branchGrowth)
	});

	nodePositions.set(branchId, {
		x: x2,
		y: y2,
		branch: commitMeta.branch,
		hash: commitMeta.hash
	});

	if (branchGrowth >= 1 && growth > depth + 1 && depth < maxDepth) {
		const nextLen = length * lengthRatio;
		// Left sub-branch (diverging feature / develop)
		buildBranches(
			x2,
			y2,
			nextLen,
			angle - spread,
			depth + 1,
			maxDepth,
			growth,
			spread,
			lengthRatio,
			colors,
			baseStrokeWidth,
			widthDecay,
			branches,
			leaves,
			commits,
			`${path}L`,
			commitMeta.hash,
			nodePositions
		);
		// Right sub-branch (continuing main / upstream)
		buildBranches(
			x2,
			y2,
			nextLen,
			angle + spread,
			depth + 1,
			maxDepth,
			growth,
			spread,
			lengthRatio,
			colors,
			baseStrokeWidth,
			widthDecay,
			branches,
			leaves,
			commits,
			`${path}R`,
			commitMeta.hash,
			nodePositions
		);
	} else if (branchGrowth > 0.25) {
		const leafColor =
			depth >= 7 ? '#f472b6' : depth >= 5 ? '#c084fc' : depth >= 3 ? '#38bdf8' : '#34d399';
		leaves.push({
			id: `leaf-${path}-${depth}`,
			x: x2,
			y: y2,
			r: Math.max(2.2, 5 - depth * 0.35),
			color: leafColor,
			opacity: Math.min(1, branchGrowth),
			tag: commitMeta.tag,
			branchName: commitMeta.branch
		});
	}
}

/**
 * Builds realistic Git merge connections between sibling/parent branches
 * turning the fractal tree into a true Directed Acyclic Graph (DAG).
 */
function buildGitMerges(
	nodePositions: Map<string, { x: number; y: number; branch: string; hash: string }>,
	growth: number,
	showMerges: boolean
): GitMergeConnection[] {
	if (!showMerges || growth < 2) return [];

	const merges: GitMergeConnection[] = [];

	const mergeSpecs = [
		{
			id: 'merge-develop-tree',
			from: 'RLL-2',
			to: 'RL-1',
			hash: 'c97feac',
			sourceBranch: 'feat/tree-walker',
			targetBranch: 'develop',
			message: "Merge branch 'feat/tree-walker' into develop",
			minGrowth: 2.8,
			color: '#38bdf8'
		},
		{
			id: 'merge-develop-packfile',
			from: 'RLR-2',
			to: 'RL-1',
			hash: 'e5d230e',
			sourceBranch: 'feat/packfile',
			targetBranch: 'develop',
			message: "Merge branch 'feat/packfile' into develop",
			minGrowth: 3.2,
			color: '#818cf8'
		},
		{
			id: 'merge-main-hotfix',
			from: 'RRL-2',
			to: 'RR-1',
			hash: 'b88040c',
			sourceBranch: 'hotfix/lock',
			targetBranch: 'main',
			message: "Merge branch 'hotfix/lock' into main",
			minGrowth: 3.5,
			color: '#a855f7'
		},
		{
			id: 'merge-main-develop',
			from: 'RL-1',
			to: 'RR-1',
			hash: '5c7570e',
			sourceBranch: 'develop',
			targetBranch: 'main',
			message: "Merge branch 'develop' into main (v1.0.0)",
			minGrowth: 4.0,
			color: '#10b981'
		},
		{
			id: 'merge-feat-dag',
			from: 'RLLR-3',
			to: 'RLL-2',
			hash: 'f1696fd',
			sourceBranch: 'feat/dag-cycle',
			targetBranch: 'feat/tree-walker',
			message: "Merge branch 'feat/dag-cycle' into feat/tree-walker",
			minGrowth: 4.6,
			color: '#38bdf8'
		},
		{
			id: 'merge-feat-diff',
			from: 'RLRL-3',
			to: 'RLR-2',
			hash: '637b096',
			sourceBranch: 'feat/diff-engine',
			targetBranch: 'feat/packfile',
			message: "Merge branch 'feat/diff-engine' into feat/packfile",
			minGrowth: 5.0,
			color: '#818cf8'
		}
	];

	for (const spec of mergeSpecs) {
		if (growth < spec.minGrowth) continue;
		const fromNode = nodePositions.get(spec.from);
		const toNode = nodePositions.get(spec.to);

		if (fromNode && toNode) {
			const opacity = Math.min(1, Math.max(0, (growth - spec.minGrowth) * 1.5));
			const midY = (fromNode.y + toNode.y) / 2;
			const deltaX = toNode.x - fromNode.x;
			const controlX1 = fromNode.x + deltaX * 0.25;
			const controlX2 = toNode.x - deltaX * 0.25;

			const pathD = `M ${fromNode.x.toFixed(1)} ${fromNode.y.toFixed(1)} C ${controlX1.toFixed(1)} ${midY.toFixed(1)}, ${controlX2.toFixed(1)} ${midY.toFixed(1)}, ${toNode.x.toFixed(1)} ${toNode.y.toFixed(1)}`;

			merges.push({
				id: spec.id,
				fromX: fromNode.x,
				fromY: fromNode.y,
				toX: toNode.x,
				toY: toNode.y,
				color: spec.color,
				pathD,
				sourceBranch: spec.sourceBranch,
				targetBranch: spec.targetBranch,
				hash: spec.hash,
				message: spec.message,
				opacity
			});
		}
	}

	return merges;
}

/**
 * Generates branch segments, tip leaves, git commit nodes, and DAG merge links.
 */
export function generateFractalTree(options: FractalTreeOptions = {}): {
	branches: Branch[];
	leaves: Leaf[];
	commits: GitCommitNode[];
	merges: GitMergeConnection[];
} {
	const {
		startX = 480,
		startY = 430,
		initialLength = 115,
		initialAngle = -Math.PI / 2,
		maxDepth = 8,
		growth = 0,
		spread = 0.45,
		lengthRatio = 0.735,
		depthColors = DEFAULT_DEPTH_COLORS,
		baseStrokeWidth = 6.5,
		widthDecay = 0.65,
		showMerges = true
	} = options;

	const branches: Branch[] = [];
	const leaves: Leaf[] = [];
	const commits: GitCommitNode[] = [];
	const nodePositions = new Map<string, { x: number; y: number; branch: string; hash: string }>();

	// Add root commit at starting trunk position
	if (growth > 0) {
		const rootMeta = GIT_COMMIT_CATALOG['R-0'];
		commits.push({
			id: 'commit-root',
			hash: rootMeta.hash,
			message: rootMeta.message,
			author: rootMeta.author,
			date: rootMeta.date,
			branchName: rootMeta.branch,
			x: startX,
			y: startY,
			depth: 0,
			color: depthColors[0],
			isHead: false,
			tag: rootMeta.tag,
			parents: [],
			opacity: Math.min(1, growth)
		});
		nodePositions.set('root', {
			x: startX,
			y: startY,
			branch: 'main',
			hash: rootMeta.hash
		});
	}

	buildBranches(
		startX,
		startY,
		initialLength,
		initialAngle,
		0,
		maxDepth,
		growth,
		spread,
		lengthRatio,
		depthColors,
		baseStrokeWidth,
		widthDecay,
		branches,
		leaves,
		commits,
		'R',
		'commit-root',
		nodePositions
	);

	const merges = buildGitMerges(nodePositions, growth, showMerges);

	return { branches, leaves, commits, merges };
}

/**
 * Dedicated Git Graph generator built on top of the fractal branching algorithm.
 */
export function generateGitFractalGraph(
	options: FractalTreeOptions = {}
): GitFractalGraphResult {
	const result = generateFractalTree(options);
	const branchNames = new Set(result.commits.map((c) => c.branchName));

	return {
		branches: result.branches,
		leaves: result.leaves,
		commits: result.commits,
		merges: result.merges,
		stats: {
			totalCommits: result.commits.length,
			branchCount: Math.max(1, branchNames.size),
			mergeCount: result.merges.length,
			maxDepth: options.maxDepth ?? 8
		}
	};
}
