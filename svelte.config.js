import adapter from '@sveltejs/adapter-static';
import preprocess from 'svelte-preprocess';

const config = {
  kit: {
    adapter: adapter({
      pages: 'docs',
      assets: 'docs',
    }),
		paths: {
			base: '/resume'
		}
  },
  preprocess: preprocess()
};

export default config;