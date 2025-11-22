// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	integrations: [
		starlight({
			title: 'charmOS documentation',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/bluegummi/charmos' }],
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
                    collapsed: true,
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
                    collapsed: true,
				},
			],
		}),
	],
});
