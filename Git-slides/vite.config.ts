import { defineConfig, type Plugin } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import { sveltekit } from '@sveltejs/kit/vite';

/**
 * Custom Vite plugin that guarantees automatic full-page reload
 * whenever slides are added, modified, renamed, or deleted.
 */
function watchSlidesPlugin(): Plugin {
	return {
		name: 'vite-plugin-watch-slides',
		configureServer(server) {
			const invalidateAndReload = (filePath: string) => {
				if (filePath.includes('slides') || filePath.endsWith('.svelte')) {
					// Invalidate Slides.svelte and slide modules so import.meta.glob is re-evaluated
					for (const mod of server.moduleGraph.idToModuleMap.values()) {
						if (mod.file && (mod.file.includes('Slides.svelte') || mod.file.includes('slides'))) {
							server.moduleGraph.invalidateModule(mod);
						}
					}
					server.ws.send({ type: 'full-reload' });
				}
			};
			server.watcher.on('add', invalidateAndReload);
			server.watcher.on('unlink', invalidateAndReload);
			server.watcher.on('change', invalidateAndReload);
			server.watcher.on('addDir', invalidateAndReload);
			server.watcher.on('unlinkDir', invalidateAndReload);
		},
		handleHotUpdate({ file, server }) {
			if (file.includes('slides')) {
				for (const mod of server.moduleGraph.idToModuleMap.values()) {
					if (mod.file && (mod.file.includes('Slides.svelte') || mod.file.includes('slides'))) {
						server.moduleGraph.invalidateModule(mod);
					}
				}
				server.ws.send({ type: 'full-reload' });
			}
		}
	};
}

import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default defineConfig({
	resolve: {
		alias: [
			{
				find: /@animotion\/core\/.*\/slides\.svelte$/,
				replacement: path.resolve(__dirname, 'src/lib/components/Slides.svelte')
			}
		]
	},
	plugins: [
		tailwindcss(),
		sveltekit(),
		watchSlidesPlugin()
	],
	optimizeDeps: {
		exclude: ['@animotion/core', '@animotion/motion']
	},
	server: {
		watch: {
			usePolling: true,
			interval: 100
		}
	}
});
